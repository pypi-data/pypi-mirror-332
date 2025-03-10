"""
Python module generated from Java source file org.bukkit.block.data.FaceAttachable

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class FaceAttachable(BlockData):
    """
    'face' represents the face to which a lever or button is stuck.
    
    This is used in conjunction with Directional to compute the
    orientation of these blocks.
    """

    def getAttachedFace(self) -> "AttachedFace":
        """
        Gets the value of the 'face' property.

        Returns
        - the 'face' value
        """
        ...


    def setAttachedFace(self, face: "AttachedFace") -> None:
        """
        Sets the value of the 'face' property.

        Arguments
        - face: the new 'face' value
        """
        ...


    class AttachedFace(Enum):
        """
        The face to which a switch type block is stuck.
        """

        FLOOR = 0
        """
        The switch is mounted to the floor and pointing upwards.
        """
        WALL = 1
        """
        The switch is mounted to the wall.
        """
        CEILING = 2
        """
        The switch is mounted to the ceiling and pointing dowanrds.
        """
