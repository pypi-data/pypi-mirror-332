"""
Python module generated from Java source file org.bukkit.material.Wood

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Wood(MaterialData):
    """
    Represents wood blocks of different species.

    See
    - Material.LEGACY_WOOD_DOUBLE_STEP

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a wood block.
        """
        ...


    def __init__(self, species: "TreeSpecies"):
        """
        Constructs a wood block of the given tree species.

        Arguments
        - species: the species of the wood block
        """
        ...


    def __init__(self, type: "Material"):
        """
        Constructs a wood block of the given type.

        Arguments
        - type: the type of wood block
        """
        ...


    def __init__(self, type: "Material", species: "TreeSpecies"):
        """
        Constructs a wood block of the given type and tree species.

        Arguments
        - type: the type of wood block
        - species: the species of the wood block
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


    def getSpecies(self) -> "TreeSpecies":
        """
        Gets the current species of this wood block

        Returns
        - TreeSpecies of this wood block
        """
        ...


    def setSpecies(self, species: "TreeSpecies") -> None:
        """
        Sets the species of this wood block

        Arguments
        - species: New species of this wood block
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Wood":
        ...
