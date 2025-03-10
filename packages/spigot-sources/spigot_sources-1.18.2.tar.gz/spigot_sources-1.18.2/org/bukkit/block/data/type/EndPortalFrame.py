"""
Python module generated from Java source file org.bukkit.block.data.type.EndPortalFrame

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class EndPortalFrame(Directional):
    """
    'eye' denotes whether this end portal frame has been activated by having an
    eye of ender placed in it.
    """

    def hasEye(self) -> bool:
        """
        Gets the value of the 'eye' property.

        Returns
        - the 'eye' value
        """
        ...


    def setEye(self, eye: bool) -> None:
        """
        Sets the value of the 'eye' property.

        Arguments
        - eye: the new 'eye' value
        """
        ...
