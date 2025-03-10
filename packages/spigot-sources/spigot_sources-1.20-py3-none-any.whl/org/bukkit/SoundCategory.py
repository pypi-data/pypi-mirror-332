"""
Python module generated from Java source file org.bukkit.SoundCategory

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class SoundCategory(Enum):
    """
    An Enum of categories for sounds.
    """

    MASTER = 0
    MUSIC = 1
    RECORDS = 2
    WEATHER = 3
    BLOCKS = 4
    HOSTILE = 5
    NEUTRAL = 6
    PLAYERS = 7
    AMBIENT = 8
    VOICE = 9
