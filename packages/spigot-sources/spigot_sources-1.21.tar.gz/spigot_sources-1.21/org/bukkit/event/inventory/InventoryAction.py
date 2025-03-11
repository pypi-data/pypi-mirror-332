"""
Python module generated from Java source file org.bukkit.event.inventory.InventoryAction

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event.inventory import *
from typing import Any, Callable, Iterable, Tuple


class InventoryAction(Enum):
    """
    An estimation of what the result will be.
    """

    NOTHING = 0
    """
    Nothing will happen from the click.
    
    There may be cases where nothing will happen and this is value is not
    provided, but it is guaranteed that this value is accurate when given.
    """
    PICKUP_ALL = 1
    """
    All of the items on the clicked slot are moved to the cursor.
    """
    PICKUP_SOME = 2
    """
    Some of the items on the clicked slot are moved to the cursor.
    """
    PICKUP_HALF = 3
    """
    Half of the items on the clicked slot are moved to the cursor.
    """
    PICKUP_ONE = 4
    """
    One of the items on the clicked slot are moved to the cursor.
    """
    PLACE_ALL = 5
    """
    All of the items on the cursor are moved to the clicked slot.
    """
    PLACE_SOME = 6
    """
    Some of the items from the cursor are moved to the clicked slot
    (usually up to the max stack size).
    """
    PLACE_ONE = 7
    """
    A single item from the cursor is moved to the clicked slot.
    """
    SWAP_WITH_CURSOR = 8
    """
    The clicked item and the cursor are exchanged.
    """
    DROP_ALL_CURSOR = 9
    """
    The entire cursor item is dropped.
    """
    DROP_ONE_CURSOR = 10
    """
    One item is dropped from the cursor.
    """
    DROP_ALL_SLOT = 11
    """
    The entire clicked slot is dropped.
    """
    DROP_ONE_SLOT = 12
    """
    One item is dropped from the clicked slot.
    """
    MOVE_TO_OTHER_INVENTORY = 13
    """
    The item is moved to the opposite inventory if a space is found.
    """
    HOTBAR_MOVE_AND_READD = 14
    """
    The clicked item is moved to the hotbar, and the item currently there
    is re-added to the player's inventory.
    
    The hotbar includes the player's off hand.
    """
    HOTBAR_SWAP = 15
    """
    The clicked slot and the picked hotbar slot are swapped.
    
    The hotbar includes the player's off hand.
    """
    CLONE_STACK = 16
    """
    A max-size stack of the clicked item is put on the cursor.
    """
    COLLECT_TO_CURSOR = 17
    """
    The inventory is searched for the same material, and they are put on
    the cursor up to org.bukkit.Material.getMaxStackSize().
    """
    UNKNOWN = 18
    """
    An unrecognized ClickType.
    """
