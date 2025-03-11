"""
Python module generated from Java source file org.bukkit.event.player.PlayerItemMendEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import ExperienceOrb
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerItemMendEvent(PlayerEvent, Cancellable):
    """
    Represents when a player has an item repaired via the Mending enchantment.
    
    This event is fired directly before the PlayerExpChangeEvent, and the
    results of this event directly affect the PlayerExpChangeEvent.
    """

    def __init__(self, who: "Player", item: "ItemStack", slot: "EquipmentSlot", experienceOrb: "ExperienceOrb", repairAmount: int):
        ...


    def __init__(self, who: "Player", item: "ItemStack", experienceOrb: "ExperienceOrb", repairAmount: int):
        ...


    def getItem(self) -> "ItemStack":
        """
        Get the ItemStack to be repaired.
        
        This is not necessarily the item the player is holding.

        Returns
        - the item to be repaired
        """
        ...


    def getSlot(self) -> "EquipmentSlot":
        """
        Get the EquipmentSlot in which the repaired ItemStack
        may be found.

        Returns
        - the repaired slot
        """
        ...


    def getExperienceOrb(self) -> "ExperienceOrb":
        """
        Get the experience orb triggering the event.

        Returns
        - the experience orb
        """
        ...


    def getRepairAmount(self) -> int:
        """
        Get the amount the item is to be repaired.
        
        The default value is twice the value of the consumed experience orb
        or the remaining damage left on the item, whichever is smaller.

        Returns
        - how much damage will be repaired by the experience orb
        """
        ...


    def setRepairAmount(self, amount: int) -> None:
        """
        Set the amount the item will be repaired.
        
        Half of this value will be subtracted from the experience orb which initiated this event.

        Arguments
        - amount: how much damage will be repaired on the item
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
