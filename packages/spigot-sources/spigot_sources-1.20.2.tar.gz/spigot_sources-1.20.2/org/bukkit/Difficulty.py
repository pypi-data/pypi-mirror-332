"""
Python module generated from Java source file org.bukkit.Difficulty

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Difficulty(Enum):
    """
    Represents the various difficulty levels that are available.
    """

    PEACEFUL = (0)
    """
    Players regain health over time, hostile mobs don't spawn, the hunger
    bar does not deplete.
    """
    EASY = (1)
    """
    Hostile mobs spawn, enemies deal less damage than on normal difficulty,
    the hunger bar does deplete and starving deals up to 5 hearts of
    damage. (Default value)
    """
    NORMAL = (2)
    """
    Hostile mobs spawn, enemies deal normal amounts of damage, the hunger
    bar does deplete and starving deals up to 9.5 hearts of damage.
    """
    HARD = (3)
    """
    Hostile mobs spawn, enemies deal greater damage than on normal
    difficulty, the hunger bar does deplete and starving can kill players.
    """


    def getValue(self) -> int:
        """
        Gets the difficulty value associated with this Difficulty.

        Returns
        - An integer value of this difficulty

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByValue(value: int) -> "Difficulty":
        """
        Gets the Difficulty represented by the specified value

        Arguments
        - value: Value to check

        Returns
        - Associative Difficulty with the given value, or null if
            it doesn't exist

        Deprecated
        - Magic value
        """
        ...
