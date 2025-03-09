"""
Python module generated from Java source file org.bukkit.block.data.type.Gate

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Openable
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Gate(Directional, Openable, Powerable):
    """
    'in_wall" indicates if the fence gate is attached to a wall, and if True the
    texture is lowered by a small amount to blend in better.
    """

    def isInWall(self) -> bool:
        """
        Gets the value of the 'in_wall' property.

        Returns
        - the 'in_wall' value
        """
        ...


    def setInWall(self, inWall: bool) -> None:
        """
        Sets the value of the 'in_wall' property.

        Arguments
        - inWall: the new 'in_wall' value
        """
        ...
