"""
Python module generated from Java source file org.bukkit.SandstoneType

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class SandstoneType(Enum):
    """
    Represents the three different types of Sandstone
    """

    CRACKED = (0x0)
    GLYPHED = (0x1)
    SMOOTH = (0x2)


    def getData(self) -> int:
        """
        Gets the associated data value representing this type of sandstone

        Returns
        - A byte containing the data value of this sandstone type

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByData(data: int) -> "SandstoneType":
        """
        Gets the type of sandstone with the given data value

        Arguments
        - data: Data value to fetch

        Returns
        - The SandstoneType representing the given value, or null
            if it doesn't exist

        Deprecated
        - Magic value
        """
        ...
