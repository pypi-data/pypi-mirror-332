"""
Python module generated from Java source file org.bukkit.entity.Vex

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Vex(Monster):
    """
    Represents a Vex.
    """

    def isCharging(self) -> bool:
        """
        Gets the charging state of this entity.
        
        When this entity is charging it will having a glowing red texture.

        Returns
        - charging state
        """
        ...


    def setCharging(self, charging: bool) -> None:
        """
        Sets the charging state of this entity.
        
        When this entity is charging it will having a glowing red texture.

        Arguments
        - charging: new state
        """
        ...


    def getBound(self) -> "Location":
        """
        Gets the bound of this entity.
        
        An idle vex will navigate a 15x11x15 area centered around its bound
        location.
        
        When summoned by an Evoker, this location will be set to that of the
        summoner.

        Returns
        - Location of the bound or null if not set
        """
        ...


    def setBound(self, location: "Location") -> None:
        """
        Sets the bound of this entity.
        
        An idle vex will navigate a 15x11x15 area centered around its bound
        location.
        
        When summoned by an Evoker, this location will be set to that of the
        summoner.

        Arguments
        - location: Location of the bound or null to clear
        """
        ...


    def getLifeTicks(self) -> int:
        """
        Gets the remaining lifespan of this entity.

        Returns
        - life in ticks
        """
        ...


    def setLifeTicks(self, lifeTicks: int) -> None:
        """
        Sets the remaining lifespan of this entity.

        Arguments
        - lifeTicks: life in ticks, or negative for unlimited lifepan
        """
        ...


    def hasLimitedLife(self) -> bool:
        """
        Gets if the entity has a limited life.

        Returns
        - True if the entity has limited life
        """
        ...
