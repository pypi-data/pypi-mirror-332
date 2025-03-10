"""
Python module generated from Java source file net.md_5.bungee.api.ChatColor

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Locale
from java.util import Objects
from java.util.regex import Pattern
from net.md_5.bungee.api import *
from typing import Any, Callable, Iterable, Tuple


class ChatColor:
    """
    Simplistic enumeration of all supported color values for chat.
    """

    COLOR_CHAR = '\u00A7'
    """
    The special character which prefixes all chat colour codes. Use this if
    you need to dynamically convert colour codes from your custom format.
    """
    ALL_CODES = "0123456789AaBbCcDdEeFfKkLlMmNnOoRrXx"
    STRIP_COLOR_PATTERN = Pattern.compile("(?i)" + String.valueOf(COLOR_CHAR) + "[0-9A-FK-ORX]")
    """
    Pattern to remove all colour codes.
    """
    BLACK = ChatColor('0', "black", Color(0x000000))
    """
    Represents black.
    """
    DARK_BLUE = ChatColor('1', "dark_blue", Color(0x0000AA))
    """
    Represents dark blue.
    """
    DARK_GREEN = ChatColor('2', "dark_green", Color(0x00AA00))
    """
    Represents dark green.
    """
    DARK_AQUA = ChatColor('3', "dark_aqua", Color(0x00AAAA))
    """
    Represents dark blue (aqua).
    """
    DARK_RED = ChatColor('4', "dark_red", Color(0xAA0000))
    """
    Represents dark red.
    """
    DARK_PURPLE = ChatColor('5', "dark_purple", Color(0xAA00AA))
    """
    Represents dark purple.
    """
    GOLD = ChatColor('6', "gold", Color(0xFFAA00))
    """
    Represents gold.
    """
    GRAY = ChatColor('7', "gray", Color(0xAAAAAA))
    """
    Represents gray.
    """
    DARK_GRAY = ChatColor('8', "dark_gray", Color(0x555555))
    """
    Represents dark gray.
    """
    BLUE = ChatColor('9', "blue", Color(0x5555FF))
    """
    Represents blue.
    """
    GREEN = ChatColor('a', "green", Color(0x55FF55))
    """
    Represents green.
    """
    AQUA = ChatColor('b', "aqua", Color(0x55FFFF))
    """
    Represents aqua.
    """
    RED = ChatColor('c', "red", Color(0xFF5555))
    """
    Represents red.
    """
    LIGHT_PURPLE = ChatColor('d', "light_purple", Color(0xFF55FF))
    """
    Represents light purple.
    """
    YELLOW = ChatColor('e', "yellow", Color(0xFFFF55))
    """
    Represents yellow.
    """
    WHITE = ChatColor('f', "white", Color(0xFFFFFF))
    """
    Represents white.
    """
    MAGIC = ChatColor('k', "obfuscated")
    """
    Represents magical characters that change around randomly.
    """
    BOLD = ChatColor('l', "bold")
    """
    Makes the text bold.
    """
    STRIKETHROUGH = ChatColor('m', "strikethrough")
    """
    Makes a line appear through the text.
    """
    UNDERLINE = ChatColor('n', "underline")
    """
    Makes the text appear underlined.
    """
    ITALIC = ChatColor('o', "italic")
    """
    Makes the text italic.
    """
    RESET = ChatColor('r', "reset")
    """
    Resets all previous chat colors or formats.
    """


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    @staticmethod
    def stripColor(input: str) -> str:
        """
        Strips the given message of all color codes

        Arguments
        - input: String to strip of color

        Returns
        - A copy of the input string, without any coloring
        """
        ...


    @staticmethod
    def translateAlternateColorCodes(altColorChar: str, textToTranslate: str) -> str:
        ...


    @staticmethod
    def getByChar(code: str) -> "ChatColor":
        """
        Get the colour represented by the specified code.

        Arguments
        - code: the code to search for

        Returns
        - the mapped colour, or null if non exists
        """
        ...


    @staticmethod
    def of(color: "Color") -> "ChatColor":
        ...


    @staticmethod
    def of(string: str) -> "ChatColor":
        ...


    @staticmethod
    def valueOf(name: str) -> "ChatColor":
        """
        See Enum.valueOf(java.lang.Class, java.lang.String).

        Arguments
        - name: color name

        Returns
        - ChatColor

        Deprecated
        - holdover from when this class was an enum
        """
        ...


    @staticmethod
    def values() -> list["ChatColor"]:
        """
        Get an array of all defined colors and formats.

        Returns
        - copied array of all colors and formats

        Deprecated
        - holdover from when this class was an enum
        """
        ...


    def name(self) -> str:
        """
        See Enum.name().

        Returns
        - constant name

        Deprecated
        - holdover from when this class was an enum
        """
        ...


    def ordinal(self) -> int:
        """
        See Enum.ordinal().

        Returns
        - ordinal

        Deprecated
        - holdover from when this class was an enum
        """
        ...
