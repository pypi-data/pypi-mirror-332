"""
Python module generated from Java source file org.bukkit.event.entity.ProjectileLaunchEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Projectile
from org.bukkit.event import Cancellable
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ProjectileLaunchEvent(EntitySpawnEvent, Cancellable):
    """
    Called when a projectile is launched.
    """

    def __init__(self, what: "Entity"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Projectile":
        ...
