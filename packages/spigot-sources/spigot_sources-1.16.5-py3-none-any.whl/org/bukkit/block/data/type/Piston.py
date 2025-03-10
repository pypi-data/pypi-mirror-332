"""
Python module generated from Java source file org.bukkit.block.data.type.Piston

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Piston(Directional):
    """
    'extended' denotes whether the piston head is currently extended or not.
    """

    def isExtended(self) -> bool:
        """
        Gets the value of the 'extended' property.

        Returns
        - the 'extended' value
        """
        ...


    def setExtended(self, extended: bool) -> None:
        """
        Sets the value of the 'extended' property.

        Arguments
        - extended: the new 'extended' value
        """
        ...
