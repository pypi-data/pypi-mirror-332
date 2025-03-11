"""
Python module generated from Java source file org.bukkit.inventory.EntityEquipment

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.entity import Mob
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class EntityEquipment:
    """
    An interface to a creatures inventory
    """

    def setItem(self, slot: "EquipmentSlot", item: "ItemStack") -> None:
        """
        Stores the ItemStack at the given equipment slot in the inventory.

        Arguments
        - slot: the slot to put the ItemStack
        - item: the ItemStack to set
        """
        ...


    def setItem(self, slot: "EquipmentSlot", item: "ItemStack", silent: bool) -> None:
        """
        Stores the ItemStack at the given equipment slot in the inventory.

        Arguments
        - slot: the slot to put the ItemStack
        - item: the ItemStack to set
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getItem(self, slot: "EquipmentSlot") -> "ItemStack":
        """
        Gets the ItemStack at the given equipment slot in the inventory.

        Arguments
        - slot: the slot to get the ItemStack

        Returns
        - the ItemStack in the given slot
        """
        ...


    def getItemInMainHand(self) -> "ItemStack":
        """
        Gets a copy of the item the entity is currently holding
        in their main hand.

        Returns
        - the currently held item
        """
        ...


    def setItemInMainHand(self, item: "ItemStack") -> None:
        """
        Sets the item the entity is holding in their main hand.

        Arguments
        - item: The item to put into the entities hand
        """
        ...


    def setItemInMainHand(self, item: "ItemStack", silent: bool) -> None:
        """
        Sets the item the entity is holding in their main hand.

        Arguments
        - item: The item to put into the entities hand
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getItemInOffHand(self) -> "ItemStack":
        """
        Gets a copy of the item the entity is currently holding
        in their off hand.

        Returns
        - the currently held item
        """
        ...


    def setItemInOffHand(self, item: "ItemStack") -> None:
        """
        Sets the item the entity is holding in their off hand.

        Arguments
        - item: The item to put into the entities hand
        """
        ...


    def setItemInOffHand(self, item: "ItemStack", silent: bool) -> None:
        """
        Sets the item the entity is holding in their off hand.

        Arguments
        - item: The item to put into the entities hand
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getItemInHand(self) -> "ItemStack":
        """
        Gets a copy of the item the entity is currently holding

        Returns
        - the currently held item

        See
        - .getItemInOffHand()

        Deprecated
        - entities can duel wield now use the methods for the
             specific hand instead
        """
        ...


    def setItemInHand(self, stack: "ItemStack") -> None:
        """
        Sets the item the entity is holding

        Arguments
        - stack: The item to put into the entities hand

        See
        - .setItemInOffHand(ItemStack)

        Deprecated
        - entities can duel wield now use the methods for the
             specific hand instead
        """
        ...


    def getHelmet(self) -> "ItemStack":
        """
        Gets a copy of the helmet currently being worn by the entity

        Returns
        - The helmet being worn
        """
        ...


    def setHelmet(self, helmet: "ItemStack") -> None:
        """
        Sets the helmet worn by the entity

        Arguments
        - helmet: The helmet to put on the entity
        """
        ...


    def setHelmet(self, helmet: "ItemStack", silent: bool) -> None:
        """
        Sets the helmet worn by the entity

        Arguments
        - helmet: The helmet to put on the entity
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getChestplate(self) -> "ItemStack":
        """
        Gets a copy of the chest plate currently being worn by the entity

        Returns
        - The chest plate being worn
        """
        ...


    def setChestplate(self, chestplate: "ItemStack") -> None:
        """
        Sets the chest plate worn by the entity

        Arguments
        - chestplate: The chest plate to put on the entity
        """
        ...


    def setChestplate(self, chestplate: "ItemStack", silent: bool) -> None:
        """
        Sets the chest plate worn by the entity

        Arguments
        - chestplate: The chest plate to put on the entity
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getLeggings(self) -> "ItemStack":
        """
        Gets a copy of the leggings currently being worn by the entity

        Returns
        - The leggings being worn
        """
        ...


    def setLeggings(self, leggings: "ItemStack") -> None:
        """
        Sets the leggings worn by the entity

        Arguments
        - leggings: The leggings to put on the entity
        """
        ...


    def setLeggings(self, leggings: "ItemStack", silent: bool) -> None:
        """
        Sets the leggings worn by the entity

        Arguments
        - leggings: The leggings to put on the entity
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getBoots(self) -> "ItemStack":
        """
        Gets a copy of the boots currently being worn by the entity

        Returns
        - The boots being worn
        """
        ...


    def setBoots(self, boots: "ItemStack") -> None:
        """
        Sets the boots worn by the entity

        Arguments
        - boots: The boots to put on the entity
        """
        ...


    def setBoots(self, boots: "ItemStack", silent: bool) -> None:
        """
        Sets the boots worn by the entity

        Arguments
        - boots: The boots to put on the entity
        - silent: whether or not the equip sound should be silenced
        """
        ...


    def getArmorContents(self) -> list["ItemStack"]:
        """
        Gets all ItemStacks from the armor slots.

        Returns
        - all the ItemStacks from the armor slots. Individual items can be
        null and are returned in a fixed order starting from the boots and going
        up to the helmet
        """
        ...


    def setArmorContents(self, items: list["ItemStack"]) -> None:
        """
        Sets the entities armor to the provided array of ItemStacks

        Arguments
        - items: The items to set the armor as. Individual items may be null.
        """
        ...


    def clear(self) -> None:
        """
        Clears the entity of all armor and held items
        """
        ...


    def getItemInHandDropChance(self) -> float:
        """
        Returns
        - drop chance

        See
        - .getItemInOffHandDropChance()

        Deprecated
        - entities can duel wield now use the methods for the specific
        hand instead
        """
        ...


    def setItemInHandDropChance(self, chance: float) -> None:
        """
        Arguments
        - chance: drop chance

        See
        - .setItemInOffHandDropChance(float)

        Deprecated
        - entities can duel wield now use the methods for the specific
        hand instead
        """
        ...


    def getItemInMainHandDropChance(self) -> float:
        """
        Gets the chance of the main hand item being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - chance of the currently held item being dropped (1 for non-Mob)
        """
        ...


    def setItemInMainHandDropChance(self, chance: float) -> None:
        """
        Sets the chance of the item this creature is currently holding in their
        main hand being dropped upon this creature's death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: the chance of the main hand item being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getItemInOffHandDropChance(self) -> float:
        """
        Gets the chance of the off hand item being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - chance of the off hand item being dropped (1 for non-Mob)
        """
        ...


    def setItemInOffHandDropChance(self, chance: float) -> None:
        """
        Sets the chance of the off hand item being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: the chance of off hand item being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getHelmetDropChance(self) -> float:
        """
        Gets the chance of the helmet being dropped upon this creature's death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - the chance of the helmet being dropped (1 for non-Mob)
        """
        ...


    def setHelmetDropChance(self, chance: float) -> None:
        """
        Sets the chance of the helmet being dropped upon this creature's death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: of the helmet being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getChestplateDropChance(self) -> float:
        """
        Gets the chance of the chest plate being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - the chance of the chest plate being dropped (1 for non-Mob)
        """
        ...


    def setChestplateDropChance(self, chance: float) -> None:
        """
        Sets the chance of the chest plate being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: of the chest plate being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getLeggingsDropChance(self) -> float:
        """
        Gets the chance of the leggings being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - the chance of the leggings being dropped (1 for non-Mob)
        """
        ...


    def setLeggingsDropChance(self, chance: float) -> None:
        """
        Sets the chance of the leggings being dropped upon this creature's
        death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: chance of the leggings being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getBootsDropChance(self) -> float:
        """
        Gets the chance of the boots being dropped upon this creature's death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Returns
        - the chance of the boots being dropped (1 for non-Mob)
        """
        ...


    def setBootsDropChance(self, chance: float) -> None:
        """
        Sets the chance of the boots being dropped upon this creature's death.
        
        
        - A drop chance of 0.0F will never drop
        - A drop chance of 1.0F will always drop

        Arguments
        - chance: of the boots being dropped

        Raises
        - UnsupportedOperationException: when called on non-Mob
        """
        ...


    def getHolder(self) -> "Entity":
        """
        Get the entity this EntityEquipment belongs to

        Returns
        - the entity this EntityEquipment belongs to
        """
        ...
