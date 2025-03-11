"""
Python module generated from Java source file org.bukkit.Color

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableMap
from java.util import Arrays
from java.util import Locale
from java.util import Objects
from org.bukkit import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from typing import Any, Callable, Iterable, Tuple


class Color(ConfigurationSerializable):
    """
    A container for a color palette. This class is immutable; the set methods
    return a new color. The color names listed as fields are HTML4 standards,
    but subject to change.
    """

    WHITE = fromRGB(0xFFFFFF)
    """
    White, or (0xFF,0xFF,0xFF) in (R,G,B)
    """
    SILVER = fromRGB(0xC0C0C0)
    """
    Silver, or (0xC0,0xC0,0xC0) in (R,G,B)
    """
    GRAY = fromRGB(0x808080)
    """
    Gray, or (0x80,0x80,0x80) in (R,G,B)
    """
    BLACK = fromRGB(0x000000)
    """
    Black, or (0x00,0x00,0x00) in (R,G,B)
    """
    RED = fromRGB(0xFF0000)
    """
    Red, or (0xFF,0x00,0x00) in (R,G,B)
    """
    MAROON = fromRGB(0x800000)
    """
    Maroon, or (0x80,0x00,0x00) in (R,G,B)
    """
    YELLOW = fromRGB(0xFFFF00)
    """
    Yellow, or (0xFF,0xFF,0x00) in (R,G,B)
    """
    OLIVE = fromRGB(0x808000)
    """
    Olive, or (0x80,0x80,0x00) in (R,G,B)
    """
    LIME = fromRGB(0x00FF00)
    """
    Lime, or (0x00,0xFF,0x00) in (R,G,B)
    """
    GREEN = fromRGB(0x008000)
    """
    Green, or (0x00,0x80,0x00) in (R,G,B)
    """
    AQUA = fromRGB(0x00FFFF)
    """
    Aqua, or (0x00,0xFF,0xFF) in (R,G,B)
    """
    TEAL = fromRGB(0x008080)
    """
    Teal, or (0x00,0x80,0x80) in (R,G,B)
    """
    BLUE = fromRGB(0x0000FF)
    """
    Blue, or (0x00,0x00,0xFF) in (R,G,B)
    """
    NAVY = fromRGB(0x000080)
    """
    Navy, or (0x00,0x00,0x80) in (R,G,B)
    """
    FUCHSIA = fromRGB(0xFF00FF)
    """
    Fuchsia, or (0xFF,0x00,0xFF) in (R,G,B)
    """
    PURPLE = fromRGB(0x800080)
    """
    Purple, or (0x80,0x00,0x80) in (R,G,B)
    """
    ORANGE = fromRGB(0xFFA500)
    """
    Orange, or (0xFF,0xA5,0x00) in (R,G,B)
    """


    @staticmethod
    def fromARGB(alpha: int, red: int, green: int, blue: int) -> "Color":
        """
        Creates a new Color object from an alpha, red, green, and blue

        Arguments
        - alpha: integer from 0-255
        - red: integer from 0-255
        - green: integer from 0-255
        - blue: integer from 0-255

        Returns
        - a new Color object for the alpha, red, green, blue

        Raises
        - IllegalArgumentException: if any value is strictly >255 or <0
        """
        ...


    @staticmethod
    def fromRGB(red: int, green: int, blue: int) -> "Color":
        """
        Creates a new Color object from a red, green, and blue

        Arguments
        - red: integer from 0-255
        - green: integer from 0-255
        - blue: integer from 0-255

        Returns
        - a new Color object for the red, green, blue

        Raises
        - IllegalArgumentException: if any value is strictly >255 or <0
        """
        ...


    @staticmethod
    def fromBGR(blue: int, green: int, red: int) -> "Color":
        """
        Creates a new Color object from a blue, green, and red

        Arguments
        - blue: integer from 0-255
        - green: integer from 0-255
        - red: integer from 0-255

        Returns
        - a new Color object for the red, green, blue

        Raises
        - IllegalArgumentException: if any value is strictly >255 or <0
        """
        ...


    @staticmethod
    def fromRGB(rgb: int) -> "Color":
        """
        Creates a new color object from an integer that contains the red,
        green, and blue bytes in the lowest order 24 bits.

        Arguments
        - rgb: the integer storing the red, green, and blue values

        Returns
        - a new color object for specified values

        Raises
        - IllegalArgumentException: if any data is in the highest order 8
            bits
        """
        ...


    @staticmethod
    def fromARGB(argb: int) -> "Color":
        """
        Creates a new color object from an integer that contains the alpha, red,
        green, and blue bytes.

        Arguments
        - argb: the integer storing the alpha, red, green, and blue values

        Returns
        - a new color object for specified values
        """
        ...


    @staticmethod
    def fromBGR(bgr: int) -> "Color":
        """
        Creates a new color object from an integer that contains the blue,
        green, and red bytes in the lowest order 24 bits.

        Arguments
        - bgr: the integer storing the blue, green, and red values

        Returns
        - a new color object for specified values

        Raises
        - IllegalArgumentException: if any data is in the highest order 8
            bits
        """
        ...


    def getAlpha(self) -> int:
        """
        Gets the alpha component

        Returns
        - alpha component, from 0 to 255
        """
        ...


    def setAlpha(self, alpha: int) -> "Color":
        """
        Creates a new Color object with specified component

        Arguments
        - alpha: the alpha component, from 0 to 255

        Returns
        - a new color object with the red component
        """
        ...


    def getRed(self) -> int:
        """
        Gets the red component

        Returns
        - red component, from 0 to 255
        """
        ...


    def setRed(self, red: int) -> "Color":
        """
        Creates a new Color object with specified component

        Arguments
        - red: the red component, from 0 to 255

        Returns
        - a new color object with the red component
        """
        ...


    def getGreen(self) -> int:
        """
        Gets the green component

        Returns
        - green component, from 0 to 255
        """
        ...


    def setGreen(self, green: int) -> "Color":
        """
        Creates a new Color object with specified component

        Arguments
        - green: the red component, from 0 to 255

        Returns
        - a new color object with the red component
        """
        ...


    def getBlue(self) -> int:
        """
        Gets the blue component

        Returns
        - blue component, from 0 to 255
        """
        ...


    def setBlue(self, blue: int) -> "Color":
        """
        Creates a new Color object with specified component

        Arguments
        - blue: the red component, from 0 to 255

        Returns
        - a new color object with the red component
        """
        ...


    def asRGB(self) -> int:
        """
        Gets the color as an RGB integer.

        Returns
        - An integer representation of this color, as 0xRRGGBB
        """
        ...


    def asARGB(self) -> int:
        """
        Gets the color as an ARGB integer.

        Returns
        - An integer representation of this color, as 0xAARRGGBB
        """
        ...


    def asBGR(self) -> int:
        """
        Gets the color as an BGR integer.

        Returns
        - An integer representation of this color, as 0xBBGGRR
        """
        ...


    def mixDyes(self, *colors: Tuple["DyeColor", ...]) -> "Color":
        ...


    def mixColors(self, *colors: Tuple["Color", ...]) -> "Color":
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(map: dict[str, "Object"]) -> "Color":
        ...


    def toString(self) -> str:
        ...
