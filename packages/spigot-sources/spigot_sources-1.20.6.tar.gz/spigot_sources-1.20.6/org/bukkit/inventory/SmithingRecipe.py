"""
Python module generated from Java source file org.bukkit.inventory.SmithingRecipe

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class SmithingRecipe(Recipe, Keyed):
    """
    Represents a smithing recipe.
    """

    def __init__(self, key: "NamespacedKey", result: "ItemStack", base: "RecipeChoice", addition: "RecipeChoice"):
        """
        Create a smithing recipe to produce the specified result ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - base: The base ingredient
        - addition: The addition ingredient

        Deprecated
        - as of Minecraft 1.20, smithing recipes are now separated into two
        distinct recipe types, SmithingTransformRecipe and SmithingTrimRecipe.
        This class now acts as a base class to these two classes and will do nothing when
        added to the server.
        """
        ...


    def getBase(self) -> "RecipeChoice":
        """
        Get the base recipe item.

        Returns
        - base choice
        """
        ...


    def getAddition(self) -> "RecipeChoice":
        """
        Get the addition recipe item.

        Returns
        - addition choice
        """
        ...


    def getResult(self) -> "ItemStack":
        ...


    def getKey(self) -> "NamespacedKey":
        ...
