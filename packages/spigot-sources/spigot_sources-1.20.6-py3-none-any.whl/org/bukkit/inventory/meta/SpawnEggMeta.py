"""
Python module generated from Java source file org.bukkit.inventory.meta.SpawnEggMeta

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import EntitySnapshot
from org.bukkit.entity import EntityType
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class SpawnEggMeta(ItemMeta):
    """
    Represents a spawn egg and it's spawned type.
    """

    def getSpawnedType(self) -> "EntityType":
        """
        Get the type of entity this egg will spawn.

        Returns
        - The entity type. May be null for implementation specific default.

        Deprecated
        - different types are different items
        """
        ...


    def setSpawnedType(self, type: "EntityType") -> None:
        """
        Set the type of entity this egg will spawn.

        Arguments
        - type: The entity type. May be null for implementation specific
        default.

        Deprecated
        - different types are different items
        """
        ...


    def getSpawnedEntity(self) -> "EntitySnapshot":
        """
        Gets the EntitySnapshot that will be spawned by this spawn egg or null if no entity
        has been set. 
        
        All applicable data from the egg will be copied, such as custom name, health,
        and velocity. 

        Returns
        - the entity snapshot or null if no entity has been set
        """
        ...


    def setSpawnedEntity(self, snapshot: "EntitySnapshot") -> None:
        """
        Sets the EntitySnapshot that will be spawned by this spawn egg. 
        
        All applicable data from the entity will be copied, such as custom name,
        health, and velocity. 

        Arguments
        - snapshot: the snapshot
        """
        ...


    def clone(self) -> "SpawnEggMeta":
        ...
