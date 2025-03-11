"""
Python module generated from Java source file org.bukkit.inventory.ItemFactory

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import Material
from org.bukkit import Server
from org.bukkit import World
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import Entity
from org.bukkit.entity import EntityType
from org.bukkit.inventory import *
from org.bukkit.inventory.meta import BookMeta
from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.inventory.meta import SkullMeta
from typing import Any, Callable, Iterable, Tuple


class ItemFactory:
    """
    An instance of the ItemFactory can be obtained with Server.getItemFactory().
    
    The ItemFactory is solely responsible for creating item meta containers to
    apply on item stacks.
    """

    def getItemMeta(self, material: "Material") -> "ItemMeta":
        """
        This creates a new item meta for the material.

        Arguments
        - material: The material to consider as base for the meta

        Returns
        - a new ItemMeta that could be applied to an item stack of the
            specified material
        """
        ...


    def isApplicable(self, meta: "ItemMeta", stack: "ItemStack") -> bool:
        """
        This method checks the item meta to confirm that it is applicable (no
        data lost if applied) to the specified ItemStack.
        
        A SkullMeta would not be valid for a sword, but a normal ItemMeta from an enchanted dirt block would.

        Arguments
        - meta: Meta to check
        - stack: Item that meta will be applied to

        Returns
        - True if the meta can be applied without losing data, False
            otherwise

        Raises
        - IllegalArgumentException: if the meta was not created by this
            factory
        """
        ...


    def isApplicable(self, meta: "ItemMeta", material: "Material") -> bool:
        """
        This method checks the item meta to confirm that it is applicable (no
        data lost if applied) to the specified Material.
        
        A SkullMeta would not be valid for a sword, but a normal ItemMeta from an enchanted dirt block would.

        Arguments
        - meta: Meta to check
        - material: Material that meta will be applied to

        Returns
        - True if the meta can be applied without losing data, False
            otherwise

        Raises
        - IllegalArgumentException: if the meta was not created by this
            factory
        """
        ...


    def equals(self, meta1: "ItemMeta", meta2: "ItemMeta") -> bool:
        """
        This method is used to compare two item meta data objects.

        Arguments
        - meta1: First meta to compare, and may be null to indicate no data
        - meta2: Second meta to compare, and may be null to indicate no
            data

        Returns
        - False if one of the meta has data the other does not, otherwise
            True

        Raises
        - IllegalArgumentException: if either meta was not created by this
            factory
        """
        ...


    def asMetaFor(self, meta: "ItemMeta", stack: "ItemStack") -> "ItemMeta":
        """
        Returns an appropriate item meta for the specified stack.
        
        The item meta returned will always be a valid meta for a given
        ItemStack of the specified material. It may be a more or less specific
        meta, and could also be the same meta or meta type as the parameter.
        The item meta returned will also always be the most appropriate meta.
        
        Example, if a SkullMeta is being applied to a book, this method
        would return a BookMeta containing all information in the
        specified meta that is applicable to an ItemMeta, the highest
        common interface.

        Arguments
        - meta: the meta to convert
        - stack: the stack to convert the meta for

        Returns
        - An appropriate item meta for the specified item stack. No
            guarantees are made as to if a copy is returned. This will be null
            for a stack of air.

        Raises
        - IllegalArgumentException: if the specified meta was not created
            by this factory
        """
        ...


    def asMetaFor(self, meta: "ItemMeta", material: "Material") -> "ItemMeta":
        """
        Returns an appropriate item meta for the specified material.
        
        The item meta returned will always be a valid meta for a given
        ItemStack of the specified material. It may be a more or less specific
        meta, and could also be the same meta or meta type as the parameter.
        The item meta returned will also always be the most appropriate meta.
        
        Example, if a SkullMeta is being applied to a book, this method
        would return a BookMeta containing all information in the
        specified meta that is applicable to an ItemMeta, the highest
        common interface.

        Arguments
        - meta: the meta to convert
        - material: the material to convert the meta for

        Returns
        - An appropriate item meta for the specified item material. No
            guarantees are made as to if a copy is returned. This will be null for air.

        Raises
        - IllegalArgumentException: if the specified meta was not created
            by this factory
        """
        ...


    def getDefaultLeatherColor(self) -> "Color":
        """
        Returns the default color for all leather armor.

        Returns
        - the default color for leather armor
        """
        ...


    def createItemStack(self, input: str) -> "ItemStack":
        """
        Create a new ItemStack given the supplied input.
        
        The input should match the same input as expected by Minecraft's `/give`
        command. For example,
        ```"minecraft:diamond_sword[minecraft:enchantments={levels:{"minecraft:sharpness": 3}}]"```
        would yield an ItemStack of Material.DIAMOND_SWORD with an ItemMeta
        containing a level 3 Enchantment.SHARPNESS enchantment.

        Arguments
        - input: the item input string

        Returns
        - the created ItemStack

        Raises
        - IllegalArgumentException: if the input string was provided in an
        invalid or unsupported format
        """
        ...


    def getSpawnEgg(self, type: "EntityType") -> "Material":
        """
        Gets a Material representing the spawn egg for the provided
        EntityType. 
        Will return null for EntityTypes that do not have a corresponding spawn egg.

        Arguments
        - type: the entity type

        Returns
        - the Material of this EntityTypes spawn egg or null
        """
        ...


    def enchantItem(self, entity: "Entity", item: "ItemStack", level: int, allowTreasures: bool) -> "ItemStack":
        """
        Enchants the given item at the provided level.
        
        If an item that is air is passed through an error is thrown.

        Arguments
        - entity: the entity to use as a source of randomness
        - item: the item to enchant
        - level: the level to use, which is the level in the enchantment table
        - allowTreasures: allows treasure enchants, e.g. mending, if True.

        Returns
        - a new ItemStack containing the result of the Enchantment
        """
        ...


    def enchantItem(self, world: "World", item: "ItemStack", level: int, allowTreasures: bool) -> "ItemStack":
        """
        Enchants the given item at the provided level.
        
        If an item that is air is passed through an error is thrown.

        Arguments
        - world: the world to use as a source of randomness
        - item: the item to enchant
        - level: the level to use, which is the level in the enchantment table
        - allowTreasures: allow the treasure enchants, e.g. mending, if True.

        Returns
        - a new ItemStack containing the result of the Enchantment
        """
        ...


    def enchantItem(self, item: "ItemStack", level: int, allowTreasures: bool) -> "ItemStack":
        """
        Enchants the given item at the provided level.
        
        If an item that is air is passed through an error is thrown.

        Arguments
        - item: the item to enchant
        - level: the level to use, which is the level in the enchantment table
        - allowTreasures: allow treasure enchantments, e.g. mending, if True.

        Returns
        - a new ItemStack containing the result of the Enchantment
        """
        ...
