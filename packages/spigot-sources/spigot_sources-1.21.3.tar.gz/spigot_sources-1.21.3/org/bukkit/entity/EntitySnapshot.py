"""
Python module generated from Java source file org.bukkit.entity.EntitySnapshot

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntitySnapshot:
    """
    Represents an immutable copy of an entity's state. Can be used at any time to
    create an instance of the stored entity.
    """

    def createEntity(self, world: "World") -> "Entity":
        """
        Creates an entity using this template. Does not spawn the copy in the world.

        Arguments
        - world: the world to create the entity in

        Returns
        - a copy of this entity.
        """
        ...


    def createEntity(self, to: "Location") -> "Entity":
        """
        Creates an entity using this template and spawns it at the provided location.

        Arguments
        - to: the location to copy to

        Returns
        - the new entity.
        """
        ...


    def getEntityType(self) -> "EntityType":
        """
        Gets the type of entity this template holds.

        Returns
        - the type
        """
        ...


    def getAsString(self) -> str:
        """
        Get this EntitySnapshot as an NBT string.
        
        This string should not be relied upon as a serializable value.

        Returns
        - the NBT string
        """
        ...
