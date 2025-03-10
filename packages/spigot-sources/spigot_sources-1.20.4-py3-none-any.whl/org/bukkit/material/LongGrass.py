"""
Python module generated from Java source file org.bukkit.material.LongGrass

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GrassSpecies
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class LongGrass(MaterialData):
    """
    Represents the different types of long grasses.

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, species: "GrassSpecies"):
        ...


    def __init__(self, type: "Material"):
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


    def getSpecies(self) -> "GrassSpecies":
        """
        Gets the current species of this grass

        Returns
        - GrassSpecies of this grass
        """
        ...


    def setSpecies(self, species: "GrassSpecies") -> None:
        """
        Sets the species of this grass

        Arguments
        - species: New species of this grass
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "LongGrass":
        ...
