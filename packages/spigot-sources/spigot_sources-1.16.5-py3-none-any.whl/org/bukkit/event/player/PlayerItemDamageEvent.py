"""
Python module generated from Java source file org.bukkit.event.player.PlayerItemDamageEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

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


class PlayerItemDamageEvent(PlayerEvent, Cancellable):
    """
    Called when an item used by the player takes durability damage as a result of
    being used.
    """

    def __init__(self, player: "Player", what: "ItemStack", damage: int):
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item being damaged.

        Returns
        - the item
        """
        ...


    def getDamage(self) -> int:
        """
        Gets the amount of durability damage this item will be taking.

        Returns
        - durability change
        """
        ...


    def setDamage(self, damage: int) -> None:
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
