"""
Python module generated from Java source file org.bukkit.inventory.meta.BannerMeta

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.banner import Pattern
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class BannerMeta(ItemMeta):

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

        Raises
        - IndexOutOfBoundsException: when index is not in [0, numberOfPatterns()) range
        """
        ...


    def removePattern(self, i: int) -> "Pattern":
        """
        Removes the pattern at the specified index

        Arguments
        - i: the index

        Returns
        - the removed pattern

        Raises
        - IndexOutOfBoundsException: when index is not in [0, numberOfPatterns()) range
        """
        ...


    def setPattern(self, i: int, pattern: "Pattern") -> None:
        """
        Sets the pattern at the specified index

        Arguments
        - i: the index
        - pattern: the new pattern

        Raises
        - IndexOutOfBoundsException: when index is not in [0, numberOfPatterns()) range
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
