"""
Python module generated from Java source file org.bukkit.block.data.type.BigDripleaf

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class BigDripleaf(Dripleaf):
    """
    'tilt' indicates how far the leaf is tilted.
    """

    def getTilt(self) -> "Tilt":
        """
        Gets the value of the 'tilt' property.

        Returns
        - the 'tilt' value
        """
        ...


    def setTilt(self, tilt: "Tilt") -> None:
        """
        Sets the value of the 'tilt' property.

        Arguments
        - tilt: the new 'tilt' value
        """
        ...


    class Tilt(Enum):
        """
        The tilt of a leaf.
        """

        NONE = 0
        """
        No tilt.
        """
        UNSTABLE = 1
        """
        Unstable tilt.
        """
        PARTIAL = 2
        """
        Partial tilt.
        """
        FULL = 3
        """
        Pinball.
        """
