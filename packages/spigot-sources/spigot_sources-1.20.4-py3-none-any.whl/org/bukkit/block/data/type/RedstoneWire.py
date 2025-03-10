"""
Python module generated from Java source file org.bukkit.block.data.type.RedstoneWire

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import BlockFace
from org.bukkit.block.data import AnaloguePowerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class RedstoneWire(AnaloguePowerable):
    """
    'north', 'east', 'south', 'west' represent the types of connections this
    redstone wire has to adjacent blocks.
    """

    def getFace(self, face: "BlockFace") -> "Connection":
        """
        Checks the type of connection on the specified face.

        Arguments
        - face: to check

        Returns
        - connection type
        """
        ...


    def setFace(self, face: "BlockFace", connection: "Connection") -> None:
        """
        Sets the type of connection on the specified face.

        Arguments
        - face: to set
        - connection: the connection type
        """
        ...


    def getAllowedFaces(self) -> set["BlockFace"]:
        """
        Gets all of this faces which may be set on this block.

        Returns
        - all allowed faces
        """
        ...


    class Connection(Enum):
        """
        The way in which a redstone wire can connect to an adjacent block face.
        """

        UP = 0
        """
        The wire travels up the side of the block adjacent to this face.
        """
        SIDE = 1
        """
        The wire travels flat from this face and into the adjacent block.
        """
        NONE = 2
        """
        The wire does not connect in this direction.
        """
