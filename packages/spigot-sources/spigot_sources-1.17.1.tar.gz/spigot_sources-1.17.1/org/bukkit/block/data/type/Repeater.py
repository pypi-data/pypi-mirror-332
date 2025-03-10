"""
Python module generated from Java source file org.bukkit.block.data.type.Repeater

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Repeater(Directional, Powerable):
    """
    'delay' is the propagation delay of a repeater, i.e. how many ticks before it
    will be activated from a current change and propagate it to the next block.
    
    Delay may not be lower than .getMinimumDelay() or higher than
    .getMaximumDelay().
    
    'locked' denotes whether the repeater is in the locked state or not.
    
    A locked repeater will not change its output until it is unlocked. In game, a
    locked repeater is created by having a constant current perpendicularly
    entering the block.
    """

    def getDelay(self) -> int:
        """
        Gets the value of the 'delay' property.

        Returns
        - the 'delay' value
        """
        ...


    def setDelay(self, delay: int) -> None:
        """
        Sets the value of the 'delay' property.

        Arguments
        - delay: the new 'delay' value
        """
        ...


    def getMinimumDelay(self) -> int:
        """
        Gets the minimum allowed value of the 'delay' property.

        Returns
        - the minimum 'delay' value
        """
        ...


    def getMaximumDelay(self) -> int:
        """
        Gets the maximum allowed value of the 'delay' property.

        Returns
        - the maximum 'delay' value
        """
        ...


    def isLocked(self) -> bool:
        """
        Gets the value of the 'locked' property.

        Returns
        - the 'locked' value
        """
        ...


    def setLocked(self, locked: bool) -> None:
        """
        Sets the value of the 'locked' property.

        Arguments
        - locked: the new 'locked' value
        """
        ...
