"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryClickEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import HumanEntity
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.event.inventory.InventoryType import SlotType
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import ItemStack
from org.bukkit.plugin import Plugin
from org.bukkit.scheduler import BukkitScheduler
from typing import Any, Callable, Iterable, Tuple


class InventoryClickEvent(InventoryInteractEvent):
    """
    This event is called when a player clicks in an inventory.
    
    Because InventoryClickEvent occurs within a modification of the Inventory,
    not all Inventory related methods are safe to use.
    
    The following should never be invoked by an EventHandler for
    InventoryClickEvent using the HumanEntity or InventoryView associated with
    this event:
    
    - HumanEntity.closeInventory()
    - HumanEntity.openInventory(Inventory)
    - HumanEntity.openWorkbench(Location, boolean)
    - HumanEntity.openEnchanting(Location, boolean)
    - InventoryView.close()
    
    To invoke one of these methods, schedule a task using
    BukkitScheduler.runTask(Plugin, Runnable), which will run the task
    on the next tick. Also be aware that this is not an exhaustive list, and
    other methods could potentially create issues as well.
    
    Assuming the EntityHuman associated with this event is an instance of a
    Player, manipulating the MaxStackSize or contents of an Inventory will
    require an Invocation of Player.updateInventory().
    
    Modifications to slots that are modified by the results of this
    InventoryClickEvent can be overwritten. To change these slots, this event
    should be cancelled and all desired changes to the inventory applied.
    Alternatively, scheduling a task using BukkitScheduler.runTask(
    Plugin, Runnable), which would execute the task on the next tick, would
    work as well.
    """

    def __init__(self, view: "InventoryView", type: "SlotType", slot: int, click: "ClickType", action: "InventoryAction"):
        ...


    def __init__(self, view: "InventoryView", type: "SlotType", slot: int, click: "ClickType", action: "InventoryAction", key: int):
        ...


    def getSlotType(self) -> "SlotType":
        """
        Gets the type of slot that was clicked.

        Returns
        - the slot type
        """
        ...


    def getCursor(self) -> "ItemStack":
        """
        Gets the current ItemStack on the cursor.

        Returns
        - the cursor ItemStack
        """
        ...


    def getCurrentItem(self) -> "ItemStack":
        """
        Gets the ItemStack currently in the clicked slot.

        Returns
        - the item in the clicked
        """
        ...


    def isRightClick(self) -> bool:
        """
        Gets whether or not the ClickType for this event represents a right
        click.

        Returns
        - True if the ClickType uses the right mouse button.

        See
        - ClickType.isRightClick()
        """
        ...


    def isLeftClick(self) -> bool:
        """
        Gets whether or not the ClickType for this event represents a left
        click.

        Returns
        - True if the ClickType uses the left mouse button.

        See
        - ClickType.isLeftClick()
        """
        ...


    def isShiftClick(self) -> bool:
        """
        Gets whether the ClickType for this event indicates that the key was
        pressed down when the click was made.

        Returns
        - True if the ClickType uses Shift or Ctrl.

        See
        - ClickType.isShiftClick()
        """
        ...


    def setCursor(self, stack: "ItemStack") -> None:
        """
        Sets the item on the cursor.

        Arguments
        - stack: the new cursor item

        Deprecated
        - This changes the ItemStack in their hand before any
            calculations are applied to the Inventory, which has a tendency to
            create inconsistencies between the Player and the server, and to
            make unexpected changes in the behavior of the clicked Inventory.
        """
        ...


    def setCurrentItem(self, stack: "ItemStack") -> None:
        """
        Sets the ItemStack currently in the clicked slot.

        Arguments
        - stack: the item to be placed in the current slot
        """
        ...


    def getClickedInventory(self) -> "Inventory":
        """
        Gets the inventory corresponding to the clicked slot.

        Returns
        - inventory, or null if clicked outside

        See
        - InventoryView.getInventory(int)
        """
        ...


    def getSlot(self) -> int:
        """
        The slot number that was clicked, ready for passing to
        Inventory.getItem(int). Note that there may be two slots with
        the same slot number, since a view links two different inventories.

        Returns
        - The slot number.
        """
        ...


    def getRawSlot(self) -> int:
        """
        The raw slot number clicked, ready for passing to InventoryView
        .getItem(int) This slot number is unique for the view.

        Returns
        - the slot number
        """
        ...


    def getHotbarButton(self) -> int:
        """
        If the ClickType is NUMBER_KEY, this method will return the index of
        the pressed key (0-8).

        Returns
        - the number on the key minus 1 (range 0-8); or -1 if not
            a NUMBER_KEY action
        """
        ...


    def getAction(self) -> "InventoryAction":
        """
        Gets the InventoryAction that triggered this event.
        
        This action cannot be changed, and represents what the normal outcome
        of the event will be. To change the behavior of this
        InventoryClickEvent, changes must be manually applied.

        Returns
        - the InventoryAction that triggered this event.
        """
        ...


    def getClick(self) -> "ClickType":
        """
        Gets the ClickType for this event.
        
        This is insulated against changes to the inventory by other plugins.

        Returns
        - the type of inventory click
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
