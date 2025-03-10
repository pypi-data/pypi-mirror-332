"""
Python module generated from Java source file org.bukkit.packs.DataPackManager

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import World
from org.bukkit.entity import EntityType
from org.bukkit.packs import *
from typing import Any, Callable, Iterable, Tuple


class DataPackManager:
    """
    Manager of data packs.
    """

    def getDataPacks(self) -> Iterable["DataPack"]:
        """
        Return all the available DataPacks on the server.

        Returns
        - a Collection of DataPack
        """
        ...


    def getDataPack(self, dataPackKey: "NamespacedKey") -> "DataPack":
        """
        Gets a DataPack by its key.

        Arguments
        - dataPackKey: the key of the DataPack

        Returns
        - the DataPack or null if it does not exist
        """
        ...


    def getEnabledDataPacks(self, world: "World") -> Iterable["DataPack"]:
        """
        Return all the enabled DataPack in the World.

        Arguments
        - world: the world to search

        Returns
        - a Collection of DataPack
        """
        ...


    def getDisabledDataPacks(self, world: "World") -> Iterable["DataPack"]:
        """
        Return all the disabled DataPack in the World.

        Arguments
        - world: the world to search

        Returns
        - a Collection of DataPack
        """
        ...


    def isEnabledByFeature(self, material: "Material", world: "World") -> bool:
        """
        Gets if the Material is enabled for use by the features in World.

        Arguments
        - material: Material to check (needs to be an Material.isItem() or Material.isBlock())
        - world: World to check

        Returns
        - `True` if the Item/Block related to the material is enabled
        """
        ...


    def isEnabledByFeature(self, entityType: "EntityType", world: "World") -> bool:
        """
        Gets if the EntityType is enabled for use by the Features in World.

        Arguments
        - entityType: EntityType to check
        - world: World to check

        Returns
        - `True` if the type of entity is enabled
        """
        ...
