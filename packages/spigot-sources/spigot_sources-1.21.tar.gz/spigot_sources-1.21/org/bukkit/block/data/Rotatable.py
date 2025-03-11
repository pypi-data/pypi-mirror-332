"""
Python module generated from Java source file org.bukkit.block.data.Rotatable

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Rotatable(BlockData):
    """
    'rotation' represents the current rotation of this block.
    """

    def getRotation(self) -> "BlockFace":
        """
        Gets the value of the 'rotation' property.

        Returns
        - the 'rotation' value
        """
        ...


    def setRotation(self, rotation: "BlockFace") -> None:
        """
        Sets the value of the 'rotation' property.

        Arguments
        - rotation: the new 'rotation' value
        """
        ...
