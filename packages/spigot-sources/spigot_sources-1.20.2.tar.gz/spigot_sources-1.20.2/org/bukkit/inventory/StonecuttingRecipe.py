"""
Python module generated from Java source file org.bukkit.inventory.StonecuttingRecipe

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Collections
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class StonecuttingRecipe(Recipe, Keyed):
    """
    Represents a Stonecutting recipe.
    """

    def __init__(self, key: "NamespacedKey", result: "ItemStack", source: "Material"):
        """
        Create a Stonecutting recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - source: The input material.
        """
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", input: "RecipeChoice"):
        """
        Create a cooking recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - input: The input choices.
        """
        ...


    def setInput(self, input: "Material") -> "StonecuttingRecipe":
        """
        Sets the input of this cooking recipe.

        Arguments
        - input: The input material.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def getInput(self) -> "ItemStack":
        """
        Get the input material.

        Returns
        - The input material.
        """
        ...


    def setInputChoice(self, input: "RecipeChoice") -> "StonecuttingRecipe":
        """
        Sets the input of this cooking recipe.

        Arguments
        - input: The input choice.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def getInputChoice(self) -> "RecipeChoice":
        """
        Get the input choice.

        Returns
        - The input choice.
        """
        ...


    def getResult(self) -> "ItemStack":
        """
        Get the result of this recipe.

        Returns
        - The resulting stack.
        """
        ...


    def getKey(self) -> "NamespacedKey":
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
