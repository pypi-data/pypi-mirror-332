"""
Python module generated from Java source file org.bukkit.block.data.type.TNT

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class TNT(BlockData):
    """
    'unstable' indicates whether this TNT will explode on punching.
    """

    def isUnstable(self) -> bool:
        """
        Gets the value of the 'unstable' property.

        Returns
        - the 'unstable' value
        """
        ...


    def setUnstable(self, unstable: bool) -> None:
        """
        Sets the value of the 'unstable' property.

        Arguments
        - unstable: the new 'unstable' value
        """
        ...
