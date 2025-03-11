"""
Python module generated from Java source file org.bukkit.map.MapFont

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ChatColor
from org.bukkit.map import *
from typing import Any, Callable, Iterable, Tuple


class MapFont:
    """
    Represents a bitmap font drawable to a map.
    """

    def setChar(self, ch: str, sprite: "CharacterSprite") -> None:
        """
        Set the sprite for a given character.

        Arguments
        - ch: The character to set the sprite for.
        - sprite: The CharacterSprite to set.

        Raises
        - IllegalStateException: if this font is static.
        """
        ...


    def getChar(self, ch: str) -> "CharacterSprite":
        """
        Get the sprite for a given character.

        Arguments
        - ch: The character to get the sprite for.

        Returns
        - The CharacterSprite associated with the character, or null if
            there is none.
        """
        ...


    def getWidth(self, text: str) -> int:
        """
        Get the width of the given text as it would be rendered using this
        font.

        Arguments
        - text: The text.

        Returns
        - The width in pixels.
        """
        ...


    def getHeight(self) -> int:
        """
        Get the height of this font.

        Returns
        - The height of the font.
        """
        ...


    def isValid(self, text: str) -> bool:
        """
        Check whether the given text is valid.

        Arguments
        - text: The text.

        Returns
        - True if the string contains only defined characters, False
            otherwise.
        """
        ...


    class CharacterSprite:
        """
        Represents the graphics for a single character in a MapFont.
        """

        def __init__(self, width: int, height: int, data: list[bool]):
            ...


        def get(self, row: int, col: int) -> bool:
            """
            Get the value of a pixel of the character.

            Arguments
            - row: The row, in the range [0,8).
            - col: The column, in the range [0,8).

            Returns
            - True if the pixel is solid, False if transparent.
            """
            ...


        def getWidth(self) -> int:
            """
            Get the width of the character sprite.

            Returns
            - The width of the character.
            """
            ...


        def getHeight(self) -> int:
            """
            Get the height of the character sprite.

            Returns
            - The height of the character.
            """
            ...
