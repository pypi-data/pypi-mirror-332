"""
Python module generated from Java source file org.bukkit.event.block.Action

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class Action(Enum):

    LEFT_CLICK_BLOCK = 0
    """
    Left-clicking a block
    """
    RIGHT_CLICK_BLOCK = 1
    """
    Right-clicking a block
    """
    LEFT_CLICK_AIR = 2
    """
    Left-clicking the air
    """
    RIGHT_CLICK_AIR = 3
    """
    Right-clicking the air
    """
    PHYSICAL = 4
    """
    Stepping onto or into a block (Ass-pressure)
    
    Examples:
    
    - Jumping on soil
    - Standing on pressure plate
    - Triggering redstone ore
    - Triggering tripwire
    """
