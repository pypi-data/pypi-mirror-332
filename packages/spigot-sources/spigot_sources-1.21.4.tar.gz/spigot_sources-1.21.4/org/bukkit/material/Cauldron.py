"""
Python module generated from Java source file org.bukkit.material.Cauldron

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Cauldron(MaterialData):
    """
    Represents a cauldron

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
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


    def __init__(self, data: int):
        """
        Arguments
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def isFull(self) -> bool:
        """
        Check if the cauldron is full.

        Returns
        - True if it is full.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Check if the cauldron is empty.

        Returns
        - True if it is empty.
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Cauldron":
        ...
