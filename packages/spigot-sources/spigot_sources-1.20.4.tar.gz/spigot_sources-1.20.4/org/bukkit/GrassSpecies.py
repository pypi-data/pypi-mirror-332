"""
Python module generated from Java source file org.bukkit.GrassSpecies

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class GrassSpecies(Enum):
    """
    Represents the different types of grass.
    """

    DEAD = (0x0)
    """
    Represents the dead looking grass.
    """
    NORMAL = (0x1)
    """
    Represents the normal grass species.
    """
    FERN_LIKE = (0x2)
    """
    Represents the fern-looking grass species.
    """


    def getData(self) -> int:
        """
        Gets the associated data value representing this species

        Returns
        - A byte containing the data value of this grass species

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByData(data: int) -> "GrassSpecies":
        """
        Gets the GrassSpecies with the given data value

        Arguments
        - data: Data value to fetch

        Returns
        - The GrassSpecies representing the given value, or null
            if it doesn't exist

        Deprecated
        - Magic value
        """
        ...
