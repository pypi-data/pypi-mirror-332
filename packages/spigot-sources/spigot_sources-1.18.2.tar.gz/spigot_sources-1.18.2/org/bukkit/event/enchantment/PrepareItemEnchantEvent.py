"""
Python module generated from Java source file org.bukkit.event.enchantment.PrepareItemEnchantEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.enchantments import EnchantmentOffer
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.enchantment import *
from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PrepareItemEnchantEvent(InventoryEvent, Cancellable):
    """
    Called when an ItemStack is inserted in an enchantment table - can be
    called multiple times
    """

    def __init__(self, enchanter: "Player", view: "InventoryView", table: "Block", item: "ItemStack", offers: list["EnchantmentOffer"], bonus: int):
        ...


    def getEnchanter(self) -> "Player":
        """
        Gets the player enchanting the item

        Returns
        - enchanting player
        """
        ...


    def getEnchantBlock(self) -> "Block":
        """
        Gets the block being used to enchant the item

        Returns
        - the block used for enchanting
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item to be enchanted.

        Returns
        - ItemStack of item
        """
        ...


    def getExpLevelCostsOffered(self) -> list[int]:
        """
        Get a list of offered experience level costs of the enchantment.

        Returns
        - experience level costs offered

        Deprecated
        - Use .getOffers() instead of this method
        """
        ...


    def getOffers(self) -> list["EnchantmentOffer"]:
        """
        Get a list of available EnchantmentOffer for the player. You can
        modify the values to change the available offers for the player. An offer
        may be null, if there isn't a enchantment offer at a specific slot. There
        are 3 slots in the enchantment table available to modify.

        Returns
        - list of available enchantment offers
        """
        ...


    def getEnchantmentBonus(self) -> int:
        """
        Get enchantment bonus in effect - corresponds to number of bookshelves

        Returns
        - enchantment bonus
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
