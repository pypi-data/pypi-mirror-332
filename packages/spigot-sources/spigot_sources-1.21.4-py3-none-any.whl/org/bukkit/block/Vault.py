"""
Python module generated from Java source file org.bukkit.block.Vault

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit.block import *
from org.bukkit.inventory import ItemStack
from org.bukkit.loot import LootTable
from typing import Any, Callable, Iterable, Tuple


class Vault(TileState):
    """
    Represents a captured state of a vault.
    """

    def getActivationRange(self) -> float:
        """
        Gets the distance at which a player must enter for this vault to
        activate.

        Returns
        - the distance at which a player must enter for this vault
        to activate.
        """
        ...


    def setActivationRange(self, range: float) -> None:
        """
        Sets the distance at which a player must enter for this vault to
        activate.

        Arguments
        - range: the distance at which a player must enter for this
        vault to activate.
        """
        ...


    def getDeactivationRange(self) -> float:
        """
        Gets the distance at which a player must exit for the vault to
        deactivate.

        Returns
        - the distance at which a player must exit for the vault
        to deactivate.
        """
        ...


    def setDeactivationRange(self, range: float) -> None:
        """
        Sets the distance at which a player must exit for this vault to
        deactivate.

        Arguments
        - range: the distance at which a player must exit for this
        vault to deactivate.
        """
        ...


    def getLootTable(self) -> "LootTable":
        """
        Gets the LootTable this vault will pick rewards from.

        Returns
        - the loot table
        """
        ...


    def setLootTable(self, table: "LootTable") -> None:
        """
        Sets the LootTable this vault will pick rewards from.

        Arguments
        - table: the loot table
        """
        ...


    def getDisplayLootTable(self) -> "LootTable":
        """
        Gets the LootTable this vault will display items from. 
        If this value is null the regular loot table will be used to display
        items.

        Returns
        - the loot table to display items from
        """
        ...


    def setDisplayLootTable(self, table: "LootTable") -> None:
        """
        Sets the LootTable this vault will display items from. 
        If this value is set to null the regular loot table will be used to
        display items.

        Arguments
        - table: the loot table to display items from
        """
        ...


    def getKeyItem(self) -> "ItemStack":
        """
        Gets the ItemStack players must use to unlock this vault.

        Returns
        - the key item
        """
        ...


    def setKeyItem(self, keyItem: "ItemStack") -> None:
        """
        Sets the ItemStack players must use to unlock this vault.

        Arguments
        - keyItem: the key item
        """
        ...


    def getRewardedPlayers(self) -> set["UUID"]:
        """
        Gets the players who have already received rewards from this vault.

        Returns
        - unmodifiable set of player UUIDs

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...
