"""
Python module generated from Java source file org.bukkit.block.Beehive

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.block import *
from org.bukkit.entity import Bee
from typing import Any, Callable, Iterable, Tuple


class Beehive(EntityBlockStorage):
    """
    Represents a captured state of a bee hive.
    """

    def getFlower(self) -> "Location":
        """
        Get the hive's flower location.

        Returns
        - flower location or null
        """
        ...


    def setFlower(self, location: "Location") -> None:
        """
        Set the hive's flower location.

        Arguments
        - location: or null
        """
        ...


    def isSedated(self) -> bool:
        """
        Check if the hive is sedated due to smoke from a nearby campfire.

        Returns
        - True if hive is sedated
        """
        ...
