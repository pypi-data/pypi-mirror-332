"""
Python module generated from Java source file org.bukkit.event.entity.ProjectileHitEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import Projectile
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class ProjectileHitEvent(EntityEvent, Cancellable):
    """
    Called when a projectile hits an object
    """

    def __init__(self, projectile: "Projectile"):
        ...


    def __init__(self, projectile: "Projectile", hitEntity: "Entity"):
        ...


    def __init__(self, projectile: "Projectile", hitBlock: "Block"):
        ...


    def __init__(self, projectile: "Projectile", hitEntity: "Entity", hitBlock: "Block"):
        ...


    def __init__(self, projectile: "Projectile", hitEntity: "Entity", hitBlock: "Block", hitFace: "BlockFace"):
        ...


    def getEntity(self) -> "Projectile":
        ...


    def getHitBlock(self) -> "Block":
        """
        Gets the block that was hit, if it was a block that was hit.

        Returns
        - hit block or else null
        """
        ...


    def getHitBlockFace(self) -> "BlockFace":
        """
        Gets the block face that was hit, if it was a block that was hit and the
        face was provided in the event.

        Returns
        - hit face or else null
        """
        ...


    def getHitEntity(self) -> "Entity":
        """
        Gets the entity that was hit, if it was an entity that was hit.

        Returns
        - hit entity or else null
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Whether to cancel the action that occurs when the projectile hits.
        
        In the case of an entity, it will not collide (unless it's a firework,
        then use FireworkExplodeEvent).
        
        In the case of a block, some blocks (eg target block, bell) will not
        perform the action associated.
        
        This does NOT prevent block collisions, and explosions will still occur
        unless their respective events are cancelled.

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
