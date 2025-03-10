"""
Python module generated from Java source file org.bukkit.event.block.BlockIgniteEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class BlockIgniteEvent(BlockEvent, Cancellable):
    """
    Called when a block is ignited. If you want to catch when a Player places
    fire, you need to use BlockPlaceEvent.
    
    If a Block Ignite event is cancelled, the block will not be ignited.
    """

    def __init__(self, theBlock: "Block", cause: "IgniteCause", ignitingEntity: "Entity"):
        ...


    def __init__(self, theBlock: "Block", cause: "IgniteCause", ignitingBlock: "Block"):
        ...


    def __init__(self, theBlock: "Block", cause: "IgniteCause", ignitingEntity: "Entity", ignitingBlock: "Block"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getCause(self) -> "IgniteCause":
        """
        Gets the cause of block ignite.

        Returns
        - An IgniteCause value detailing the cause of block ignition
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player who ignited this block

        Returns
        - The Player that placed/ignited the fire block, or null if not ignited by a Player.
        """
        ...


    def getIgnitingEntity(self) -> "Entity":
        """
        Gets the entity who ignited this block

        Returns
        - The Entity that placed/ignited the fire block, or null if not ignited by a Entity.
        """
        ...


    def getIgnitingBlock(self) -> "Block":
        """
        Gets the block which ignited this block

        Returns
        - The Block that placed/ignited the fire block, or null if not ignited by a Block.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class IgniteCause(Enum):
        """
        An enum to specify the cause of the ignite
        """

        LAVA = 0
        """
        Block ignition caused by lava.
        """
        FLINT_AND_STEEL = 1
        """
        Block ignition caused by a player or dispenser using flint-and-steel.
        """
        SPREAD = 2
        """
        Block ignition caused by dynamic spreading of fire.
        """
        LIGHTNING = 3
        """
        Block ignition caused by lightning.
        """
        FIREBALL = 4
        """
        Block ignition caused by an entity using a fireball.
        """
        ENDER_CRYSTAL = 5
        """
        Block ignition caused by an Ender Crystal.
        """
        EXPLOSION = 6
        """
        Block ignition caused by explosion.
        """
        ARROW = 7
        """
        Block ignition caused by a flaming arrow.
        """
