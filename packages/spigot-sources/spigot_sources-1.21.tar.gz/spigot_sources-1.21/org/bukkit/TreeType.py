"""
Python module generated from Java source file org.bukkit.TreeType

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class TreeType(Enum):
    """
    Tree and organic structure types.
    """

    TREE = 0
    """
    Regular tree, no branches
    """
    BIG_TREE = 1
    """
    Regular tree, extra tall with branches
    """
    REDWOOD = 2
    """
    Redwood tree, shaped like a pine tree
    """
    TALL_REDWOOD = 3
    """
    Tall redwood tree with just a few leaves at the top
    """
    BIRCH = 4
    """
    Birch tree
    """
    JUNGLE = 5
    """
    Standard jungle tree; 4 blocks wide and tall
    """
    SMALL_JUNGLE = 6
    """
    Smaller jungle tree; 1 block wide
    """
    COCOA_TREE = 7
    """
    Jungle tree with cocoa plants; 1 block wide
    """
    JUNGLE_BUSH = 8
    """
    Small bush that grows in the jungle
    """
    RED_MUSHROOM = 9
    """
    Big red mushroom; short and fat
    """
    BROWN_MUSHROOM = 10
    """
    Big brown mushroom; tall and umbrella-like
    """
    SWAMP = 11
    """
    Swamp tree (regular with vines on the side)
    """
    ACACIA = 12
    """
    Acacia tree.
    """
    DARK_OAK = 13
    """
    Dark Oak tree.
    """
    MEGA_REDWOOD = 14
    """
    Mega redwood tree; 4 blocks wide and tall
    """
    MEGA_PINE = 15
    """
    Mega pine tree
    """
    TALL_BIRCH = 16
    """
    Tall birch tree
    """
    CHORUS_PLANT = 17
    """
    Large plant native to The End
    """
    CRIMSON_FUNGUS = 18
    """
    Large crimson fungus native to the nether
    """
    WARPED_FUNGUS = 19
    """
    Large warped fungus native to the nether
    """
    AZALEA = 20
    """
    Tree with large roots which grows above lush caves
    """
    MANGROVE = 21
    """
    Mangrove tree
    """
    TALL_MANGROVE = 22
    """
    Tall mangrove tree
    """
    CHERRY = 23
    """
    Cherry tree
    """
