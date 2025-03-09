"""
Python module generated from Java source file org.bukkit.material.Tree

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Tree(Wood):
    """
    Represents the different types of Tree block that face a direction.

    See
    - Material.LEGACY_LOG_2

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a tree block.
        """
        ...


    def __init__(self, species: "TreeSpecies"):
        """
        Constructs a tree block of the given tree species.

        Arguments
        - species: the species of the tree block
        """
        ...


    def __init__(self, species: "TreeSpecies", dir: "BlockFace"):
        """
        Constructs a tree block of the given tree species, and facing the given
        direction.

        Arguments
        - species: the species of the tree block
        - dir: the direction the tree block is facing
        """
        ...


    def __init__(self, type: "Material"):
        """
        Constructs a tree block of the given type.

        Arguments
        - type: the type of tree block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies"):
        """
        Constructs a tree block of the given type and tree species.

        Arguments
        - type: the type of tree block
        - species: the species of the tree block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies", dir: "BlockFace"):
        """
        Constructs a tree block of the given type and tree species, and facing
        the given direction.

        Arguments
        - type: the type of tree block
        - species: the species of the tree block
        - dir: the direction the tree block is facing
        """
        ...


    def __init__(self, type: "Material", data: int):
        """
        Arguments
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def getDirection(self) -> "BlockFace":
        """
        Get direction of the log

        Returns
        - one of:
        
        - BlockFace.TOP for upright (default)
        - BlockFace.NORTH (east-west)
        - BlockFace.WEST (north-south)
        - BlockFace.SELF (directionless)
        """
        ...


    def setDirection(self, dir: "BlockFace") -> None:
        """
        Set direction of the log

        Arguments
        - dir: - direction of end of log (BlockFace.SELF for no direction)
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Tree":
        ...
