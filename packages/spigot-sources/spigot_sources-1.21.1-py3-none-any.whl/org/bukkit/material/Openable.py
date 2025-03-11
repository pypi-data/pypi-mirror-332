"""
Python module generated from Java source file org.bukkit.material.Openable

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Openable:

    def isOpen(self) -> bool:
        """
        Check to see if the door is open.

        Returns
        - True if the door has swung counterclockwise around its hinge.
        """
        ...


    def setOpen(self, isOpen: bool) -> None:
        """
        Configure this door to be either open or closed;

        Arguments
        - isOpen: True to open the door.
        """
        ...
