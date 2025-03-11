"""
Python module generated from Java source file org.bukkit.inventory.TransmuteRecipe

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class TransmuteRecipe(CraftingRecipe, ComplexRecipe):
    """
    Represents a recipe which will change the type of the input material when
    combined with an additional material, but preserve all custom data. Only the
    item type of the result stack will be used.
    
    Used for dyeing shulker boxes in Vanilla.
    """

    def __init__(self, key: "NamespacedKey", result: "Material", input: "RecipeChoice", material: "RecipeChoice"):
        """
        Create a transmute recipe to produce a result of the specified type.

        Arguments
        - key: the unique recipe key
        - result: the transmuted result material
        - input: the input ingredient
        - material: the additional ingredient
        """
        ...


    def getInput(self) -> "RecipeChoice":
        """
        Gets the input material, which will be transmuted.

        Returns
        - the input from transmutation
        """
        ...


    def getMaterial(self) -> "RecipeChoice":
        """
        Gets the additional material required to cause the transmutation.

        Returns
        - the ingredient material
        """
        ...
