"""
Python module generated from Java source file org.bukkit.event.inventory.TradeSelectEvent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import *
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import MerchantInventory
from org.bukkit.inventory.view import MerchantView
from typing import Any, Callable, Iterable, Tuple


class TradeSelectEvent(InventoryInteractEvent):
    """
    This event is called whenever a player clicks a new trade on the trades
    sidebar.
    
    This event allows the user to get the index of the trade, letting them get
    the MerchantRecipe via the Merchant.
    """

    def __init__(self, transaction: "MerchantView", newIndex: int):
        ...


    def getIndex(self) -> int:
        """
        Used to get the index of the trade the player clicked on.

        Returns
        - The index of the trade clicked by the player
        """
        ...


    def getInventory(self) -> "MerchantInventory":
        ...


    def getMerchant(self) -> "Merchant":
        """
        Get the Merchant involved.

        Returns
        - the Merchant
        """
        ...


    def getView(self) -> "MerchantView":
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
