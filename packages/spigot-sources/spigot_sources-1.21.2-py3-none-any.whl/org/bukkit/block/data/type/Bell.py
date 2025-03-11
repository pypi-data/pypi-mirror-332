"""
Python module generated from Java source file org.bukkit.block.data.type.Bell

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Bell(Directional, Powerable):
    """
    'attachment' denotes how the bell is attached to its block.
    """

    def getAttachment(self) -> "Attachment":
        """
        Gets the value of the 'attachment' property.

        Returns
        - the 'attachment' value
        """
        ...


    def setAttachment(self, attachment: "Attachment") -> None:
        """
        Sets the value of the 'attachment' property.

        Arguments
        - attachment: the new 'attachment' value
        """
        ...


    class Attachment(Enum):
        """
        What the bell is attached to.
        """

        FLOOR = 0
        """
        Placed on floor.
        """
        CEILING = 1
        """
        Placed on ceiling.
        """
        SINGLE_WALL = 2
        """
        Placed on one wall.
        """
        DOUBLE_WALL = 3
        """
        Placed between two walls.
        """
