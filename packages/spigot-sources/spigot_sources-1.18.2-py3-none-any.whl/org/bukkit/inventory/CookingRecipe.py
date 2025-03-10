"""
Python module generated from Java source file org.bukkit.inventory.CookingRecipe

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

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


class CookingRecipe(Recipe, Keyed):
    """
    Represents a cooking recipe.
    
    Type `<T>`: type of recipe
    """

    def __init__(self, key: "NamespacedKey", result: "ItemStack", source: "Material", experience: float, cookingTime: int):
        """
        Create a cooking recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - source: The input material.
        - experience: The experience given by this recipe
        - cookingTime: The cooking time (in ticks)
        """
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", input: "RecipeChoice", experience: float, cookingTime: int):
        """
        Create a cooking recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - input: The input choices.
        - experience: The experience given by this recipe
        - cookingTime: The cooking time (in ticks)
        """
        ...


    def setInput(self, input: "Material") -> "CookingRecipe":
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


    def setInputChoice(self, input: "RecipeChoice") -> "T":
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


    def setExperience(self, experience: float) -> None:
        """
        Sets the experience given by this recipe.

        Arguments
        - experience: the experience level
        """
        ...


    def getExperience(self) -> float:
        """
        Get the experience given by this recipe.

        Returns
        - experience level
        """
        ...


    def setCookingTime(self, cookingTime: int) -> None:
        """
        Set the cooking time for this recipe in ticks.

        Arguments
        - cookingTime: new cooking time
        """
        ...


    def getCookingTime(self) -> int:
        """
        Get the cooking time for this recipe in ticks.

        Returns
        - cooking time
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
