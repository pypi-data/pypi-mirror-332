"""
Python module generated from Java source file net.md_5.bungee.api.chat.ComponentStyle

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ComponentStyle(Cloneable):
    """
    Represents a style that may be applied to a BaseComponent.
    """

    def getColor(self) -> "ChatColor":
        """
        Returns the color of this style. May return null.

        Returns
        - the color of this style, or null if default color
        """
        ...


    def hasColor(self) -> bool:
        """
        Returns whether or not this style has a color set.

        Returns
        - whether a color is set
        """
        ...


    def getFont(self) -> str:
        """
        Returns the font of this style. May return null.

        Returns
        - the font of this style, or null if default font
        """
        ...


    def hasFont(self) -> bool:
        """
        Returns whether or not this style has a font set.

        Returns
        - whether a font is set
        """
        ...


    def isBold(self) -> bool:
        """
        Returns whether this style is bold.

        Returns
        - whether the style is bold
        """
        ...


    def isBoldRaw(self) -> "Boolean":
        """
        Returns whether this style is bold. May return null.

        Returns
        - whether the style is bold, or null if not set
        """
        ...


    def isItalic(self) -> bool:
        """
        Returns whether this style is italic. May return null.

        Returns
        - whether the style is italic
        """
        ...


    def isItalicRaw(self) -> "Boolean":
        """
        Returns whether this style is italic. May return null.

        Returns
        - whether the style is italic, or null if not set
        """
        ...


    def isUnderlined(self) -> bool:
        """
        Returns whether this style is underlined.

        Returns
        - whether the style is underlined
        """
        ...


    def isUnderlinedRaw(self) -> "Boolean":
        """
        Returns whether this style is underlined. May return null.

        Returns
        - whether the style is underlined, or null if not set
        """
        ...


    def isStrikethrough(self) -> bool:
        """
        Returns whether this style is strikethrough

        Returns
        - whether the style is strikethrough
        """
        ...


    def isStrikethroughRaw(self) -> "Boolean":
        """
        Returns whether this style is strikethrough. May return null.

        Returns
        - whether the style is strikethrough, or null if not set
        """
        ...


    def isObfuscated(self) -> bool:
        """
        Returns whether this style is obfuscated.

        Returns
        - whether the style is obfuscated
        """
        ...


    def isObfuscatedRaw(self) -> "Boolean":
        """
        Returns whether this style is obfuscated. May return null.

        Returns
        - whether the style is obfuscated, or null if not set
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns whether this style has any formatting explicitly set.

        Returns
        - True if at least one value is set, False if none are set
        """
        ...


    def clone(self) -> "ComponentStyle":
        ...


    @staticmethod
    def builder() -> "ComponentStyleBuilder":
        """
        Get a new ComponentStyleBuilder.

        Returns
        - the builder
        """
        ...


    @staticmethod
    def builder(other: "ComponentStyle") -> "ComponentStyleBuilder":
        """
        Get a new ComponentStyleBuilder with values initialized to the
        style values of the supplied ComponentStyle.

        Arguments
        - other: the component style whose values to copy into the builder

        Returns
        - the builder
        """
        ...
