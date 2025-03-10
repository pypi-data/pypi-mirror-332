"""
Python module generated from Java source file org.bukkit.event.block.BlockMultiPlaceEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableList
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockMultiPlaceEvent(BlockPlaceEvent):
    """
    Fired when a single block placement action of a player triggers the
    creation of multiple blocks(e.g. placing a bed block). The block returned
    by .getBlockPlaced() and its related methods is the block where
    the placed block would exist if the placement only affected a single
    block.
    """

    def __init__(self, states: list["BlockState"], clicked: "Block", itemInHand: "ItemStack", thePlayer: "Player", canBuild: bool):
        ...


    def getReplacedBlockStates(self) -> list["BlockState"]:
        """
        Gets a list of blockstates for all blocks which were replaced by the
        placement of the new blocks. Most of these blocks will just have a
        Material type of AIR.

        Returns
        - immutable list of replaced BlockStates
        """
        ...
