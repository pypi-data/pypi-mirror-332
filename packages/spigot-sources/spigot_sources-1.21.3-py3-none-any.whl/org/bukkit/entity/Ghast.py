"""
Python module generated from Java source file org.bukkit.entity.Ghast

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Ghast(Flying, Enemy):
    """
    Represents a Ghast.
    """

    def isCharging(self) -> bool:
        """
        Gets whether the Ghast is charging

        Returns
        - Whether the Ghast is charging
        """
        ...


    def setCharging(self, flag: bool) -> None:
        """
        Sets whether the Ghast is charging

        Arguments
        - flag: Whether the Ghast is charging
        """
        ...
