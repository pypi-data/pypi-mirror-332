"""
Python module generated from Java source file org.bukkit.entity.EnderSignal

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EnderSignal(Entity):
    """
    Represents an EnderSignal, which is created upon throwing an ender eye.
    """

    def getTargetLocation(self) -> "Location":
        """
        Get the location this EnderSignal is moving towards.

        Returns
        - the Location this EnderSignal is moving towards.
        """
        ...


    def setTargetLocation(self, location: "Location") -> None:
        """
        Set the Location this EnderSignal is moving towards.
        
        When setting a new target location, the .getDropItem() resets to
        a random value and the despawn timer gets set back to 0.

        Arguments
        - location: the new target location
        """
        ...


    def getDropItem(self) -> bool:
        """
        Gets if the EnderSignal should drop an item on death.
        If `True`, it will drop an item. If `False`, it will shatter.

        Returns
        - True if the EnderSignal will drop an item on death, or False if
        it will shatter
        """
        ...


    def setDropItem(self, drop: bool) -> None:
        """
        Sets if the EnderSignal should drop an item on death; or if it should
        shatter.

        Arguments
        - drop: True if the EnderSignal should drop an item on death, or
        False if it should shatter.
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Get the ItemStack to be displayed while in the air and to be
        dropped on death.

        Returns
        - the item stack
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Set the ItemStack to be displayed while in the air and to be
        dropped on death.

        Arguments
        - item: the item to set. If null, resets to the default eye of ender
        """
        ...


    def getDespawnTimer(self) -> int:
        """
        Gets the amount of time this entity has been alive (in ticks).
        
        When this number is greater than 80, it will despawn on the next tick.

        Returns
        - the number of ticks this EnderSignal has been alive.
        """
        ...


    def setDespawnTimer(self, timer: int) -> None:
        """
        Set how long this entity has been alive (in ticks).
        
        When this number is greater than 80, it will despawn on the next tick.

        Arguments
        - timer: how long (in ticks) this EnderSignal has been alive.
        """
        ...
