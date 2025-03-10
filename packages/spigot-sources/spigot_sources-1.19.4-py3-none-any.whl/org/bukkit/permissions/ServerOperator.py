"""
Python module generated from Java source file org.bukkit.permissions.ServerOperator

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.permissions import *
from typing import Any, Callable, Iterable, Tuple


class ServerOperator:
    """
    Represents an object that may become a server operator, such as a Player
    """

    def isOp(self) -> bool:
        """
        Checks if this object is a server operator

        Returns
        - True if this is an operator, otherwise False
        """
        ...


    def setOp(self, value: bool) -> None:
        """
        Sets the operator status of this object

        Arguments
        - value: New operator value
        """
        ...
