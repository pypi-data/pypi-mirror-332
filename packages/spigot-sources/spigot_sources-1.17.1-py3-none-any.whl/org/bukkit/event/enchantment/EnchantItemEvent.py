"""
Python module generated from Java source file org.bukkit.event.enchantment.EnchantItemEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import Validate
from org.bukkit.block import Block
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.enchantment import *
from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class EnchantItemEvent(InventoryEvent, Cancellable):
    """
    Called when an ItemStack is successfully enchanted (currently at
    enchantment table)
    """

    def __init__(self, enchanter: "Player", view: "InventoryView", table: "Block", item: "ItemStack", level: int, enchants: dict["Enchantment", "Integer"], i: int):
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
        Gets the item to be enchanted (can be modified)

        Returns
        - ItemStack of item
        """
        ...


    def getExpLevelCost(self) -> int:
        """
        Gets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        Returns
        - experience level cost
        """
        ...


    def setExpLevelCost(self, level: int) -> None:
        """
        Sets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        Arguments
        - level: - cost in levels
        """
        ...


    def getEnchantsToAdd(self) -> dict["Enchantment", "Integer"]:
        """
        Get map of enchantment (levels, keyed by type) to be added to item
        (modify map returned to change values). Note: Any enchantments not
        allowed for the item will be ignored

        Returns
        - map of enchantment levels, keyed by enchantment
        """
        ...


    def whichButton(self) -> int:
        """
        Which button was pressed to initiate the enchanting.

        Returns
        - The button index (0, 1, or 2).
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
