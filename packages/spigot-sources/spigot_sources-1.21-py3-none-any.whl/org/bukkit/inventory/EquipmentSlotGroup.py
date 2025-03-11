"""
Python module generated from Java source file org.bukkit.inventory.EquipmentSlotGroup

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Locale
from java.util.function import Predicate
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class EquipmentSlotGroup(Predicate):
    """
    Represents a group of EquipmentSlot.
    """

    ANY = get("any", (test) -> true, EquipmentSlot.HAND)
    MAINHAND = get("mainhand", EquipmentSlot.HAND)
    OFFHAND = get("offhand", EquipmentSlot.OFF_HAND)
    HAND = get("hand", (test) -> test == EquipmentSlot.HAND || test == EquipmentSlot.OFF_HAND, EquipmentSlot.HAND)
    FEET = get("feet", EquipmentSlot.FEET)
    LEGS = get("legs", EquipmentSlot.LEGS)
    CHEST = get("chest", EquipmentSlot.CHEST)
    HEAD = get("head", EquipmentSlot.HEAD)
    ARMOR = get("armor", (test) -> test == EquipmentSlot.FEET || test == EquipmentSlot.LEGS || test == EquipmentSlot.CHEST || test == EquipmentSlot.HEAD, EquipmentSlot.CHEST)


    def test(self, test: "EquipmentSlot") -> bool:
        ...


    def toString(self) -> str:
        ...


    def getExample(self) -> "EquipmentSlot":
        """
        Gets an EquipmentSlot which is an example of a slot in this
        group.

        Returns
        - an example slot

        Deprecated
        - for internal compatibility use only
        """
        ...


    @staticmethod
    def getByName(name: str) -> "EquipmentSlotGroup":
        """
        Gets the EquipmentSlotGroup corresponding to the given string.

        Arguments
        - name: group name

        Returns
        - associated group or null
        """
        ...
