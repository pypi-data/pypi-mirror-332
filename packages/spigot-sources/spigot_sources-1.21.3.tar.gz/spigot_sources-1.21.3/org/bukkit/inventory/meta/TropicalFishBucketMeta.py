"""
Python module generated from Java source file org.bukkit.inventory.meta.TropicalFishBucketMeta

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.entity import TropicalFish
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class TropicalFishBucketMeta(ItemMeta):
    """
    Represents a bucket of tropical fish.
    """

    def getPatternColor(self) -> "DyeColor":
        """
        Gets the color of the fish's pattern.
        
        Plugins should check that hasVariant() returns `True` before
        calling this method.

        Returns
        - pattern color
        """
        ...


    def setPatternColor(self, color: "DyeColor") -> None:
        """
        Sets the color of the fish's pattern.
        
        Setting this when hasVariant() returns `False` will initialize
        all other values to unspecified defaults.

        Arguments
        - color: pattern color
        """
        ...


    def getBodyColor(self) -> "DyeColor":
        """
        Gets the color of the fish's body.
        
        Plugins should check that hasVariant() returns `True` before
        calling this method.

        Returns
        - pattern color
        """
        ...


    def setBodyColor(self, color: "DyeColor") -> None:
        """
        Sets the color of the fish's body.
        
        Setting this when hasVariant() returns `False` will initialize
        all other values to unspecified defaults.

        Arguments
        - color: body color
        """
        ...


    def getPattern(self) -> "TropicalFish.Pattern":
        """
        Gets the fish's pattern.
        
        Plugins should check that hasVariant() returns `True` before
        calling this method.

        Returns
        - pattern
        """
        ...


    def setPattern(self, pattern: "TropicalFish.Pattern") -> None:
        """
        Sets the fish's pattern.
        
        Setting this when hasVariant() returns `False` will initialize
        all other values to unspecified defaults.

        Arguments
        - pattern: new pattern
        """
        ...


    def hasVariant(self) -> bool:
        """
        Checks for existence of a variant tag indicating a specific fish will be
        spawned.

        Returns
        - if there is a variant
        """
        ...


    def clone(self) -> "TropicalFishBucketMeta":
        ...
