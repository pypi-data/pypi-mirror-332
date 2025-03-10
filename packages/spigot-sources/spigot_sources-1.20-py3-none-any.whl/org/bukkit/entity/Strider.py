"""
Python module generated from Java source file org.bukkit.entity.Strider

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Strider(Steerable, Vehicle):
    """
    Represents a Strider.
    """

    def isShivering(self) -> bool:
        """
        Check whether or not this strider is out of warm blocks and shivering.

        Returns
        - True if shivering, False otherwise
        """
        ...


    def setShivering(self, shivering: bool) -> None:
        """
        Set whether or not this strider is shivering.
        
        Note that the shivering state is updated frequently on the server,
        therefore this method may not affect the entity for long enough to have a
        noticeable difference.

        Arguments
        - shivering: its new shivering state
        """
        ...
