"""
Python module generated from Java source file org.bukkit.event.player.PlayerBucketEmptyEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class PlayerBucketEmptyEvent(PlayerBucketEvent):
    """
    Called when a player empties a bucket
    """

    def __init__(self, who: "Player", blockClicked: "Block", blockFace: "BlockFace", bucket: "Material", itemInHand: "ItemStack"):
        ...


    def __init__(self, who: "Player", block: "Block", blockClicked: "Block", blockFace: "BlockFace", bucket: "Material", itemInHand: "ItemStack"):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
