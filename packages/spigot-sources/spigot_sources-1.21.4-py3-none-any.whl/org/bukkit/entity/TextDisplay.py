"""
Python module generated from Java source file org.bukkit.entity.TextDisplay

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Color
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class TextDisplay(Display):
    """
    Represents a text display entity.
    """

    def getText(self) -> str:
        """
        Gets the displayed text.

        Returns
        - the displayed text.
        """
        ...


    def setText(self, text: str) -> None:
        """
        Sets the displayed text.

        Arguments
        - text: the new text
        """
        ...


    def getLineWidth(self) -> int:
        """
        Gets the maximum line width before wrapping.

        Returns
        - the line width
        """
        ...


    def setLineWidth(self, width: int) -> None:
        """
        Sets the maximum line width before wrapping.

        Arguments
        - width: new line width
        """
        ...


    def getBackgroundColor(self) -> "Color":
        """
        Gets the text background color.

        Returns
        - the background color
        """
        ...


    def setBackgroundColor(self, color: "Color") -> None:
        """
        Sets the text background color.

        Arguments
        - color: new background color
        """
        ...


    def getTextOpacity(self) -> int:
        """
        Gets the text opacity.

        Returns
        - opacity or -1 if not set
        """
        ...


    def setTextOpacity(self, opacity: int) -> None:
        """
        Sets the text opacity.

        Arguments
        - opacity: new opacity or -1 if default
        """
        ...


    def isShadowed(self) -> bool:
        """
        Gets if the text is shadowed.

        Returns
        - shadow status
        """
        ...


    def setShadowed(self, shadow: bool) -> None:
        """
        Sets if the text is shadowed.

        Arguments
        - shadow: if shadowed
        """
        ...


    def isSeeThrough(self) -> bool:
        """
        Gets if the text is see through.

        Returns
        - see through status
        """
        ...


    def setSeeThrough(self, seeThrough: bool) -> None:
        """
        Sets if the text is see through.

        Arguments
        - seeThrough: if see through
        """
        ...


    def isDefaultBackground(self) -> bool:
        """
        Gets if the text has its default background.

        Returns
        - default background
        """
        ...


    def setDefaultBackground(self, defaultBackground: bool) -> None:
        """
        Sets if the text has its default background.

        Arguments
        - defaultBackground: if default
        """
        ...


    def getAlignment(self) -> "TextAlignment":
        """
        Gets the text alignment for this display.

        Returns
        - text alignment
        """
        ...


    def setAlignment(self, alignment: "TextAlignment") -> None:
        """
        Sets the text alignment for this display.

        Arguments
        - alignment: new alignment
        """
        ...


    class TextAlignment(Enum):
        """
        Represents possible text alignments for this display.
        """

        CENTER = 0
        """
        Center aligned text (default).
        """
        LEFT = 1
        """
        Left aligned text.
        """
        RIGHT = 2
        """
        Right aligned text.
        """
