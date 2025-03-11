"""
Python module generated from Java source file org.bukkit.metadata.MetadataValue

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class MetadataValue:

    def value(self) -> "Object":
        """
        Fetches the value of this metadata item.

        Returns
        - the metadata value.
        """
        ...


    def asInt(self) -> int:
        """
        Attempts to convert the value of this metadata item into an int.

        Returns
        - the value as an int.
        """
        ...


    def asFloat(self) -> float:
        """
        Attempts to convert the value of this metadata item into a float.

        Returns
        - the value as a float.
        """
        ...


    def asDouble(self) -> float:
        """
        Attempts to convert the value of this metadata item into a double.

        Returns
        - the value as a double.
        """
        ...


    def asLong(self) -> int:
        """
        Attempts to convert the value of this metadata item into a long.

        Returns
        - the value as a long.
        """
        ...


    def asShort(self) -> int:
        """
        Attempts to convert the value of this metadata item into a short.

        Returns
        - the value as a short.
        """
        ...


    def asByte(self) -> int:
        """
        Attempts to convert the value of this metadata item into a byte.

        Returns
        - the value as a byte.
        """
        ...


    def asBoolean(self) -> bool:
        """
        Attempts to convert the value of this metadata item into a boolean.

        Returns
        - the value as a boolean.
        """
        ...


    def asString(self) -> str:
        """
        Attempts to convert the value of this metadata item into a string.

        Returns
        - the value as a string.
        """
        ...


    def getOwningPlugin(self) -> "Plugin":
        """
        Returns the Plugin that created this metadata item.

        Returns
        - the plugin that owns this metadata value. Could be null if the plugin was already unloaded.
        """
        ...


    def invalidate(self) -> None:
        """
        Invalidates this metadata item, forcing it to recompute when next
        accessed.
        """
        ...
