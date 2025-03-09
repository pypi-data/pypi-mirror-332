"""
Python module generated from Java source file org.bukkit.entity.Frog

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Frog(Animals):
    """
    A Frog.
    """

    def getTongueTarget(self) -> "Entity":
        """
        Gets the tongue target of this frog.

        Returns
        - tongue target or null if not set
        """
        ...


    def setTongueTarget(self, target: "Entity") -> None:
        """
        Sets the tongue target of this frog.

        Arguments
        - target: tongue target or null to clear
        """
        ...


    def getVariant(self) -> "Variant":
        """
        Get the variant of this frog.

        Returns
        - frog variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this frog.

        Arguments
        - variant: frog variant
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a frog - ie its color.
        """

        TEMPERATE = 0
        """
        Temperate (brown-orange) frog.
        """
        WARM = 1
        """
        Warm (gray) frog.
        """
        COLD = 2
        """
        Cold (green) frog.
        """


        def getKey(self) -> "NamespacedKey":
            ...
