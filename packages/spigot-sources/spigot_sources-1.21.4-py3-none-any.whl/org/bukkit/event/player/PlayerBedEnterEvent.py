"""
Python module generated from Java source file org.bukkit.event.player.PlayerBedEnterEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import World
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerBedEnterEvent(PlayerEvent, Cancellable):
    """
    This event is fired when the player is almost about to enter the bed.
    """

    def __init__(self, who: "Player", bed: "Block", bedEnterResult: "BedEnterResult"):
        ...


    def __init__(self, who: "Player", bed: "Block"):
        ...


    def getBedEnterResult(self) -> "BedEnterResult":
        """
        This describes the default outcome of this event.

        Returns
        - the bed enter result representing the default outcome of this event
        """
        ...


    def useBed(self) -> "Result":
        """
        This controls the action to take with the bed that was clicked on.
        
        In case of org.bukkit.event.Event.Result.DEFAULT, the default outcome is described by
        .getBedEnterResult().

        Returns
        - the action to take with the interacted bed

        See
        - .setUseBed(org.bukkit.event.Event.Result)
        """
        ...


    def setUseBed(self, useBed: "Result") -> None:
        """
        Sets the action to take with the interacted bed.
        
        org.bukkit.event.Event.Result.ALLOW will result in the player sleeping, regardless of
        the default outcome described by .getBedEnterResult().
        
        org.bukkit.event.Event.Result.DENY will prevent the player from sleeping. This has the
        same effect as canceling the event via .setCancelled(boolean).
        
        org.bukkit.event.Event.Result.DEFAULT will result in the outcome described by
        .getBedEnterResult().

        Arguments
        - useBed: the action to take with the interacted bed

        See
        - .useBed()
        """
        ...


    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. Set to True if you want to
        prevent the player from sleeping.
        
        Canceling the event has the same effect as setting .useBed() to
        org.bukkit.event.Event.Result.DENY.
        
        For backwards compatibility reasons this also returns True if
        .useBed() is org.bukkit.event.Event.Result.DEFAULT and the
        .getBedEnterResult() default action is to prevent bed entering.

        Returns
        - boolean cancellation state
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A canceled event will not be
        executed in the server, but will still pass to other plugins.
        
        Canceling this event will prevent use of the bed.

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...


    def getBed(self) -> "Block":
        """
        Returns the bed block involved in this event.

        Returns
        - the bed block involved in this event
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class BedEnterResult(Enum):
        """
        Represents the default possible outcomes of this event.
        """

        OK = 0
        """
        The player will enter the bed.
        """
        NOT_POSSIBLE_HERE = 1
        """
        The world doesn't allow sleeping or saving the spawn point (eg,
        Nether, The End or Custom Worlds). This is based on
        World.isBedWorks() and World.isNatural().
        
        Entering the bed is prevented and if World.isBedWorks() is
        False then the bed explodes.
        """
        NOT_POSSIBLE_NOW = 2
        """
        Entering the bed is prevented due to it not being night nor
        thundering currently.
        
        If the event is forcefully allowed during daytime, the player will
        enter the bed (and set its bed location), but might get immediately
        thrown out again.
        """
        TOO_FAR_AWAY = 3
        """
        Entering the bed is prevented due to the player being too far away.
        """
        NOT_SAFE = 4
        """
        Entering the bed is prevented due to there being monsters nearby.
        """
        OTHER_PROBLEM = 5
        """
        Entering the bed is prevented due to there being some other problem.
        """
