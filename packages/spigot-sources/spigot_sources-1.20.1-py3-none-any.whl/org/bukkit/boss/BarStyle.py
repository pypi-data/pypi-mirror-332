"""
Python module generated from Java source file org.bukkit.boss.BarStyle

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.boss import *
from typing import Any, Callable, Iterable, Tuple


class BarStyle(Enum):

    SOLID = 0
    """
    Makes the boss bar solid (no segments)
    """
    SEGMENTED_6 = 1
    """
    Splits the boss bar into 6 segments
    """
    SEGMENTED_10 = 2
    """
    Splits the boss bar into 10 segments
    """
    SEGMENTED_12 = 3
    """
    Splits the boss bar into 12 segments
    """
    SEGMENTED_20 = 4
    """
    Splits the boss bar into 20 segments
    """
