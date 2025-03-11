"""
Python module generated from Java source file org.bukkit.ChatColor

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Maps
from enum import Enum
from java.util.regex import Pattern
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class ChatColor(Enum):
    """
    All supported color values for chat
    """

# Static fields
    COLOR_CHAR = '\u00A7'
    """
    The special character which prefixes all chat colour codes. Use this if
    you need to dynamically convert colour codes from your custom format.
    """


    BLACK = ('0', 0x00)
    """
    Represents black
    """
    DARK_BLUE = ('1', 0x1)
    """
    Represents dark blue
    """
    DARK_GREEN = ('2', 0x2)
    """
    Represents dark green
    """
    DARK_AQUA = ('3', 0x3)
    """
    Represents dark blue (aqua)
    """
    DARK_RED = ('4', 0x4)
    """
    Represents dark red
    """
    DARK_PURPLE = ('5', 0x5)
    """
    Represents dark purple
    """
    GOLD = ('6', 0x6)
    """
    Represents gold
    """
    GRAY = ('7', 0x7)
    """
    Represents gray
    """
    DARK_GRAY = ('8', 0x8)
    """
    Represents dark gray
    """
    BLUE = ('9', 0x9)
    """
    Represents blue
    """
    GREEN = ('a', 0xA)
    """
    Represents green
    """
    AQUA = ('b', 0xB)
    """
    Represents aqua
    """
    RED = ('c', 0xC)
    """
    Represents red
    """
    LIGHT_PURPLE = ('d', 0xD)
    """
    Represents light purple
    """
    YELLOW = ('e', 0xE)
    """
    Represents yellow
    """
    WHITE = ('f', 0xF)
    """
    Represents white
    """
    MAGIC = ('k', 0x10, True)
    """
    Represents magical characters that change around randomly
    """
    BOLD = ('l', 0x11, True)
    """
    Makes the text bold.
    """
    STRIKETHROUGH = ('m', 0x12, True)
    """
    Makes a line appear through the text.
    """
    UNDERLINE = ('n', 0x13, True)
    """
    Makes the text appear underlined.
    """
    ITALIC = ('o', 0x14, True)
    """
    Makes the text italic.
    """
    RESET = ('r', 0x15)
    """
    Resets all previous chat colors or formats.
    """


    def asBungee(self) -> "net.md_5.bungee.api.ChatColor":
        ...


    def getChar(self) -> str:
        """
        Gets the char value associated with this color

        Returns
        - A char value of this color code
        """
        ...


    def toString(self) -> str:
        ...


    def isFormat(self) -> bool:
        """
        Checks if this code is a format code as opposed to a color code.

        Returns
        - whether this ChatColor is a format code
        """
        ...


    def isColor(self) -> bool:
        """
        Checks if this code is a color code as opposed to a format code.

        Returns
        - whether this ChatColor is a color code
        """
        ...


    @staticmethod
    def getByChar(code: str) -> "ChatColor":
        """
        Gets the color represented by the specified color code

        Arguments
        - code: Code to check

        Returns
        - Associative org.bukkit.ChatColor with the given code,
            or null if it doesn't exist
        """
        ...


    @staticmethod
    def getByChar(code: str) -> "ChatColor":
        """
        Gets the color represented by the specified color code

        Arguments
        - code: Code to check

        Returns
        - Associative org.bukkit.ChatColor with the given code,
            or null if it doesn't exist
        """
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
        """
        Translates a string using an alternate color code character into a
        string that uses the internal ChatColor.COLOR_CODE color code
        character. The alternate color code character will only be replaced if
        it is immediately followed by 0-9, A-F, a-f, K-O, k-o, R or r.

        Arguments
        - altColorChar: The alternate color code character to replace. Ex: &
        - textToTranslate: Text containing the alternate color code character.

        Returns
        - Text containing the ChatColor.COLOR_CODE color code character.
        """
        ...


    @staticmethod
    def getLastColors(input: str) -> str:
        """
        Gets the ChatColors used at the end of the given input string.

        Arguments
        - input: Input string to retrieve the colors from.

        Returns
        - Any remaining ChatColors to pass onto the next line.
        """
        ...
