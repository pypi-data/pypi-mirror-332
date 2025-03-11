"""
Python module generated from Java source file org.bukkit.entity.Item

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Item(Entity):
    """
    Represents a dropped item.
    """

    def getItemStack(self) -> "ItemStack":
        """
        Gets the item stack associated with this item drop.

        Returns
        - An item stack.
        """
        ...


    def setItemStack(self, stack: "ItemStack") -> None:
        """
        Sets the item stack associated with this item drop.

        Arguments
        - stack: An item stack.
        """
        ...


    def getPickupDelay(self) -> int:
        """
        Gets the delay before this Item is available to be picked up by players

        Returns
        - Remaining delay
        """
        ...


    def setPickupDelay(self, delay: int) -> None:
        """
        Sets the delay before this Item is available to be picked up by players

        Arguments
        - delay: New delay
        """
        ...


    def setUnlimitedLifetime(self, unlimited: bool) -> None:
        """
        Sets if this Item should live forever

        Arguments
        - unlimited: True if the lifetime is unlimited
        """
        ...


    def isUnlimitedLifetime(self) -> bool:
        """
        Gets if this Item lives forever

        Returns
        - True if the lifetime is unlimited
        """
        ...


    def setOwner(self, owner: "UUID") -> None:
        """
        Sets the owner of this item.
        
        Other entities will not be able to pickup this item when an owner is set.

        Arguments
        - owner: UUID of new owner
        """
        ...


    def getOwner(self) -> "UUID":
        """
        Get the owner of this item.

        Returns
        - UUID of owner
        """
        ...


    def setThrower(self, uuid: "UUID") -> None:
        """
        Set the thrower of this item.
        
        The thrower is the entity which dropped the item. This affects the
        trigger criteria for item pickups, for things such as advancements.

        Arguments
        - uuid: UUID of thrower
        """
        ...


    def getThrower(self) -> "UUID":
        """
        Get the thrower of this item.
        
        The thrower is the entity which dropped the item.

        Returns
        - UUID of thrower
        """
        ...
