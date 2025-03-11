"""
Python module generated from Java source file org.bukkit.inventory.view.StonecutterView

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import StonecutterInventory
from org.bukkit.inventory import StonecuttingRecipe
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class StonecutterView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    stonecutter view data.
    """

    def getTopInventory(self) -> "StonecutterInventory":
        ...


    def getSelectedRecipeIndex(self) -> int:
        """
        Gets the current index of the selected recipe.

        Returns
        - The index of the selected recipe in the stonecutter or -1 if null
        """
        ...


    def getRecipes(self) -> list["StonecuttingRecipe"]:
        """
        Gets a copy of all recipes currently available to the player.

        Returns
        - A copy of the StonecuttingRecipe's currently available
        for the player
        """
        ...


    def getRecipeAmount(self) -> int:
        """
        Gets the amount of recipes currently available.

        Returns
        - The amount of recipes currently available for the player
        """
        ...
