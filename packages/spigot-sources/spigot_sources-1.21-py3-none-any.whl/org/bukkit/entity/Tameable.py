"""
Python module generated from Java source file org.bukkit.entity.Tameable

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Tameable(Animals):

    def isTamed(self) -> bool:
        """
        Check if this is tamed
        
        If something is tamed then a player can not tame it through normal
        methods, even if it does not belong to anyone in particular.

        Returns
        - True if this has been tamed
        """
        ...


    def setTamed(self, tame: bool) -> None:
        """
        Sets if this has been tamed. Not necessary if the method setOwner has
        been used, as it tames automatically.
        
        If something is tamed then a player can not tame it through normal
        methods, even if it does not belong to anyone in particular.

        Arguments
        - tame: True if tame
        """
        ...


    def getOwner(self) -> "AnimalTamer":
        """
        Gets the current owning AnimalTamer

        Returns
        - the owning AnimalTamer, or null if not owned
        """
        ...


    def setOwner(self, tamer: "AnimalTamer") -> None:
        """
        Set this to be owned by given AnimalTamer.
        
        If the owner is not null, this will be tamed and will have any current
        path it is following removed. If the owner is set to null, this will be
        untamed, and the current owner removed.

        Arguments
        - tamer: the AnimalTamer who should own this
        """
        ...
