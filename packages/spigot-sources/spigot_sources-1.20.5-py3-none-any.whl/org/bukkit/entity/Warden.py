"""
Python module generated from Java source file org.bukkit.entity.Warden

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Warden(Monster):
    """
    A Warden.
    """

    def getAnger(self) -> int:
        """
        Gets the anger level of this warden.
        
        Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
        target it will actively pursue it.

        Returns
        - anger level
        """
        ...


    def getAnger(self, entity: "Entity") -> int:
        """
        Gets the anger level of this warden.
        
        Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
        target it will actively pursue it.

        Arguments
        - entity: target entity

        Returns
        - anger level
        """
        ...


    def increaseAnger(self, entity: "Entity", increase: int) -> None:
        """
        Increases the anger level of this warden.
        
        Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
        target it will actively pursue it.

        Arguments
        - entity: target entity
        - increase: number to increase by

        See
        - .getAnger(org.bukkit.entity.Entity)
        """
        ...


    def setAnger(self, entity: "Entity", anger: int) -> None:
        """
        Sets the anger level of this warden.
        
        Anger is an integer from 0 to 150. Once a Warden reaches 80 anger at a
        target it will actively pursue it.

        Arguments
        - entity: target entity
        - anger: new anger level

        See
        - .getAnger(org.bukkit.entity.Entity)
        """
        ...


    def clearAnger(self, entity: "Entity") -> None:
        """
        Clears the anger level of this warden.

        Arguments
        - entity: target entity
        """
        ...


    def getEntityAngryAt(self) -> "LivingEntity":
        """
        Gets the LivingEntity at which this warden is most angry.

        Returns
        - The target LivingEntity or null
        """
        ...


    def setDisturbanceLocation(self, location: "Location") -> None:
        """
        Make the warden sense a disturbance in the force at the location given.

        Arguments
        - location: location of the disturbance
        """
        ...


    def getAngerLevel(self) -> "AngerLevel":
        """
        Get the level of anger of this warden.

        Returns
        - The level of anger
        """
        ...


    class AngerLevel(Enum):

        CALM = 0
        """
        Anger level 0-39.
        """
        AGITATED = 1
        """
        Anger level 40-79.
        """
        ANGRY = 2
        """
        Anger level 80 or above.
        """
