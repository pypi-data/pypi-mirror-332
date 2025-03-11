"""
Python module generated from Java source file org.bukkit.entity.Wolf

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.entity import *
from org.bukkit.registry import RegistryAware
from typing import Any, Callable, Iterable, Tuple


class Wolf(Tameable, Sittable):
    """
    Represents a Wolf
    """

    def isAngry(self) -> bool:
        """
        Checks if this wolf is angry

        Returns
        - Anger True if angry
        """
        ...


    def setAngry(self, angry: bool) -> None:
        """
        Sets the anger of this wolf.
        
        An angry wolf can not be fed or tamed.

        Arguments
        - angry: True if angry

        See
        - .setTarget(org.bukkit.entity.LivingEntity)
        """
        ...


    def getCollarColor(self) -> "DyeColor":
        """
        Get the collar color of this wolf

        Returns
        - the color of the collar
        """
        ...


    def setCollarColor(self, color: "DyeColor") -> None:
        """
        Set the collar color of this wolf

        Arguments
        - color: the color to apply
        """
        ...


    def isWet(self) -> bool:
        """
        Gets whether the wolf is wet

        Returns
        - Whether the wolf is wet
        """
        ...


    def getTailAngle(self) -> float:
        """
        Gets the wolf's tail angle in radians

        Returns
        - The angle of the wolf's tail in radians
        """
        ...


    def isInterested(self) -> bool:
        """
        Gets if the wolf is interested

        Returns
        - Whether the wolf is interested
        """
        ...


    def setInterested(self, interested: bool) -> None:
        """
        Set wolf to be interested

        Arguments
        - interested: Whether the wolf is interested
        """
        ...


    def getVariant(self) -> "Variant":
        """
        Get the variant of this wolf.

        Returns
        - wolf variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this wolf.

        Arguments
        - variant: wolf variant
        """
        ...
