"""
Python module generated from Java source file org.bukkit.scoreboard.DisplaySlot

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

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
