"""
Python module generated from Java source file org.bukkit.inventory.CampfireRecipe

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class CampfireRecipe(CookingRecipe):
    """
    Represents a campfire recipe.
    """

    def __init__(self, key: "NamespacedKey", result: "ItemStack", source: "Material", experience: float, cookingTime: int):
        ...


    def __init__(self, key: "NamespacedKey", result: "ItemStack", input: "RecipeChoice", experience: float, cookingTime: int):
        ...
