"""
Python module generated from Java source file org.bukkit.block.SculkShrieker

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import Player
from typing import Any, Callable, Iterable, Tuple


class SculkShrieker(TileState):
    """
    Represents a captured state of a sculk shrieker.
    """

    def getWarningLevel(self) -> int:
        """
        Gets the most recent warning level of this block.
        
        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        Returns
        - current warning level
        """
        ...


    def setWarningLevel(self, level: int) -> None:
        """
        Sets the most recent warning level of this block.
        
        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        Arguments
        - level: new warning level
        """
        ...


    def tryShriek(self, player: "Player") -> None:
        """
        Simulates a player causing a vibration.

        Arguments
        - player: the player that "caused" the shriek
        """
        ...
