"""
Python module generated from Java source file org.bukkit.inventory.FurnaceRecipe

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class FurnaceRecipe(CookingRecipe):
    """
    Represents a furnace recipe.
    """

    def __init__(self, result: "ItemStack", source: "Material"):
        ...


    def __init__(self, result: "ItemStack", source: "MaterialData"):
        ...


    def __init__(self, result: "ItemStack", source: "MaterialData", experience: float):
        ...


    def __init__(self, result: "ItemStack", source: "Material", data: int):
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", source: "Material", experience: float, cookingTime: int):
        """
        Create a furnace recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - source: The input material.
        - experience: The experience given by this recipe
        - cookingTime: The cooking time (in ticks)
        """
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", source: "Material", data: int, experience: float, cookingTime: int):
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", input: "RecipeChoice", experience: float, cookingTime: int):
        """
        Create a furnace recipe to craft the specified ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - input: The input choices.
        - experience: The experience given by this recipe
        - cookingTime: The cooking time (in ticks)
        """
        ...


    def setInput(self, input: "MaterialData") -> "FurnaceRecipe":
        """
        Sets the input of this furnace recipe.

        Arguments
        - input: The input material.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def setInput(self, input: "Material") -> "FurnaceRecipe":
        ...


    def setInput(self, input: "Material", data: int) -> "FurnaceRecipe":
        """
        Sets the input of this furnace recipe.

        Arguments
        - input: The input material.
        - data: The data value. (Note: This is currently ignored by the
            CraftBukkit server.)

        Returns
        - The changed recipe, so you can chain calls.

        Deprecated
        - Magic value
        """
        ...


    def setInputChoice(self, input: "RecipeChoice") -> "FurnaceRecipe":
        ...
