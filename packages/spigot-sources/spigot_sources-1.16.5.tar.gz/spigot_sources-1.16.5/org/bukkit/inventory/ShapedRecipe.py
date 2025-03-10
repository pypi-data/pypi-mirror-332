"""
Python module generated from Java source file org.bukkit.inventory.ShapedRecipe

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Collections
from org.apache.commons.lang import Validate
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class ShapedRecipe(Recipe, Keyed):
    """
    Represents a shaped (ie normal) crafting recipe.
    """

    def __init__(self, result: "ItemStack"):
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack"):
        """
        Create a shaped recipe to craft the specified ItemStack. The
        constructor merely determines the result and type; to set the actual
        recipe, you'll need to call the appropriate methods.

        Arguments
        - key: the unique recipe key
        - result: The item you want the recipe to create.

        See
        - ShapedRecipe.setIngredient(char, MaterialData)
        """
        ...


    def shape(self, *shape: Tuple[str, ...]) -> "ShapedRecipe":
        """
        Set the shape of this recipe to the specified rows. Each character
        represents a different ingredient; exactly what each character
        represents is set separately. The first row supplied corresponds with
        the upper most part of the recipe on the workbench e.g. if all three
        rows are supplies the first string represents the top row on the
        workbench.

        Arguments
        - shape: The rows of the recipe (up to 3 rows).

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def setIngredient(self, key: str, ingredient: "MaterialData") -> "ShapedRecipe":
        """
        Sets the material that a character in the recipe shape refers to.

        Arguments
        - key: The character that represents the ingredient in the shape.
        - ingredient: The ingredient.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def setIngredient(self, key: str, ingredient: "Material") -> "ShapedRecipe":
        """
        Sets the material that a character in the recipe shape refers to.

        Arguments
        - key: The character that represents the ingredient in the shape.
        - ingredient: The ingredient.

        Returns
        - The changed recipe, so you can chain calls.
        """
        ...


    def setIngredient(self, key: str, ingredient: "Material", raw: int) -> "ShapedRecipe":
        """
        Sets the material that a character in the recipe shape refers to.

        Arguments
        - key: The character that represents the ingredient in the shape.
        - ingredient: The ingredient.
        - raw: The raw material data as an integer.

        Returns
        - The changed recipe, so you can chain calls.

        Deprecated
        - Magic value
        """
        ...


    def setIngredient(self, key: str, ingredient: "RecipeChoice") -> "ShapedRecipe":
        ...


    def getIngredientMap(self) -> dict["Character", "ItemStack"]:
        """
        Get a copy of the ingredients map.

        Returns
        - The mapping of character to ingredients.
        """
        ...


    def getChoiceMap(self) -> dict["Character", "RecipeChoice"]:
        ...


    def getShape(self) -> list[str]:
        """
        Get the shape.

        Returns
        - The recipe's shape.

        Raises
        - NullPointerException: when not set yet
        """
        ...


    def getResult(self) -> "ItemStack":
        """
        Get the result.

        Returns
        - The result stack.
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
