"""
Python module generated from Java source file org.bukkit.entity.LightningStrike

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import GameEvent
from org.bukkit.enchantments import Enchantment
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class LightningStrike(Entity):
    """
    Represents an instance of a lightning strike. May or may not do damage.
    """

    def isEffect(self) -> bool:
        """
        Returns whether the strike is an effect that does no damage.

        Returns
        - whether the strike is an effect
        """
        ...


    def getFlashes(self) -> int:
        """
        Get the amount of flashes that will occur before the lightning is
        removed. By default this value is between 1 and 3.

        Returns
        - the flashes
        """
        ...


    def setFlashes(self, flashes: int) -> None:
        """
        Set the amount of flashes that will occur before the lightning is
        removed. One flash will occur after this lightning strike's life
        has reduced below 0.

        Arguments
        - flashes: the flashes
        """
        ...


    def getLifeTicks(self) -> int:
        """
        Get the amount of ticks this lightning strike will inflict damage
        upon its hit entities.
        
        When life ticks are negative, there is a random chance that another
        flash will be initiated and life ticks reset to 1.

        Returns
        - the life ticks
        """
        ...


    def setLifeTicks(self, ticks: int) -> None:
        """
        Get the amount of ticks this lightning strike will inflict damage
        upon its hit entities.
        
        When life ticks are negative, there is a random chance that another
        flash will be initiated and life ticks reset to 1. Additionally, if
        life ticks are set to 2 (the default value when a lightning strike
        has been spawned), a list of events will occur:
        
          - Impact sound effects will be played
          - Fire will be spawned (dependent on difficulty)
          - Lightning rods will be powered (if hit)
          - Copper will be stripped (if hit)
          - GameEvent.LIGHTNING_STRIKE will be dispatched

        Arguments
        - ticks: the life ticks
        """
        ...


    def getCausingPlayer(self) -> "Player":
        """
        Get the Player that caused this lightning to strike. This
        will occur naturally if a trident enchanted with
        Enchantment.CHANNELING Channeling were thrown at an entity
        during a storm.

        Returns
        - the player
        """
        ...


    def setCausingPlayer(self, player: "Player") -> None:
        """
        Set the Player that caused this lightning to strike.

        Arguments
        - player: the player
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot(Spigot):

        def isSilent(self) -> bool:
            """
            Returns whether the strike is silent.

            Returns
            - whether the strike is silent.

            Deprecated
            - sound is now client side and cannot be removed
            """
            ...
