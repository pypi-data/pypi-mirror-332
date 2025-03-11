"""
Python module generated from Java source file org.bukkit.inventory.view.builder.MerchantInventoryViewBuilder

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Server
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Merchant
from org.bukkit.inventory.view.builder import *
from typing import Any, Callable, Iterable, Tuple


class MerchantInventoryViewBuilder(InventoryViewBuilder):
    """
    An InventoryViewBuilder for creating merchant views
    
    Type `<V>`: the type of InventoryView created by this builder
    """

    def copy(self) -> "MerchantInventoryViewBuilder"["V"]:
        ...


    def title(self, title: str) -> "MerchantInventoryViewBuilder"["V"]:
        ...


    def merchant(self, merchant: "Merchant") -> "MerchantInventoryViewBuilder"["V"]:
        """
        Adds a merchant to this builder

        Arguments
        - merchant: the merchant

        Returns
        - this builder
        """
        ...


    def checkReachable(self, checkReachable: bool) -> "MerchantInventoryViewBuilder"["V"]:
        """
        Determines whether or not the server should check if the player can reach
        the location.
        
        Given checkReachable is provided and a virtual merchant is provided to
        the builder from Server.createMerchant(String) this method will
        have no effect on the actual menu status.

        Arguments
        - checkReachable: whether or not to check if the view is "reachable"

        Returns
        - this builder
        """
        ...
