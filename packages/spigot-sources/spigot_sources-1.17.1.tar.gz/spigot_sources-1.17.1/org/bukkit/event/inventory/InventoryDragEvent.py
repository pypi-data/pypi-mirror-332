"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryDragEvent

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableSet
from java.util import Collections
from org.apache.commons.lang import Validate
from org.bukkit import Location
from org.bukkit.entity import HumanEntity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import BukkitScheduler
from typing import Any, Callable, Iterable, Tuple


class InventoryDragEvent(InventoryInteractEvent):
    """
    This event is called when the player drags an item in their cursor across
    the inventory. The ItemStack is distributed across the slots the
    HumanEntity dragged over. The method of distribution is described by the
    DragType returned by .getType().
    
    Canceling this event will result in none of the changes described in
    .getNewItems() being applied to the Inventory.
    
    Because InventoryDragEvent occurs within a modification of the Inventory,
    not all Inventory related methods are safe to use.
    
    The following should never be invoked by an EventHandler for
    InventoryDragEvent using the HumanEntity or InventoryView associated with
    this event.
    
    - HumanEntity.closeInventory()
    - HumanEntity.openInventory(Inventory)
    - HumanEntity.openWorkbench(Location, boolean)
    - HumanEntity.openEnchanting(Location, boolean)
    - InventoryView.close()
    
    To invoke one of these methods, schedule a task using
    BukkitScheduler.runTask(Plugin, Runnable), which will run the task
    on the next tick.  Also be aware that this is not an exhaustive list, and
    other methods could potentially create issues as well.
    
    Assuming the EntityHuman associated with this event is an instance of a
    Player, manipulating the MaxStackSize or contents of an Inventory will
    require an Invocation of Player.updateInventory().
    
    Any modifications to slots that are modified by the results of this
    InventoryDragEvent will be overwritten. To change these slots, this event
    should be cancelled and the changes applied. Alternatively, scheduling a
    task using BukkitScheduler.runTask(Plugin, Runnable), which would
    execute the task on the next tick, would work as well.
    """

    def __init__(self, what: "InventoryView", newCursor: "ItemStack", oldCursor: "ItemStack", right: bool, slots: dict["Integer", "ItemStack"]):
        ...


    def getNewItems(self) -> dict["Integer", "ItemStack"]:
        """
        Gets all items to be added to the inventory in this drag.

        Returns
        - map from raw slot id to new ItemStack
        """
        ...


    def getRawSlots(self) -> set["Integer"]:
        """
        Gets the raw slot ids to be changed in this drag.

        Returns
        - list of raw slot ids, suitable for getView().getItem(int)
        """
        ...


    def getInventorySlots(self) -> set["Integer"]:
        """
        Gets the slots to be changed in this drag.

        Returns
        - list of converted slot ids, suitable for org.bukkit.inventory.Inventory.getItem(int).
        """
        ...


    def getCursor(self) -> "ItemStack":
        """
        Gets the result cursor after the drag is done. The returned value is
        mutable.

        Returns
        - the result cursor
        """
        ...


    def setCursor(self, newCursor: "ItemStack") -> None:
        """
        Sets the result cursor after the drag is done.
        
        Changing this item stack changes the cursor item. Note that changing
        the affected "dragged" slots does not change this ItemStack, nor does
        changing this ItemStack affect the "dragged" slots.

        Arguments
        - newCursor: the new cursor ItemStack
        """
        ...


    def getOldCursor(self) -> "ItemStack":
        """
        Gets an ItemStack representing the cursor prior to any modifications
        as a result of this drag.

        Returns
        - the original cursor
        """
        ...


    def getType(self) -> "DragType":
        """
        Gets the DragType that describes the behavior of ItemStacks placed
        after this InventoryDragEvent.
        
        The ItemStacks and the raw slots that they're being applied to can be
        found using .getNewItems().

        Returns
        - the DragType of this InventoryDragEvent
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
