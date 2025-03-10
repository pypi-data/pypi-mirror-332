"""
Python module generated from Java source file org.bukkit.block.Banner

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.block import *
from org.bukkit.block.banner import Pattern
from typing import Any, Callable, Iterable, Tuple


class Banner(TileState):
    """
    Represents a captured state of a banner.
    """

    def getBaseColor(self) -> "DyeColor":
        """
        Returns the base color for this banner

        Returns
        - the base color
        """
        ...


    def setBaseColor(self, color: "DyeColor") -> None:
        """
        Sets the base color for this banner.
        **Only valid for shield pseudo banners, otherwise base depends on block
        type**

        Arguments
        - color: the base color
        """
        ...


    def getPatterns(self) -> list["Pattern"]:
        """
        Returns a list of patterns on this banner

        Returns
        - the patterns
        """
        ...


    def setPatterns(self, patterns: list["Pattern"]) -> None:
        """
        Sets the patterns used on this banner

        Arguments
        - patterns: the new list of patterns
        """
        ...


    def addPattern(self, pattern: "Pattern") -> None:
        """
        Adds a new pattern on top of the existing
        patterns

        Arguments
        - pattern: the new pattern to add
        """
        ...


    def getPattern(self, i: int) -> "Pattern":
        """
        Returns the pattern at the specified index

        Arguments
        - i: the index

        Returns
        - the pattern
        """
        ...


    def removePattern(self, i: int) -> "Pattern":
        """
        Removes the pattern at the specified index

        Arguments
        - i: the index

        Returns
        - the removed pattern
        """
        ...


    def setPattern(self, i: int, pattern: "Pattern") -> None:
        """
        Sets the pattern at the specified index

        Arguments
        - i: the index
        - pattern: the new pattern
        """
        ...


    def numberOfPatterns(self) -> int:
        """
        Returns the number of patterns on this
        banner

        Returns
        - the number of patterns
        """
        ...
