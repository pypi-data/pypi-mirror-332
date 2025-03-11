"""
Python module generated from Java source file org.bukkit.inventory.meta.components.UseCooldownComponent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

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
        Gets the time in seconds it will take for an item in this cooldown group
        to be available to use again.

        Returns
        - cooldown time
        """
        ...


    def setCooldownSeconds(self, cooldown: float) -> None:
        """
        Sets the time in seconds it will take for an item in this cooldown group
        to be available to use again.

        Arguments
        - cooldown: new eat time, must be greater than 0
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
