"""
Python module generated from Java source file org.bukkit.scoreboard.RenderType

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class RenderType(Enum):
    """
    Controls the way in which an Objective is rendered client side.
    """

    INTEGER = 0
    """
    Display integer value.
    """
    HEARTS = 1
    """
    Display number of hearts corresponding to value.
    """
