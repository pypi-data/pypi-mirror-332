"""
Python module generated from Java source file org.bukkit.entity.Wolf

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit.entity import *
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
