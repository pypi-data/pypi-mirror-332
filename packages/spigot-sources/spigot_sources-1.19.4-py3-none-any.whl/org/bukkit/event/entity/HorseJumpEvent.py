"""
Python module generated from Java source file org.bukkit.event.entity.HorseJumpEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import AbstractHorse
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class HorseJumpEvent(EntityEvent, Cancellable):
    """
    Called when a horse jumps.
    """

    def __init__(self, horse: "AbstractHorse", power: float):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Deprecated
        - horse jumping was moved client side.
        """
        ...


    def getEntity(self) -> "AbstractHorse":
        ...


    def getPower(self) -> float:
        """
        Gets the power of the jump.
        
        Power is a value that defines how much of the horse's jump strength
        should be used for the jump. Power is effectively multiplied times
        the horse's jump strength to determine how high the jump is; 0
        represents no jump strength while 1 represents full jump strength.
        Setting power to a value above 1 will use additional jump strength
        that the horse does not usually have.
        
        Power does not affect how high the horse is capable of jumping, only
        how much of its jumping capability will be used in this jump. To set
        the horse's overall jump strength, see AbstractHorse.setJumpStrength(double).

        Returns
        - jump strength
        """
        ...


    def setPower(self, power: float) -> None:
        """
        Sets the power of the jump.
        
        Jump power can be set to a value above 1.0 which will increase the
        strength of this jump above the horse's actual jump strength.
        
        Setting the jump power to 0 will result in the jump animation still
        playing, but the horse not leaving the ground. Only canceling this
        event will result in no jump animation at all.

        Arguments
        - power: power of the jump

        Deprecated
        - horse jumping was moved client side.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
