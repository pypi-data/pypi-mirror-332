"""
Python module generated from Java source file org.bukkit.block.TrialSpawner

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.spawner import TrialSpawnerConfiguration
from typing import Any, Callable, Iterable, Tuple


class TrialSpawner(TileState):
    """
    Represents a captured state of a trial spawner.
    """

    def getCooldownLength(self) -> int:
        """
        Gets the length in ticks the spawner will stay in cooldown for.

        Returns
        - the number of ticks
        """
        ...


    def setCooldownLength(self, ticks: int) -> None:
        """
        Sets the length in ticks the spawner will stay in cooldown for.

        Arguments
        - ticks: the number of ticks
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


    def getTrackedPlayers(self) -> Iterable["Player"]:
        """
        Gets the players this spawner is currently tracking.
        
        **Note:** the returned collection is immutable, use
        .startTrackingPlayer(Player) or .stopTrackingPlayer(Player)
        instead.

        Returns
        - a collection of players this spawner is tracking or an empty
                collection if there aren't any
        """
        ...


    def isTrackingPlayer(self, player: "Player") -> bool:
        """
        Checks if this spawner is currently tracking the provided player.

        Arguments
        - player: the player

        Returns
        - True if this spawner is tracking the provided player
        """
        ...


    def startTrackingPlayer(self, player: "Player") -> None:
        """
        Force this spawner to start tracking the provided player.
        
        **Note:** the spawner may decide to stop tracking this player at any given
        time.

        Arguments
        - player: the player
        """
        ...


    def stopTrackingPlayer(self, player: "Player") -> None:
        """
        Force this spawner to stop tracking the provided player.
        
        **Note:** the spawner may decide to start tracking this player again at
        any given time.

        Arguments
        - player: the player
        """
        ...


    def getTrackedEntities(self) -> Iterable["Entity"]:
        """
        Gets a list of entities this spawner is currently tracking.
        
        **Note:** the returned collection is immutable, use
        .startTrackingEntity(Entity) or .stopTrackingEntity(Entity)
        instead.

        Returns
        - a collection of entities this spawner is tracking or an empty
                collection if there aren't any
        """
        ...


    def isTrackingEntity(self, entity: "Entity") -> bool:
        """
        Checks if this spawner is currently tracking the provided entity.

        Arguments
        - entity: the entity

        Returns
        - True if this spawner is tracking the provided entity
        """
        ...


    def startTrackingEntity(self, entity: "Entity") -> None:
        """
        Force this spawner to start tracking the provided entity.
        
        **Note:** the spawner may decide to stop tracking this entity at any given
        time.

        Arguments
        - entity: the entity
        """
        ...


    def stopTrackingEntity(self, entity: "Entity") -> None:
        """
        Force this spawner to stop tracking the provided entity.
        
        **Note:** the spawner may decide to start tracking this entity again at
        any given time.

        Arguments
        - entity: the entity
        """
        ...


    def isOminous(self) -> bool:
        """
        Checks if this spawner is using the ominous
        TrialSpawnerConfiguration.

        Returns
        - True is using the ominous configuration
        """
        ...


    def setOminous(self, ominous: bool) -> None:
        """
        Changes this spawner between the normal and ominous
        TrialSpawnerConfiguration.

        Arguments
        - ominous: True to use the ominous TrialSpawnerConfiguration, False to
                       use the normal one.
        """
        ...


    def getNormalConfiguration(self) -> "TrialSpawnerConfiguration":
        """
        Gets the TrialSpawnerConfiguration used when .isOminous() is
        False.

        Returns
        - the TrialSpawnerConfiguration
        """
        ...


    def getOminousConfiguration(self) -> "TrialSpawnerConfiguration":
        """
        Gets the TrialSpawnerConfiguration used when .isOminous() is
        True.

        Returns
        - the TrialSpawnerConfiguration
        """
        ...
