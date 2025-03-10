"""
Python module generated from Java source file org.bukkit.inventory.CraftingInventory

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class CraftingInventory(Inventory):
    """
    Interface to the crafting inventories
    """

    def getResult(self) -> "ItemStack":
        """
        Check what item is in the result slot of this crafting inventory.

        Returns
        - The result item.
        """
        ...


    def getMatrix(self) -> list["ItemStack"]:
        """
        Get the contents of the crafting matrix.

        Returns
        - The contents. Individual entries may be null.
        """
        ...


    def setResult(self, newResult: "ItemStack") -> None:
        """
        Set the item in the result slot of the crafting inventory.

        Arguments
        - newResult: The new result item.
        """
        ...


    def setMatrix(self, contents: list["ItemStack"]) -> None:
        """
        Replace the contents of the crafting matrix

        Arguments
        - contents: The new contents. Individual entries may be null.

        Raises
        - IllegalArgumentException: if the length of contents is greater
            than the size of the crafting matrix.
        """
        ...


    def getRecipe(self) -> "Recipe":
        """
        Get the current recipe formed on the crafting inventory, if any.

        Returns
        - The recipe, or null if the current contents don't match any
            recipe.
        """
        ...
