"""
Python module generated from Java source file org.bukkit.inventory.Inventory

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import ListIterator
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit.entity import HumanEntity
from org.bukkit.event.inventory import InventoryType
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class Inventory(Iterable):
    """
    Interface to the various inventories. Behavior relating to Material.AIR is unspecified.
    
    
    **Note that whilst .iterator() deals with the entire inventory, add
    / contains / remove methods deal only with the storage contents.**
    
    **Consider using .getContents() and .getStorageContents() for
    specific iteration.**

    See
    - .getStorageContents()
    """

    def getSize(self) -> int:
        """
        Returns the size of the inventory

        Returns
        - The size of the inventory
        """
        ...


    def getMaxStackSize(self) -> int:
        """
        Returns the maximum stack size for an ItemStack in this inventory.

        Returns
        - The maximum size for an ItemStack in this inventory.
        """
        ...


    def setMaxStackSize(self, size: int) -> None:
        """
        This method allows you to change the maximum stack size for an
        inventory.
        
        **Caveats:**
        
        - Not all inventories respect this value.
        - Stacks larger than 127 may be clipped when the world is saved.
        - This value is not guaranteed to be preserved; be sure to set it
            before every time you want to set a slot over the max stack size.
        - Stacks larger than the default max size for this type of inventory
            may not display correctly in the client.

        Arguments
        - size: The new maximum stack size for items in this inventory.
        """
        ...


    def getItem(self, index: int) -> "ItemStack":
        """
        Returns the ItemStack found in the slot at the given index

        Arguments
        - index: The index of the Slot's ItemStack to return

        Returns
        - The ItemStack in the slot
        """
        ...


    def setItem(self, index: int, item: "ItemStack") -> None:
        """
        Stores the ItemStack at the given index of the inventory.

        Arguments
        - index: The index where to put the ItemStack
        - item: The ItemStack to set
        """
        ...


    def addItem(self, *items: Tuple["ItemStack", ...]) -> dict["Integer", "ItemStack"]:
        """
        Stores the given ItemStacks in the inventory. This will try to fill
        existing stacks and empty slots as well as it can.
        
        The returned HashMap contains what it couldn't store, where the key is
        the index of the parameter, and the value is the ItemStack at that
        index of the varargs parameter. If all items are stored, it will return
        an empty HashMap.
        
        If you pass in ItemStacks which exceed the maximum stack size for the
        Material, first they will be added to partial stacks where
        Material.getMaxStackSize() is not exceeded, up to
        Material.getMaxStackSize(). When there are no partial stacks left
        stacks will be split on Inventory.getMaxStackSize() allowing you to
        exceed the maximum stack size for that material.
        
        It is known that in some implementations this method will also set
        the inputted argument amount to the number of that item not placed in
        slots.

        Arguments
        - items: The ItemStacks to add

        Returns
        - A HashMap containing items that didn't fit.

        Raises
        - IllegalArgumentException: if items or any element in it is null
        """
        ...


    def removeItem(self, *items: Tuple["ItemStack", ...]) -> dict["Integer", "ItemStack"]:
        """
        Removes the given ItemStacks from the inventory.
        
        It will try to remove 'as much as possible' from the types and amounts
        you give as arguments.
        
        The returned HashMap contains what it couldn't remove, where the key is
        the index of the parameter, and the value is the ItemStack at that
        index of the varargs parameter. If all the given ItemStacks are
        removed, it will return an empty HashMap.
        
        It is known that in some implementations this method will also set the
        inputted argument amount to the number of that item not removed from
        slots.

        Arguments
        - items: The ItemStacks to remove

        Returns
        - A HashMap containing items that couldn't be removed.

        Raises
        - IllegalArgumentException: if items is null
        """
        ...


    def getContents(self) -> list["ItemStack"]:
        """
        Returns all ItemStacks from the inventory

        Returns
        - An array of ItemStacks from the inventory. Individual items may be null.
        """
        ...


    def setContents(self, items: list["ItemStack"]) -> None:
        """
        Completely replaces the inventory's contents. Removes all existing
        contents and replaces it with the ItemStacks given in the array.

        Arguments
        - items: A complete replacement for the contents; the length must
            be less than or equal to .getSize().

        Raises
        - IllegalArgumentException: If the array has more items than the
            inventory.
        """
        ...


    def getStorageContents(self) -> list["ItemStack"]:
        """
        Return the contents from the section of the inventory where items can
        reasonably be expected to be stored. In most cases this will represent
        the entire inventory, but in some cases it may exclude armor or result
        slots.
        
        It is these contents which will be used for add / contains / remove
        methods which look for a specific stack.

        Returns
        - inventory storage contents. Individual items may be null.
        """
        ...


    def setStorageContents(self, items: list["ItemStack"]) -> None:
        """
        Put the given ItemStacks into the storage slots

        Arguments
        - items: The ItemStacks to use as storage contents

        Raises
        - IllegalArgumentException: If the array has more items than the
        inventory.
        """
        ...


    def contains(self, material: "Material") -> bool:
        """
        Checks if the inventory contains any ItemStacks with the given
        material.

        Arguments
        - material: The material to check for

        Returns
        - True if an ItemStack is found with the given Material

        Raises
        - IllegalArgumentException: if material is null
        """
        ...


    def contains(self, item: "ItemStack") -> bool:
        """
        Checks if the inventory contains any ItemStacks matching the given
        ItemStack.
        
        This will only return True if both the type and the amount of the stack
        match.

        Arguments
        - item: The ItemStack to match against

        Returns
        - False if item is null, True if any exactly matching ItemStacks
            were found
        """
        ...


    def contains(self, material: "Material", amount: int) -> bool:
        """
        Checks if the inventory contains any ItemStacks with the given
        material, adding to at least the minimum amount specified.

        Arguments
        - material: The material to check for
        - amount: The minimum amount

        Returns
        - True if amount is less than 1, True if enough ItemStacks were
            found to add to the given amount

        Raises
        - IllegalArgumentException: if material is null
        """
        ...


    def contains(self, item: "ItemStack", amount: int) -> bool:
        """
        Checks if the inventory contains at least the minimum amount specified
        of exactly matching ItemStacks.
        
        An ItemStack only counts if both the type and the amount of the stack
        match.

        Arguments
        - item: the ItemStack to match against
        - amount: how many identical stacks to check for

        Returns
        - False if item is null, True if amount less than 1, True if
            amount of exactly matching ItemStacks were found

        See
        - .containsAtLeast(ItemStack, int)
        """
        ...


    def containsAtLeast(self, item: "ItemStack", amount: int) -> bool:
        """
        Checks if the inventory contains ItemStacks matching the given
        ItemStack whose amounts sum to at least the minimum amount specified.

        Arguments
        - item: the ItemStack to match against
        - amount: the minimum amount

        Returns
        - False if item is null, True if amount less than 1, True if
            enough ItemStacks were found to add to the given amount
        """
        ...


    def all(self, material: "Material") -> dict["Integer", "ItemStack"]:
        """
        Returns a HashMap with all slots and ItemStacks in the inventory with
        the given Material.
        
        The HashMap contains entries where, the key is the slot index, and the
        value is the ItemStack in that slot. If no matching ItemStack with the
        given Material is found, an empty map is returned.

        Arguments
        - material: The material to look for

        Returns
        - A HashMap containing the slot index, ItemStack pairs

        Raises
        - IllegalArgumentException: if material is null
        """
        ...


    def all(self, item: "ItemStack") -> dict["Integer", "ItemStack"]:
        """
        Finds all slots in the inventory containing any ItemStacks with the
        given ItemStack. This will only match slots if both the type and the
        amount of the stack match
        
        The HashMap contains entries where, the key is the slot index, and the
        value is the ItemStack in that slot. If no matching ItemStack with the
        given Material is found, an empty map is returned.

        Arguments
        - item: The ItemStack to match against

        Returns
        - A map from slot indexes to item at index
        """
        ...


    def first(self, material: "Material") -> int:
        """
        Finds the first slot in the inventory containing an ItemStack with the
        given material

        Arguments
        - material: The material to look for

        Returns
        - The slot index of the given Material or -1 if not found

        Raises
        - IllegalArgumentException: if material is null
        """
        ...


    def first(self, item: "ItemStack") -> int:
        """
        Returns the first slot in the inventory containing an ItemStack with
        the given stack. This will only match a slot if both the type and the
        amount of the stack match

        Arguments
        - item: The ItemStack to match against

        Returns
        - The slot index of the given ItemStack or -1 if not found
        """
        ...


    def firstEmpty(self) -> int:
        """
        Returns the first empty Slot.

        Returns
        - The first empty Slot found, or -1 if no empty slots.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Check whether or not this inventory is empty. An inventory is considered
        to be empty if there are no ItemStacks in any slot of this inventory.

        Returns
        - True if empty, False otherwise
        """
        ...


    def remove(self, material: "Material") -> None:
        """
        Removes all stacks in the inventory matching the given material.

        Arguments
        - material: The material to remove

        Raises
        - IllegalArgumentException: if material is null
        """
        ...


    def remove(self, item: "ItemStack") -> None:
        """
        Removes all stacks in the inventory matching the given stack.
        
        This will only match a slot if both the type and the amount of the
        stack match

        Arguments
        - item: The ItemStack to match against
        """
        ...


    def clear(self, index: int) -> None:
        """
        Clears out a particular slot in the index.

        Arguments
        - index: The index to empty.
        """
        ...


    def clear(self) -> None:
        """
        Clears out the whole Inventory.
        """
        ...


    def getViewers(self) -> list["HumanEntity"]:
        """
        Gets a list of players viewing the inventory. Note that a player is
        considered to be viewing their own inventory and internal crafting
        screen even when said inventory is not open. They will normally be
        considered to be viewing their inventory even when they have a
        different inventory screen open, but it's possible for customized
        inventory screens to exclude the viewer's inventory, so this should
        never be assumed to be non-empty.

        Returns
        - A list of HumanEntities who are viewing this Inventory.
        """
        ...


    def getType(self) -> "InventoryType":
        """
        Returns what type of inventory this is.

        Returns
        - The InventoryType representing the type of inventory.
        """
        ...


    def getHolder(self) -> "InventoryHolder":
        """
        Gets the block or entity belonging to the open inventory

        Returns
        - The holder of the inventory; null if it has no holder.
        """
        ...


    def iterator(self) -> "ListIterator"["ItemStack"]:
        ...


    def iterator(self, index: int) -> "ListIterator"["ItemStack"]:
        """
        Returns an iterator starting at the given index. If the index is
        positive, then the first call to next() will return the item at that
        index; if it is negative, the first call to previous will return the
        item at index (getSize() + index).

        Arguments
        - index: The index.

        Returns
        - An iterator.
        """
        ...


    def getLocation(self) -> "Location":
        """
        Get the location of the block or entity which corresponds to this inventory. May return null if this container
        was custom created or is a virtual / subcontainer.

        Returns
        - location or null if not applicable.
        """
        ...
