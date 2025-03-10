"""
Python module generated from Java source file org.bukkit.block.data.Waterlogged

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Waterlogged(BlockData):
    """
    'waterlogged' denotes whether this block has fluid in it.
    """

    def isWaterlogged(self) -> bool:
        """
        Gets the value of the 'waterlogged' property.

        Returns
        - the 'waterlogged' value
        """
        ...


    def setWaterlogged(self, waterlogged: bool) -> None:
        """
        Sets the value of the 'waterlogged' property.

        Arguments
        - waterlogged: the new 'waterlogged' value
        """
        ...
