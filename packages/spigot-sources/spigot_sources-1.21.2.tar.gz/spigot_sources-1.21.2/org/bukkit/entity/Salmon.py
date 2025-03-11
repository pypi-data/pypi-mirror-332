"""
Python module generated from Java source file org.bukkit.entity.Salmon

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Salmon(Fish):
    """
    Represents a salmon fish.
    """

    def getVariant(self) -> "Variant":
        """
        Get the variant of this salmon.

        Returns
        - salmon variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this salmon.

        Arguments
        - variant: salmon variant
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a salmon - ie its size.
        """

        SMALL = 0
        """
        Small salmon.
        """
        MEDIUM = 1
        """
        Default salmon.
        """
        LARGE = 2
        """
        Large salmon.
        """
