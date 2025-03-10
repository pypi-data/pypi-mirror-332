"""
Python module generated from Java source file org.bukkit.event.inventory.DragType

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.event.inventory import *
from typing import Any, Callable, Iterable, Tuple


class DragType(Enum):
    """
    Represents the effect of a drag that will be applied to an Inventory in an
    InventoryDragEvent.
    """

    SINGLE = 0
    """
    One item from the cursor is placed in each selected slot.
    """
    EVEN = 1
    """
    The cursor is split evenly across all selected slots, not to exceed the
    Material's max stack size, with the remainder going to the cursor.
    """
