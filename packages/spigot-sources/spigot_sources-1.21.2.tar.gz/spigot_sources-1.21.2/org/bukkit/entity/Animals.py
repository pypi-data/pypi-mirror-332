"""
Python module generated from Java source file org.bukkit.entity.Animals

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import Material
from org.bukkit.entity import *
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class Animals(Breedable):
    """
    Represents an Animal.
    """

    def getBreedCause(self) -> "UUID":
        """
        Get the UUID of the entity that caused this entity to enter the
        .canBreed() state.

        Returns
        - uuid if set, or null
        """
        ...


    def setBreedCause(self, uuid: "UUID") -> None:
        """
        Set the UUID of the entity that caused this entity to enter the
        .canBreed() state.

        Arguments
        - uuid: new uuid, or null
        """
        ...


    def isLoveMode(self) -> bool:
        """
        Get whether or not this entity is in love mode and will produce
        offspring with another entity in love mode. Will return True if
        and only if .getLoveModeTicks() is greater than 0.

        Returns
        - True if in love mode, False otherwise
        """
        ...


    def getLoveModeTicks(self) -> int:
        """
        Get the amount of ticks remaining for this entity in love mode.
        If the entity is not in love mode, 0 will be returned.

        Returns
        - the remaining love mode ticks
        """
        ...


    def setLoveModeTicks(self, ticks: int) -> None:
        """
        Set the amount of ticks for which this entity should be in love mode.
        Setting the love mode ticks to 600 is the equivalent of a player
        feeding the entity their breeding item of choice.

        Arguments
        - ticks: the love mode ticks. Must be positive
        """
        ...


    def isBreedItem(self, stack: "ItemStack") -> bool:
        """
        Check if the provided ItemStack is the correct item used for breeding
        this entity.

        Arguments
        - stack: ItemStack to check.

        Returns
        - if the provided ItemStack is the correct food item for this
        entity.
        """
        ...


    def isBreedItem(self, material: "Material") -> bool:
        """
        Check if the provided ItemStack is the correct item used for breeding
        this entity..

        Arguments
        - material: Material to check.

        Returns
        - if the provided ItemStack is the correct food item for this
        entity.
        """
        ...
