"""
Python module generated from Java source file org.bukkit.entity.PigZombie

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class PigZombie(Zombie):
    """
    Represents a Pig Zombie.
    """

    def getAnger(self) -> int:
        """
        Get the pig zombie's current anger level.

        Returns
        - The anger level.
        """
        ...


    def setAnger(self, level: int) -> None:
        """
        Set the pig zombie's current anger level.

        Arguments
        - level: The anger level. Higher levels of anger take longer to
            wear off.
        """
        ...


    def setAngry(self, angry: bool) -> None:
        """
        Shorthand; sets to either 0 or the default level.

        Arguments
        - angry: Whether the zombie should be angry.
        """
        ...


    def isAngry(self) -> bool:
        """
        Shorthand; gets whether the zombie is angry.

        Returns
        - True if the zombie is angry, otherwise False.
        """
        ...


    def isConverting(self) -> bool:
        """
        **Not applicable to this entity**

        Returns
        - False
        """
        ...


    def getConversionTime(self) -> int:
        """
        **Not applicable to this entity**

        Returns
        - UnsuppotedOperationException
        """
        ...


    def setConversionTime(self, time: int) -> None:
        """
        **Not applicable to this entity**

        Arguments
        - time: unused
        """
        ...
