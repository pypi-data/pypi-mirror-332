"""
Python module generated from Java source file org.bukkit.inventory.view.FurnaceView

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Furnace
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class FurnaceView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    furnace view data.
    """

    def getCookTime(self) -> float:
        """
        The cook time for this view.
        
        See Furnace.getCookTime() for more information.

        Returns
        - a number between 0 and 1
        """
        ...


    def getBurnTime(self) -> float:
        """
        The total burn time for this view.
        
        See Furnace.getBurnTime() for more information.

        Returns
        - a number between 0 and 1
        """
        ...


    def isBurning(self) -> bool:
        """
        Checks whether or not the furnace is burning

        Returns
        - True given that the furnace is burning
        """
        ...


    def setCookTime(self, cookProgress: int, cookDuration: int) -> None:
        """
        Sets the cook time
        
        Setting cook time requires manipulation of both cookProgress and
        cookDuration. This method does a simple division to get total progress
        within the furnaces visual duration bar. For a clear visual effect
        (cookProgress / cookDuration) should return a number between 0 and 1
        inclusively.

        Arguments
        - cookProgress: the current of the cooking
        - cookDuration: the total cook time
        """
        ...


    def setBurnTime(self, burnProgress: int, burnDuration: int) -> None:
        """
        Sets the burn time
        
        Setting burn time requires manipulation of both burnProgress and
        burnDuration. This method does a simple division to get total progress
        within the furnaces visual burning bar. For a clear visual effect
        (burnProgress / burnDuration) should return a number between 0 and 1
        inclusively.

        Arguments
        - burnProgress: the progress towards the burnDuration
        - burnDuration: the total duration the view should be lit
        """
        ...
