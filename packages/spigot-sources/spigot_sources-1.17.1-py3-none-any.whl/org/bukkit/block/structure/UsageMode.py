"""
Python module generated from Java source file org.bukkit.block.structure.UsageMode

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.structure import *
from typing import Any, Callable, Iterable, Tuple


class UsageMode(Enum):
    """
    Represents how a org.bukkit.block.Structure can be used.
    """

    SAVE = 0
    """
    The mode used when saving a structure.
    """
    LOAD = 1
    """
    The mode used when loading a structure.
    """
    CORNER = 2
    """
    Used when saving a structure for easy size calculation. When using this
    mode, the Structure name MUST match the name in the second Structure
    block that is in UsageMode.SAVE.
    """
    DATA = 3
    """
    Used to run specific custom functions, which can only be used for certain
    Structures. The structure block is removed after this function completes.
    The data tags (functions) can be found on the
    <a href="http://minecraft.gamepedia.com/Structure_Block#Data">wiki</a>.
    """
