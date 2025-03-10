"""
Python module generated from Java source file org.bukkit.material.Sapling

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Sapling(Wood):
    """
    Represents the different types of Tree block that face a direction.

    See
    - Material.LEGACY_SAPLING

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a sapling.
        """
        ...


    def __init__(self, species: "TreeSpecies"):
        """
        Constructs a sapling of the given tree species.

        Arguments
        - species: the species of the sapling
        """
        ...


    def __init__(self, species: "TreeSpecies", isInstantGrowable: bool):
        """
        Constructs a sapling of the given tree species and if is it instant
        growable

        Arguments
        - species: the species of the tree block
        - isInstantGrowable: True if the Sapling should grow when next ticked with bonemeal
        """
        ...


    def __init__(self, type: "Material"):
        """
        Constructs a sapling of the given type.

        Arguments
        - type: the type of tree block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies"):
        """
        Constructs a sapling of the given type and tree species.

        Arguments
        - type: the type of sapling
        - species: the species of the sapling
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies", isInstantGrowable: bool):
        """
        Constructs a sapling of the given type and tree species and if is it
        instant growable

        Arguments
        - type: the type of sapling
        - species: the species of the sapling
        - isInstantGrowable: True if the Sapling should grow when next ticked
        with bonemeal
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


    def isInstantGrowable(self) -> bool:
        """
        Checks if the Sapling would grow when next ticked with bonemeal

        Returns
        - True if the Sapling would grow when next ticked with bonemeal
        """
        ...


    def setIsInstantGrowable(self, isInstantGrowable: bool) -> None:
        """
        Set whether this sapling will grow when next ticked with bonemeal

        Arguments
        - isInstantGrowable: True if the Sapling should grow when next ticked
        with bonemeal
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Sapling":
        ...
