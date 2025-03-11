"""
Python module generated from Java source file org.bukkit.material.Leaves

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Leaves(Wood):
    """
    Represents the different types of leaf block that may be permanent or can
    decay when too far from a log.

    See
    - Material.LEGACY_LEAVES_2

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a leaf block.
        """
        ...


    def __init__(self, species: "TreeSpecies"):
        """
        Constructs a leaf block of the given tree species.

        Arguments
        - species: the species of the wood block
        """
        ...


    def __init__(self, species: "TreeSpecies", isDecayable: bool):
        """
        Constructs a leaf block of the given tree species and flag for whether
        this leaf block will disappear when too far from a log.

        Arguments
        - species: the species of the wood block
        - isDecayable: whether the block is permanent or can disappear
        """
        ...


    def __init__(self, type: "Material"):
        """
        Constructs a leaf block of the given type.

        Arguments
        - type: the type of leaf block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies"):
        """
        Constructs a leaf block of the given type and tree species.

        Arguments
        - type: the type of leaf block
        - species: the species of the wood block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies", isDecayable: bool):
        """
        Constructs a leaf block of the given type and tree species and flag for
        whether this leaf block will disappear when too far from a log.

        Arguments
        - type: the type of leaf block
        - species: the species of the wood block
        - isDecayable: whether the block is permanent or can disappear
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


    def isDecaying(self) -> bool:
        """
        Checks if this leaf block is in the process of decaying

        Returns
        - True if the leaf block is in the process of decaying
        """
        ...


    def setDecaying(self, isDecaying: bool) -> None:
        """
        Set whether this leaf block is in the process of decaying

        Arguments
        - isDecaying: whether the block is decaying or not
        """
        ...


    def isDecayable(self) -> bool:
        """
        Checks if this leaf block is permanent or can decay when too far from a
        log

        Returns
        - True if the leaf block is permanent or can decay when too far
        from a log
        """
        ...


    def setDecayable(self, isDecayable: bool) -> None:
        """
        Set whether this leaf block will disappear when too far from a log

        Arguments
        - isDecayable: whether the block is permanent or can disappear
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Leaves":
        ...
