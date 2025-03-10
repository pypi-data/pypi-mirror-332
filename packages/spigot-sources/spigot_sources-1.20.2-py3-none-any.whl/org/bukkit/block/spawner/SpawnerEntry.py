"""
Python module generated from Java source file org.bukkit.block.spawner.SpawnerEntry

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.block.spawner import *
from org.bukkit.entity import EntitySnapshot
from typing import Any, Callable, Iterable, Tuple


class SpawnerEntry:
    """
    Represents a weighted spawn potential that can be added to a monster spawner.
    """

    def __init__(self, snapshot: "EntitySnapshot", spawnWeight: int, spawnRule: "SpawnRule"):
        ...


    def getSnapshot(self) -> "EntitySnapshot":
        """
        Gets the EntitySnapshot for this SpawnerEntry.

        Returns
        - the snapshot
        """
        ...


    def setSnapshot(self, snapshot: "EntitySnapshot") -> None:
        """
        Sets the EntitySnapshot for this SpawnerEntry.

        Arguments
        - snapshot: the snapshot
        """
        ...


    def getSpawnWeight(self) -> int:
        """
        Gets the weight for this SpawnerEntry, when added to a spawner entries
        with higher weight will spawn more often.

        Returns
        - the weight
        """
        ...


    def setSpawnWeight(self, spawnWeight: int) -> None:
        """
        Sets the weight for this SpawnerEntry, when added to a spawner entries
        with higher weight will spawn more often.

        Arguments
        - spawnWeight: the new spawn weight
        """
        ...


    def getSpawnRule(self) -> "SpawnRule":
        """
        Gets a copy of the SpawnRule for this SpawnerEntry, or null if
        none has been set.

        Returns
        - a copy of the spawn rule or null
        """
        ...


    def setSpawnRule(self, spawnRule: "SpawnRule") -> None:
        """
        Sets the SpawnRule for this SpawnerEntry, null may be used to
        clear the current spawn rule.

        Arguments
        - spawnRule: the new spawn rule to use or null
        """
        ...
