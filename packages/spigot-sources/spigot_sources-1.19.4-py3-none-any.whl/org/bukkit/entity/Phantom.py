"""
Python module generated from Java source file org.bukkit.entity.Phantom

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Phantom(Flying, Enemy):
    """
    Represents a phantom.
    """

    def getSize(self) -> int:
        """
        Returns
        - The size of the phantom
        """
        ...


    def setSize(self, sz: int) -> None:
        """
        Arguments
        - sz: The new size of the phantom.
        """
        ...
