"""
Python module generated from Java source file org.bukkit.entity.Rabbit

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Rabbit(Animals):

    def getRabbitType(self) -> "Type":
        """
        Returns
        - The type of rabbit.
        """
        ...


    def setRabbitType(self, type: "Type") -> None:
        """
        Arguments
        - type: Sets the type of rabbit for this entity.
        """
        ...


    class Type(Enum):
        """
        Represents the various types a Rabbit might be.
        """

        BROWN = 0
        """
        Chocolate colored rabbit.
        """
        WHITE = 1
        """
        Pure white rabbit.
        """
        BLACK = 2
        """
        Black rabbit.
        """
        BLACK_AND_WHITE = 3
        """
        Black with white patches, or white with black patches?
        """
        GOLD = 4
        """
        Golden bunny.
        """
        SALT_AND_PEPPER = 5
        """
        Salt and pepper colored, whatever that means.
        """
        THE_KILLER_BUNNY = 6
        """
        Rabbit with pure white fur, blood red horizontal eyes, and is hostile to players.
        """
