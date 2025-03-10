"""
Python module generated from Java source file org.bukkit.scoreboard.DisplaySlot

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class DisplaySlot(Enum):
    """
    Locations for displaying objectives to the player
    """

    BELOW_NAME = 0
    PLAYER_LIST = 1
    SIDEBAR = 2
    SIDEBAR_BLACK = 3
    SIDEBAR_DARK_BLUE = 4
    SIDEBAR_DARK_GREEN = 5
    SIDEBAR_DARK_AQUA = 6
    SIDEBAR_DARK_RED = 7
    SIDEBAR_DARK_PURPLE = 8
    SIDEBAR_GOLD = 9
    SIDEBAR_GRAY = 10
    SIDEBAR_DARK_GRAY = 11
    SIDEBAR_BLUE = 12
    SIDEBAR_GREEN = 13
    SIDEBAR_AQUA = 14
    SIDEBAR_RED = 15
    SIDEBAR_LIGHT_PURPLE = 16
    SIDEBAR_YELLOW = 17
    SIDEBAR_WHITE = 18
