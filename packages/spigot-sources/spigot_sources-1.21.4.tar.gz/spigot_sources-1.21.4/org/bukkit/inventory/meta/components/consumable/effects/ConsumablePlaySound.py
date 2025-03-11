"""
Python module generated from Java source file org.bukkit.inventory.meta.components.consumable.effects.ConsumablePlaySound

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Sound
from org.bukkit.inventory.meta.components.consumable.effects import *
from typing import Any, Callable, Iterable, Tuple


class ConsumablePlaySound(ConsumableEffect):
    """
    Represent a sound played when an item is consumed.
    """

    def getSound(self) -> "Sound":
        """
        Gets the sound to play on completion of the item's consumption.

        Returns
        - the sound
        """
        ...


    def setSound(self, sound: "Sound") -> None:
        """
        Sets the sound to play on completion of the item's consumption.

        Arguments
        - sound: sound
        """
        ...
