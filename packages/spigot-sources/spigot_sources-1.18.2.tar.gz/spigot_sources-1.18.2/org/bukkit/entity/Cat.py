"""
Python module generated from Java source file org.bukkit.entity.Cat

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import DyeColor
from org.bukkit.entity import *
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


    class Type(Enum):
        """
        Represents the various different cat types there are.
        """

        TABBY = 0
        BLACK = 1
        RED = 2
        SIAMESE = 3
        BRITISH_SHORTHAIR = 4
        CALICO = 5
        PERSIAN = 6
        RAGDOLL = 7
        WHITE = 8
        JELLIE = 9
        ALL_BLACK = 10
