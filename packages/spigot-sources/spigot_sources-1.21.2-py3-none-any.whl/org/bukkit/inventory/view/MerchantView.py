"""
Python module generated from Java source file org.bukkit.inventory.view.MerchantView

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import MerchantInventory
from org.bukkit.inventory.view import *
from typing import Any, Callable, Iterable, Tuple


class MerchantView(InventoryView):
    """
    An instance of InventoryView which provides extra methods related to
    merchant view data.
    """

    def getTopInventory(self) -> "MerchantInventory":
        ...


    def getMerchant(self) -> "Merchant":
        """
        Gets the merchant that this view is for.

        Returns
        - The merchant that this view uses
        """
        ...
