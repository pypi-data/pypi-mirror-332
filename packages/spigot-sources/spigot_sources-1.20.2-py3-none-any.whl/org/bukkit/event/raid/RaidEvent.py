"""
Python module generated from Java source file org.bukkit.event.raid.RaidEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.event.raid import *
from org.bukkit.event.world import WorldEvent
from typing import Any, Callable, Iterable, Tuple


class RaidEvent(WorldEvent):
    """
    Represents events related to raids.
    """

    def getRaid(self) -> "Raid":
        """
        Returns the raid involved with this event.

        Returns
        - Raid
        """
        ...
