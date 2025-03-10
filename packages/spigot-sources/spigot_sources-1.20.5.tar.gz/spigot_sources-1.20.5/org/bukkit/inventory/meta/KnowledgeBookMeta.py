"""
Python module generated from Java source file org.bukkit.inventory.meta.KnowledgeBookMeta

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class KnowledgeBookMeta(ItemMeta):

    def hasRecipes(self) -> bool:
        """
        Checks for the existence of recipes in the book.

        Returns
        - True if the book has recipes
        """
        ...


    def getRecipes(self) -> list["NamespacedKey"]:
        """
        Gets all the recipes in the book.

        Returns
        - list of all the recipes in the book
        """
        ...


    def setRecipes(self, recipes: list["NamespacedKey"]) -> None:
        """
        Clears the existing book recipes, and sets the book to use the provided
        recipes.

        Arguments
        - recipes: A list of recipes to set the book to use
        """
        ...


    def addRecipe(self, *recipes: Tuple["NamespacedKey", ...]) -> None:
        """
        Adds new recipe to the end of the book.

        Arguments
        - recipes: A list of recipe keys
        """
        ...


    def clone(self) -> "KnowledgeBookMeta":
        ...
