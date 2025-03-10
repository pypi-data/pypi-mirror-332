"""
Python module generated from Java source file org.bukkit.event.block.TNTPrimeEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class TNTPrimeEvent(BlockEvent, Cancellable):
    """
    Called when a block of TNT in the world become primed.
    
    If a TNT Prime event is cancelled, the block of TNT will not become primed.
    """

    def __init__(self, block: "Block", igniteCause: "PrimeCause", primingEntity: "Entity", primingBlock: "Block"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getCause(self) -> "PrimeCause":
        """
        Get the cause of the TNT becoming primed.

        Returns
        - the cause
        """
        ...


    def getPrimingEntity(self) -> "Entity":
        """
        Get the entity that caused the TNT to be primed.

        Returns
        - the entity that caused the TNT to be primed, or null if it was
        not caused by an entity.
        """
        ...


    def getPrimingBlock(self) -> "Block":
        """
        Get the block that caused the TNT to be primed.

        Returns
        - the block that caused the TNT to be primed, or null if it was not
        caused by a block.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class PrimeCause(Enum):
        """
        An enum to represent the cause of a TNT block becoming primed.
        """

        FIRE = 0
        """
        When TNT is primed by fire spreading.
        """
        REDSTONE = 1
        """
        When TNT is primed by a redstone signal.
        """
        PLAYER = 2
        """
        When TNT is primed by a player interacting with it directly.
        """
        EXPLOSION = 3
        """
        When TNT is primed by a nearby explosion.
        """
        PROJECTILE = 4
        """
        When TNT is primed after getting hit with a burning projectile.
        """
        BLOCK_BREAK = 5
        """
        When TNT with the unstable block state set to True is broken.
        
        Note: Canceling a prime event with this cause will stop the primed
        TNT from spawning but will not stop the block from being broken.
        """
        DISPENSER = 6
        """
        When TNT is primed by a dispenser holding flint and steel.
        
        Note: This event is not called for a dispenser dispensing TNT
        directly.
        """
