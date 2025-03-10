"""
Python module generated from Java source file org.bukkit.event.entity.EntityExhaustionEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityExhaustionEvent(EntityEvent, Cancellable):
    """
    Called when a human entity experiences exhaustion.
    
    An exhaustion level greater than 4.0 causes a decrease in saturation by 1.
    """

    def __init__(self, who: "HumanEntity", exhaustionReason: "ExhaustionReason", exhaustion: float):
        ...


    def getExhaustionReason(self) -> "ExhaustionReason":
        """
        Gets the ExhaustionReason for this event

        Returns
        - the exhaustion reason
        """
        ...


    def getExhaustion(self) -> float:
        """
        Get the amount of exhaustion to add to the player's current exhaustion.

        Returns
        - amount of exhaustion
        """
        ...


    def setExhaustion(self, exhaustion: float) -> None:
        """
        Set the exhaustion to apply to the player.
        
        The maximum exhaustion that a player can have is 40. No error will be
        thrown if this limit is hit. This value may be negative, but there is
        unknown behavior for when exhaustion is below 0.

        Arguments
        - exhaustion: new exhaustion to add
        """
        ...


    def getEntity(self) -> "HumanEntity":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class ExhaustionReason(Enum):
        """
        The reason for why a PlayerExhaustionEvent takes place
        """

        BLOCK_MINED = 0
        """
        Player mines a block
        """
        HUNGER_EFFECT = 1
        """
        Player has the hunger potion effect
        """
        DAMAGED = 2
        """
        Player takes damage
        """
        ATTACK = 3
        """
        Player attacks another entity
        """
        JUMP_SPRINT = 4
        """
        Player is sprint jumping
        """
        JUMP = 5
        """
        Player jumps
        """
        SWIM = 6
        """
        Player swims one centimeter
        """
        WALK_UNDERWATER = 7
        """
        Player walks underwater one centimeter
        """
        WALK_ON_WATER = 8
        """
        Player moves on the surface of water one centimeter
        """
        SPRINT = 9
        """
        Player sprints one centimeter
        """
        CROUCH = 10
        """
        Player crouches one centimeter (does not effect exhaustion, but fires
        nonetheless)
        """
        WALK = 11
        """
        Player walks one centimeter (does not effect exhaustion, but fires
        nonetheless)
        """
        REGEN = 12
        """
        Player regenerated health
        """
        UNKNOWN = 13
        """
        Unknown exhaustion reason
        """
