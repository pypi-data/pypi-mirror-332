"""
Python module generated from Java source file org.bukkit.block.data.type.Lantern

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Lantern(Waterlogged):
    """
    'hanging' denotes whether the lantern is hanging from a block.
    """

    def isHanging(self) -> bool:
        """
        Gets the value of the 'hanging' property.

        Returns
        - the 'hanging' value
        """
        ...


    def setHanging(self, hanging: bool) -> None:
        """
        Sets the value of the 'hanging' property.

        Arguments
        - hanging: the new 'hanging' value
        """
        ...
