"""
Python module generated from Java source file org.bukkit.inventory.InventoryView

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit.entity import HumanEntity
from org.bukkit.event.inventory import InventoryType
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class InventoryView:
    """
    Represents a view linking two inventories and a single player (whose
    inventory may or may not be one of the two).
    
    Note: If you implement this interface but fail to satisfy the expected
    contracts of certain methods, there's no guarantee that the game will work
    as it should.
    """

    OUTSIDE = -999


    def getTopInventory(self) -> "Inventory":
        """
        Get the upper inventory involved in this transaction.

        Returns
        - the inventory
        """
        ...


    def getBottomInventory(self) -> "Inventory":
        """
        Get the lower inventory involved in this transaction.

        Returns
        - the inventory
        """
        ...


    def getPlayer(self) -> "HumanEntity":
        """
        Get the player viewing.

        Returns
        - the player
        """
        ...


    def getType(self) -> "InventoryType":
        """
        Determine the type of inventory involved in the transaction. This
        indicates the window style being shown. It will never return PLAYER,
        since that is common to all windows.

        Returns
        - the inventory type
        """
        ...


    def setItem(self, slot: int, item: "ItemStack") -> None:
        """
        Sets one item in this inventory view by its raw slot ID.
        
        Note: If slot ID -999 is chosen, it may be expected that the item is
        dropped on the ground. This is not required behaviour, however.

        Arguments
        - slot: The ID as returned by InventoryClickEvent.getRawSlot()
        - item: The new item to put in the slot, or null to clear it.
        """
        ...


    def getItem(self, slot: int) -> "ItemStack":
        """
        Gets one item in this inventory view by its raw slot ID.

        Arguments
        - slot: The ID as returned by InventoryClickEvent.getRawSlot()

        Returns
        - The item currently in the slot.
        """
        ...


    def setCursor(self, item: "ItemStack") -> None:
        """
        Sets the item on the cursor of one of the viewing players.

        Arguments
        - item: The item to put on the cursor, or null to remove the item
            on their cursor.
        """
        ...


    def getCursor(self) -> "ItemStack":
        """
        Get the item on the cursor of one of the viewing players.

        Returns
        - The item on the player's cursor, or null if they aren't holding
            one.
        """
        ...


    def getInventory(self, rawSlot: int) -> "Inventory":
        """
        Gets the inventory corresponding to the given raw slot ID.
        
        If the slot ID is .OUTSIDE null will be returned, otherwise
        behaviour for illegal and negative slot IDs is undefined.
        
        May be used with .convertSlot(int) to directly index an
        underlying inventory.

        Arguments
        - rawSlot: The raw slot ID.

        Returns
        - corresponding inventory, or null
        """
        ...


    def convertSlot(self, rawSlot: int) -> int:
        """
        Converts a raw slot ID into its local slot ID into whichever of the two
        inventories the slot points to.
        
        If the raw slot refers to the upper inventory, it will be returned
        unchanged and thus be suitable for getTopInventory().getItem(); if it
        refers to the lower inventory, the output will differ from the input
        and be suitable for getBottomInventory().getItem().

        Arguments
        - rawSlot: The raw slot ID.

        Returns
        - The converted slot ID.
        """
        ...


    def getSlotType(self, slot: int) -> "InventoryType.SlotType":
        """
        Determine the type of the slot by its raw slot ID.
        
        If the type of the slot is unknown, then
        InventoryType.SlotType.CONTAINER will be returned.

        Arguments
        - slot: The raw slot ID

        Returns
        - the slot type
        """
        ...


    def close(self) -> None:
        """
        Closes the inventory view.
        """
        ...


    def countSlots(self) -> int:
        """
        Check the total number of slots in this view, combining the upper and
        lower inventories.
        
        Note though that it's possible for this to be greater than the sum of
        the two inventories if for example some slots are not being used.

        Returns
        - The total size
        """
        ...


    def setProperty(self, prop: "Property", value: int) -> bool:
        """
        Sets an extra property of this inventory if supported by that
        inventory, for example the state of a progress bar.

        Arguments
        - prop: the window property to update
        - value: the new value for the window property

        Returns
        - True if the property was updated successfully, False if the
            property is not supported by that inventory
        """
        ...


    def getTitle(self) -> str:
        """
        Get the title of this inventory window.

        Returns
        - The title.
        """
        ...


    def getOriginalTitle(self) -> str:
        """
        Get the original title of this inventory window, before any changes were
        made using .setTitle(String).

        Returns
        - the original title
        """
        ...


    def setTitle(self, title: str) -> None:
        """
        Sets the title of this inventory window to the specified title if the
        inventory window supports it.
        
        Note if the inventory does not support titles that can be changed (ie, it
        is not creatable or viewed by a player), then this method will throw an
        exception.

        Arguments
        - title: The new title.
        """
        ...


    class Property(Enum):
        """
        Represents various extra properties of certain inventory windows.
        """

        BREW_TIME = (0, InventoryType.BREWING)
        """
        The progress of the down-pointing arrow in a brewing inventory.
        """
        FUEL_TIME = (1, InventoryType.BREWING)
        """
        The progress of the fuel slot in a brewing inventory.
        
        This is a value between 0 and 20, with 0 making the bar empty, and 20
        making the bar full.
        """
        BURN_TIME = (0, InventoryType.FURNACE)
        """
        The progress of the flame in a furnace inventory.
        """
        TICKS_FOR_CURRENT_FUEL = (1, InventoryType.FURNACE)
        """
        How many total ticks the current fuel should last.
        """
        COOK_TIME = (2, InventoryType.FURNACE)
        """
        The progress of the right-pointing arrow in a furnace inventory.
        """
        TICKS_FOR_CURRENT_SMELTING = (3, InventoryType.FURNACE)
        """
        How many total ticks the current smelting should last.
        """
        ENCHANT_BUTTON1 = (0, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the top button's experience level
        value.
        """
        ENCHANT_BUTTON2 = (1, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the middle button's experience level
        value.
        """
        ENCHANT_BUTTON3 = (2, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the bottom button's experience level
        value.
        """
        ENCHANT_XP_SEED = (3, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the first four bits of the player's xpSeed.
        """
        ENCHANT_ID1 = (4, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the top button's enchantment's id
        """
        ENCHANT_ID2 = (5, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the middle button's enchantment's id
        """
        ENCHANT_ID3 = (6, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the bottom button's enchantment's id
        """
        ENCHANT_LEVEL1 = (7, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the top button's level value.
        """
        ENCHANT_LEVEL2 = (8, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the middle button's level value.
        """
        ENCHANT_LEVEL3 = (9, InventoryType.ENCHANTING)
        """
        In an enchanting inventory, the bottom button's level value.
        """
        LEVELS = (0, InventoryType.BEACON)
        """
        In an beacon inventory, the levels of the beacon
        """
        PRIMARY_EFFECT = (1, InventoryType.BEACON)
        """
        In an beacon inventory, the primary potion effect
        """
        SECONDARY_EFFECT = (2, InventoryType.BEACON)
        """
        In an beacon inventory, the secondary potion effect
        """
        REPAIR_COST = (0, InventoryType.ANVIL)
        """
        The repair's cost in xp levels
        """
        BOOK_PAGE = (0, InventoryType.LECTERN)
        """
        The lectern's current open book page
        """


        def getType(self) -> "InventoryType":
            ...


        def getId(self) -> int:
            """
            Gets the id of this view.

            Returns
            - the id of this view

            Deprecated
            - Magic value
            """
            ...
