"""
Python module generated from Java source file org.bukkit.block.Sign

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.block import *
from org.bukkit.block.sign import Side
from org.bukkit.block.sign import SignSide
from org.bukkit.entity import Player
from org.bukkit.material import Colorable
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

        Deprecated
        - A sign may have multiple writable sides now. Use Sign.getSide(Side) and SignSide.getLines().
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

        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.getLine(int).
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

        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.setLine(int, String).
        """
        ...


    def isEditable(self) -> bool:
        """
        Marks whether this sign can be edited by players.

        Returns
        - if this sign is currently editable

        Deprecated
        - use .isWaxed() instead
        """
        ...


    def setEditable(self, editable: bool) -> None:
        """
        Marks whether this sign can be edited by players.

        Arguments
        - editable: if this sign is currently editable

        Deprecated
        - use .setWaxed(boolean) instead
        """
        ...


    def isWaxed(self) -> bool:
        """
        Gets whether or not this sign has been waxed. If a sign has been waxed, it
        cannot be edited by a player.

        Returns
        - if this sign is waxed
        """
        ...


    def setWaxed(self, waxed: bool) -> None:
        """
        Sets whether or not this sign has been waxed. If a sign has been waxed, it
        cannot be edited by a player.

        Arguments
        - waxed: if this sign is waxed
        """
        ...


    def isGlowingText(self) -> bool:
        """
        Gets whether this sign has glowing text. Only affects the Side.FRONT.

        Returns
        - if this sign has glowing text

        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.isGlowingText().
        """
        ...


    def setGlowingText(self, glowing: bool) -> None:
        """
        Sets whether this sign has glowing text. Only affects the Side.FRONT.

        Arguments
        - glowing: if this sign has glowing text

        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.setGlowingText(boolean).
        """
        ...


    def getColor(self) -> "DyeColor":
        """
        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.getColor().
        """
        ...


    def setColor(self, color: "DyeColor") -> None:
        """
        Deprecated
        - A sign may have multiple writable sides now. Use .getSide(Side) and SignSide.setColor(org.bukkit.DyeColor).
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


    def getTargetSide(self, player: "Player") -> "SignSide":
        """
        Gets the side of this sign the given player is currently standing on.

        Arguments
        - player: the player

        Returns
        - the side the player is standing on
        """
        ...


    def getAllowedEditor(self) -> "Player":
        """
        Gets the player that is currently allowed to edit this sign. 
        Edits from other players will be rejected if this value is not null.

        Returns
        - the player allowed to edit this sign, or null
        """
        ...
