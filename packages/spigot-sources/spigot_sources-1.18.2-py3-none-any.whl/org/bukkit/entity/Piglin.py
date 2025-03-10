"""
Python module generated from Java source file org.bukkit.entity.Piglin

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.entity import *
from org.bukkit.inventory import InventoryHolder
from typing import Any, Callable, Iterable, Tuple


class Piglin(PiglinAbstract, InventoryHolder):
    """
    Represents a Piglin.
    """

    def isAbleToHunt(self) -> bool:
        """
        Get whether the piglin is able to hunt hoglins.

        Returns
        - Whether the piglin is able to hunt hoglins
        """
        ...


    def setIsAbleToHunt(self, flag: bool) -> None:
        """
        Sets whether the piglin is able to hunt hoglins.

        Arguments
        - flag: Whether the piglin is able to hunt hoglins.
        """
        ...


    def addBarterMaterial(self, material: "Material") -> bool:
        """
        Adds a material to the allowed list of materials to barter with.

        Arguments
        - material: The material to add

        Returns
        - True if the item has been added successfully, False otherwise
        """
        ...


    def removeBarterMaterial(self, material: "Material") -> bool:
        """
        Removes a material from the allowed list of materials to barter with.
        
        <strong>Note:</strong> It's not possible to override the default
        bartering item gold_ingots as payment. To block gold_ingots see
        org.bukkit.event.entity.PiglinBarterEvent.

        Arguments
        - material: The material to remove

        Returns
        - True if the item has been removed successfully, False otherwise
        """
        ...


    def addMaterialOfInterest(self, material: "Material") -> bool:
        """
        Adds a material the piglin will pickup and store in his inventory.

        Arguments
        - material: The material you want the piglin to be interested in

        Returns
        - True if the item has been added successfully, False otherwise
        """
        ...


    def removeMaterialOfInterest(self, material: "Material") -> bool:
        """
        Removes a material from the list of materials the piglin will pickup.
        
        <strong>Note:</strong> It's not possible to override the default list of
        item the piglin will pickup. To cancel pickup see
        org.bukkit.event.entity.EntityPickupItemEvent.

        Arguments
        - material: The material you want removed from the interest list

        Returns
        - True if the item has been removed successfully, False otherwise
        """
        ...


    def getInterestList(self) -> set["Material"]:
        """
        Returns a immutable set of materials the piglins will pickup.
        
        <strong>Note:</strong> This set will not include the items that are set
        by default. To interact with those items see
        org.bukkit.event.entity.EntityPickupItemEvent.

        Returns
        - An immutable materials set
        """
        ...


    def getBarterList(self) -> set["Material"]:
        """
        Returns a immutable set of materials the piglins will barter with.
        
        <strong>Note:</strong> This set will not include the items that are set
        by default. To interact with those items see
        org.bukkit.event.entity.PiglinBarterEvent.

        Returns
        - An immutable materials set
        """
        ...
