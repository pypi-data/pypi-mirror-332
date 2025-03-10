"""
Python module generated from Java source file org.bukkit.entity.Cat

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import DyeColor
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
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

        TABBY = ("tabby")
        BLACK = ("black")
        RED = ("red")
        SIAMESE = ("siamese")
        BRITISH_SHORTHAIR = ("british_shorthair")
        CALICO = ("calico")
        PERSIAN = ("persian")
        RAGDOLL = ("ragdoll")
        WHITE = ("white")
        JELLIE = ("jellie")
        ALL_BLACK = ("all_black")


        def getKey(self) -> "NamespacedKey":
            ...
