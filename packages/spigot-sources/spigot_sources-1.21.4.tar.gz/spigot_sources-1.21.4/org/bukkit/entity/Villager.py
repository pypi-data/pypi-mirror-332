"""
Python module generated from Java source file org.bukkit.entity.Villager

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from java.util import UUID
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import Location
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import *
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Villager(AbstractVillager):
    """
    Represents a villager NPC
    """

    def getProfession(self) -> "Profession":
        """
        Gets the current profession of this villager.

        Returns
        - Current profession.
        """
        ...


    def setProfession(self, profession: "Profession") -> None:
        """
        Sets the new profession of this villager.

        Arguments
        - profession: New profession.
        """
        ...


    def getVillagerType(self) -> "Type":
        """
        Gets the current type of this villager.

        Returns
        - Current type.
        """
        ...


    def setVillagerType(self, type: "Type") -> None:
        """
        Sets the new type of this villager.

        Arguments
        - type: New type.
        """
        ...


    def getVillagerLevel(self) -> int:
        """
        Gets the level of this villager.
        
        A villager with a level of 1 and no experience is liable to lose its
        profession.

        Returns
        - this villager's level
        """
        ...


    def setVillagerLevel(self, level: int) -> None:
        """
        Sets the level of this villager.
        
        A villager with a level of 1 and no experience is liable to lose its
        profession.

        Arguments
        - level: the new level

        Raises
        - IllegalArgumentException: if level not between [1, 5]
        """
        ...


    def getVillagerExperience(self) -> int:
        """
        Gets the trading experience of this villager.

        Returns
        - trading experience
        """
        ...


    def setVillagerExperience(self, experience: int) -> None:
        """
        Sets the trading experience of this villager.

        Arguments
        - experience: new experience

        Raises
        - IllegalArgumentException: if experience &lt; 0
        """
        ...


    def sleep(self, location: "Location") -> bool:
        """
        Attempts to make this villager sleep at the given location.
        
        The location must be in the current world and have a bed placed at the
        location. The villager will put its head on the specified block while
        sleeping.

        Arguments
        - location: the location of the bed

        Returns
        - whether the sleep was successful
        """
        ...


    def wakeup(self) -> None:
        """
        Causes this villager to wake up if he's currently sleeping.

        Raises
        - IllegalStateException: if not sleeping
        """
        ...


    def shakeHead(self) -> None:
        """
        Causes this villager to shake his head.
        """
        ...


    def zombify(self) -> "ZombieVillager":
        """
        Convert this Villager into a ZombieVillager as if it was killed by a
        Zombie.
        
        **Note:** this will fire a EntityTransformEvent

        Returns
        - the converted entity ZombieVillager or null if the
        conversion its cancelled
        """
        ...


    def getReputation(self, uuid: "UUID", reputationType: "ReputationType") -> int:
        """
        Gets the reputation of an entity for a given type.

        Arguments
        - uuid: the UUID of the entity whose reputation is being checked
        - reputationType: reputation type to be retrieved

        Returns
        - current reputation for the given reputation type
        """
        ...


    def getWeightedReputation(self, uuid: "UUID", reputationType: "ReputationType") -> int:
        """
        Gets the weighted reputation of an entity for a given type.
        
        The total reputation of an entity is a sum of its weighted
        reputations of each type, where the reputation is multiplied by weight
        assigned to its type.

        Arguments
        - uuid: the UUID of the entity whose reputation is being checked
        - reputationType: reputation type to be retrieved

        Returns
        - current reputation for the given reputation type

        See
        - ReputationType.getWeight()
        """
        ...


    def getReputation(self, uuid: "UUID") -> int:
        """
        Gets the reputation of an entity.

        Arguments
        - uuid: the UUID of the entity whose reputation is being checked

        Returns
        - current reputation for the given reputation type
        """
        ...


    def addReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int) -> None:
        """
        Add reputation of a given type towards a given entity.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    added
        - reputationType: reputation type to be modified
        - amount: amount of reputation to add
        """
        ...


    def addReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int, changeReason: "ReputationEvent") -> None:
        """
        Add reputation of a given type towards a given entity, with a specific
        change reason.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    added
        - reputationType: reputation type to be modified
        - amount: amount of reputation to add
        - changeReason: reputation change reason
        """
        ...


    def removeReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int) -> None:
        """
        Remove reputation of a given type towards a given entity.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    removed
        - reputationType: reputation type to be modified
        - amount: amount of reputation to remove
        """
        ...


    def removeReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int, changeReason: "ReputationEvent") -> None:
        """
        Remove reputation of a given type towards a given entity, with a
        specific change reason.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    removed
        - reputationType: reputation type to be modified
        - amount: amount of reputation to remove
        - changeReason: reputation change reason
        """
        ...


    def setReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int) -> None:
        """
        Set reputation of a given type towards a given entity.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    added
        - reputationType: reputation type to be modified
        - amount: amount of reputation to add
        """
        ...


    def setReputation(self, uuid: "UUID", reputationType: "ReputationType", amount: int, changeReason: "ReputationEvent") -> None:
        """
        Set reputation of a given type towards a given entity, with a specific
        change reason.
        
        The final value will be clamped to the maximum value supported by the
        provided reputation type. If the final value is below the reputation
        discard threshold, gossip associated with this reputation type will be
        removed.
        
        Note: this will fire a
        org.bukkit.event.entity.VillagerReputationChangeEvent.

        Arguments
        - uuid: the UUID of the entity for whom the reputation is being
                    added
        - reputationType: reputation type to be modified
        - amount: amount of reputation to add
        - changeReason: reputation change reason
        """
        ...


    def setGossipDecayTime(self, ticks: int) -> None:
        """
        Sets the reputation decay time for this villager.
        
        Defaults to **24000** (1 daylight cycle).

        Arguments
        - ticks: amount of ticks until the villager's reputation decays
        """
        ...


    def getGossipDecayTime(self) -> int:
        """
        Gets the reputation decay time for this villager.
        
        Defaults to **24000** (1 daylight cycle).

        Returns
        - amount of ticks until the villager's reputation decays
        """
        ...
