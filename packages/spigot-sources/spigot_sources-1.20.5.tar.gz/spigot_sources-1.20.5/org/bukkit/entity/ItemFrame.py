"""
Python module generated from Java source file org.bukkit.entity.ItemFrame

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Rotation
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class ItemFrame(Hanging):
    """
    Represents an Item Frame
    """

    def getItem(self) -> "ItemStack":
        """
        Get the item in this frame

        Returns
        - a defensive copy the item in this item frame
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Set the item in this frame

        Arguments
        - item: the new item
        """
        ...


    def setItem(self, item: "ItemStack", playSound: bool) -> None:
        """
        Set the item in this frame

        Arguments
        - item: the new item
        - playSound: whether or not to play the item placement sound
        """
        ...


    def getItemDropChance(self) -> float:
        """
        Gets the chance of the item being dropped upon this frame's destruction.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - chance of the off hand item being dropped
        """
        ...


    def setItemDropChance(self, chance: float) -> None:
        """
        Sets the chance of the off hand item being dropped upon this frame's
        destruction.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: the chance of off hand item being dropped
        """
        ...


    def getRotation(self) -> "Rotation":
        """
        Get the rotation of the frame's item

        Returns
        - the direction
        """
        ...


    def setRotation(self, rotation: "Rotation") -> None:
        """
        Set the rotation of the frame's item

        Arguments
        - rotation: the new rotation

        Raises
        - IllegalArgumentException: if rotation is null
        """
        ...


    def isVisible(self) -> bool:
        """
        Returns whether the item frame is be visible or not.

        Returns
        - whether the item frame is visible or not
        """
        ...


    def setVisible(self, visible: bool) -> None:
        """
        Sets whether the item frame should be visible or not.

        Arguments
        - visible: whether the item frame is visible or not
        """
        ...


    def isFixed(self) -> bool:
        """
        Returns whether the item frame is "fixed" or not.
        
        When True it's not possible to destroy/move the frame (e.g. by damage,
        interaction, pistons, or missing supporting blocks), rotate the item or
        place/remove items.

        Returns
        - whether the item frame is fixed or not
        """
        ...


    def setFixed(self, fixed: bool) -> None:
        """
        Sets whether the item frame should be fixed or not.
        
        When set to True it's not possible to destroy/move the frame (e.g. by
        damage, interaction, pistons, or missing supporting blocks), rotate the
        item or place/remove items.

        Arguments
        - fixed: whether the item frame is fixed or not
        """
        ...
