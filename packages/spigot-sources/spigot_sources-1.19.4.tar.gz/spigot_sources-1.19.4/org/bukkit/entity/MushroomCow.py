"""
Python module generated from Java source file org.bukkit.entity.MushroomCow

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class MushroomCow(Cow):
    """
    Represents a mushroom Cow
    """

    def getVariant(self) -> "Variant":
        """
        Get the variant of this cow.

        Returns
        - cow variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this cow.

        Arguments
        - variant: cow variant
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a cow - ie its color.
        """

        RED = 0
        """
        Red mushroom cow.
        """
        BROWN = 1
        """
        Brown mushroom cow.
        """
