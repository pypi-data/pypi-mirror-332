"""
Python module generated from Java source file org.bukkit.block.data.type.TechnicalPiston

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class TechnicalPiston(Directional):
    """
    'type' represents the type of piston which this (technical) block corresponds
    to.
    """

    def getType(self) -> "Type":
        """
        Gets the value of the 'type' property.

        Returns
        - the 'type' value
        """
        ...


    def setType(self, type: "Type") -> None:
        """
        Sets the value of the 'type' property.

        Arguments
        - type: the new 'type' value
        """
        ...


    class Type(Enum):
        """
        Different piston variants.
        """

        NORMAL = 0
        """
        A normal piston which does not pull connected blocks backwards on
        retraction.
        """
        STICKY = 1
        """
        A sticky piston which will also retract connected blocks.
        """
