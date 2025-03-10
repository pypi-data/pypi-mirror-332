"""
Python module generated from Java source file org.bukkit.entity.AbstractHorse

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory import AbstractHorseInventory
from org.bukkit.inventory import InventoryHolder
from typing import Any, Callable, Iterable, Tuple


class AbstractHorse(Vehicle, InventoryHolder, Tameable):
    """
    Represents a Horse-like creature.
    """

    def getVariant(self) -> "Horse.Variant":
        """
        Gets the horse's variant.
        
        A horse's variant defines its physical appearance and capabilities.
        Whether a horse is a regular horse, donkey, mule, or other kind of horse
        is determined using the variant.

        Returns
        - a Horse.Variant representing the horse's variant

        Deprecated
        - different variants are different classes
        """
        ...


    def setVariant(self, variant: "Horse.Variant") -> None:
        """
        Arguments
        - variant: variant

        Deprecated
        - you are required to spawn a different entity
        """
        ...


    def getDomestication(self) -> int:
        """
        Gets the domestication level of this horse.
        
        A higher domestication level indicates that the horse is closer to
        becoming tame. As the domestication level gets closer to the max
        domestication level, the chance of the horse becoming tame increases.

        Returns
        - domestication level
        """
        ...


    def setDomestication(self, level: int) -> None:
        """
        Sets the domestication level of this horse.
        
        Setting the domestication level to a high value will increase the
        horse's chances of becoming tame.
        
        Domestication level must be greater than zero and no greater than
        the max domestication level of the horse, determined with
        .getMaxDomestication()

        Arguments
        - level: domestication level
        """
        ...


    def getMaxDomestication(self) -> int:
        """
        Gets the maximum domestication level of this horse.
        
        The higher this level is, the longer it will likely take
        for the horse to be tamed.

        Returns
        - the max domestication level
        """
        ...


    def setMaxDomestication(self, level: int) -> None:
        """
        Sets the maximum domestication level of this horse.
        
        Setting a higher max domestication will increase the amount of
        domesticating (feeding, riding, etc.) necessary in order to tame it,
        while setting a lower max value will have the opposite effect.
        
        Maximum domestication must be greater than zero.

        Arguments
        - level: the max domestication level
        """
        ...


    def getJumpStrength(self) -> float:
        """
        Gets the jump strength of this horse.
        
        Jump strength defines how high the horse can jump. A higher jump strength
        increases how high a jump will go.

        Returns
        - the horse's jump strength
        """
        ...


    def setJumpStrength(self, strength: float) -> None:
        """
        Sets the jump strength of this horse.
        
        A higher jump strength increases how high a jump will go.
        Setting a jump strength to 0 will result in no jump.
        You cannot set a jump strength to a value below 0 or
        above 2.

        Arguments
        - strength: jump strength for this horse
        """
        ...


    def isEatingHaystack(self) -> bool:
        """
        Gets whether the horse is currently grazing hay.

        Returns
        - True if eating hay
        """
        ...


    def setEatingHaystack(self, eatingHaystack: bool) -> None:
        """
        Sets whether the horse is grazing hay.

        Arguments
        - eatingHaystack: new hay grazing status
        """
        ...


    def getInventory(self) -> "AbstractHorseInventory":
        ...
