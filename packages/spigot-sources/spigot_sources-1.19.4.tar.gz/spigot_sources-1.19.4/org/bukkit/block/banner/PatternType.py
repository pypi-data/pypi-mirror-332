"""
Python module generated from Java source file org.bukkit.block.banner.PatternType

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.banner import *
from typing import Any, Callable, Iterable, Tuple


class PatternType(Enum):

    BASE = ("b")
    SQUARE_BOTTOM_LEFT = ("bl")
    SQUARE_BOTTOM_RIGHT = ("br")
    SQUARE_TOP_LEFT = ("tl")
    SQUARE_TOP_RIGHT = ("tr")
    STRIPE_BOTTOM = ("bs")
    STRIPE_TOP = ("ts")
    STRIPE_LEFT = ("ls")
    STRIPE_RIGHT = ("rs")
    STRIPE_CENTER = ("cs")
    STRIPE_MIDDLE = ("ms")
    STRIPE_DOWNRIGHT = ("drs")
    STRIPE_DOWNLEFT = ("dls")
    STRIPE_SMALL = ("ss")
    CROSS = ("cr")
    STRAIGHT_CROSS = ("sc")
    TRIANGLE_BOTTOM = ("bt")
    TRIANGLE_TOP = ("tt")
    TRIANGLES_BOTTOM = ("bts")
    TRIANGLES_TOP = ("tts")
    DIAGONAL_LEFT = ("ld")
    DIAGONAL_RIGHT = ("rd")
    DIAGONAL_LEFT_MIRROR = ("lud")
    DIAGONAL_RIGHT_MIRROR = ("rud")
    CIRCLE_MIDDLE = ("mc")
    RHOMBUS_MIDDLE = ("mr")
    HALF_VERTICAL = ("vh")
    HALF_HORIZONTAL = ("hh")
    HALF_VERTICAL_MIRROR = ("vhr")
    HALF_HORIZONTAL_MIRROR = ("hhb")
    BORDER = ("bo")
    CURLY_BORDER = ("cbo")
    CREEPER = ("cre")
    GRADIENT = ("gra")
    GRADIENT_UP = ("gru")
    BRICKS = ("bri")
    SKULL = ("sku")
    FLOWER = ("flo")
    MOJANG = ("moj")
    GLOBE = ("glb")
    PIGLIN = ("pig")


    def getIdentifier(self) -> str:
        """
        Returns the identifier used to represent
        this pattern type

        Returns
        - the pattern's identifier
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
        """
        ...
