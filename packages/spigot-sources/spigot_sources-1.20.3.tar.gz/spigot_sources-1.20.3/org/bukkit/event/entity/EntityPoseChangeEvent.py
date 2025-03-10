"""
Python module generated from Java source file org.bukkit.event.entity.EntityPoseChangeEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Pose
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityPoseChangeEvent(EntityEvent):
    """
    Called when an entity changes its pose.

    See
    - Entity.getPose()
    """

    def __init__(self, who: "Entity", pose: "Pose"):
        ...


    def getPose(self) -> "Pose":
        """
        Gets the entity's new pose.

        Returns
        - the new pose
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
