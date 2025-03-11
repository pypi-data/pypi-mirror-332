"""
Python module generated from Java source file org.bukkit.event.player.PlayerRiptideEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class PlayerRiptideEvent(PlayerEvent):
    """
    This event is fired when the player activates the riptide enchantment, using
    their trident to propel them through the air.
    
    N.B. the riptide action is currently performed client side, so manipulating
    the player in this event may have undesired effects.
    """

    def __init__(self, who: "Player", item: "ItemStack", velocity: "Vector"):
        ...


    def __init__(self, who: "Player", item: "ItemStack"):
        ...


    def getItem(self) -> "ItemStack":
        """
        Gets the item containing the used enchantment.

        Returns
        - held enchanted item
        """
        ...


    def getVelocity(self) -> "Vector":
        """
        Get the velocity applied to the player as a result of this riptide.

        Returns
        - the riptide velocity
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
