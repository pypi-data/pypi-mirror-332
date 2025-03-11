"""
Python module generated from Java source file org.bukkit.entity.Frog

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import *
from org.bukkit.util import OldEnum
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
