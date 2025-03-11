"""
Python module generated from Java source file org.bukkit.entity.WanderingTrader

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class WanderingTrader(AbstractVillager):
    """
    Represents a wandering trader NPC
    """

    def getDespawnDelay(self) -> int:
        """
        Gets the despawn delay before this WanderingTrader is forcibly
        despawned.
        
        If this is less than or equal to 0, then the trader will not be
        despawned.

        Returns
        - The despawn delay before this WanderingTrader is forcibly
        despawned
        """
        ...


    def setDespawnDelay(self, despawnDelay: int) -> None:
        """
        Sets the despawn delay before this WanderingTrader is forcibly
        despawned.
        
        If this is less than or equal to 0, then the trader will not be
        despawned.

        Arguments
        - despawnDelay: The new despawn delay before this
        WanderingTrader is forcibly despawned
        """
        ...
