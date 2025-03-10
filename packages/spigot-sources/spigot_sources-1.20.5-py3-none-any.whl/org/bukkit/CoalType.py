"""
Python module generated from Java source file org.bukkit.CoalType

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class CoalType(Enum):
    """
    Represents the two types of coal
    """

    COAL = (0x0)
    CHARCOAL = (0x1)


    def getData(self) -> int:
        """
        Gets the associated data value representing this type of coal

        Returns
        - A byte containing the data value of this coal type

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByData(data: int) -> "CoalType":
        """
        Gets the type of coal with the given data value

        Arguments
        - data: Data value to fetch

        Returns
        - The CoalType representing the given value, or null if
            it doesn't exist

        Deprecated
        - Magic value
        """
        ...
