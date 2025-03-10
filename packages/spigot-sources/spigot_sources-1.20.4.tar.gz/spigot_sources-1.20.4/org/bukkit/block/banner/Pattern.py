"""
Python module generated from Java source file org.bukkit.block.banner.Pattern

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableMap
from java.util import NoSuchElementException
from org.bukkit import DyeColor
from org.bukkit.block.banner import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from typing import Any, Callable, Iterable, Tuple


class Pattern(ConfigurationSerializable):

    def __init__(self, color: "DyeColor", pattern: "PatternType"):
        """
        Creates a new pattern from the specified color and
        pattern type

        Arguments
        - color: the pattern color
        - pattern: the pattern type
        """
        ...


    def __init__(self, map: dict[str, "Object"]):
        """
        Constructor for deserialization.

        Arguments
        - map: the map to deserialize from
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    def getColor(self) -> "DyeColor":
        """
        Returns the color of the pattern

        Returns
        - the color of the pattern
        """
        ...


    def getPattern(self) -> "PatternType":
        """
        Returns the type of pattern

        Returns
        - the pattern type
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
