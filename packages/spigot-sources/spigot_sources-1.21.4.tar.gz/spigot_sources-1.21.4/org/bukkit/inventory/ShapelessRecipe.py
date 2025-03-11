"""
Python module generated from Java source file org.bukkit.inventory.ShapelessRecipe

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Collections
from java.util import Iterator
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class ShapelessRecipe(CraftingRecipe):
    """
    Represents a shapeless recipe, where the arrangement of the ingredients on
    the crafting grid does not matter.
    """

    def __init__(self, result: "ItemStack"):
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack"):
        """
        Create a shapeless recipe to craft the specified ItemStack. The
        constructor merely determines the result and type; to set the actual
        recipe, you'll need to call the appropriate methods.

        Arguments
        - key: the unique recipe key
        - result: The item you want the recipe to create.

        Raises
        - IllegalArgumentException: if the `result` is an empty item (AIR)

        See
        - ShapelessRecipe.addIngredient(int,Material,int)
        """
        ...


    def addIngredient(self, ingredient: "MaterialData") -> "ShapelessRecipe":
        """
        Adds the specified ingredient.

        Arguments
        - ingredient: The ingredient to add.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def addIngredient(self, ingredient: "Material") -> "ShapelessRecipe":
        """
        Adds the specified ingredient.

        Arguments
        - ingredient: The ingredient to add.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def addIngredient(self, ingredient: "Material", rawdata: int) -> "ShapelessRecipe":
        """
        Adds the specified ingredient.

        Arguments
        - ingredient: The ingredient to add.
        - rawdata: The data value, or -1 to allow any data value.

        Returns
        - The changed recipe, so you can chain calls.

        Deprecated
        - Magic value
        """
        ...


    def addIngredient(self, count: int, ingredient: "MaterialData") -> "ShapelessRecipe":
        """
        Adds multiples of the specified ingredient.

        Arguments
        - count: How many to add (can't be more than 9!)
        - ingredient: The ingredient to add.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def addIngredient(self, count: int, ingredient: "Material") -> "ShapelessRecipe":
        """
        Adds multiples of the specified ingredient.

        Arguments
        - count: How many to add (can't be more than 9!)
        - ingredient: The ingredient to add.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def addIngredient(self, count: int, ingredient: "Material", rawdata: int) -> "ShapelessRecipe":
        """
        Adds multiples of the specified ingredient.

        Arguments
        - count: How many to add (can't be more than 9!)
        - ingredient: The ingredient to add.
        - rawdata: The data value, or -1 to allow any data value.

        Returns
        - The changed recipe, so you can chain calls.

        Deprecated
        - Magic value
        """
        ...


    def addIngredient(self, ingredient: "RecipeChoice") -> "ShapelessRecipe":
        ...


    def removeIngredient(self, ingredient: "RecipeChoice") -> "ShapelessRecipe":
        """
        Removes an ingredient from the list.

        Arguments
        - ingredient: The ingredient to remove

        Returns
        - The changed recipe.
        """
        ...


    def removeIngredient(self, ingredient: "Material") -> "ShapelessRecipe":
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. Only removes exact matches,
        with a data value of 0.

        Arguments
        - ingredient: The ingredient to remove

        Returns
        - The changed recipe.
        """
        ...


    def removeIngredient(self, ingredient: "MaterialData") -> "ShapelessRecipe":
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. If the data value is -1,
        only ingredients with a -1 data value will be removed.

        Arguments
        - ingredient: The ingredient to remove

        Returns
        - The changed recipe.
        """
        ...


    def removeIngredient(self, count: int, ingredient: "Material") -> "ShapelessRecipe":
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances then specified, all will be removed. Only removes exact
        matches, with a data value of 0.

        Arguments
        - count: The number of copies to remove.
        - ingredient: The ingredient to remove

        Returns
        - The changed recipe.
        """
        ...


    def removeIngredient(self, count: int, ingredient: "MaterialData") -> "ShapelessRecipe":
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances then specified, all will be removed. If the data value
        is -1, only ingredients with a -1 data value will be removed.

        Arguments
        - count: The number of copies to remove.
        - ingredient: The ingredient to remove.

        Returns
        - The changed recipe.
        """
        ...


    def removeIngredient(self, ingredient: "Material", rawdata: int) -> "ShapelessRecipe":
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. If the data value is -1,
        only ingredients with a -1 data value will be removed.

        Arguments
        - ingredient: The ingredient to remove
        - rawdata: The data value;

        Returns
        - The changed recipe.

        Deprecated
        - Magic value
        """
        ...


    def removeIngredient(self, count: int, ingredient: "Material", rawdata: int) -> "ShapelessRecipe":
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances then specified, all will be removed. If the data value
        is -1, only ingredients with a -1 data value will be removed.

        Arguments
        - count: The number of copies to remove.
        - ingredient: The ingredient to remove.
        - rawdata: The data value.

        Returns
        - The changed recipe.

        Deprecated
        - Magic value
        """
        ...


    def getIngredientList(self) -> list["ItemStack"]:
        """
        Get the list of ingredients used for this recipe.

        Returns
        - The input list
        """
        ...


    def getChoiceList(self) -> list["RecipeChoice"]:
        ...
