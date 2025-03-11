"""
Python module generated from Java source file org.bukkit.Fluid

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import Locale
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Fluid(Enum):
    """
    Represents a fluid type.
    """

    WATER = 0
    """
    Stationary water.
    """
    FLOWING_WATER = 1
    """
    Flowing water.
    """
    LAVA = 2
    """
    Stationary lava.
    """
    FLOWING_LAVA = 3
    """
    Flowing lava.
    """


    def getKey(self) -> "NamespacedKey":
        ...
