"""
Python module generated from Java source file org.bukkit.event.player.PlayerSwapHandItemsEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerSwapHandItemsEvent(PlayerEvent, Cancellable):
    """
    Called when a player swap items between main hand and off hand using the
    hotkey.
    """

    def __init__(self, player: "Player", mainHandItem: "ItemStack", offHandItem: "ItemStack"):
        ...


    def getMainHandItem(self) -> "ItemStack":
        """
        Gets the item switched to the main hand.

        Returns
        - item in the main hand
        """
        ...


    def setMainHandItem(self, mainHandItem: "ItemStack") -> None:
        """
        Sets the item in the main hand.

        Arguments
        - mainHandItem: new item in the main hand
        """
        ...


    def getOffHandItem(self) -> "ItemStack":
        """
        Gets the item switched to the off hand.

        Returns
        - item in the off hand
        """
        ...


    def setOffHandItem(self, offHandItem: "ItemStack") -> None:
        """
        Sets the item in the off hand.

        Arguments
        - offHandItem: new item in the off hand
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
