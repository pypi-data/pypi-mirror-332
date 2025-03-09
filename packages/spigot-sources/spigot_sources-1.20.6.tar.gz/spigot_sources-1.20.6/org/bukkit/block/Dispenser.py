"""
Python module generated from Java source file org.bukkit.block.Dispenser

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Nameable
from org.bukkit.block import *
from org.bukkit.loot import Lootable
from org.bukkit.projectiles import BlockProjectileSource
from typing import Any, Callable, Iterable, Tuple


class Dispenser(Container, Nameable, Lootable):
    """
    Represents a captured state of a dispenser.
    """

    def getBlockProjectileSource(self) -> "BlockProjectileSource":
        """
        Gets the BlockProjectileSource object for the dispenser.
        
        If the block represented by this state is no longer a dispenser, this
        will return null.

        Returns
        - a BlockProjectileSource if valid, otherwise null

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def dispense(self) -> bool:
        """
        Attempts to dispense the contents of the dispenser.
        
        If the block represented by this state is no longer a dispenser, this
        will return False.

        Returns
        - True if successful, otherwise False

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...
