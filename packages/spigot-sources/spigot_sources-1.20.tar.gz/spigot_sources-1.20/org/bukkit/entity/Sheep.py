"""
Python module generated from Java source file org.bukkit.entity.Sheep

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.material import Colorable
from typing import Any, Callable, Iterable, Tuple


class Sheep(Animals, Colorable):
    """
    Represents a Sheep.
    """

    def isSheared(self) -> bool:
        """
        Returns
        - Whether the sheep is sheared.
        """
        ...


    def setSheared(self, flag: bool) -> None:
        """
        Arguments
        - flag: Whether to shear the sheep
        """
        ...
