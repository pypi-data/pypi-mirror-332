"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryType

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event.inventory import *
from org.bukkit.inventory import InventoryHolder
from org.bukkit.inventory import MenuType
from typing import Any, Callable, Iterable, Tuple


class InventoryType(Enum):
    """
    Represents the different kinds of inventories available in Bukkit.
    
    Only InventoryTypes marked .isCreatable() can be created.
    
    The current list of inventories that cannot be created via
    org.bukkit.Bukkit.createInventory are:
    <blockquote>
        InventoryType.CREATIVE, InventoryType.CRAFTING and
        InventoryType.MERCHANT
    </blockquote>
    
    See org.bukkit.Bukkit.createInventory for more information.

    See
    - org.bukkit.Bukkit.createInventory(InventoryHolder, InventoryType)
    """

    CHEST = (27, "Chest", MenuType.GENERIC_9X3)
    """
    A chest inventory, with 0, 9, 18, 27, 36, 45, or 54 slots of type
    CONTAINER.
    """
    DISPENSER = (9, "Dispenser", MenuType.GENERIC_3X3)
    """
    A dispenser inventory, with 9 slots of type CONTAINER.
    """
    DROPPER = (9, "Dropper", MenuType.GENERIC_3X3)
    """
    A dropper inventory, with 9 slots of type CONTAINER.
    """
    FURNACE = (3, "Furnace", MenuType.FURNACE)
    """
    A furnace inventory, with a RESULT slot, a CRAFTING slot, and a FUEL
    slot.
    """
    WORKBENCH = (10, "Crafting", MenuType.CRAFTING)
    """
    A workbench inventory, with 9 CRAFTING slots and a RESULT slot.
    """
    CRAFTING = (5, "Crafting", None, False)
    """
    A player's crafting inventory, with 4 CRAFTING slots and a RESULT slot.
    Also implies that the 4 ARMOR slots are accessible.
    """
    ENCHANTING = (2, "Enchanting", MenuType.ENCHANTMENT)
    """
    An enchantment table inventory, with two CRAFTING slots and three
    enchanting buttons.
    """
    BREWING = (5, "Brewing", MenuType.BREWING_STAND)
    """
    A brewing stand inventory, with one FUEL slot and four CRAFTING slots.
    """
    PLAYER = (41, "Player", MenuType.GENERIC_9X4)
    """
    A player's inventory, with 9 QUICKBAR slots, 27 CONTAINER slots, 4 ARMOR
    slots and 1 offhand slot. The ARMOR and offhand slots may not be visible
    to the player, though.
    """
    CREATIVE = (9, "Creative", None, False)
    """
    The creative mode inventory, with only 9 QUICKBAR slots and nothing
    else. (The actual creative interface with the items is client-side and
    cannot be altered by the server.)
    """
    MERCHANT = (3, "Villager", MenuType.MERCHANT, False)
    """
    The merchant inventory, with 2 CRAFTING slots, and 1 RESULT slot.
    """
    ENDER_CHEST = (27, "Ender Chest", MenuType.GENERIC_9X3)
    """
    The ender chest inventory, with 27 slots.
    """
    ANVIL = (3, "Repairing", MenuType.ANVIL)
    """
    An anvil inventory, with 2 CRAFTING slots and 1 RESULT slot
    """
    SMITHING = (4, "Upgrade Gear", MenuType.SMITHING)
    """
    A smithing inventory, with 3 CRAFTING slots and 1 RESULT slot.
    """
    BEACON = (1, "container.beacon", MenuType.BEACON)
    """
    A beacon inventory, with 1 CRAFTING slot
    """
    HOPPER = (5, "Item Hopper", MenuType.HOPPER)
    """
    A hopper inventory, with 5 slots of type CONTAINER.
    """
    SHULKER_BOX = (27, "Shulker Box", MenuType.SHULKER_BOX)
    """
    A shulker box inventory, with 27 slots of type CONTAINER.
    """
    BARREL = (27, "Barrel", MenuType.GENERIC_9X3)
    """
    A barrel box inventory, with 27 slots of type CONTAINER.
    """
    BLAST_FURNACE = (3, "Blast Furnace", MenuType.BLAST_FURNACE)
    """
    A blast furnace inventory, with a RESULT slot, a CRAFTING slot, and a
    FUEL slot.
    """
    LECTERN = (1, "Lectern", MenuType.LECTERN)
    """
    A lectern inventory, with 1 BOOK slot.
    """
    SMOKER = (3, "Smoker", MenuType.SMOKER)
    """
    A smoker inventory, with a RESULT slot, a CRAFTING slot, and a FUEL slot.
    """
    LOOM = (4, "Loom", MenuType.LOOM)
    """
    Loom inventory, with 3 CRAFTING slots, and 1 RESULT slot.
    """
    CARTOGRAPHY = (3, "Cartography Table", MenuType.CARTOGRAPHY_TABLE)
    """
    Cartography inventory with 2 CRAFTING slots, and 1 RESULT slot.
    """
    GRINDSTONE = (3, "Repair & Disenchant", MenuType.GRINDSTONE)
    """
    Grindstone inventory with 2 CRAFTING slots, and 1 RESULT slot.
    """
    STONECUTTER = (2, "Stonecutter", MenuType.STONECUTTER)
    """
    Stonecutter inventory with 1 CRAFTING slot, and 1 RESULT slot.
    """
    COMPOSTER = (1, "Composter", None, False)
    """
    Pseudo composter inventory with 0 or 1 slots of undefined type.
    """
    CHISELED_BOOKSHELF = (6, "Chiseled Bookshelf", None, False)
    """
    Pseudo chiseled bookshelf inventory, with 6 slots of undefined type.
    """
    JUKEBOX = (1, "Jukebox", None, False)
    """
    Pseudo jukebox inventory with 1 slot of undefined type.
    """
    CRAFTER = (9, "Crafter", MenuType.CRAFTER_3X3)
    """
    A crafter inventory, with 9 CRAFTING slots.
    """
    SMITHING_NEW = (4, "Upgrade Gear", MenuType.SMITHING)
    """
    The new smithing inventory, with 3 CRAFTING slots and 1 RESULT slot.

    Deprecated
    - use .SMITHING
    """


    def getDefaultSize(self) -> int:
        ...


    def getDefaultTitle(self) -> str:
        ...


    def getMenuType(self) -> "MenuType":
        """
        Gets the corresponding MenuType of this InventoryType.
        
        Not all InventoryType correspond to a MenuType. These
        InventoryTypes are also not creatable. If this method returns null,
        .isCreatable() will return False, with the exception of
        .MERCHANT.
        
        As well as not necessarily corresponding to a MenuType some
        InventoryType correspond to the same MenuType, including:
        
        - Dropper, Dispenser
        - ShulkerBox, Barrel, Chest

        Returns
        - the corresponding MenuType
        """
        ...


    def isCreatable(self) -> bool:
        """
        Denotes that this InventoryType can be created via the normal
        org.bukkit.Bukkit.createInventory methods.

        Returns
        - if this InventoryType can be created and shown to a player
        """
        ...


    class SlotType(Enum):

        RESULT = 0
        """
        A result slot in a furnace or crafting inventory.
        """
        CRAFTING = 1
        """
        A slot in the crafting matrix, or an 'input' slot.
        """
        ARMOR = 2
        """
        An armour slot in the player's inventory.
        """
        CONTAINER = 3
        """
        A regular slot in the container or the player's inventory; anything
        not covered by the other enum values.
        """
        QUICKBAR = 4
        """
        A slot in the bottom row or quickbar.
        """
        OUTSIDE = 5
        """
        A pseudo-slot representing the area outside the inventory window.
        """
        FUEL = 6
        """
        The fuel slot in a furnace inventory, or the ingredient slot in a
        brewing stand inventory.
        """
