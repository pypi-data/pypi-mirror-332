"""
Python module generated from Java source file org.bukkit.inventory.meta.components.UseCooldownComponent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components import *
from typing import Any, Callable, Iterable, Tuple


class UseCooldownComponent(ConfigurationSerializable):
    """
    Represents a component which determines the cooldown applied to use of this
    item.
    """

    def getCooldownSeconds(self) -> float:
        """
        Gets the time in seconds it will take for this item to be eaten.

        Returns
        - eat time
        """
        ...


    def setCooldownSeconds(self, eatSeconds: float) -> None:
        """
        Sets the time in seconds it will take for this item to be eaten.

        Arguments
        - eatSeconds: new eat time, must be positive
        """
        ...


    def getCooldownGroup(self) -> "NamespacedKey":
        """
        Gets the custom cooldown group to be used for similar items, if set.

        Returns
        - the cooldown group
        """
        ...


    def setCooldownGroup(self, song: "NamespacedKey") -> None:
        """
        Sets the custom cooldown group to be used for similar items.

        Arguments
        - song: the cooldown group
        """
        ...
