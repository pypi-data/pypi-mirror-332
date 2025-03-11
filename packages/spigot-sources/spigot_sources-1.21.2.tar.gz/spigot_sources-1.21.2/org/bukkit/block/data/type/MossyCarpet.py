"""
Python module generated from Java source file org.bukkit.block.data.type.MossyCarpet

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import MinecraftExperimental
from org.bukkit.block import BlockFace
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class MossyCarpet(BlockData):
    """
    This class encompasses the 'north', 'east', 'south', 'west', height flags
    which are used to set the height of a face.
    
    'bottom' denotes whether this is a bottom block.
    """

    def isBottom(self) -> bool:
        """
        Gets the value of the 'bottom' property.

        Returns
        - the 'bottom' value
        """
        ...


    def setBottom(self, bottom: bool) -> None:
        """
        Sets the value of the 'bottom' property.

        Arguments
        - bottom: the new 'bottom' value
        """
        ...


    def getHeight(self, face: "BlockFace") -> "Height":
        """
        Gets the height of the specified face.

        Arguments
        - face: to check

        Returns
        - if face is enabled
        """
        ...


    def setHeight(self, face: "BlockFace", height: "Height") -> None:
        """
        Set the height of the specified face.

        Arguments
        - face: to set
        - height: the height
        """
        ...


    class Height(Enum):
        """
        The different heights a face may have.
        """

        NONE = 0
        """
        Not present.
        """
        LOW = 1
        """
        Low face present.
        """
        TALL = 2
        """
        Tall face present.
        """
