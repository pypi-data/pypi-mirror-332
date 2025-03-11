"""
Python module generated from Java source file org.bukkit.TreeSpecies

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class TreeSpecies(Enum):
    """
    Represents the different species of trees regardless of size.

    Deprecated
    - Deprecated, see usage methods for replacement(s)
    """

    GENERIC = (0x0)
    """
    Represents the common tree species.
    """
    REDWOOD = (0x1)
    """
    Represents the darker barked/leaved tree species.
    """
    BIRCH = (0x2)
    """
    Represents birches.
    """
    JUNGLE = (0x3)
    """
    Represents jungle trees.
    """
    ACACIA = (0x4)
    """
    Represents acacia trees.
    """
    DARK_OAK = (0x5)
    """
    Represents dark oak trees.
    """


    def getData(self) -> int:
        """
        Gets the associated data value representing this species

        Returns
        - A byte containing the data value of this tree species

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByData(data: int) -> "TreeSpecies":
        """
        Gets the TreeSpecies with the given data value

        Arguments
        - data: Data value to fetch

        Returns
        - The TreeSpecies representing the given value, or null
            if it doesn't exist

        Deprecated
        - Magic value
        """
        ...
