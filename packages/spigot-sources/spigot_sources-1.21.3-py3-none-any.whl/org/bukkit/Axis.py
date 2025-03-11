"""
Python module generated from Java source file org.bukkit.Axis

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Axis(Enum):
    """
    Represents a mutually perpendicular axis in 3D Cartesian coordinates. In
    Minecraft the x, z axes lie in the horizontal plane, whilst the y axis points
    upwards.
    """

    X = 0
    """
    The x axis.
    """
    Y = 1
    """
    The y axis.
    """
    Z = 2
    """
    The z axis.
    """
