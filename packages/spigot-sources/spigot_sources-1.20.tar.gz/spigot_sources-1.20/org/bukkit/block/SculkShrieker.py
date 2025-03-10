"""
Python module generated from Java source file org.bukkit.block.SculkShrieker

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class SculkShrieker(TileState):
    """
    Represents a captured state of a sculk shrieker.
    """

    def getWarningLevel(self) -> int:
        """
        Gets the most recent warning level of this block.
        
        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        Returns
        - current warning level
        """
        ...


    def setWarningLevel(self, level: int) -> None:
        """
        Sets the most recent warning level of this block.
        
        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        Arguments
        - level: new warning level
        """
        ...
