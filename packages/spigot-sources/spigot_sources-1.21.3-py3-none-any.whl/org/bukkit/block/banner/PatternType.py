"""
Python module generated from Java source file org.bukkit.block.banner.PatternType

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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
from org.bukkit.block.banner import *
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class PatternType(OldEnum, Keyed):

    BASE = getType("base")
    SQUARE_BOTTOM_LEFT = getType("square_bottom_left")
    SQUARE_BOTTOM_RIGHT = getType("square_bottom_right")
    SQUARE_TOP_LEFT = getType("square_top_left")
    SQUARE_TOP_RIGHT = getType("square_top_right")
    STRIPE_BOTTOM = getType("stripe_bottom")
    STRIPE_TOP = getType("stripe_top")
    STRIPE_LEFT = getType("stripe_left")
    STRIPE_RIGHT = getType("stripe_right")
    STRIPE_CENTER = getType("stripe_center")
    STRIPE_MIDDLE = getType("stripe_middle")
    STRIPE_DOWNRIGHT = getType("stripe_downright")
    STRIPE_DOWNLEFT = getType("stripe_downleft")
    SMALL_STRIPES = getType("small_stripes")
    CROSS = getType("cross")
    STRAIGHT_CROSS = getType("straight_cross")
    TRIANGLE_BOTTOM = getType("triangle_bottom")
    TRIANGLE_TOP = getType("triangle_top")
    TRIANGLES_BOTTOM = getType("triangles_bottom")
    TRIANGLES_TOP = getType("triangles_top")
    DIAGONAL_LEFT = getType("diagonal_left")
    DIAGONAL_UP_RIGHT = getType("diagonal_up_right")
    DIAGONAL_UP_LEFT = getType("diagonal_up_left")
    DIAGONAL_RIGHT = getType("diagonal_right")
    CIRCLE = getType("circle")
    RHOMBUS = getType("rhombus")
    HALF_VERTICAL = getType("half_vertical")
    HALF_HORIZONTAL = getType("half_horizontal")
    HALF_VERTICAL_RIGHT = getType("half_vertical_right")
    HALF_HORIZONTAL_BOTTOM = getType("half_horizontal_bottom")
    BORDER = getType("border")
    CURLY_BORDER = getType("curly_border")
    CREEPER = getType("creeper")
    GRADIENT = getType("gradient")
    GRADIENT_UP = getType("gradient_up")
    BRICKS = getType("bricks")
    SKULL = getType("skull")
    FLOWER = getType("flower")
    MOJANG = getType("mojang")
    GLOBE = getType("globe")
    PIGLIN = getType("piglin")
    FLOW = getType("flow")
    GUSTER = getType("guster")


    def getKey(self) -> "NamespacedKey":
        ...


    def getIdentifier(self) -> str:
        """
        Returns the identifier used to represent
        this pattern type

        Returns
        - the pattern's identifier

        See
        - .getKey

        Deprecated
        - magic value
        """
        ...


    @staticmethod
    def getByIdentifier(identifier: str) -> "PatternType":
        """
        Returns the pattern type which matches the passed
        identifier or null if no matches are found

        Arguments
        - identifier: the identifier

        Returns
        - the matched pattern type or null

        See
        - Registry.BANNER_PATTERN

        Deprecated
        - magic value, use Registry.get(NamespacedKey) instead
        """
        ...


    @staticmethod
    def getType(key: str) -> "PatternType":
        ...


    @staticmethod
    def valueOf(name: str) -> "PatternType":
        """
        Arguments
        - name: of the pattern type.

        Returns
        - the pattern type with the given name.

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["PatternType"]:
        """
        Returns
        - an array of all known pattern types.

        Deprecated
        - use Registry.iterator().
        """
        ...
