"""
Python module generated from Java source file org.bukkit.block.Sign

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.block import *
from org.bukkit.block.sign import Side
from org.bukkit.block.sign import SignSide
from org.bukkit.material import Colorable
from org.jetbrains.annotations.ApiStatus import Experimental
from typing import Any, Callable, Iterable, Tuple


class Sign(TileState, Colorable):
    """
    Represents a captured state of either a SignPost or a WallSign.
    """

    def getLines(self) -> list[str]:
        """
        Gets all the lines of text currently on the Side.FRONT of this sign.

        Returns
        - Array of Strings containing each line of text

        See
        - .getSide(Side)
        """
        ...


    def getLine(self, index: int) -> str:
        """
        Gets the line of text at the specified index.
        
        For example, getLine(0) will return the first line of text on the Side.FRONT.

        Arguments
        - index: Line number to get the text from, starting at 0

        Returns
        - Text on the given line

        Raises
        - IndexOutOfBoundsException: Thrown when the line does not exist

        See
        - .getSide(Side)
        """
        ...


    def setLine(self, index: int, line: str) -> None:
        """
        Sets the line of text at the specified index.
        
        For example, setLine(0, "Line One") will set the first line of text to
        "Line One".

        Arguments
        - index: Line number to set the text at, starting from 0
        - line: New text to set at the specified index

        Raises
        - IndexOutOfBoundsException: If the index is out of the range 0..3

        See
        - .getSide(Side)
        """
        ...


    def isEditable(self) -> bool:
        """
        Marks whether this sign can be edited by players.
        
        This is a special value, which is not persisted. It should only be set if
        a placed sign is manipulated during the BlockPlaceEvent. Behaviour
        outside of this event is undefined.

        Returns
        - if this sign is currently editable
        """
        ...


    def setEditable(self, editable: bool) -> None:
        """
        Marks whether this sign can be edited by players.
        
        This is a special value, which is not persisted. It should only be set if
        a placed sign is manipulated during the BlockPlaceEvent. Behaviour
        outside of this event is undefined.

        Arguments
        - editable: if this sign is currently editable
        """
        ...


    def isGlowingText(self) -> bool:
        """
        Gets whether this sign has glowing text. Only affects the Side.FRONT.

        Returns
        - if this sign has glowing text

        See
        - .getSide(Side)
        """
        ...


    def setGlowingText(self, glowing: bool) -> None:
        """
        Sets whether this sign has glowing text. Only affects the Side.FRONT.

        Arguments
        - glowing: if this sign has glowing text

        See
        - .getSide(Side)
        """
        ...


    def getColor(self) -> "DyeColor":
        """
        See
        - .getSide(Side)
        """
        ...


    def setColor(self, color: "DyeColor") -> None:
        """
        See
        - .getSide(Side)
        """
        ...


    def getSide(self, side: "Side") -> "SignSide":
        """
        Return the side of the sign.

        Arguments
        - side: the side of the sign

        Returns
        - the selected side of the sign
        """
        ...
