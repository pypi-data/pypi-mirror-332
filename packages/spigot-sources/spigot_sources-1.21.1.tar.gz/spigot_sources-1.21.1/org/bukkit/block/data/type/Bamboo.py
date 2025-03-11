"""
Python module generated from Java source file org.bukkit.block.data.type.Bamboo

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Ageable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Bamboo(Ageable, Sapling):
    """
    'leaves' represents the size of the leaves on this bamboo block.
    """

    def getLeaves(self) -> "Leaves":
        """
        Gets the value of the 'leaves' property.

        Returns
        - the 'leaves' value
        """
        ...


    def setLeaves(self, leaves: "Leaves") -> None:
        """
        Sets the value of the 'leaves' property.

        Arguments
        - leaves: the new 'leaves' value
        """
        ...


    class Leaves(Enum):
        """
        Bamboo leaf size.
        """

        NONE = 0
        """
        No leaves.
        """
        SMALL = 1
        """
        Small leaves.
        """
        LARGE = 2
        """
        Large leaves.
        """
