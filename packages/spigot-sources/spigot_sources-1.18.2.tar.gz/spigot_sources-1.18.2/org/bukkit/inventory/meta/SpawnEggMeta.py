"""
Python module generated from Java source file org.bukkit.inventory.meta.SpawnEggMeta

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
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


    def clone(self) -> "SpawnEggMeta":
        ...
