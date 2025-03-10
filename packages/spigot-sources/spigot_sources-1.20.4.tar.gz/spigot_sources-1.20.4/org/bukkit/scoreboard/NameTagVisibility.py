"""
Python module generated from Java source file org.bukkit.scoreboard.NameTagVisibility

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.scoreboard import *
from typing import Any, Callable, Iterable, Tuple


class NameTagVisibility(Enum):
    """
    Deprecated
    - replaced by Team.OptionStatus
    """

    ALWAYS = 0
    """
    Always show the player's nametag.
    """
    NEVER = 1
    """
    Never show the player's nametag.
    """
    HIDE_FOR_OTHER_TEAMS = 2
    """
    Show the player's nametag only to his own team members.
    """
    HIDE_FOR_OWN_TEAM = 3
    """
    Show the player's nametag only to members of other teams.
    """
