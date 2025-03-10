"""
Python module generated from Java source file org.bukkit.metadata.MetadataValueAdapter

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.lang.ref import WeakReference
from org.bukkit.metadata import *
from org.bukkit.plugin import Plugin
from org.bukkit.util import NumberConversions
from typing import Any, Callable, Iterable, Tuple


class MetadataValueAdapter(MetadataValue):
    """
    Optional base class for facilitating MetadataValue implementations.
    
    This provides all the conversion functions for MetadataValue so that
    writing an implementation of MetadataValue is as simple as implementing
    value() and invalidate().
    """

    def getOwningPlugin(self) -> "Plugin":
        ...


    def asInt(self) -> int:
        ...


    def asFloat(self) -> float:
        ...


    def asDouble(self) -> float:
        ...


    def asLong(self) -> int:
        ...


    def asShort(self) -> int:
        ...


    def asByte(self) -> int:
        ...


    def asBoolean(self) -> bool:
        ...


    def asString(self) -> str:
        ...
