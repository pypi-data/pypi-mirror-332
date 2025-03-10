"""
Python module generated from Java source file org.bukkit.configuration.MemoryConfigurationOptions

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class MemoryConfigurationOptions(ConfigurationOptions):
    """
    Various settings for controlling the input and output of a MemoryConfiguration
    """

    def configuration(self) -> "MemoryConfiguration":
        ...


    def copyDefaults(self, value: bool) -> "MemoryConfigurationOptions":
        ...


    def pathSeparator(self, value: str) -> "MemoryConfigurationOptions":
        ...
