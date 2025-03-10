"""
Python module generated from Java source file org.bukkit.block.data.type.ChiseledBookshelf

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class ChiseledBookshelf(Directional):
    """
    Interface to the 'slot_0_occupied', 'slow_1_occupied' ... 'slot_5_occupied'
    flags on a bookshelf which indicate which slots are occupied rendered on the
    outside.
    
    Block may have 0, 1... .getMaximumOccupiedSlots()-1 occupied slots.
    """

    def isSlotOccupied(self, slot: int) -> bool:
        """
        Checks if the following slot is occupied.

        Arguments
        - slot: to check

        Returns
        - if slot is occupied
        """
        ...


    def setSlotOccupied(self, slot: int, occupied: bool) -> None:
        """
        Sets whether the following slot is occupied.

        Arguments
        - slot: to set
        - occupied: book
        """
        ...


    def getOccupiedSlots(self) -> set["Integer"]:
        """
        Get the indexes of all the occupied slots present on this block.

        Returns
        - set of all occupied slots
        """
        ...


    def getMaximumOccupiedSlots(self) -> int:
        """
        Get the maximum amount of slots on this block.

        Returns
        - maximum occupied slots count
        """
        ...
