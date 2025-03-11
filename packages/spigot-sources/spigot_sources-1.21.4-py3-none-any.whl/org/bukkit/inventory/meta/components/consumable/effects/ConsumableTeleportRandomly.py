"""
Python module generated from Java source file org.bukkit.inventory.meta.components.consumable.effects.ConsumableTeleportRandomly

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta.components.consumable.effects import *
from typing import Any, Callable, Iterable, Tuple


class ConsumableTeleportRandomly(ConsumableEffect):
    """
    Represent a random teleport when an item is consumed.
    """

    def getDiameter(self) -> float:
        """
        Gets the diameter that the consumer is teleported within.

        Returns
        - the diameter
        """
        ...


    def setDiameter(self, diameter: float) -> None:
        """
        Sets the diameter that the consumer is teleported within.

        Arguments
        - diameter: new diameter
        """
        ...
