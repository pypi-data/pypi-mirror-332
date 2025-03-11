"""
Python module generated from Java source file org.bukkit.spawner.Spawner

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import CreatureSpawner
from org.bukkit.entity import EntityType
from org.bukkit.entity.minecart import SpawnerMinecart
from org.bukkit.spawner import *
from typing import Any, Callable, Iterable, Tuple


class Spawner(BaseSpawner):
    """
    Represents an entity spawner. 
    May be a SpawnerMinecart or a CreatureSpawner.
    """

    def setDelay(self, delay: int) -> None:
        """
        
        
        If set to -1, the spawn delay will be reset to a random value between
        .getMinSpawnDelay and .getMaxSpawnDelay().

        Arguments
        - delay: The delay.
        """
        ...


    def getMinSpawnDelay(self) -> int:
        """
        The minimum spawn delay amount (in ticks).
        
        This value is used when the spawner resets its delay (for any reason).
        It will choose a random number between .getMinSpawnDelay()
        and .getMaxSpawnDelay() for its next .getDelay().
        
        Default value is 200 ticks.

        Returns
        - the minimum spawn delay amount
        """
        ...


    def setMinSpawnDelay(self, delay: int) -> None:
        """
        Set the minimum spawn delay amount (in ticks).

        Arguments
        - delay: the minimum spawn delay amount

        See
        - .getMinSpawnDelay()
        """
        ...


    def getMaxSpawnDelay(self) -> int:
        """
        The maximum spawn delay amount (in ticks).
        
        This value is used when the spawner resets its delay (for any reason).
        It will choose a random number between .getMinSpawnDelay()
        and .getMaxSpawnDelay() for its next .getDelay().
        
        This value **must** be greater than 0 and less than or equal to
        .getMaxSpawnDelay().
        
        Default value is 800 ticks.

        Returns
        - the maximum spawn delay amount
        """
        ...


    def setMaxSpawnDelay(self, delay: int) -> None:
        """
        Set the maximum spawn delay amount (in ticks).
        
        This value **must** be greater than 0, as well as greater than or
        equal to .getMinSpawnDelay()

        Arguments
        - delay: the new maximum spawn delay amount

        See
        - .getMaxSpawnDelay()
        """
        ...


    def getSpawnCount(self) -> int:
        """
        Get how many mobs attempt to spawn.
        
        Default value is 4.

        Returns
        - the current spawn count
        """
        ...


    def setSpawnCount(self, spawnCount: int) -> None:
        """
        Set how many mobs attempt to spawn.

        Arguments
        - spawnCount: the new spawn count
        """
        ...


    def getMaxNearbyEntities(self) -> int:
        """
        Set the new maximum amount of similar entities that are allowed to be
        within spawning range of this spawner.
        
        If more than the maximum number of entities are within range, the spawner
        will not spawn and try again with a new .getDelay().
        
        Default value is 16.

        Returns
        - the maximum number of nearby, similar, entities
        """
        ...


    def setMaxNearbyEntities(self, maxNearbyEntities: int) -> None:
        """
        Set the maximum number of similar entities that are allowed to be within
        spawning range of this spawner.
        
        Similar entities are entities that are of the same EntityType

        Arguments
        - maxNearbyEntities: the maximum number of nearby, similar, entities
        """
        ...
