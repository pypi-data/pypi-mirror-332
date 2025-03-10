"""
Python module generated from Java source file org.bukkit.entity.Ageable

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Ageable(Creature):
    """
    Represents an entity that can age.
    """

    def getAge(self) -> int:
        """
        Gets the age of this mob.

        Returns
        - Age
        """
        ...


    def setAge(self, age: int) -> None:
        """
        Sets the age of this mob.

        Arguments
        - age: New age
        """
        ...


    def setAgeLock(self, lock: bool) -> None:
        """
        Lock the age of the animal, setting this will prevent the animal from
        maturing or getting ready for mating.

        Arguments
        - lock: new lock

        Deprecated
        - see Breedable.setAgeLock(boolean)
        """
        ...


    def getAgeLock(self) -> bool:
        """
        Gets the current agelock.

        Returns
        - the current agelock

        Deprecated
        - see Breedable.getAgeLock()
        """
        ...


    def setBaby(self) -> None:
        """
        Sets the age of the mob to a baby
        """
        ...


    def setAdult(self) -> None:
        """
        Sets the age of the mob to an adult
        """
        ...


    def isAdult(self) -> bool:
        """
        Returns True if the mob is an adult.

        Returns
        - return True if the mob is an adult
        """
        ...


    def canBreed(self) -> bool:
        """
        Return the ability to breed of the animal.

        Returns
        - the ability to breed of the animal

        Deprecated
        - see Breedable.canBreed()
        """
        ...


    def setBreed(self, breed: bool) -> None:
        """
        Set breedability of the animal, if the animal is a baby and set to
        breed it will instantly grow up.

        Arguments
        - breed: breedability of the animal

        Deprecated
        - see Breedable.setBreed(boolean)
        """
        ...
