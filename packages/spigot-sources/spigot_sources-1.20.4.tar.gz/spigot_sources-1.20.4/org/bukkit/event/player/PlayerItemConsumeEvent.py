"""
Python module generated from Java source file org.bukkit.event.player.PlayerItemConsumeEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerItemConsumeEvent(PlayerEvent, Cancellable):
    """
    This event will fire when a player is finishing consuming an item (food,
    potion, milk bucket).
    
    If the ItemStack is modified the server will use the effects of the new
    item and not remove the original one from the player's inventory.
    
    If the event is cancelled the effect will not be applied and the item will
    not be removed from the player's inventory.
    """

    def __init__(self, player: "Player", item: "ItemStack", hand: "EquipmentSlot"):
        """
        Arguments
        - player: the player consuming
        - item: the ItemStack being consumed
        - hand: the hand that was used
        """
        ...


    def __init__(self, player: "Player", item: "ItemStack"):
        """
        Arguments
        - player: the player consuming
        - item: the ItemStack being consumed

        Deprecated
        - use .PlayerItemConsumeEvent(Player, ItemStack, EquipmentSlot)
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item that is being consumed. Modifying the returned item will
        have no effect, you must use .setItem(org.bukkit.inventory.ItemStack) instead.

        Returns
        - an ItemStack for the item being consumed
        """
        ...


    def setItem(self, item: "ItemStack") -> None:
        """
        Set the item being consumed

        Arguments
        - item: the item being consumed
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand used to consume the item.

        Returns
        - the hand
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
