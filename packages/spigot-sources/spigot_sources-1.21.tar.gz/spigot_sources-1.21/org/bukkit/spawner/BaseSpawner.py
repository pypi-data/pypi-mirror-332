"""
Python module generated from Java source file org.bukkit.spawner.BaseSpawner

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import CreatureSpawner
from org.bukkit.block.spawner import SpawnRule
from org.bukkit.block.spawner import SpawnerEntry
from org.bukkit.entity import EntitySnapshot
from org.bukkit.entity import EntityType
from org.bukkit.entity.minecart import SpawnerMinecart
from org.bukkit.spawner import *
from typing import Any, Callable, Iterable, Tuple


class BaseSpawner:
    """
    Represents a basic entity spawner. 
    May be a SpawnerMinecart, CreatureSpawner or TrialSpawnerConfiguration.
    """

    def getSpawnedType(self) -> "EntityType":
        """
        Get the spawner's creature type.

        Returns
        - The creature type or null if it not set.
        """
        ...


    def setSpawnedType(self, creatureType: "EntityType") -> None:
        """
        Set the spawner's creature type. 
        This will override any entities that have been added with .addPotentialSpawn

        Arguments
        - creatureType: The creature type or null to clear.
        """
        ...


    def getDelay(self) -> int:
        """
        Get the spawner's delay.
        
        This is the delay, in ticks, until the spawner will spawn its next mob.

        Returns
        - The delay.
        """
        ...


    def setDelay(self, delay: int) -> None:
        """
        Set the spawner's delay.

        Arguments
        - delay: The delay.
        """
        ...


    def getRequiredPlayerRange(self) -> int:
        """
        Get the maximum distance(squared) a player can be in order for this
        spawner to be active.
        
        If this value is less than or equal to 0, this spawner is always active
        (given that there are players online).
        
        Default value is 16.

        Returns
        - the maximum distance(squared) a player can be in order for this
        spawner to be active.
        """
        ...


    def setRequiredPlayerRange(self, requiredPlayerRange: int) -> None:
        """
        Set the maximum distance (squared) a player can be in order for this
        spawner to be active.
        
        Setting this value to less than or equal to 0 will make this spawner
        always active (given that there are players online).

        Arguments
        - requiredPlayerRange: the maximum distance (squared) a player can be
        in order for this spawner to be active.
        """
        ...


    def getSpawnRange(self) -> int:
        """
        Get the radius around which the spawner will attempt to spawn mobs in.
        
        This area is square, includes the block the spawner is in, and is
        centered on the spawner's x,z coordinates - not the spawner itself.
        
        It is 2 blocks high, centered on the spawner's y-coordinate (its bottom);
        thus allowing mobs to spawn as high as its top surface and as low
        as 1 block below its bottom surface.
        
        Default value is 4.

        Returns
        - the spawn range
        """
        ...


    def setSpawnRange(self, spawnRange: int) -> None:
        """
        Set the new spawn range.

        Arguments
        - spawnRange: the new spawn range

        See
        - .getSpawnRange()
        """
        ...


    def getSpawnedEntity(self) -> "EntitySnapshot":
        """
        Gets the EntitySnapshot that will be spawned by this spawner or null
        if no entities have been assigned to this spawner. 
        
        All applicable data from the spawner will be copied, such as custom name,
        health, and velocity. 

        Returns
        - the entity snapshot or null if no entities have been assigned to this
                spawner.
        """
        ...


    def setSpawnedEntity(self, snapshot: "EntitySnapshot") -> None:
        """
        Sets the entity that will be spawned by this spawner. 
        This will override any previous entries that have been added with
        .addPotentialSpawn
        
        All applicable data from the snapshot will be copied, such as custom name,
        health, and velocity. 

        Arguments
        - snapshot: the entity snapshot or null to clear
        """
        ...


    def setSpawnedEntity(self, spawnerEntry: "SpawnerEntry") -> None:
        """
        Sets the SpawnerEntry that will be spawned by this spawner. 
        This will override any previous entries that have been added with
        .addPotentialSpawn

        Arguments
        - spawnerEntry: the spawner entry to use
        """
        ...


    def addPotentialSpawn(self, snapshot: "EntitySnapshot", weight: int, spawnRule: "SpawnRule") -> None:
        """
        Adds a new EntitySnapshot to the list of entities this spawner can
        spawn.
        
        The weight will determine how often this entry is chosen to spawn, higher
        weighted entries will spawn more often than lower weighted ones. 
        The SpawnRule will determine under what conditions this entry can
        spawn, passing null will use the default conditions for the given entity.

        Arguments
        - snapshot: the snapshot that will be spawned
        - weight: the weight
        - spawnRule: the spawn rule for this entity, or null
        """
        ...


    def addPotentialSpawn(self, spawnerEntry: "SpawnerEntry") -> None:
        """
        Adds a new SpawnerEntry to the list of entities this spawner can
        spawn.

        Arguments
        - spawnerEntry: the spawner entry to use

        See
        - .addPotentialSpawn(EntitySnapshot, int, SpawnRule)
        """
        ...


    def setPotentialSpawns(self, entries: Iterable["SpawnerEntry"]) -> None:
        """
        Sets the list of SpawnerEntry this spawner can spawn. 
        This will override any previous entries added with
        .addPotentialSpawn

        Arguments
        - entries: the list of entries
        """
        ...


    def getPotentialSpawns(self) -> list["SpawnerEntry"]:
        """
        Gets a list of potential spawns from this spawner or an empty list if no
        entities have been assigned to this spawner. 
        Changes made to the returned list will not be reflected in the spawner unless
        applied with .setPotentialSpawns

        Returns
        - a list of potential spawns from this spawner, or an empty list if no
                entities have been assigned to this spawner

        See
        - .getSpawnedType()
        """
        ...
