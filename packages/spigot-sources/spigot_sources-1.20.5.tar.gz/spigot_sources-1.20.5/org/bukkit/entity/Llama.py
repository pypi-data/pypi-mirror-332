"""
Python module generated from Java source file org.bukkit.entity.Llama

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from org.bukkit.inventory import LlamaInventory
from typing import Any, Callable, Iterable, Tuple


class Llama(ChestedHorse):
    """
    Represents a Llama.
    """

    def getColor(self) -> "Color":
        """
        Gets the llama's color.

        Returns
        - a Color representing the llama's color
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the llama's color.

        Arguments
        - color: a Color for this llama
        """
        ...


    def getStrength(self) -> int:
        """
        Gets the llama's strength. A higher strength llama will have more
        inventory slots and be more threatening to entities.

        Returns
        - llama strength [1,5]
        """
        ...


    def setStrength(self, strength: int) -> None:
        """
        Sets the llama's strength. A higher strength llama will have more
        inventory slots and be more threatening to entities. Inventory slots are
        equal to strength * 3.

        Arguments
        - strength: llama strength [1,5]
        """
        ...


    def getInventory(self) -> "LlamaInventory":
        ...


    class Color(Enum):
        """
        Represents the base color that the llama has.
        """

        CREAMY = 0
        """
        A cream-colored llama.
        """
        WHITE = 1
        """
        A white llama.
        """
        BROWN = 2
        """
        A brown llama.
        """
        GRAY = 3
        """
        A gray llama.
        """
