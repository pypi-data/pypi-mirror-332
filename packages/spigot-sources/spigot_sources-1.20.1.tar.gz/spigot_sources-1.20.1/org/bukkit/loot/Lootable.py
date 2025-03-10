"""
Python module generated from Java source file org.bukkit.loot.Lootable

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.loot import *
from typing import Any, Callable, Iterable, Tuple


class Lootable:
    """
    Represents a org.bukkit.block.Container or a
    org.bukkit.entity.Mob that can have a loot table.
    
    Container loot will only generate upon opening, and only when the container
    is *first* opened.
    
    Entities will only generate loot upon death.
    """

    def setLootTable(self, table: "LootTable") -> None:
        """
        Set the loot table for a container or entity.
        
        To remove a loot table use null. Do not use LootTables.EMPTY to
        clear a LootTable.

        Arguments
        - table: the Loot Table this org.bukkit.block.Container or
        org.bukkit.entity.Mob will have.
        """
        ...


    def getLootTable(self) -> "LootTable":
        """
        Gets the Loot Table attached to this block or entity.
        
        
        If an block/entity does not have a loot table, this will return null, NOT
        an empty loot table.

        Returns
        - the Loot Table attached to this block or entity.
        """
        ...


    def setSeed(self, seed: int) -> None:
        """
        Set the seed used when this Loot Table generates loot.

        Arguments
        - seed: the seed to used to generate loot. Default is 0.
        """
        ...


    def getSeed(self) -> int:
        """
        Get the Loot Table's seed.
        
        The seed is used when generating loot.

        Returns
        - the seed
        """
        ...
