"""
Python module generated from Java source file org.bukkit.inventory.ItemStack

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableMap
from java.util import Locale
from org.bukkit import Bukkit
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit import Utility
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.enchantments import Enchantment
from org.bukkit.inventory import *
from org.bukkit.inventory.meta import Damageable
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class ItemStack(Cloneable, ConfigurationSerializable, Translatable):
    """
    Represents a stack of items.
    
    **IMPORTANT: An *Item*Stack is only designed to contain *items*. Do not
    use this class to encapsulate Materials for which Material.isItem()
    returns False.**
    """

    def __init__(self, type: "Material"):
        """
        Defaults stack size to 1, with no extra data.
        
        **IMPORTANT: An *Item*Stack is only designed to contain
        *items*. Do not use this class to encapsulate Materials for which
        Material.isItem() returns False.**

        Arguments
        - type: item material
        """
        ...


    def __init__(self, type: "Material", amount: int):
        """
        An item stack with no extra data.
        
        **IMPORTANT: An *Item*Stack is only designed to contain
        *items*. Do not use this class to encapsulate Materials for which
        Material.isItem() returns False.**

        Arguments
        - type: item material
        - amount: stack size
        """
        ...


    def __init__(self, type: "Material", amount: int, damage: int):
        """
        An item stack with the specified damage / durability

        Arguments
        - type: item material
        - amount: stack size
        - damage: durability / damage

        Deprecated
        - see .setDurability(short)
        """
        ...


    def __init__(self, type: "Material", amount: int, damage: int, data: "Byte"):
        """
        Arguments
        - type: the type
        - amount: the amount in the stack
        - damage: the damage value of the item
        - data: the data value or null

        Deprecated
        - this method uses an ambiguous data byte object
        """
        ...


    def __init__(self, stack: "ItemStack"):
        """
        Creates a new item stack derived from the specified stack

        Arguments
        - stack: the stack to copy

        Raises
        - IllegalArgumentException: if the specified stack is null or
            returns an item meta not created by the item factory
        """
        ...


    def getType(self) -> "Material":
        """
        Gets the type of this item

        Returns
        - Type of the items in this stack
        """
        ...


    def setType(self, type: "Material") -> None:
        """
        Sets the type of this item
        
        Note that in doing so you will reset the MaterialData for this stack.
        
        **IMPORTANT: An *Item*Stack is only designed to contain
        *items*. Do not use this class to encapsulate Materials for which
        Material.isItem() returns False.**

        Arguments
        - type: New type to set the items in this stack to
        """
        ...


    def getAmount(self) -> int:
        """
        Gets the amount of items in this stack

        Returns
        - Amount of items in this stack
        """
        ...


    def setAmount(self, amount: int) -> None:
        """
        Sets the amount of items in this stack

        Arguments
        - amount: New amount of items in this stack
        """
        ...


    def getData(self) -> "MaterialData":
        """
        Gets the MaterialData for this stack of items

        Returns
        - MaterialData for this item
        """
        ...


    def setData(self, data: "MaterialData") -> None:
        """
        Sets the MaterialData for this stack of items

        Arguments
        - data: New MaterialData for this item
        """
        ...


    def setDurability(self, durability: int) -> None:
        """
        Sets the durability of this item

        Arguments
        - durability: Durability of this item

        Deprecated
        - durability is now part of ItemMeta. To avoid confusion and
        misuse, .getItemMeta(), .setItemMeta(ItemMeta) and
        Damageable.setDamage(int) should be used instead. This is because
        any call to this method will be overwritten by subsequent setting of
        ItemMeta which was created before this call.
        """
        ...


    def getDurability(self) -> int:
        """
        Gets the durability of this item

        Returns
        - Durability of this item

        Deprecated
        - see .setDurability(short)
        """
        ...


    def getMaxStackSize(self) -> int:
        """
        Get the maximum stack size for this item. If this item has a max stack
        size component (ItemMeta.hasMaxStackSize()), the value of that
        component will be returned. Otherwise, this item's Material's Material.getMaxStackSize() default maximum stack size will be returned
        instead.

        Returns
        - The maximum you can stack this item to.
        """
        ...


    def toString(self) -> str:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def isSimilar(self, stack: "ItemStack") -> bool:
        """
        This method is the same as equals, but does not consider stack size
        (amount).

        Arguments
        - stack: the item stack to compare to

        Returns
        - True if the two stacks are equal, ignoring the amount
        """
        ...


    def clone(self) -> "ItemStack":
        ...


    def hashCode(self) -> int:
        ...


    def containsEnchantment(self, ench: "Enchantment") -> bool:
        """
        Checks if this ItemStack contains the given Enchantment

        Arguments
        - ench: Enchantment to test

        Returns
        - True if this has the given enchantment
        """
        ...


    def getEnchantmentLevel(self, ench: "Enchantment") -> int:
        """
        Gets the level of the specified enchantment on this item stack

        Arguments
        - ench: Enchantment to check

        Returns
        - Level of the enchantment, or 0
        """
        ...


    def getEnchantments(self) -> dict["Enchantment", "Integer"]:
        """
        Gets a map containing all enchantments and their levels on this item.

        Returns
        - Map of enchantments.
        """
        ...


    def addEnchantments(self, enchantments: dict["Enchantment", "Integer"]) -> None:
        """
        Adds the specified enchantments to this item stack.
        
        This method is the same as calling .addEnchantment(org.bukkit.enchantments.Enchantment, int) for each
        element of the map.

        Arguments
        - enchantments: Enchantments to add

        Raises
        - IllegalArgumentException: if the specified enchantments is null
        - IllegalArgumentException: if any specific enchantment or level
            is null. **Warning**: Some enchantments may be added before this
            exception is thrown.
        """
        ...


    def addEnchantment(self, ench: "Enchantment", level: int) -> None:
        """
        Adds the specified Enchantment to this item stack.
        
        If this item stack already contained the given enchantment (at any
        level), it will be replaced.

        Arguments
        - ench: Enchantment to add
        - level: Level of the enchantment

        Raises
        - IllegalArgumentException: if enchantment null, or enchantment is
            not applicable
        """
        ...


    def addUnsafeEnchantments(self, enchantments: dict["Enchantment", "Integer"]) -> None:
        """
        Adds the specified enchantments to this item stack in an unsafe manner.
        
        This method is the same as calling .addUnsafeEnchantment(org.bukkit.enchantments.Enchantment, int) for
        each element of the map.

        Arguments
        - enchantments: Enchantments to add
        """
        ...


    def addUnsafeEnchantment(self, ench: "Enchantment", level: int) -> None:
        """
        Adds the specified Enchantment to this item stack.
        
        If this item stack already contained the given enchantment (at any
        level), it will be replaced.
        
        This method is unsafe and will ignore level restrictions or item type.
        Use at your own discretion.

        Arguments
        - ench: Enchantment to add
        - level: Level of the enchantment
        """
        ...


    def removeEnchantment(self, ench: "Enchantment") -> int:
        """
        Removes the specified Enchantment if it exists on this
        ItemStack

        Arguments
        - ench: Enchantment to remove

        Returns
        - Previous level, or 0
        """
        ...


    def removeEnchantments(self) -> None:
        """
        Removes all enchantments on this ItemStack.
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "ItemStack":
        """
        Required method for configuration serialization

        Arguments
        - args: map to deserialize

        Returns
        - deserialized item stack

        See
        - ConfigurationSerializable
        """
        ...


    def getItemMeta(self) -> "ItemMeta":
        """
        Get a copy of this ItemStack's ItemMeta.

        Returns
        - a copy of the current ItemStack's ItemData
        """
        ...


    def hasItemMeta(self) -> bool:
        """
        Checks to see if any meta data has been defined.

        Returns
        - Returns True if some meta data has been set for this item
        """
        ...


    def setItemMeta(self, itemMeta: "ItemMeta") -> bool:
        """
        Set the ItemMeta of this ItemStack.

        Arguments
        - itemMeta: new ItemMeta, or null to indicate meta data be cleared.

        Returns
        - True if successfully applied ItemMeta, see ItemFactory.isApplicable(ItemMeta, ItemStack)

        Raises
        - IllegalArgumentException: if the item meta was not created by
            the ItemFactory
        """
        ...


    def getTranslationKey(self) -> str:
        ...
