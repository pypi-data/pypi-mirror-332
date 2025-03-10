"""
Python module generated from Java source file org.bukkit.inventory.SmithingTransformRecipe

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class SmithingTransformRecipe(SmithingRecipe):
    """
    Represents a smithing transform recipe.
    """

    def __init__(self, key: "NamespacedKey", result: "ItemStack", template: "RecipeChoice", base: "RecipeChoice", addition: "RecipeChoice"):
        """
        Create a smithing recipe to produce the specified result ItemStack.

        Arguments
        - key: The unique recipe key
        - result: The item you want the recipe to create.
        - template: The template item.
        - base: The base ingredient
        - addition: The addition ingredient
        """
        ...


    def getTemplate(self) -> "RecipeChoice":
        """
        Get the template recipe item.

        Returns
        - template choice
        """
        ...
