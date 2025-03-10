"""
Python module generated from Java source file org.bukkit.CropState

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class CropState(Enum):
    """
    Represents the different growth states of crops
    """

    SEEDED = (0x0)
    """
    State when first seeded
    """
    GERMINATED = (0x1)
    """
    First growth stage
    """
    VERY_SMALL = (0x2)
    """
    Second growth stage
    """
    SMALL = (0x3)
    """
    Third growth stage
    """
    MEDIUM = (0x4)
    """
    Fourth growth stage
    """
    TALL = (0x5)
    """
    Fifth growth stage
    """
    VERY_TALL = (0x6)
    """
    Almost ripe stage
    """
    RIPE = (0x7)
    """
    Ripe stage
    """


    def getData(self) -> int:
        """
        Gets the associated data value representing this growth state

        Returns
        - A byte containing the data value of this growth state

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByData(data: int) -> "CropState":
        """
        Gets the CropState with the given data value

        Arguments
        - data: Data value to fetch

        Returns
        - The CropState representing the given value, or null if
            it doesn't exist

        Deprecated
        - Magic value
        """
        ...
