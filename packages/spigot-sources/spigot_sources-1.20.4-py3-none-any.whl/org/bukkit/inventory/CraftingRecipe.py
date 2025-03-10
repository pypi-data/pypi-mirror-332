"""
Python module generated from Java source file org.bukkit.inventory.CraftingRecipe

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from org.bukkit.inventory.recipe import CraftingBookCategory
from typing import Any, Callable, Iterable, Tuple


class CraftingRecipe(Recipe, Keyed):
    """
    Represents a shaped or shapeless crafting recipe.
    """

    def getKey(self) -> "NamespacedKey":
        ...


    def getResult(self) -> "ItemStack":
        """
        Get the result of this recipe.

        Returns
        - The result stack.
        """
        ...


    def getGroup(self) -> str:
        """
        Get the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        Returns
        - recipe group. An empty string denotes no group. May not be null.
        """
        ...


    def setGroup(self, group: str) -> None:
        """
        Set the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        Arguments
        - group: recipe group. An empty string denotes no group. May not be
        null.
        """
        ...


    def getCategory(self) -> "CraftingBookCategory":
        """
        Gets the category which this recipe will appear in the recipe book under.
        
        Defaults to CraftingBookCategory.MISC if not set.

        Returns
        - recipe book category
        """
        ...


    def setCategory(self, category: "CraftingBookCategory") -> None:
        """
        Sets the category which this recipe will appear in the recipe book under.
        
        Defaults to CraftingBookCategory.MISC if not set.

        Arguments
        - category: recipe book category
        """
        ...
