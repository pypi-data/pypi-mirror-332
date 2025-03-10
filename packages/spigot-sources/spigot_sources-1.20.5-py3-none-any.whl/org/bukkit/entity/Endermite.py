"""
Python module generated from Java source file org.bukkit.entity.Endermite

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Endermite(Monster):

    def isPlayerSpawned(self) -> bool:
        """
        Gets whether this Endermite was spawned by a player.
        
        An Endermite spawned by a player will be attacked by nearby Enderman.

        Returns
        - player spawned status

        Deprecated
        - this functionality no longer exists
        """
        ...


    def setPlayerSpawned(self, playerSpawned: bool) -> None:
        """
        Sets whether this Endermite was spawned by a player.
        
        An Endermite spawned by a player will be attacked by nearby Enderman.

        Arguments
        - playerSpawned: player spawned status

        Deprecated
        - this functionality no longer exists
        """
        ...
