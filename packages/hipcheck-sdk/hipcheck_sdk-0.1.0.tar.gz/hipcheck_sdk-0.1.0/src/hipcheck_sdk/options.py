# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass

# Options that can be set before starting a server.PluginServer to
# control behavior. Designed to offer roughly similar behavior to the
# feature flags available in the Rust Hipcheck SDK

@dataclass
class SdkOptions:
    rfd9_compat: bool = True

_options = SdkOptions()

# Turn an option on or off
def set_option(option_name: str, val: bool):
    global _options
    setattr(_options, option_name, val)

# Return true if option_name is enabled
def enabled(option_name: str):
    global options
    getattr(_options, option_name)

# Set the options all at once
def set_options(options: SdkOptions):
    global _options
    _options = options
