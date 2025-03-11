"""
Python module generated from Java source file org.bukkit.boss.BarFlag

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.boss import *
from typing import Any, Callable, Iterable, Tuple


class BarFlag(Enum):

    DARKEN_SKY = 0
    """
    Darkens the sky like during fighting a wither.
    """
    PLAY_BOSS_MUSIC = 1
    """
    Tells the client to play the Ender Dragon boss music.
    """
    CREATE_FOG = 2
    """
    Creates fog around the world.
    """
