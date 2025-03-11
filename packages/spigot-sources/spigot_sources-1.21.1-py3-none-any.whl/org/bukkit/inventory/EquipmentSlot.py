"""
Python module generated from Java source file org.bukkit.inventory.EquipmentSlot

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util.function import Supplier
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class EquipmentSlot(Enum):

    HAND = (() -> EquipmentSlotGroup.MAINHAND)
    OFF_HAND = (() -> EquipmentSlotGroup.OFFHAND)
    FEET = (() -> EquipmentSlotGroup.FEET)
    LEGS = (() -> EquipmentSlotGroup.LEGS)
    CHEST = (() -> EquipmentSlotGroup.CHEST)
    HEAD = (() -> EquipmentSlotGroup.HEAD)
    BODY = (() -> EquipmentSlotGroup.ARMOR)
    """
    Only for certain entities such as horses and wolves.
    """


    def getGroup(self) -> "EquipmentSlotGroup":
        """
        Gets the EquipmentSlotGroup corresponding to this slot.

        Returns
        - corresponding EquipmentSlotGroup
        """
        ...
