"""
Python module generated from Java source file org.bukkit.entity.Steerable

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Steerable(Animals):
    """
    Represents an entity which may be saddled, ridden and steered using an item.
    """

    def hasSaddle(self) -> bool:
        """
        Check if the pig has a saddle.

        Returns
        - if the pig has been saddled.
        """
        ...


    def setSaddle(self, saddled: bool) -> None:
        """
        Sets if the pig has a saddle or not

        Arguments
        - saddled: set if the pig has a saddle or not.
        """
        ...


    def getBoostTicks(self) -> int:
        """
        Get the time in ticks this entity's movement is being increased.
        
        Movement speed is often increased as a result of using the
        .getSteerMaterial().

        Returns
        - the current boost ticks
        """
        ...


    def setBoostTicks(self, ticks: int) -> None:
        """
        Set the time in ticks this entity's movement will be increased.
        
        This will reset the current boost ticks to 0
        (.getCurrentBoostTicks()).

        Arguments
        - ticks: the boost time
        """
        ...


    def getCurrentBoostTicks(self) -> int:
        """
        Get the time in ticks this entity's movement has been increased as of the
        most recent boost.
        
        Current boost ticks will never be > .getBoostTicks().

        Returns
        - the current boost ticks
        """
        ...


    def setCurrentBoostTicks(self, ticks: int) -> None:
        """
        Set the time in ticks this entity's movement has been increased relative
        to the most recent boost.

        Arguments
        - ticks: the current boost ticks. Must be >= 0 and <=
        .getBoostTicks()
        """
        ...


    def getSteerMaterial(self) -> "Material":
        """
        Get the material used to steer this entity when ridden by a player.

        Returns
        - the lure material
        """
        ...
