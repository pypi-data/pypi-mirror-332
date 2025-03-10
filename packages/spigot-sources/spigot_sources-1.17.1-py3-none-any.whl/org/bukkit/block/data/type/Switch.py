"""
Python module generated from Java source file org.bukkit.block.data.type.Switch

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data import FaceAttachable
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Switch(Directional, FaceAttachable, Powerable):

    def getFace(self) -> "Face":
        """
        Gets the value of the 'face' property.

        Returns
        - the 'face' value

        Deprecated
        - use .getAttachedFace()
        """
        ...


    def setFace(self, face: "Face") -> None:
        """
        Sets the value of the 'face' property.

        Arguments
        - face: the new 'face' value

        Deprecated
        - use .getAttachedFace()
        """
        ...


    class Face(Enum):
        """
        The face to which a switch type block is stuck.

        Deprecated
        - use AttachedFace
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
