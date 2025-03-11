"""
Python module generated from Java source file org.bukkit.generator.WorldInfo

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import World
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class WorldInfo:
    """
    Holds various information of a World
    """

    def getName(self) -> str:
        """
        Gets the unique name of this world

        Returns
        - Name of this world
        """
        ...


    def getUID(self) -> "UUID":
        """
        Gets the Unique ID of this world

        Returns
        - Unique ID of this world.
        """
        ...


    def getEnvironment(self) -> "World.Environment":
        """
        Gets the World.Environment type of this world

        Returns
        - This worlds Environment type
        """
        ...


    def getSeed(self) -> int:
        """
        Gets the Seed for this world.

        Returns
        - This worlds Seed
        """
        ...


    def getMinHeight(self) -> int:
        """
        Gets the minimum height of this world.
        
        If the min height is 0, there are only blocks from y=0.

        Returns
        - Minimum height of the world
        """
        ...


    def getMaxHeight(self) -> int:
        """
        Gets the maximum height of this world.
        
        If the max height is 100, there are only blocks from y=0 to y=99.

        Returns
        - Maximum height of the world
        """
        ...
