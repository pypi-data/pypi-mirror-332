"""
Python module generated from Java source file org.bukkit.event.world.LootGenerateEvent

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import World
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityDeathEvent
from org.bukkit.event.world import *
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import ItemStack
from org.bukkit.loot import LootContext
from org.bukkit.loot import LootTable
from typing import Any, Callable, Iterable, Tuple


class LootGenerateEvent(WorldEvent, Cancellable):
    """
    Called when a LootTable is generated in the world for an
    InventoryHolder.
    
    This event is NOT currently called when an entity's loot table has been
    generated (use EntityDeathEvent.getDrops(), but WILL be called by
    plugins invoking
    LootTable.fillInventory(org.bukkit.inventory.Inventory, java.util.Random, LootContext).
    """

    def __init__(self, world: "World", entity: "Entity", inventoryHolder: "InventoryHolder", lootTable: "LootTable", lootContext: "LootContext", items: list["ItemStack"], plugin: bool):
        ...


    def getEntity(self) -> "Entity":
        """
        Get the entity used as context for loot generation (if applicable).
        
        For inventories where entities are not required to generate loot, such as
        hoppers, null will be returned.
        
        This is a convenience method for
        `getLootContext().getLootedEntity()`.

        Returns
        - the entity
        """
        ...


    def getInventoryHolder(self) -> "InventoryHolder":
        """
        Get the inventory holder in which the loot was generated.
        
        If the loot was generated as a result of the block being broken, the
        inventory holder will be null as this event is called post block break.

        Returns
        - the inventory holder
        """
        ...


    def getLootTable(self) -> "LootTable":
        """
        Get the loot table used to generate loot.

        Returns
        - the loot table
        """
        ...


    def getLootContext(self) -> "LootContext":
        """
        Get the loot context used to provide context to the loot table's loot
        generation.

        Returns
        - the loot context
        """
        ...


    def setLoot(self, loot: Iterable["ItemStack"]) -> None:
        """
        Set the loot to be generated. Null items will be treated as air.
        
        Note: the set collection is not the one which will be returned by
        .getLoot().

        Arguments
        - loot: the loot to generate, null to clear all loot
        """
        ...


    def getLoot(self) -> list["ItemStack"]:
        """
        Get a mutable list of all loot to be generated.
        
        Any items added or removed from the returned list will be reflected in
        the loot generation. Null items will be treated as air.

        Returns
        - the loot to generate
        """
        ...


    def isPlugin(self) -> bool:
        """
        Check whether or not this event was called as a result of a plugin
        invoking
        LootTable.fillInventory(org.bukkit.inventory.Inventory, java.util.Random, LootContext).

        Returns
        - True if plugin caused, False otherwise
        """
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def isCancelled(self) -> bool:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
