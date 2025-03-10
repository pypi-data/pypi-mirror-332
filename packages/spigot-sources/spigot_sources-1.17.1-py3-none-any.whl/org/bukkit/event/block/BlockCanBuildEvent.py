"""
Python module generated from Java source file org.bukkit.event.block.BlockCanBuildEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockCanBuildEvent(BlockEvent):
    """
    Called when we try to place a block, to see if we can build it here or not.
    
    Note:
    
    - The Block returned by getBlock() is the block we are trying to place
        on, not the block we are trying to place.
    - If you want to figure out what is being placed, use .getMaterial() instead.
    """

    def __init__(self, block: "Block", type: "BlockData", canBuild: bool):
        ...


    def __init__(self, block: "Block", player: "Player", type: "BlockData", canBuild: bool):
        """
        Arguments
        - block: the block involved in this event
        - player: the player placing the block
        - type: the id of the block to place
        - canBuild: whether we can build
        """
        ...


    def isBuildable(self) -> bool:
        """
        Gets whether or not the block can be built here.
        
        By default, returns Minecraft's answer on whether the block can be
        built here or not.

        Returns
        - boolean whether or not the block can be built
        """
        ...


    def setBuildable(self, cancel: bool) -> None:
        """
        Sets whether the block can be built here or not.

        Arguments
        - cancel: True if you want to allow the block to be built here
            despite Minecraft's default behaviour
        """
        ...


    def getMaterial(self) -> "Material":
        """
        Gets the Material that we are trying to place.

        Returns
        - The Material that we are trying to place
        """
        ...


    def getBlockData(self) -> "BlockData":
        """
        Gets the BlockData that we are trying to place.

        Returns
        - The BlockData that we are trying to place
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player who placed the block involved in this event.
        
        May be null for legacy calls of the event.

        Returns
        - The Player who placed the block involved in this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
