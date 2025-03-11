"""
Python module generated from Java source file org.bukkit.event.player.PlayerItemBreakEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerItemBreakEvent(PlayerEvent):
    """
    Fired when a player's item breaks (such as a shovel or flint and steel).
    
    After this event, the item's amount will be set to `item amount - 1`
    and its durability will be reset to 0.
    """

    def __init__(self, player: "Player", brokenItem: "ItemStack"):
        ...


    def getBrokenItem(self) -> "ItemStack":
        """
        Gets the item that broke

        Returns
        - The broken item
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
