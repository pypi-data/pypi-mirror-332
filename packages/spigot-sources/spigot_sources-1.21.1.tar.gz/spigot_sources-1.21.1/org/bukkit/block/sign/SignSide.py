"""
Python module generated from Java source file org.bukkit.block.sign.SignSide

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.sign import *
from org.bukkit.material import Colorable
from typing import Any, Callable, Iterable, Tuple


class SignSide(Colorable):
    """
    Represents a side of a sign.
    """

    def getLines(self) -> list[str]:
        """
        Gets all the lines of text currently on this side of the sign.

        Returns
        - Array of Strings containing each line of text
        """
        ...


    def getLine(self, index: int) -> str:
        """
        Gets the line of text at the specified index on this side of the sign.
        
        For example, getLine(0) will return the first line of text.

        Arguments
        - index: Line number to get the text from, starting at 0

        Returns
        - Text on the given line

        Raises
        - IndexOutOfBoundsException: Thrown when the line does not exist
        """
        ...


    def setLine(self, index: int, line: str) -> None:
        """
        Sets the line of text at the specified index on this side of the sign.
        
        For example, setLine(0, "Line One") will set the first line of text to
        "Line One".

        Arguments
        - index: Line number to set the text at, starting from 0
        - line: New text to set at the specified index

        Raises
        - IndexOutOfBoundsException: If the index is out of the range 0..3
        """
        ...


    def isGlowingText(self) -> bool:
        """
        Gets whether this side of the sign has glowing text.

        Returns
        - if this side of the sign has glowing text
        """
        ...


    def setGlowingText(self, glowing: bool) -> None:
        """
        Sets whether this side of the sign has glowing text.

        Arguments
        - glowing: if this side of the sign has glowing text
        """
        ...
