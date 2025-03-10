"""
Python module generated from Java source file org.bukkit.block.spawner.SpawnerEntry

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.block.spawner import *
from org.bukkit.entity import EntitySnapshot
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.loot import LootTable
from org.bukkit.loot import LootTables
from typing import Any, Callable, Iterable, Tuple


class SpawnerEntry:
    """
    Represents a weighted spawn potential that can be added to a monster spawner.
    """

    def __init__(self, snapshot: "EntitySnapshot", spawnWeight: int, spawnRule: "SpawnRule"):
        ...


    def __init__(self, snapshot: "EntitySnapshot", spawnWeight: int, spawnRule: "SpawnRule", equipment: "Equipment"):
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


    def getEquipment(self) -> "Equipment":
        """
        Gets the equipment which will be applied to the spawned entity.

        Returns
        - the equipment, or null
        """
        ...


    def setEquipment(self, equipment: "Equipment") -> None:
        """
        Sets the equipment which will be applied to the spawned entity.

        Arguments
        - equipment: new equipment, or null
        """
        ...


    class Equipment:
        """
        Represents the equipment loot table applied to a spawned entity.
        """

        def __init__(self, equipmentLootTable: "LootTable", dropChances: dict["EquipmentSlot", "Float"]):
            ...


        def setEquipmentLootTable(self, table: "LootTable") -> None:
            """
            Set the loot table for the entity.
            
            To remove a loot table use null. Do not use LootTables.EMPTY
            to clear a LootTable.

            Arguments
            - table: this org.bukkit.entity.Mob will have.
            """
            ...


        def getEquipmentLootTable(self) -> "LootTable":
            """
            Gets the loot table for the entity.
            
            
            If an entity does not have a loot table, this will return null, NOT
            an empty loot table.

            Returns
            - the loot table for this entity.
            """
            ...


        def getDropChances(self) -> dict["EquipmentSlot", "Float"]:
            """
            Gets a mutable map of the drop chances for each slot of the entity.
            If non-null, the entity's drop chances will be overridden with the
            given value.

            Returns
            - mutable map of drop chances
            """
            ...
