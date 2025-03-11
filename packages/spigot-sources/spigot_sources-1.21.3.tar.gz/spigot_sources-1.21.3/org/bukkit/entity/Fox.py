"""
Python module generated from Java source file org.bukkit.entity.Fox

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Fox(Animals, Sittable):
    """
    What does the fox say?
    """

    def getFoxType(self) -> "Type":
        """
        Gets the current type of this fox.

        Returns
        - Type of the fox.
        """
        ...


    def setFoxType(self, type: "Type") -> None:
        """
        Sets the current type of this fox.

        Arguments
        - type: New type of this fox.
        """
        ...


    def isCrouching(self) -> bool:
        """
        Checks if this animal is crouching

        Returns
        - True if crouching
        """
        ...


    def setCrouching(self, crouching: bool) -> None:
        """
        Sets if this animal is crouching.

        Arguments
        - crouching: True if crouching
        """
        ...


    def setSleeping(self, sleeping: bool) -> None:
        """
        Sets if this animal is sleeping.

        Arguments
        - sleeping: True if sleeping
        """
        ...


    def getFirstTrustedPlayer(self) -> "AnimalTamer":
        """
        Gets the first trusted player.

        Returns
        - the owning AnimalTamer, or null if not owned
        """
        ...


    def setFirstTrustedPlayer(self, player: "AnimalTamer") -> None:
        """
        Set the first trusted player.
        
        The first trusted player may only be removed after the second.

        Arguments
        - player: the AnimalTamer to be trusted
        """
        ...


    def getSecondTrustedPlayer(self) -> "AnimalTamer":
        """
        Gets the second trusted player.

        Returns
        - the owning AnimalTamer, or null if not owned
        """
        ...


    def setSecondTrustedPlayer(self, player: "AnimalTamer") -> None:
        """
        Set the second trusted player.
        
        The second trusted player may only be added after the first.

        Arguments
        - player: the AnimalTamer to be trusted
        """
        ...


    def isFaceplanted(self) -> bool:
        """
        Gets whether the fox is faceplanting the ground

        Returns
        - Whether the fox is faceplanting the ground
        """
        ...


    class Type(Enum):
        """
        Represents the various different fox types there are.
        """

        RED = 0
        SNOW = 1
