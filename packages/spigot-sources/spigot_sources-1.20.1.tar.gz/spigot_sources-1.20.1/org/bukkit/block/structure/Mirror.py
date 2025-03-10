"""
Python module generated from Java source file org.bukkit.block.structure.Mirror

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.structure import *
from typing import Any, Callable, Iterable, Tuple


class Mirror(Enum):
    """
    Represents how a org.bukkit.block.Structure can be mirrored upon
    being loaded.
    """

    NONE = 0
    """
    No mirroring.
    
    Positive X to Positive Z
    """
    LEFT_RIGHT = 1
    """
    Structure is mirrored left to right.
    
    Similar to looking in a mirror. Positive X to Negative Z
    """
    FRONT_BACK = 2
    """
    Structure is mirrored front to back.
    
    Positive Z to Negative X
    """
