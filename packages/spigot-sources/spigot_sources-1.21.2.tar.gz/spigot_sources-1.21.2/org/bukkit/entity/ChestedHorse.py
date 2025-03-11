"""
Python module generated from Java source file org.bukkit.entity.ChestedHorse

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ChestedHorse(AbstractHorse):
    """
    Represents Horse-like creatures which can carry an inventory.
    """

    def isCarryingChest(self) -> bool:
        """
        Gets whether the horse has a chest equipped.

        Returns
        - True if the horse has chest storage
        """
        ...


    def setCarryingChest(self, chest: bool) -> None:
        """
        Sets whether the horse has a chest equipped. Removing a chest will also
        clear the chest's inventory.

        Arguments
        - chest: True if the horse should have a chest
        """
        ...
