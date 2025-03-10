"""
Python module generated from Java source file org.bukkit.inventory.meta.Repairable

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class Repairable(ItemMeta):
    """
    Represents an item that can be repaired at an anvil.
    """

    def hasRepairCost(self) -> bool:
        """
        Checks to see if this has a repair penalty

        Returns
        - True if this has a repair penalty
        """
        ...


    def getRepairCost(self) -> int:
        """
        Gets the repair penalty

        Returns
        - the repair penalty
        """
        ...


    def setRepairCost(self, cost: int) -> None:
        """
        Sets the repair penalty

        Arguments
        - cost: repair penalty
        """
        ...


    def clone(self) -> "Repairable":
        ...
