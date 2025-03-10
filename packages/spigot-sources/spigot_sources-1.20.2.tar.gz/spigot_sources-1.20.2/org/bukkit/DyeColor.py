"""
Python module generated from Java source file org.bukkit.DyeColor

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableMap
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class DyeColor(Enum):
    """
    All supported color values for dyes and cloth
    """

    WHITE = (0x0, 0xF, Color.fromRGB(0xF9FFFE), Color.fromRGB(0xF0F0F0))
    """
    Represents white dye.
    """
    ORANGE = (0x1, 0xE, Color.fromRGB(0xF9801D), Color.fromRGB(0xEB8844))
    """
    Represents orange dye.
    """
    MAGENTA = (0x2, 0xD, Color.fromRGB(0xC74EBD), Color.fromRGB(0xC354CD))
    """
    Represents magenta dye.
    """
    LIGHT_BLUE = (0x3, 0xC, Color.fromRGB(0x3AB3DA), Color.fromRGB(0x6689D3))
    """
    Represents light blue dye.
    """
    YELLOW = (0x4, 0xB, Color.fromRGB(0xFED83D), Color.fromRGB(0xDECF2A))
    """
    Represents yellow dye.
    """
    LIME = (0x5, 0xA, Color.fromRGB(0x80C71F), Color.fromRGB(0x41CD34))
    """
    Represents lime dye.
    """
    PINK = (0x6, 0x9, Color.fromRGB(0xF38BAA), Color.fromRGB(0xD88198))
    """
    Represents pink dye.
    """
    GRAY = (0x7, 0x8, Color.fromRGB(0x474F52), Color.fromRGB(0x434343))
    """
    Represents gray dye.
    """
    LIGHT_GRAY = (0x8, 0x7, Color.fromRGB(0x9D9D97), Color.fromRGB(0xABABAB))
    """
    Represents light gray dye.
    """
    CYAN = (0x9, 0x6, Color.fromRGB(0x169C9C), Color.fromRGB(0x287697))
    """
    Represents cyan dye.
    """
    PURPLE = (0xA, 0x5, Color.fromRGB(0x8932B8), Color.fromRGB(0x7B2FBE))
    """
    Represents purple dye.
    """
    BLUE = (0xB, 0x4, Color.fromRGB(0x3C44AA), Color.fromRGB(0x253192))
    """
    Represents blue dye.
    """
    BROWN = (0xC, 0x3, Color.fromRGB(0x835432), Color.fromRGB(0x51301A))
    """
    Represents brown dye.
    """
    GREEN = (0xD, 0x2, Color.fromRGB(0x5E7C16), Color.fromRGB(0x3B511A))
    """
    Represents green dye.
    """
    RED = (0xE, 0x1, Color.fromRGB(0xB02E26), Color.fromRGB(0xB3312C))
    """
    Represents red dye.
    """
    BLACK = (0xF, 0x0, Color.fromRGB(0x1D1D21), Color.fromRGB(0x1E1B1B))
    """
    Represents black dye.
    """


    def getWoolData(self) -> int:
        """
        Gets the associated wool data value representing this color.

        Returns
        - A byte containing the wool data value of this color

        See
        - .getDyeData()

        Deprecated
        - Magic value
        """
        ...


    def getDyeData(self) -> int:
        """
        Gets the associated dye data value representing this color.

        Returns
        - A byte containing the dye data value of this color

        See
        - .getWoolData()

        Deprecated
        - Magic value
        """
        ...


    def getColor(self) -> "Color":
        """
        Gets the color that this dye represents.

        Returns
        - The Color that this dye represents
        """
        ...


    def getFireworkColor(self) -> "Color":
        """
        Gets the firework color that this dye represents.

        Returns
        - The Color that this dye represents
        """
        ...


    @staticmethod
    def getByWoolData(data: int) -> "DyeColor":
        """
        Gets the DyeColor with the given wool data value.

        Arguments
        - data: Wool data value to fetch

        Returns
        - The DyeColor representing the given value, or null if
            it doesn't exist

        See
        - .getByDyeData(byte)

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByDyeData(data: int) -> "DyeColor":
        """
        Gets the DyeColor with the given dye data value.

        Arguments
        - data: Dye data value to fetch

        Returns
        - The DyeColor representing the given value, or null if
            it doesn't exist

        See
        - .getByWoolData(byte)

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByColor(color: "Color") -> "DyeColor":
        """
        Gets the DyeColor with the given color value.

        Arguments
        - color: Color value to get the dye by

        Returns
        - The DyeColor representing the given value, or null if
            it doesn't exist
        """
        ...


    @staticmethod
    def getByFireworkColor(color: "Color") -> "DyeColor":
        """
        Gets the DyeColor with the given firework color value.

        Arguments
        - color: Color value to get dye by

        Returns
        - The DyeColor representing the given value, or null if
            it doesn't exist
        """
        ...


    @staticmethod
    def legacyValueOf(name: str) -> "DyeColor":
        """
        Gets the DyeColor for the given name, possibly doing legacy transformations.

        Arguments
        - name: dye name

        Returns
        - dye color

        Deprecated
        - legacy use only
        """
        ...
