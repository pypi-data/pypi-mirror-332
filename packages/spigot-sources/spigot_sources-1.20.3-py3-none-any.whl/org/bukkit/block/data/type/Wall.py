"""
Python module generated from Java source file org.bukkit.block.data.type.Wall

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import BlockFace
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Wall(Waterlogged):
    """
    This class encompasses the 'north', 'east', 'south', 'west', height flags
    which are used to set the height of a wall.
    
    'up' denotes whether the well has a center post.
    """

    def isUp(self) -> bool:
        """
        Gets the value of the 'up' property.

        Returns
        - the 'up' value
        """
        ...


    def setUp(self, up: bool) -> None:
        """
        Sets the value of the 'up' property.

        Arguments
        - up: the new 'up' value
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
        The different heights a face of a wall may have.
        """

        NONE = 0
        """
        No wall present.
        """
        LOW = 1
        """
        Low wall present.
        """
        TALL = 2
        """
        Tall wall present.
        """
