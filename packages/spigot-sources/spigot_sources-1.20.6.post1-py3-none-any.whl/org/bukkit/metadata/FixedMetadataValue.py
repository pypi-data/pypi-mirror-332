"""
Python module generated from Java source file org.bukkit.metadata.FixedMetadataValue

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class FixedMetadataValue(LazyMetadataValue):
    """
    A FixedMetadataValue is a special case metadata item that contains the same
    value forever after initialization. Invalidating a FixedMetadataValue has
    no effect.
    
    This class extends LazyMetadataValue for historical reasons, even though it
    overrides all the implementation methods. it is possible that in the future
    that the inheritance hierarchy may change.
    """

    def __init__(self, owningPlugin: "Plugin", value: "Object"):
        """
        Initializes a FixedMetadataValue with an Object

        Arguments
        - owningPlugin: the Plugin that created this metadata value
        - value: the value assigned to this metadata value
        """
        ...


    def invalidate(self) -> None:
        ...


    def value(self) -> "Object":
        ...
