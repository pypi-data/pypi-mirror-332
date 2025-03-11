"""
Python module generated from Java source file org.bukkit.inventory.MerchantInventory

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class MerchantInventory(Inventory):
    """
    Represents a trading inventory between a player and a merchant.
    
    The holder of this Inventory is the owning Villager, or null if the player is
    trading with a merchant created by a plugin.
    """

    def getSelectedRecipeIndex(self) -> int:
        """
        Get the index of the currently selected recipe.

        Returns
        - the index of the currently selected recipe
        """
        ...


    def getSelectedRecipe(self) -> "MerchantRecipe":
        """
        Get the currently active recipe.
        
        This will be `null` if the items provided by the player do
        not match the ingredients of the selected recipe. This does not
        necessarily match the recipe selected by the player: If the player has
        selected the first recipe, the merchant will search all of its offers
        for a matching recipe to activate.

        Returns
        - the currently active recipe
        """
        ...


    def getMerchant(self) -> "Merchant":
        """
        Gets the Merchant associated with this inventory.

        Returns
        - merchant
        """
        ...
