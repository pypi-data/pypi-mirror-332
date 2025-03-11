"""
Python module generated from Java source file org.bukkit.block.data.type.Door

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Openable
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Door(Bisected, Directional, Openable, Powerable):
    """
    'hinge' indicates which hinge this door is attached to and will rotate around
    when opened.
    """

    def getHinge(self) -> "Hinge":
        """
        Gets the value of the 'hinge' property.

        Returns
        - the 'hinge' value
        """
        ...


    def setHinge(self, hinge: "Hinge") -> None:
        """
        Sets the value of the 'hinge' property.

        Arguments
        - hinge: the new 'hinge' value
        """
        ...


    class Hinge(Enum):
        """
        The hinge of a door.
        """

        LEFT = 0
        """
        Door is attached to the left side.
        """
        RIGHT = 1
        """
        Door is attached to the right side.
        """
