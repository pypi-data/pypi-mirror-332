"""
Python module generated from Java source file org.bukkit.material.SpawnEgg

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.entity import EntityType
from org.bukkit.inventory.meta import SpawnEggMeta
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class SpawnEgg(MaterialData):
    """
    Represents a spawn egg that can be used to spawn mobs

    Deprecated
    - use SpawnEggMeta
    """

    def __init__(self):
        ...


    def __init__(self, type: "Material", data: int):
        """
        Arguments
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def __init__(self, data: int):
        """
        Arguments
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def __init__(self, type: "EntityType"):
        ...


    def getSpawnedType(self) -> "EntityType":
        """
        Get the type of entity this egg will spawn.

        Returns
        - The entity type.

        Deprecated
        - This is now stored in SpawnEggMeta.
        """
        ...


    def setSpawnedType(self, type: "EntityType") -> None:
        """
        Set the type of entity this egg will spawn.

        Arguments
        - type: The entity type.

        Deprecated
        - This is now stored in SpawnEggMeta.
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "SpawnEgg":
        ...
