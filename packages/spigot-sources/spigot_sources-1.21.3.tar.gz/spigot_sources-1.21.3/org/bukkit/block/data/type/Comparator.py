"""
Python module generated from Java source file org.bukkit.block.data.type.Comparator

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Comparator(Directional, Powerable):
    """
    'mode' indicates what mode this comparator will operate in.
    """

    def getMode(self) -> "Mode":
        """
        Gets the value of the 'mode' property.

        Returns
        - the 'mode' value
        """
        ...


    def setMode(self, mode: "Mode") -> None:
        """
        Sets the value of the 'mode' property.

        Arguments
        - mode: the new 'mode' value
        """
        ...


    class Mode(Enum):
        """
        The mode in which a comparator will operate in.
        """

        COMPARE = 0
        """
        The default mode, similar to a transistor. The comparator will turn
        off if either side input is greater than the rear input.
        """
        SUBTRACT = 1
        """
        Alternate subtraction mode. The output signal strength will be equal
        to max(rear-max(left,right),0).
        """
