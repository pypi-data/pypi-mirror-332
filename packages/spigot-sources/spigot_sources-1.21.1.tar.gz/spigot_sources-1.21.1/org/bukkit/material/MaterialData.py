"""
Python module generated from Java source file org.bukkit.material.MaterialData

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.inventory import ItemStack
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class MaterialData(Cloneable):
    """
    Handles specific metadata for certain items or blocks

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

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


    def getData(self) -> int:
        """
        Gets the raw data in this material

        Returns
        - Raw data

        Deprecated
        - Magic value
        """
        ...


    def setData(self, data: int) -> None:
        """
        Sets the raw data of this material

        Arguments
        - data: New raw data

        Deprecated
        - Magic value
        """
        ...


    def getItemType(self) -> "Material":
        """
        Gets the Material that this MaterialData represents

        Returns
        - Material represented by this MaterialData
        """
        ...


    def toItemStack(self) -> "ItemStack":
        """
        Creates a new ItemStack based on this MaterialData

        Returns
        - New ItemStack containing a copy of this MaterialData

        Deprecated
        - this method creates an ItemStack of size 0 which is not
        generally useful. Consider .toItemStack(int).
        """
        ...


    def toItemStack(self, amount: int) -> "ItemStack":
        """
        Creates a new ItemStack based on this MaterialData

        Arguments
        - amount: The stack size of the new stack

        Returns
        - New ItemStack containing a copy of this MaterialData
        """
        ...


    def toString(self) -> str:
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def clone(self) -> "MaterialData":
        ...
