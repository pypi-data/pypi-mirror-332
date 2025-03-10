"""
Python module generated from Java source file org.bukkit.inventory.SmithingInventory

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class SmithingInventory(Inventory):
    """
    Interface to the inventory of a Smithing table.
    """

    def getResult(self) -> "ItemStack":
        """
        Check what item is in the result slot of this smithing table.

        Returns
        - the result item
        """
        ...


    def setResult(self, newResult: "ItemStack") -> None:
        """
        Set the item in the result slot of the smithing table

        Arguments
        - newResult: the new result item
        """
        ...


    def getRecipe(self) -> "Recipe":
        """
        Get the current recipe formed on the smithing table, if any.

        Returns
        - the recipe, or null if the current contents don't match any
        recipe
        """
        ...
