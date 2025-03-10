"""
Python module generated from Java source file org.bukkit.block.data.type.Campfire

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Lightable
from org.bukkit.block.data import Waterlogged
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Campfire(Directional, Lightable, Waterlogged):
    """
    'signal_fire' denotes whether the fire is extra smokey due to having a hay
    bale placed beneath it.
    """

    def isSignalFire(self) -> bool:
        """
        Gets the value of the 'signal_fire' property.

        Returns
        - the 'signal_fire' value
        """
        ...


    def setSignalFire(self, signalFire: bool) -> None:
        """
        Sets the value of the 'signal_fire' property.

        Arguments
        - signalFire: the new 'signal_fire' value
        """
        ...
