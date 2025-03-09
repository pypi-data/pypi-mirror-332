"""
Python module generated from Java source file org.bukkit.entity.TropicalFish

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import DyeColor
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class TropicalFish(Fish):
    """
    Tropical fish.
    """

    def getPatternColor(self) -> "DyeColor":
        """
        Gets the color of the fish's pattern.

        Returns
        - pattern color
        """
        ...


    def setPatternColor(self, color: "DyeColor") -> None:
        """
        Sets the color of the fish's pattern

        Arguments
        - color: pattern color
        """
        ...


    def getBodyColor(self) -> "DyeColor":
        """
        Gets the color of the fish's body.

        Returns
        - pattern color
        """
        ...


    def setBodyColor(self, color: "DyeColor") -> None:
        """
        Sets the color of the fish's body

        Arguments
        - color: body color
        """
        ...


    def getPattern(self) -> "Pattern":
        """
        Gets the fish's pattern.

        Returns
        - pattern
        """
        ...


    def setPattern(self, pattern: "Pattern") -> None:
        """
        Sets the fish's pattern

        Arguments
        - pattern: new pattern
        """
        ...


    class Pattern(Enum):
        """
        Enumeration of all different fish patterns. Refer to the
        <a href="https://minecraft.wiki/w/Fish">Minecraft Wiki</a>
        for pictures.
        """

        KOB = 0
        SUNSTREAK = 1
        SNOOPER = 2
        DASHER = 3
        BRINELY = 4
        SPOTTY = 5
        FLOPPER = 6
        STRIPEY = 7
        GLITTER = 8
        BLOCKFISH = 9
        BETTY = 10
        CLAYFISH = 11
