"""
Python module generated from Java source file org.bukkit.inventory.meta.FireworkEffectMeta

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import FireworkEffect
from org.bukkit import Material
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class FireworkEffectMeta(ItemMeta):
    """
    Represents a meta that can store a single FireworkEffect. An example
    includes Material.FIREWORK_STAR.
    """

    def setEffect(self, effect: "FireworkEffect") -> None:
        """
        Sets the firework effect for this meta.

        Arguments
        - effect: the effect to set, or null to indicate none.
        """
        ...


    def hasEffect(self) -> bool:
        """
        Checks if this meta has an effect.

        Returns
        - True if this meta has an effect, False otherwise
        """
        ...


    def getEffect(self) -> "FireworkEffect":
        """
        Gets the firework effect for this meta.

        Returns
        - the current effect, or null if none
        """
        ...


    def clone(self) -> "FireworkEffectMeta":
        ...
