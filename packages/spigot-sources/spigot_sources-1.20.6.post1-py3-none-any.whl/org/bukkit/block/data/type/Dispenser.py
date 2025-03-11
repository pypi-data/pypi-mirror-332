"""
Python module generated from Java source file org.bukkit.block.data.type.Dispenser

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Dispenser(Directional):
    """
    Similar to Powerable, 'triggered' indicates whether or not the
    dispenser is currently activated.
    """

    def isTriggered(self) -> bool:
        """
        Gets the value of the 'triggered' property.

        Returns
        - the 'triggered' value
        """
        ...


    def setTriggered(self, triggered: bool) -> None:
        """
        Sets the value of the 'triggered' property.

        Arguments
        - triggered: the new 'triggered' value
        """
        ...
