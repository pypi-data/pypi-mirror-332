"""
Python module generated from Java source file org.bukkit.event.inventory.FurnaceExtractEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event.block import BlockExpEvent
from org.bukkit.event.inventory import *
from typing import Any, Callable, Iterable, Tuple


class FurnaceExtractEvent(BlockExpEvent):
    """
    This event is called when a player takes items out of the furnace
    """

    def __init__(self, player: "Player", block: "Block", itemType: "Material", itemAmount: int, exp: int):
        ...


    def getPlayer(self) -> "Player":
        """
        Get the player that triggered the event

        Returns
        - the relevant player
        """
        ...


    def getItemType(self) -> "Material":
        """
        Get the Material of the item being retrieved

        Returns
        - the material of the item
        """
        ...


    def getItemAmount(self) -> int:
        """
        Get the item count being retrieved

        Returns
        - the amount of the item
        """
        ...
