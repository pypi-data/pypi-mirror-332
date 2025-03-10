"""
Python module generated from Java source file org.bukkit.entity.Breedable

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Breedable(Ageable):
    """
    Represents an entity that can age and breed.
    """

    def setAgeLock(self, lock: bool) -> None:
        """
        Lock the age of the animal, setting this will prevent the animal from
        maturing or getting ready for mating.

        Arguments
        - lock: new lock
        """
        ...


    def getAgeLock(self) -> bool:
        """
        Gets the current agelock.

        Returns
        - the current agelock
        """
        ...


    def canBreed(self) -> bool:
        """
        Return the ability to breed of the animal.

        Returns
        - the ability to breed of the animal
        """
        ...


    def setBreed(self, breed: bool) -> None:
        """
        Set breedability of the animal, if the animal is a baby and set to
        breed it will instantly grow up.

        Arguments
        - breed: breedability of the animal
        """
        ...
