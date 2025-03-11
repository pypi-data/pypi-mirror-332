"""
Python module generated from Java source file org.bukkit.inventory.MenuType

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import *
from org.bukkit.inventory.view import AnvilView
from org.bukkit.inventory.view import BeaconView
from org.bukkit.inventory.view import BrewingStandView
from org.bukkit.inventory.view import CrafterView
from org.bukkit.inventory.view import EnchantmentView
from org.bukkit.inventory.view import FurnaceView
from org.bukkit.inventory.view import LecternView
from org.bukkit.inventory.view import LoomView
from org.bukkit.inventory.view import MerchantView
from org.bukkit.inventory.view import StonecutterView
from typing import Any, Callable, Iterable, Tuple


class MenuType(Keyed):
    """
    Represents different kinds of views, also known as menus, which can be
    created and viewed by the player.
    """

    GENERIC_9X1 = get("generic_9x1")
    """
    A MenuType which represents a chest with 1 row.
    """
    GENERIC_9X2 = get("generic_9x2")
    """
    A MenuType which represents a chest with 2 rows.
    """
    GENERIC_9X3 = get("generic_9x3")
    """
    A MenuType which represents a chest with 3 rows.
    """
    GENERIC_9X4 = get("generic_9x4")
    """
    A MenuType which represents a chest with 4 rows.
    """
    GENERIC_9X5 = get("generic_9x5")
    """
    A MenuType which represents a chest with 5 rows.
    """
    GENERIC_9X6 = get("generic_9x6")
    """
    A MenuType which represents a chest with 6 rows.
    """
    GENERIC_3X3 = get("generic_3x3")
    """
    A MenuType which represents a dispenser/dropper like menu with 3 columns
    and 3 rows.
    """
    CRAFTER_3X3 = get("crafter_3x3")
    """
    A MenuType which represents a crafter
    """
    ANVIL = get("anvil")
    """
    A MenuType which represents an anvil.
    """
    BEACON = get("beacon")
    """
    A MenuType which represents a beacon.
    """
    BLAST_FURNACE = get("blast_furnace")
    """
    A MenuType which represents a blast furnace.
    """
    BREWING_STAND = get("brewing_stand")
    """
    A MenuType which represents a brewing stand.
    """
    CRAFTING = get("crafting")
    """
    A MenuType which represents a crafting table.
    """
    ENCHANTMENT = get("enchantment")
    """
    A MenuType which represents an enchantment table.
    """
    FURNACE = get("furnace")
    """
    A MenuType which represents a furnace.
    """
    GRINDSTONE = get("grindstone")
    """
    A MenuType which represents a grindstone.
    """
    HOPPER = get("hopper")
    """
    A MenuType which represents a hopper.
    """
    LECTERN = get("lectern")
    """
    A MenuType which represents a lectern, a book like view.
    """
    LOOM = get("loom")
    """
    A MenuType which represents a loom.
    """
    MERCHANT = get("merchant")
    """
    A MenuType which represents a merchant.
    """
    SHULKER_BOX = get("shulker_box")
    """
    A MenuType which represents a shulker box.
    """
    SMITHING = get("smithing")
    """
    A MenuType which represents a stonecutter.
    """
    SMOKER = get("smoker")
    """
    A MenuType which represents a smoker.
    """
    CARTOGRAPHY_TABLE = get("cartography_table")
    """
    A MenuType which represents a cartography table.
    """
    STONECUTTER = get("stonecutter")
    """
    A MenuType which represents a stonecutter.
    """


    def typed(self) -> "MenuType.Typed"["InventoryView"]:
        """
        Yields this MenuType as a typed version of itself with a plain
        InventoryView representing it.

        Returns
        - the typed MenuType.
        """
        ...


    def typed(self, viewClass: type["V"]) -> "MenuType.Typed"["V"]:
        """
        Yields this MenuType as a typed version of itself with a specific
        InventoryView representing it.
        
        Type `<V>`: the generic type of the InventoryView to get this MenuType
        with

        Arguments
        - viewClass: the class type of the InventoryView to type this
        InventoryView with.

        Returns
        - the typed MenuType

        Raises
        - IllegalArgumentException: if the provided viewClass cannot be
        typed to this MenuType
        """
        ...


    def getInventoryViewClass(self) -> type["InventoryView"]:
        """
        Gets the InventoryView class of this MenuType.

        Returns
        - the InventoryView class of this MenuType
        """
        ...


    @staticmethod
    def get(key: str) -> "T":
        ...
