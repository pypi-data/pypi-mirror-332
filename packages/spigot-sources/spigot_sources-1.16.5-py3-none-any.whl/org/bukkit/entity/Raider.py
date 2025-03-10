"""
Python module generated from Java source file org.bukkit.entity.Raider

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Raider(Monster):

    def getPatrolTarget(self) -> "Block":
        """
        Gets the block the raider is targeting to patrol.

        Returns
        - target block or null
        """
        ...


    def setPatrolTarget(self, block: "Block") -> None:
        """
        Sets the block the raider is targeting to patrol.

        Arguments
        - block: target block or null. Must be in same world as the entity
        """
        ...


    def isPatrolLeader(self) -> bool:
        """
        Gets whether this entity is a patrol leader.

        Returns
        - patrol leader status
        """
        ...


    def setPatrolLeader(self, leader: bool) -> None:
        """
        Sets whether this entity is a patrol leader.

        Arguments
        - leader: patrol leader status
        """
        ...


    def isCanJoinRaid(self) -> bool:
        """
        Gets whether this mob can join an active raid.

        Returns
        - CanJoinRaid status
        """
        ...


    def setCanJoinRaid(self, join: bool) -> None:
        """
        Sets whether this mob can join an active raid.

        Arguments
        - join: CanJoinRaid status
        """
        ...
