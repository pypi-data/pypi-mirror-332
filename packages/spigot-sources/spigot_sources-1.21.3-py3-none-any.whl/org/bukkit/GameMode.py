"""
Python module generated from Java source file org.bukkit.GameMode

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from org.bukkit.entity import HumanEntity
from typing import Any, Callable, Iterable, Tuple


class GameMode(Enum):
    """
    Represents the various type of game modes that HumanEntitys may
    have
    """

    CREATIVE = (1)
    """
    Creative mode may fly, build instantly, become invulnerable and create
    free items.
    """
    SURVIVAL = (0)
    """
    Survival mode is the "normal" gameplay type, with no special features.
    """
    ADVENTURE = (2)
    """
    Adventure mode cannot break blocks without the correct tools.
    """
    SPECTATOR = (3)
    """
    Spectator mode cannot interact with the world in anyway and is
    invisible to normal players. This grants the player the
    ability to no-clip through the world.
    """


    def getValue(self) -> int:
        """
        Gets the mode value associated with this GameMode

        Returns
        - An integer value of this gamemode

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByValue(value: int) -> "GameMode":
        """
        Gets the GameMode represented by the specified value

        Arguments
        - value: Value to check

        Returns
        - Associative GameMode with the given value, or null if
            it doesn't exist

        Deprecated
        - Magic value
        """
        ...
