"""
Python module generated from Java source file org.bukkit.inventory.meta.OminousBottleMeta

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class OminousBottleMeta(ItemMeta):
    """
    Represents a map that can be scalable.
    """

    def hasAmplifier(self) -> bool:
        """
        Checks for the presence of an amplifier.

        Returns
        - True if a customer amplifier is applied
        """
        ...


    def getAmplifier(self) -> int:
        """
        Gets the amplifier amount for an Ominous Bottle's bad omen effect.
        
        Plugins should check that hasAmplifier() returns True before calling this
        method.

        Returns
        - amplifier
        """
        ...


    def setAmplifier(self, amplifier: int) -> None:
        """
        Sets the amplifier amount for an Ominous Bottle's bad omen effect.

        Arguments
        - amplifier: between 0 and 4
        """
        ...


    def clone(self) -> "OminousBottleMeta":
        ...
