"""
Python module generated from Java source file org.bukkit.block.CreatureSpawner

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import EntityType
from typing import Any, Callable, Iterable, Tuple


class CreatureSpawner(TileState):
    """
    Represents a captured state of a creature spawner.
    """

    def getSpawnedType(self) -> "EntityType":
        """
        Get the spawner's creature type.

        Returns
        - The creature type.
        """
        ...


    def setSpawnedType(self, creatureType: "EntityType") -> None:
        """
        Set the spawner's creature type.

        Arguments
        - creatureType: The creature type.
        """
        ...


    def setCreatureTypeByName(self, creatureType: str) -> None:
        """
        Set the spawner mob type.

        Arguments
        - creatureType: The creature type's name.

        Deprecated
        - magic value, use
        .setSpawnedType(org.bukkit.entity.EntityType).
        """
        ...


    def getCreatureTypeName(self) -> str:
        """
        Get the spawner's creature type.

        Returns
        - The creature type's name.

        Deprecated
        - magic value, use .getSpawnedType().
        """
        ...


    def getDelay(self) -> int:
        """
        Get the spawner's delay.
        
        This is the delay, in ticks, until the spawner will spawn its next mob.

        Returns
        - The delay.
        """
        ...


    def setDelay(self, delay: int) -> None:
        """
        Set the spawner's delay.
        
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


    def getRequiredPlayerRange(self) -> int:
        """
        Get the maximum distance(squared) a player can be in order for this
        spawner to be active.
        
        If this value is less than or equal to 0, this spawner is always active
        (given that there are players online).
        
        Default value is 16.

        Returns
        - the maximum distance(squared) a player can be in order for this
        spawner to be active.
        """
        ...


    def setRequiredPlayerRange(self, requiredPlayerRange: int) -> None:
        """
        Set the maximum distance (squared) a player can be in order for this
        spawner to be active.
        
        Setting this value to less than or equal to 0 will make this spawner
        always active (given that there are players online).

        Arguments
        - requiredPlayerRange: the maximum distance (squared) a player can be
        in order for this spawner to be active.
        """
        ...


    def getSpawnRange(self) -> int:
        """
        Get the radius around which the spawner will attempt to spawn mobs in.
        
        This area is square, includes the block the spawner is in, and is
        centered on the spawner's x,z coordinates - not the spawner itself.
        
        It is 2 blocks high, centered on the spawner's y-coordinate (its bottom);
        thus allowing mobs to spawn as high as its top surface and as low
        as 1 block below its bottom surface.
        
        Default value is 4.

        Returns
        - the spawn range
        """
        ...


    def setSpawnRange(self, spawnRange: int) -> None:
        """
        Set the new spawn range.

        Arguments
        - spawnRange: the new spawn range

        See
        - .getSpawnRange()
        """
        ...
