"""
Python module generated from Java source file org.bukkit.Rotation

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Rotation(Enum):
    """
    An enum to specify a rotation based orientation, like that on a clock.
    
    It represents how something is viewed, as opposed to cardinal directions.
    """

    NONE = 0
    """
    No rotation
    """
    CLOCKWISE_45 = 1
    """
    Rotated clockwise by 45 degrees
    """
    CLOCKWISE = 2
    """
    Rotated clockwise by 90 degrees
    """
    CLOCKWISE_135 = 3
    """
    Rotated clockwise by 135 degrees
    """
    FLIPPED = 4
    """
    Flipped upside-down, a 180 degree rotation
    """
    FLIPPED_45 = 5
    """
    Flipped upside-down + 45 degree rotation
    """
    COUNTER_CLOCKWISE = 6
    """
    Rotated counter-clockwise by 90 degrees
    """
    COUNTER_CLOCKWISE_45 = 7
    """
    Rotated counter-clockwise by 45 degrees
    """


    def rotateClockwise(self) -> "Rotation":
        """
        Rotate clockwise by 90 degrees.

        Returns
        - the relative rotation
        """
        ...


    def rotateCounterClockwise(self) -> "Rotation":
        """
        Rotate counter-clockwise by 90 degrees.

        Returns
        - the relative rotation
        """
        ...
