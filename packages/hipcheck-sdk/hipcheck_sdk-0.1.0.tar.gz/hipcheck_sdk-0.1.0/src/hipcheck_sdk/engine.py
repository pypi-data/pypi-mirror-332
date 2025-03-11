# SPDX-License-Identifier: Apache-2.0

from typing import Union, List, Tuple, Optional
from enum import Enum
from dataclasses import dataclass

import asyncio
import json

import hipcheck_sdk.gen as gen
from hipcheck_sdk.chunk import *
from hipcheck_sdk.error import *

# Split `s` at first instance of `delim`. Return substring before
# `delim`. If `delim` does not exist, second tuple element is None,
# else it is everything after the first `delim` occurence.
def split_once(s: str, delim: str) -> Tuple[str, Optional[str]]:
    res = s.split(delim, 1)
    if len(res) != 2:
        res.append(None)
    return tuple(res)

# Return a tuple of (publisher, plugin, endpoint_name) from a target
# string (e.g. "mitre/example/query"). If no endpoint_name given,
# return "" for endpoint_name, indicating the default query endpoint.
def parse_target_str(target: str) -> Tuple[str, str, str]:
    publisher, rest = split_once(target, "/")
    if rest is None:
        raise InvalidQueryTargetFormat()
    plugin, name = split_once(rest, "/")
    if name is None:
        name = ""
    return (publisher, plugin, name)

#  Manages a particular query session.
#
#  This struct invokes the `func` field of an `Endpoint`, passing a handle to itself. This
#  allows the query logic to request information from other Hipcheck plugins in order to complete.
class PluginEngine:

    def __init__(self, session_id: int, tx: asyncio.Queue, rx: asyncio.Queue, drop_tx: asyncio.Queue):
        self.id: int = session_id
        self.tx: asyncio.Queue = tx
        self.rx: asyncio.Queue = rx
        # So that we can remove ourselves when we get dropped
        self.drop_tx: asyncio.Queue = drop_tx
        self.concerns: List[str] = []
        # When unit testing, this enables the user to mock plugin responses to various inputs
        self.mock_responses = {}  # @Todo - implement mock interface

    # Query another Hipcheck plugin `target` with key `input`. On success, the deserialized result object
    # of the query is returned. `target` shoul be a string of the format
    # `"publisher/plugin[/query]"`, where the bracketed substring is optional if the plugin's
    # default query endpoint is desired. `key` is an object that can be serialized using `json.dumps()`.
    # @Todo - better target type hint / QueryTarget
    async def query(self, target: str, key: object) -> object:
        publisher, plugin, name = parse_target_str(target)

        query = Query(
            id=self.id,
            direction=QueryDirection.REQUEST,
            publisher=publisher,
            plugin=plugin,
            query=name,
            key=[key],
            output=[],
            concerns=[]
        )

        await self.send(query)
        resp: Query = await self.recv()

        return resp.output[0]

    # Query another Hipcheck plugin `target` with a list of `keys`. On success, the deserialized result
    # objects of each query is returned. `target` should be a string of the format
    # `"publisher/plugin[/query]"`, where the bracketed substring is optional if the plugin's default query
    # endpoint is desired. `keys` must be a list containing a objects that can be serialized using `json.dumps()`.
    async def batch_query(self, target: str, keys: List[object]) -> List[object]:
        publisher, plugin, name = parse_target_str(target)

        query = Query(
            id=self.id,
            direction=QueryDirection.REQUEST,
            publisher=publisher,
            plugin=plugin,
            query=name,
            key=keys,
            output=[],
            concerns=[]
        )

        await self.send(query)
        resp: Query = await self.recv()

        return resp.output


    async def recv_raw(self) -> Optional[List[gen.Query]]:
        out = []

        try:
            first = await self.rx.get()
        except Exception as e:
            # Underlying gRPC channel closed
            # @Todo - tighten this exception
            print(f"Recv exception: {e}")
            return None

        out.append(first)

        # If more messages in the queue, opportunistically read more
        while True:
            try:
                msg = self.rx.get_nowait()
            except asyncio.QueueEmpty:
                break
            except Exception as e:
                # @Todo - tighten this exception
                print(f"Recv exception: {e}")
                break
            out.append(msg)

        return out


    async def send_session_error(self, plugin):
        query = gen.Query(
            id=self.id,
            state=gen.QUERY_STATE_UNSPECIFIED,
            publisher_name=plugin.publisher,
            plugin_name=plugin.name,
            query_name="",
            concern=self.take_concerns(),
            split=False
        )
        await self.tx.put(query)


    async def recv(self) -> Optional[Query]:
        synth = QuerySynthesizer()
        res: Optional[Query] = None;
        while res is None:
            opt_msg_chunks = await self.recv_raw()
            if opt_msg_chunks is None:
                return None
            msg_chunks = opt_msg_chunks
            res = synth.add(msg_chunks)
        return res


    # Records a string-like concern that will be emitted in the final Hipcheck report.
    # Intended for use within a `@query`-decorated function.
    def record_concern(self, concern):
        self.concerns.append(concern)

    def take_concerns(self):
        out = self.concerns
        self.concerns = []
        return out

    # Send a gRPC query from plugin to the hipcheck server
    async def send(self, query: Query):
        query.id = self.id # incoming id value is just a placeholder
        for pq in prepare(query):
            await self.tx.put(pq)

    async def handle_session_fallible(self, plugin):
        query: Query = await self.recv()

        if query.direction == QueryDirection.RESPONSE:
            raise ReceivedReplyWhenExpectingSubmitChunk()

        name = query.query

        # Per RFD 0009, there should only be one query key per query
        if len(query.key) != 1:
            raise UnspecifiedQueryState()
        key = query.key[0]

        query = next((x for x in plugin.queries() if x.name == name), None)
        if query is None:
            raise UnknownPluginQuery()

        value = await query.func(self, key)

        out = Query(
            id=self.id,
            direction=QueryDirection.RESPONSE,
            publisher=plugin.publisher,
            plugin=plugin.name,
            query=name,
            key=[],
            output=[value],
            concerns=self.take_concerns()
        )

        await self.send(out)

        # Notify HcSessionSocket that session is closed
        await self.drop_tx.put(self.id)

    async def handle_session(self, plugin):
        try:
            await self.handle_session_fallible(plugin)
        # Errors that we raise intentionally
        except SdkError as e:
            print("SDK: ", e)
            await self.send_session_error(plugin)
        # Other errors, such as syntactical ones
        except Exception as e:
            print("OTHER: ", e)
            await self.send_session_error(plugin)
        # except asyncio.QueueShutDown:
        #     return

