"""
Python module generated from Java source file org.bukkit.configuration.MemoryConfiguration

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.configuration import *
from typing import Any, Callable, Iterable, Tuple


class MemoryConfiguration(MemorySection, Configuration):
    """
    This is a Configuration implementation that does not save or load
    from any source, and stores all values in memory only.
    This is useful for temporary Configurations for providing defaults.
    """

    def __init__(self):
        """
        Creates an empty MemoryConfiguration with no default values.
        """
        ...


    def __init__(self, defaults: "Configuration"):
        """
        Creates an empty MemoryConfiguration using the specified Configuration as a source for all default values.

        Arguments
        - defaults: Default value provider

        Raises
        - IllegalArgumentException: Thrown if defaults is null
        """
        ...


    def addDefault(self, path: str, value: "Object") -> None:
        ...


    def addDefaults(self, defaults: dict[str, "Object"]) -> None:
        ...


    def addDefaults(self, defaults: "Configuration") -> None:
        ...


    def setDefaults(self, defaults: "Configuration") -> None:
        ...


    def getDefaults(self) -> "Configuration":
        ...


    def getParent(self) -> "ConfigurationSection":
        ...


    def options(self) -> "MemoryConfigurationOptions":
        ...
