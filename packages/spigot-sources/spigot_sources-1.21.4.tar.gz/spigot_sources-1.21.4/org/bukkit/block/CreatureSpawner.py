"""
Python module generated from Java source file org.bukkit.block.CreatureSpawner

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.spawner import Spawner
from typing import Any, Callable, Iterable, Tuple


class CreatureSpawner(TileState, Spawner):
    """
    Represents a captured state of a creature spawner.
    """

    def setCreatureTypeByName(self, creatureType: str) -> None:
        """
        Set the spawner mob type.

        Arguments
        - creatureType: The creature type's name or null to clear.

        Deprecated
        - magic value, use
        .setSpawnedType(org.bukkit.entity.EntityType).
        """
        ...


    def getCreatureTypeName(self) -> str:
        """
        Get the spawner's creature type.

        Returns
        - The creature type's name if is set.

        Deprecated
        - magic value, use .getSpawnedType().
        """
        ...
