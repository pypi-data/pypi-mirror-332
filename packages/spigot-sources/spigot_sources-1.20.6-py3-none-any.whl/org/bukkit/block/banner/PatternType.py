"""
Python module generated from Java source file org.bukkit.block.banner.PatternType

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Keyed
from org.bukkit import MinecraftExperimental
from org.bukkit.MinecraftExperimental import Requires
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.block.banner import *
from typing import Any, Callable, Iterable, Tuple


class PatternType(Enum):

    BASE = ("b", "base")
    SQUARE_BOTTOM_LEFT = ("bl", "square_bottom_left")
    SQUARE_BOTTOM_RIGHT = ("br", "square_bottom_right")
    SQUARE_TOP_LEFT = ("tl", "square_top_left")
    SQUARE_TOP_RIGHT = ("tr", "square_top_right")
    STRIPE_BOTTOM = ("bs", "stripe_bottom")
    STRIPE_TOP = ("ts", "stripe_top")
    STRIPE_LEFT = ("ls", "stripe_left")
    STRIPE_RIGHT = ("rs", "stripe_right")
    STRIPE_CENTER = ("cs", "stripe_center")
    STRIPE_MIDDLE = ("ms", "stripe_middle")
    STRIPE_DOWNRIGHT = ("drs", "stripe_downright")
    STRIPE_DOWNLEFT = ("dls", "stripe_downleft")
    SMALL_STRIPES = ("ss", "small_stripes")
    CROSS = ("cr", "cross")
    STRAIGHT_CROSS = ("sc", "straight_cross")
    TRIANGLE_BOTTOM = ("bt", "triangle_bottom")
    TRIANGLE_TOP = ("tt", "triangle_top")
    TRIANGLES_BOTTOM = ("bts", "triangles_bottom")
    TRIANGLES_TOP = ("tts", "triangles_top")
    DIAGONAL_LEFT = ("ld", "diagonal_left")
    DIAGONAL_UP_RIGHT = ("rd", "diagonal_up_right")
    DIAGONAL_UP_LEFT = ("lud", "diagonal_up_left")
    DIAGONAL_RIGHT = ("rud", "diagonal_right")
    CIRCLE = ("mc", "circle")
    RHOMBUS = ("mr", "rhombus")
    HALF_VERTICAL = ("vh", "half_vertical")
    HALF_HORIZONTAL = ("hh", "half_horizontal")
    HALF_VERTICAL_RIGHT = ("vhr", "half_vertical_right")
    HALF_HORIZONTAL_BOTTOM = ("hhb", "half_horizontal_bottom")
    BORDER = ("bo", "border")
    CURLY_BORDER = ("cbo", "curly_border")
    CREEPER = ("cre", "creeper")
    GRADIENT = ("gra", "gradient")
    GRADIENT_UP = ("gru", "gradient_up")
    BRICKS = ("bri", "bricks")
    SKULL = ("sku", "skull")
    FLOWER = ("flo", "flower")
    MOJANG = ("moj", "mojang")
    GLOBE = ("glb", "globe")
    PIGLIN = ("pig", "piglin")
    FLOW = ("flw", "flow")
    GUSTER = ("gus", "guster")


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
