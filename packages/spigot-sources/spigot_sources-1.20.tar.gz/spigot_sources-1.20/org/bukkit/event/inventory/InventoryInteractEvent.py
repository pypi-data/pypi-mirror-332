"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryInteractEvent

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryView
from typing import Any, Callable, Iterable, Tuple


class InventoryInteractEvent(InventoryEvent, Cancellable):
    """
    An abstract base class for events that describe an interaction between a
    HumanEntity and the contents of an Inventory.
    """

    def __init__(self, transaction: "InventoryView"):
        ...


    def getWhoClicked(self) -> "HumanEntity":
        """
        Gets the player who performed the click.

        Returns
        - The clicking player.
        """
        ...


    def setResult(self, newResult: "Result") -> None:
        """
        Sets the result of this event. This will change whether or not this
        event is considered cancelled.

        Arguments
        - newResult: the new org.bukkit.event.Event.Result for this event

        See
        - .isCancelled()
        """
        ...


    def getResult(self) -> "Result":
        """
        Gets the org.bukkit.event.Event.Result of this event. The Result describes the
        behavior that will be applied to the inventory in relation to this
        event.

        Returns
        - the Result of this event.
        """
        ...


    def isCancelled(self) -> bool:
        """
        Gets whether or not this event is cancelled. This is based off of the
        Result value returned by .getResult().  Result.ALLOW and
        Result.DEFAULT will result in a returned value of False, but
        Result.DENY will result in a returned value of True.
        

        Returns
        - whether the event is cancelled
        """
        ...


    def setCancelled(self, toCancel: bool) -> None:
        """
        Proxy method to .setResult(org.bukkit.event.Event.Result) for the Cancellable
        interface. .setResult(org.bukkit.event.Event.Result) is preferred, as it allows
        you to specify the Result beyond Result.DENY and Result.ALLOW.
        

        Arguments
        - toCancel: result becomes DENY if True, ALLOW if False
        """
        ...
