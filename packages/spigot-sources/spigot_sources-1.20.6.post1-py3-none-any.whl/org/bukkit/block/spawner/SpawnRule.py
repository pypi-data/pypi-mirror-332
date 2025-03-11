"""
Python module generated from Java source file org.bukkit.block.spawner.SpawnRule

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.block.spawner import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from typing import Any, Callable, Iterable, Tuple


class SpawnRule(Cloneable, ConfigurationSerializable):
    """
    Represents a spawn rule that controls what conditions an entity from a
    monster spawner can spawn.
    """

    def __init__(self, minBlockLight: int, maxBlockLight: int, minSkyLight: int, maxSkyLight: int):
        """
        Constructs a new SpawnRule.

        Arguments
        - minBlockLight: The minimum (inclusive) block light required for
        spawning to succeed.
        - maxBlockLight: The maximum (inclusive) block light required for
        spawning to succeed.
        - minSkyLight: The minimum (inclusive) sky light required for
        spawning to succeed.
        - maxSkyLight: The maximum (inclusive) sky light required for
        spawning to succeed.
        """
        ...


    def getMinBlockLight(self) -> int:
        """
        Gets the minimum (inclusive) block light required for spawning to
        succeed.

        Returns
        - minimum block light
        """
        ...


    def setMinBlockLight(self, minBlockLight: int) -> None:
        """
        Sets the minimum (inclusive) block light required for spawning to
        succeed.

        Arguments
        - minBlockLight: minimum block light
        """
        ...


    def getMaxBlockLight(self) -> int:
        """
        Gets the maximum (inclusive) block light required for spawning to
        succeed.

        Returns
        - maximum block light
        """
        ...


    def setMaxBlockLight(self, maxBlockLight: int) -> None:
        """
        Sets the maximum (inclusive) block light required for spawning to
        succeed.

        Arguments
        - maxBlockLight: maximum block light
        """
        ...


    def getMinSkyLight(self) -> int:
        """
        Gets the minimum (inclusive) sky light required for spawning to succeed.

        Returns
        - minimum sky light
        """
        ...


    def setMinSkyLight(self, minSkyLight: int) -> None:
        """
        Sets the minimum (inclusive) sky light required for spawning to succeed.

        Arguments
        - minSkyLight: minimum sky light
        """
        ...


    def getMaxSkyLight(self) -> int:
        """
        Gets the maximum (inclusive) sky light required for spawning to succeed.

        Returns
        - maximum sky light
        """
        ...


    def setMaxSkyLight(self, maxSkyLight: int) -> None:
        """
        Sets the maximum (inclusive) sky light required for spawning to succeed.

        Arguments
        - maxSkyLight: maximum sky light
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def clone(self) -> "SpawnRule":
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "SpawnRule":
        ...
