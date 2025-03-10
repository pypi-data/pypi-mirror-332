"""
Python module generated from Java source file org.bukkit.block.data.Snowable

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Snowable(BlockData):
    """
    'snowy' denotes whether this block has a snow covered side and top texture
    (normally because the block above is snow).
    """

    def isSnowy(self) -> bool:
        """
        Gets the value of the 'snowy' property.

        Returns
        - the 'snowy' value
        """
        ...


    def setSnowy(self, snowy: bool) -> None:
        """
        Sets the value of the 'snowy' property.

        Arguments
        - snowy: the new 'snowy' value
        """
        ...
