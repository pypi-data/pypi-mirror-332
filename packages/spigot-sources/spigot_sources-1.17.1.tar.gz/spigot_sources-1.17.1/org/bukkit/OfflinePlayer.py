"""
Python module generated from Java source file org.bukkit.OfflinePlayer

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import *
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.entity import AnimalTamer
from org.bukkit.entity import EntityType
from org.bukkit.entity import Player
from org.bukkit.permissions import ServerOperator
from typing import Any, Callable, Iterable, Tuple


class OfflinePlayer(ServerOperator, AnimalTamer, ConfigurationSerializable):

    def isOnline(self) -> bool:
        """
        Checks if this player is currently online

        Returns
        - True if they are online
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of this player
        
        Names are no longer unique past a single game session. For persistent storage
        it is recommended that you use .getUniqueId() instead.

        Returns
        - Player name or null if we have not seen a name for this player yet
        """
        ...


    def getUniqueId(self) -> "UUID":
        """
        Returns the UUID of this player

        Returns
        - Player UUID
        """
        ...


    def isBanned(self) -> bool:
        """
        Checks if this player is banned or not

        Returns
        - True if banned, otherwise False
        """
        ...


    def isWhitelisted(self) -> bool:
        """
        Checks if this player is whitelisted or not

        Returns
        - True if whitelisted
        """
        ...


    def setWhitelisted(self, value: bool) -> None:
        """
        Sets if this player is whitelisted or not

        Arguments
        - value: True if whitelisted
        """
        ...


    def getPlayer(self) -> "Player":
        """
        Gets a Player object that this represents, if there is one
        
        If the player is online, this will return that player. Otherwise,
        it will return null.

        Returns
        - Online player
        """
        ...


    def getFirstPlayed(self) -> int:
        """
        Gets the first date and time that this player was witnessed on this
        server.
        
        If the player has never played before, this will return 0. Otherwise,
        it will be the amount of milliseconds since midnight, January 1, 1970
        UTC.

        Returns
        - Date of first log-in for this player, or 0
        """
        ...


    def getLastPlayed(self) -> int:
        """
        Gets the last date and time that this player was witnessed on this
        server.
        
        If the player has never played before, this will return 0. Otherwise,
        it will be the amount of milliseconds since midnight, January 1, 1970
        UTC.

        Returns
        - Date of last log-in for this player, or 0
        """
        ...


    def hasPlayedBefore(self) -> bool:
        """
        Checks if this player has played on this server before.

        Returns
        - True if the player has played before, otherwise False
        """
        ...


    def getBedSpawnLocation(self) -> "Location":
        """
        Gets the Location where the player will spawn at their bed, null if
        they have not slept in one or their current bed spawn is invalid.

        Returns
        - Bed Spawn Location if bed exists, otherwise null.
        """
        ...


    def incrementStatistic(self, statistic: "Statistic") -> None:
        """
        Increments the given statistic for this player.
        
        This is equivalent to the following code:
        `incrementStatistic(Statistic, 1)`

        Arguments
        - statistic: Statistic to increment

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def decrementStatistic(self, statistic: "Statistic") -> None:
        """
        Decrements the given statistic for this player.
        
        This is equivalent to the following code:
        `decrementStatistic(Statistic, 1)`

        Arguments
        - statistic: Statistic to decrement

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def incrementStatistic(self, statistic: "Statistic", amount: int) -> None:
        """
        Increments the given statistic for this player.

        Arguments
        - statistic: Statistic to increment
        - amount: Amount to increment this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def decrementStatistic(self, statistic: "Statistic", amount: int) -> None:
        """
        Decrements the given statistic for this player.

        Arguments
        - statistic: Statistic to decrement
        - amount: Amount to decrement this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def setStatistic(self, statistic: "Statistic", newValue: int) -> None:
        """
        Sets the given statistic for this player.

        Arguments
        - statistic: Statistic to set
        - newValue: The value to set this statistic to

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if newValue is negative
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def getStatistic(self, statistic: "Statistic") -> int:
        """
        Gets the value of the given statistic for this player.

        Arguments
        - statistic: Statistic to check

        Returns
        - the value of the given statistic

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if the statistic requires an
            additional parameter
        """
        ...


    def incrementStatistic(self, statistic: "Statistic", material: "Material") -> None:
        """
        Increments the given statistic for this player for the given material.
        
        This is equivalent to the following code:
        `incrementStatistic(Statistic, Material, 1)`

        Arguments
        - statistic: Statistic to increment
        - material: Material to offset the statistic with

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def decrementStatistic(self, statistic: "Statistic", material: "Material") -> None:
        """
        Decrements the given statistic for this player for the given material.
        
        This is equivalent to the following code:
        `decrementStatistic(Statistic, Material, 1)`

        Arguments
        - statistic: Statistic to decrement
        - material: Material to offset the statistic with

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def getStatistic(self, statistic: "Statistic", material: "Material") -> int:
        """
        Gets the value of the given statistic for this player.

        Arguments
        - statistic: Statistic to check
        - material: Material offset of the statistic

        Returns
        - the value of the given statistic

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def incrementStatistic(self, statistic: "Statistic", material: "Material", amount: int) -> None:
        """
        Increments the given statistic for this player for the given material.

        Arguments
        - statistic: Statistic to increment
        - material: Material to offset the statistic with
        - amount: Amount to increment this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def decrementStatistic(self, statistic: "Statistic", material: "Material", amount: int) -> None:
        """
        Decrements the given statistic for this player for the given material.

        Arguments
        - statistic: Statistic to decrement
        - material: Material to offset the statistic with
        - amount: Amount to decrement this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def setStatistic(self, statistic: "Statistic", material: "Material", newValue: int) -> None:
        """
        Sets the given statistic for this player for the given material.

        Arguments
        - statistic: Statistic to set
        - material: Material to offset the statistic with
        - newValue: The value to set this statistic to

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if material is null
        - IllegalArgumentException: if newValue is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def incrementStatistic(self, statistic: "Statistic", entityType: "EntityType") -> None:
        """
        Increments the given statistic for this player for the given entity.
        
        This is equivalent to the following code:
        `incrementStatistic(Statistic, EntityType, 1)`

        Arguments
        - statistic: Statistic to increment
        - entityType: EntityType to offset the statistic with

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def decrementStatistic(self, statistic: "Statistic", entityType: "EntityType") -> None:
        """
        Decrements the given statistic for this player for the given entity.
        
        This is equivalent to the following code:
        `decrementStatistic(Statistic, EntityType, 1)`

        Arguments
        - statistic: Statistic to decrement
        - entityType: EntityType to offset the statistic with

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def getStatistic(self, statistic: "Statistic", entityType: "EntityType") -> int:
        """
        Gets the value of the given statistic for this player.

        Arguments
        - statistic: Statistic to check
        - entityType: EntityType offset of the statistic

        Returns
        - the value of the given statistic

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def incrementStatistic(self, statistic: "Statistic", entityType: "EntityType", amount: int) -> None:
        """
        Increments the given statistic for this player for the given entity.

        Arguments
        - statistic: Statistic to increment
        - entityType: EntityType to offset the statistic with
        - amount: Amount to increment this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def decrementStatistic(self, statistic: "Statistic", entityType: "EntityType", amount: int) -> None:
        """
        Decrements the given statistic for this player for the given entity.

        Arguments
        - statistic: Statistic to decrement
        - entityType: EntityType to offset the statistic with
        - amount: Amount to decrement this statistic by

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if amount is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...


    def setStatistic(self, statistic: "Statistic", entityType: "EntityType", newValue: int) -> None:
        """
        Sets the given statistic for this player for the given entity.

        Arguments
        - statistic: Statistic to set
        - entityType: EntityType to offset the statistic with
        - newValue: The value to set this statistic to

        Raises
        - IllegalArgumentException: if statistic is null
        - IllegalArgumentException: if entityType is null
        - IllegalArgumentException: if newValue is negative
        - IllegalArgumentException: if the given parameter is not valid
            for the statistic
        """
        ...
