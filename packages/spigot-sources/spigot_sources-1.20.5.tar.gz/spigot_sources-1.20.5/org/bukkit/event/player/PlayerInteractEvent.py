"""
Python module generated from Java source file org.bukkit.event.player.PlayerInteractEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import Action
from org.bukkit.event.block import BlockCanBuildEvent
from org.bukkit.event.player import *
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class PlayerInteractEvent(PlayerEvent, Cancellable):
    """
    Represents an event that is called when a player interacts with an object or
    air, potentially fired once for each hand. The hand can be determined using
    .getHand().
    
    This event will fire as cancelled if the vanilla behavior is to do nothing
    (e.g interacting with air). For the purpose of avoiding doubt, this means
    that the event will only be in the cancelled state if it is fired as a result
    of some prediction made by the server where no subsequent code will run,
    rather than when the subsequent interaction activity (e.g. placing a block in
    an illegal position (BlockCanBuildEvent) will fail.
    """

    def __init__(self, who: "Player", action: "Action", item: "ItemStack", clickedBlock: "Block", clickedFace: "BlockFace"):
        ...


    def __init__(self, who: "Player", action: "Action", item: "ItemStack", clickedBlock: "Block", clickedFace: "BlockFace", hand: "EquipmentSlot"):
        ...


    def __init__(self, who: "Player", action: "Action", item: "ItemStack", clickedBlock: "Block", clickedFace: "BlockFace", hand: "EquipmentSlot", clickedPosition: "Vector"):
        ...


    def getAction(self) -> "Action":
        """
        Returns the action type

        Returns
        - Action returns the type of interaction
        """
        ...


    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. Set to True if you want to
        prevent buckets from placing water and so forth

        Returns
        - boolean cancellation state

        Deprecated
        - This event has two possible cancellation states, one for
        .useInteractedBlock() and one for .useItemInHand(). It is
        possible a call might have the former False, but the latter True, eg in
        the case of using a firework whilst gliding. Callers should check the
        relevant methods individually.
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A canceled event will not be
        executed in the server, but will still pass to other plugins
        
        Canceling this event will prevent use of food (player won't lose the
        food item), prevent bows/snowballs/eggs from firing, etc. (player won't
        lose the ammo)

        Arguments
        - cancel: True if you wish to cancel this event
        """
        ...


    def getItem(self) -> "ItemStack":
        """
        Returns the item in hand represented by this event

        Returns
        - ItemStack the item used
        """
        ...


    def getMaterial(self) -> "Material":
        """
        Convenience method. Returns the material of the item represented by
        this event

        Returns
        - Material the material of the item used
        """
        ...


    def hasBlock(self) -> bool:
        """
        Check if this event involved a block

        Returns
        - boolean True if it did
        """
        ...


    def hasItem(self) -> bool:
        """
        Check if this event involved an item

        Returns
        - boolean True if it did
        """
        ...


    def isBlockInHand(self) -> bool:
        """
        Convenience method to inform the user whether this was a block
        placement event.

        Returns
        - boolean True if the item in hand was a block
        """
        ...


    def getClickedBlock(self) -> "Block":
        """
        Returns the clicked block

        Returns
        - Block returns the block clicked with this item.
        """
        ...


    def getBlockFace(self) -> "BlockFace":
        """
        Returns the face of the block that was clicked

        Returns
        - BlockFace returns the face of the block that was clicked
        """
        ...


    def useInteractedBlock(self) -> "Result":
        """
        This controls the action to take with the block (if any) that was
        clicked on. This event gets processed for all blocks, but most don't
        have a default action

        Returns
        - the action to take with the interacted block
        """
        ...


    def setUseInteractedBlock(self, useInteractedBlock: "Result") -> None:
        """
        Arguments
        - useInteractedBlock: the action to take with the interacted block
        """
        ...


    def useItemInHand(self) -> "Result":
        """
        This controls the action to take with the item the player is holding.
        This includes both blocks and items (such as flint and steel or
        records). When this is set to default, it will be allowed if no action
        is taken on the interacted block.

        Returns
        - the action to take with the item in hand
        """
        ...


    def setUseItemInHand(self, useItemInHand: "Result") -> None:
        """
        Arguments
        - useItemInHand: the action to take with the item in hand
        """
        ...


    def getHand(self) -> "EquipmentSlot":
        """
        The hand used to perform this interaction. May be null in the case of
        Action.PHYSICAL.

        Returns
        - the hand used to interact. May be null.
        """
        ...


    def getClickedPosition(self) -> "Vector":
        """
        Gets the exact position on the block the player interacted with, this will
        be null outside of Action.RIGHT_CLICK_BLOCK.
        
        All vector components are between 0.0 and 1.0 inclusive.

        Returns
        - the clicked position. May be null.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
