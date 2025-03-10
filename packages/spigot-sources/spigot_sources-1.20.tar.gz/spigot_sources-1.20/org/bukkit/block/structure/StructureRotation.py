"""
Python module generated from Java source file org.bukkit.block.structure.StructureRotation

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.structure import *
from typing import Any, Callable, Iterable, Tuple


class StructureRotation(Enum):
    """
    Represents how a org.bukkit.block.Structure can be rotated.
    """

    NONE = 0
    """
    No rotation.
    """
    CLOCKWISE_90 = 1
    """
    Rotated clockwise 90 degrees.
    """
    CLOCKWISE_180 = 2
    """
    Rotated clockwise 180 degrees.
    """
    COUNTERCLOCKWISE_90 = 3
    """
    Rotated counter clockwise 90 degrees.
    
    Equivalent to rotating clockwise 270 degrees.
    """
