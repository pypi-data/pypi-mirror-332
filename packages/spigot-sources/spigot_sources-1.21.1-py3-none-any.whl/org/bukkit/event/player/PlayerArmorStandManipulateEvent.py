"""
Python module generated from Java source file org.bukkit.event.player.PlayerArmorStandManipulateEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import ArmorStand
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerArmorStandManipulateEvent(PlayerInteractEntityEvent):
    """
    Called when a player interacts with an armor stand and will either swap, retrieve or
    place an item.
    """

    def __init__(self, who: "Player", clickedEntity: "ArmorStand", playerItem: "ItemStack", armorStandItem: "ItemStack", slot: "EquipmentSlot", hand: "EquipmentSlot"):
        ...


    def __init__(self, who: "Player", clickedEntity: "ArmorStand", playerItem: "ItemStack", armorStandItem: "ItemStack", slot: "EquipmentSlot"):
        ...


    def getPlayerItem(self) -> "ItemStack":
        """
        Returns the item held by the player.
        
        If this item is empty and the armor stand item is also empty, there will be no
        transaction between the player and the armor stand. If the player's item is empty
        but the armor stand item is not, the player's item will be placed on the armor
        stand. If both items are not empty, the items will be swapped.
        
        In the case that this event is cancelled, the original items will remain the same.

        Returns
        - the item held by the player.
        """
        ...


    def getArmorStandItem(self) -> "ItemStack":
        """
        Returns the item held by the armor stand.
        
        If this item is empty and the player's item is also empty, there will be no
        transaction between the player and the armor stand. If the player's item is empty
        but the armor stand item is not, then the player will obtain the armor stand item.
        In the case that the player's item is not empty but the armor stand item is empty,
        the player's item will be placed on the armor stand. If both items are not empty,
        the items will be swapped.
        
        In the case that the event is cancelled the original items will remain the same.

        Returns
        - the item held by the armor stand.
        """
        ...


    def getSlot(self) -> "EquipmentSlot":
        """
        Returns the raw item slot of the armor stand in this event.

        Returns
        - the index of the item obtained or placed of the armor stand.
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        
        
        Note that this is not the hand of the armor stand that was changed, but rather
        the hand used by the player to swap items with the armor stand.
        """
        ...


    def getRightClicked(self) -> "ArmorStand":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
