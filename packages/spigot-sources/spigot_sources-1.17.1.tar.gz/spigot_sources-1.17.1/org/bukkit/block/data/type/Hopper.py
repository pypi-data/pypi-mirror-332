"""
Python module generated from Java source file org.bukkit.block.data.type.Hopper

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Hopper(Directional):
    """
    Similar to Powerable, 'enabled' indicates whether or not the hopper
    is currently activated.
    
    Unlike most other blocks, a hopper is only enabled when it is **not**
    receiving any power.
    """

    def isEnabled(self) -> bool:
        """
        Gets the value of the 'enabled' property.

        Returns
        - the 'enabled' value
        """
        ...


    def setEnabled(self, enabled: bool) -> None:
        """
        Sets the value of the 'enabled' property.

        Arguments
        - enabled: the new 'enabled' value
        """
        ...
