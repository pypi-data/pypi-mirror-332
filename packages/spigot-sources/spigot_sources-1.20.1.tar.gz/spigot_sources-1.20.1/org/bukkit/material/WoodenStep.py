"""
Python module generated from Java source file org.bukkit.material.WoodenStep

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class WoodenStep(Wood):
    """
    Represents the different types of wooden steps.

    See
    - Material.LEGACY_WOOD_STEP

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a wooden step.
        """
        ...


    def __init__(self, species: "TreeSpecies"):
        """
        Constructs a wooden step of the given tree species.

        Arguments
        - species: the species of the wooden step
        """
        ...


    def __init__(self, species: "TreeSpecies", inv: bool):
        """
        Constructs a wooden step of the given type and tree species, either
        inverted or not.

        Arguments
        - species: the species of the wooden step
        - inv: True the step is at the top of the block
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


    def isInverted(self) -> bool:
        """
        Test if step is inverted

        Returns
        - True if inverted (top half), False if normal (bottom half)
        """
        ...


    def setInverted(self, inv: bool) -> None:
        """
        Set step inverted state

        Arguments
        - inv: - True if step is inverted (top half), False if step is normal
        (bottom half)
        """
        ...


    def clone(self) -> "WoodenStep":
        ...


    def toString(self) -> str:
        ...
