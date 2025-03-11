"""
Python module generated from Java source file org.bukkit.inventory.Merchant

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class Merchant:
    """
    Represents a merchant. A merchant is a special type of inventory which can
    facilitate custom trades between items.
    """

    def getRecipes(self) -> list["MerchantRecipe"]:
        """
        Get a list of trades currently available from this merchant.

        Returns
        - an immutable list of trades
        """
        ...


    def setRecipes(self, recipes: list["MerchantRecipe"]) -> None:
        """
        Set the list of trades currently available from this merchant.
        
        This will not change the selected trades of players currently trading
        with this merchant.

        Arguments
        - recipes: a list of recipes
        """
        ...


    def getRecipe(self, i: int) -> "MerchantRecipe":
        """
        Get the recipe at a certain index of this merchant's trade list.

        Arguments
        - i: the index

        Returns
        - the recipe

        Raises
        - IndexOutOfBoundsException: if recipe index out of bounds
        """
        ...


    def setRecipe(self, i: int, recipe: "MerchantRecipe") -> None:
        """
        Set the recipe at a certain index of this merchant's trade list.

        Arguments
        - i: the index
        - recipe: the recipe

        Raises
        - IndexOutOfBoundsException: if recipe index out of bounds
        """
        ...


    def getRecipeCount(self) -> int:
        """
        Get the number of trades this merchant currently has available.

        Returns
        - the recipe count
        """
        ...


    def isTrading(self) -> bool:
        """
        Gets whether this merchant is currently trading.

        Returns
        - whether the merchant is trading
        """
        ...


    def getTrader(self) -> "HumanEntity":
        """
        Gets the player this merchant is trading with, or null if it is not
        currently trading.

        Returns
        - the trader, or null
        """
        ...
