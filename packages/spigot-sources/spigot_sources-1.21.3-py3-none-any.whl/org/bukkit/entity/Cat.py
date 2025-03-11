"""
Python module generated from Java source file org.bukkit.entity.Cat

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import DyeColor
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import *
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Cat(Tameable, Sittable):
    """
    Meow.
    """

    def getCatType(self) -> "Type":
        """
        Gets the current type of this cat.

        Returns
        - Type of the cat.
        """
        ...


    def setCatType(self, type: "Type") -> None:
        """
        Sets the current type of this cat.

        Arguments
        - type: New type of this cat.
        """
        ...


    def getCollarColor(self) -> "DyeColor":
        """
        Get the collar color of this cat

        Returns
        - the color of the collar
        """
        ...


    def setCollarColor(self, color: "DyeColor") -> None:
        """
        Set the collar color of this cat

        Arguments
        - color: the color to apply
        """
        ...
