"""
Python module generated from Java source file org.bukkit.event.player.PlayerFishEvent

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Entity
from org.bukkit.entity import FishHook
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from typing import Any, Callable, Iterable, Tuple


class PlayerFishEvent(PlayerEvent, Cancellable):
    """
    Thrown when a player is fishing
    """

    def __init__(self, player: "Player", entity: "Entity", hookEntity: "FishHook", hand: "EquipmentSlot", state: "State"):
        ...


    def __init__(self, player: "Player", entity: "Entity", hookEntity: "FishHook", state: "State"):
        ...


    def getCaught(self) -> "Entity":
        """
        Gets the entity caught by the player.
        
        If player has fished successfully, the result may be cast to org.bukkit.entity.Item.

        Returns
        - Entity caught by the player, Entity if fishing, and null if
            bobber has gotten stuck in the ground or nothing has been caught
        """
        ...


    def getHook(self) -> "FishHook":
        """
        Gets the fishing hook.

        Returns
        - the entity representing the fishing hook/bobber.
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getExpToDrop(self) -> int:
        """
        Gets the amount of experience received when fishing.
        
        Note: This value has no default effect unless the event state is State.CAUGHT_FISH.

        Returns
        - the amount of experience to drop
        """
        ...


    def setExpToDrop(self, amount: int) -> None:
        """
        Sets the amount of experience received when fishing.
        
        Note: This value has no default effect unless the event state is State.CAUGHT_FISH.

        Arguments
        - amount: the amount of experience to drop
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        Get the hand that was used in this event.
        
        The hand used is only present when the event state is State.FISHING.
        In all other states, the hand is null.

        Returns
        - the hand
        """
        ...


    def getState(self) -> "State":
        """
        Gets the state of the fishing

        Returns
        - A State detailing the state of the fishing
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class State(Enum):
        """
        An enum to specify the state of the fishing
        """

        FISHING = 0
        """
        When a player is fishing, ie casting the line out.
        """
        CAUGHT_FISH = 1
        """
        When a player has successfully caught a fish and is reeling it in. In
        this instance, a "fish" is any item retrieved from water as a result
        of fishing, ie an item, but not necessarily a fish.
        """
        CAUGHT_ENTITY = 2
        """
        When a player has successfully caught an entity. This refers to any
        already spawned entity in the world that has been hooked directly by
        the rod.
        """
        IN_GROUND = 3
        """
        When a bobber is stuck in the ground.
        """
        FAILED_ATTEMPT = 4
        """
        When a player fails to catch a bite while fishing usually due to
        poor timing.
        """
        REEL_IN = 5
        """
        When a player reels in their hook without receiving any bites.
        """
        BITE = 6
        """
        Called when there is a bite on the hook and it is ready to be reeled
        in.
        """
