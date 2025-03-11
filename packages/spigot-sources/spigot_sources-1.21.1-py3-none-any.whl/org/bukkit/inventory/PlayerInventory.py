"""
Python module generated from Java source file org.bukkit.inventory.PlayerInventory

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class PlayerInventory(Inventory):
    """
    Interface to the inventory of a Player, including the four armor slots and any extra slots.
    """

    def getArmorContents(self) -> list["ItemStack"]:
        """
        Gets all ItemStacks from the armor slots.

        Returns
        - all the ItemStacks from the armor slots. Individual items can be
        null and are returned in a fixed order starting from the boots and going
        up to the helmet
        """
        ...


    def getExtraContents(self) -> list["ItemStack"]:
        """
        Get all additional ItemStacks stored in this inventory.
        
        NB: What defines an extra slot is up to the implementation, however it
        will not be contained within .getStorageContents() or
        .getArmorContents()

        Returns
        - All additional ItemStacks. Individual items can be null.
        """
        ...


    def getHelmet(self) -> "ItemStack":
        """
        Return the ItemStack from the helmet slot

        Returns
        - The ItemStack in the helmet slot
        """
        ...


    def getChestplate(self) -> "ItemStack":
        """
        Return the ItemStack from the chestplate slot

        Returns
        - The ItemStack in the chestplate slot
        """
        ...


    def getLeggings(self) -> "ItemStack":
        """
        Return the ItemStack from the leg slot

        Returns
        - The ItemStack in the leg slot
        """
        ...


    def getBoots(self) -> "ItemStack":
        """
        Return the ItemStack from the boots slot

        Returns
        - The ItemStack in the boots slot
        """
        ...


    def setItem(self, index: int, item: "ItemStack") -> None:
        """
        Stores the ItemStack at the given index of the inventory.
        
        Indexes 0 through 8 refer to the hotbar. 9 through 35 refer to the main inventory, counting up from 9 at the top
        left corner of the inventory, moving to the right, and moving to the row below it back on the left side when it
        reaches the end of the row. It follows the same path in the inventory like you would read a book.
        
        Indexes 36 through 39 refer to the armor slots. Though you can set armor with this method using these indexes,
        you are encouraged to use the provided methods for those slots.
        
        Index 40 refers to the off hand (shield) item slot. Though you can set off hand with this method using this index,
        you are encouraged to use the provided method for this slot.
        
        If you attempt to use this method with an index less than 0 or greater than 40, an ArrayIndexOutOfBounds
        exception will be thrown.

        Arguments
        - index: The index where to put the ItemStack
        - item: The ItemStack to set

        Raises
        - ArrayIndexOutOfBoundsException: when index &lt; 0 || index &gt; 40

        See
        - .setItemInOffHand(ItemStack)
        """
        ...


    def setItem(self, slot: "EquipmentSlot", item: "ItemStack") -> None:
        """
        Stores the ItemStack at the given equipment slot in the inventory.

        Arguments
        - slot: the slot to put the ItemStack
        - item: the ItemStack to set

        See
        - .setItem(int, ItemStack)
        """
        ...


    def getItem(self, slot: "EquipmentSlot") -> "ItemStack":
        """
        Gets the ItemStack at the given equipment slot in the inventory.

        Arguments
        - slot: the slot to get the ItemStack

        Returns
        - the ItemStack in the given slot or null if there is not one
        """
        ...


    def setArmorContents(self, items: list["ItemStack"]) -> None:
        """
        Put the given ItemStacks into the armor slots

        Arguments
        - items: The ItemStacks to use as armour
        """
        ...


    def setExtraContents(self, items: list["ItemStack"]) -> None:
        """
        Put the given ItemStacks into the extra slots
        
        See .getExtraContents() for an explanation of extra slots.

        Arguments
        - items: The ItemStacks to use as extra
        """
        ...


    def setHelmet(self, helmet: "ItemStack") -> None:
        """
        Put the given ItemStack into the helmet slot. This does not check if
        the ItemStack is a helmet

        Arguments
        - helmet: The ItemStack to use as helmet
        """
        ...


    def setChestplate(self, chestplate: "ItemStack") -> None:
        """
        Put the given ItemStack into the chestplate slot. This does not check
        if the ItemStack is a chestplate

        Arguments
        - chestplate: The ItemStack to use as chestplate
        """
        ...


    def setLeggings(self, leggings: "ItemStack") -> None:
        """
        Put the given ItemStack into the leg slot. This does not check if the
        ItemStack is a pair of leggings

        Arguments
        - leggings: The ItemStack to use as leggings
        """
        ...


    def setBoots(self, boots: "ItemStack") -> None:
        """
        Put the given ItemStack into the boots slot. This does not check if the
        ItemStack is a boots

        Arguments
        - boots: The ItemStack to use as boots
        """
        ...


    def getItemInMainHand(self) -> "ItemStack":
        """
        Gets a copy of the item the player is currently holding
        in their main hand.

        Returns
        - the currently held item
        """
        ...


    def setItemInMainHand(self, item: "ItemStack") -> None:
        """
        Sets the item the player is holding in their main hand.

        Arguments
        - item: The item to put into the player's hand
        """
        ...


    def getItemInOffHand(self) -> "ItemStack":
        """
        Gets a copy of the item the player is currently holding
        in their off hand.

        Returns
        - the currently held item
        """
        ...


    def setItemInOffHand(self, item: "ItemStack") -> None:
        """
        Sets the item the player is holding in their off hand.

        Arguments
        - item: The item to put into the player's hand
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Gets a copy of the item the player is currently holding

        Returns
        - the currently held item

        See
        - .getItemInOffHand()

        Deprecated
        - players can duel wield now use the methods for the
             specific hand instead
        """
        ...


    def setItemInHand(self, stack: "ItemStack") -> None:
        """
        Sets the item the player is holding

        Arguments
        - stack: The item to put into the player's hand

        See
        - .setItemInOffHand(ItemStack)

        Deprecated
        - players can duel wield now use the methods for the
             specific hand instead
        """
        ...


    def getHeldItemSlot(self) -> int:
        """
        Get the slot number of the currently held item

        Returns
        - Held item slot number
        """
        ...


    def setHeldItemSlot(self, slot: int) -> None:
        """
        Set the slot number of the currently held item.
        
        This validates whether the slot is between 0 and 8 inclusive.

        Arguments
        - slot: The new slot number

        Raises
        - IllegalArgumentException: Thrown if slot is not between 0 and 8
            inclusive
        """
        ...


    def getHolder(self) -> "HumanEntity":
        ...
