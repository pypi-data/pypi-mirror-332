"""
Python module generated from Java source file org.bukkit.NetherWartsState

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class NetherWartsState(Enum):

    SEEDED = 0
    """
    State when first seeded
    """
    STAGE_ONE = 1
    """
    First growth stage
    """
    STAGE_TWO = 2
    """
    Second growth stage
    """
    RIPE = 3
    """
    Ready to harvest
    """
