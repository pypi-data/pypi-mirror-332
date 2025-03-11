"""
Python module generated from Java source file org.bukkit.spawner.TrialSpawnerConfiguration

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.loot import LootTable
from org.bukkit.spawner import *
from typing import Any, Callable, Iterable, Tuple


class TrialSpawnerConfiguration(BaseSpawner):
    """
    Represents one of the configurations of a trial spawner.
    """

    def getBaseSpawnsBeforeCooldown(self) -> float:
        """
        Gets the base number of entities the spawner will spawn before going into
        cooldown.

        Returns
        - the number of entities
        """
        ...


    def setBaseSpawnsBeforeCooldown(self, amount: float) -> None:
        """
        Sets the base number of entities the spawner will spawn before going into
        cooldown.

        Arguments
        - amount: the number of entities
        """
        ...


    def getBaseSimultaneousEntities(self) -> float:
        """
        Gets the base number of entities this spawner can track at once. 
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        Returns
        - the number of entities
        """
        ...


    def setBaseSimultaneousEntities(self, amount: float) -> None:
        """
        Sets the base number of entities this spawner can track at once. 
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        Arguments
        - amount: the number of entities
        """
        ...


    def getAdditionalSpawnsBeforeCooldown(self) -> float:
        """
        Gets the additional number of entities the spawner will spawn per tracked player
        before going into cooldown.

        Returns
        - the number of entities
        """
        ...


    def setAdditionalSpawnsBeforeCooldown(self, amount: float) -> None:
        """
        Sets the additional number of entities the spawner will spawn per tracked player
        before going into cooldown.

        Arguments
        - amount: the number of entities
        """
        ...


    def getAdditionalSimultaneousEntities(self) -> float:
        """
        Gets the additional number of entities this spawner can track at once per
        tracked player. 
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        Returns
        - the number of entities
        """
        ...


    def setAdditionalSimultaneousEntities(self, amount: float) -> None:
        """
        Sets the additional number of entities this spawner can track at once per
        tracked player. 
        If the limit is reached the spawner will not be able to spawn any more
        entities until the existing entities are killed or move too far away.

        Arguments
        - amount: the number of entities
        """
        ...


    def getPossibleRewards(self) -> dict["LootTable", "Integer"]:
        """
        Gets a list of LootTables this spawner can pick a reward from as
        well as their associated weight to be chosen.

        Returns
        - a map of loot tables and their associated weight, or an empty
                map if there are none
        """
        ...


    def addPossibleReward(self, table: "LootTable", weight: int) -> None:
        """
        Add a LootTable to the list of tables this spawner can pick a reward
        from with a given weight.

        Arguments
        - table: the loot table
        - weight: the weight, must be at least 1
        """
        ...


    def removePossibleReward(self, table: "LootTable") -> None:
        """
        Removes the provided LootTable from the list of tables this spawner
        can pick a reward from.

        Arguments
        - table: the loot table
        """
        ...


    def setPossibleRewards(self, rewards: dict["LootTable", "Integer"]) -> None:
        """
        Sets the list of LootTables and their weights this spawner can pick a
        reward from. 
        All loot tables in the map must be non-null and all weights must be at least
        1.

        Arguments
        - rewards: a map of loot tables and their weights, or null to clear all
                       possible tables
        """
        ...
