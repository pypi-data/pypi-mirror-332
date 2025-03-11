"""
Python module generated from Java source file org.bukkit.event.block.BlockDispenseLootEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockDispenseLootEvent(BlockEvent, Cancellable):
    """
    Called when a block dispenses loot from its designated LootTable. This is not
    to be confused with events like BlockDispenseEvent which fires when a
    singular item is dispensed from its inventory container.
    
    Example: A player unlocks a trial chamber vault and the vault block dispenses
    its loot.
    """

    def __init__(self, player: "Player", theBlock: "Block", dispensedLoot: list["ItemStack"]):
        ...


    def getDispensedLoot(self) -> list["ItemStack"]:
        """
        Gets the loot that will be dispensed.

        Returns
        - the loot that will be dispensed
        """
        ...


    def setDispensedLoot(self, dispensedLoot: list["ItemStack"]) -> None:
        """
        Sets the loot that will be dispensed.

        Arguments
        - dispensedLoot: new loot to dispense
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Gets the player associated with this event.
        
        **Warning:** Some event instances like a
        org.bukkit.block.TrialSpawner dispensing its reward loot may not
        have a player associated with them and will return null.

        Returns
        - the player who unlocked the vault
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
