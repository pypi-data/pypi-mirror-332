"""
Python module generated from Java source file org.bukkit.entity.Goat

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Goat(Animals):
    """
    A Goat.
    """

    def hasLeftHorn(self) -> bool:
        """
        Gets if this goat has its left horn.

        Returns
        - left horn status
        """
        ...


    def setLeftHorn(self, hasHorn: bool) -> None:
        """
        Sets if this goat has its left horn.

        Arguments
        - hasHorn: left horn status
        """
        ...


    def hasRightHorn(self) -> bool:
        """
        Gets if this goat has its right horn.

        Returns
        - right horn status
        """
        ...


    def setRightHorn(self, hasHorn: bool) -> None:
        """
        Sets if this goat has its right horn.

        Arguments
        - hasHorn: right horn status
        """
        ...


    def isScreaming(self) -> bool:
        """
        Gets if this is a screaming goat.
        
        A screaming goat makes screaming sounds and rams more often. They do not
        offer home loans.

        Returns
        - screaming status
        """
        ...


    def setScreaming(self, screaming: bool) -> None:
        """
        Sets if this is a screaming goat.
        
        A screaming goat makes screaming sounds and rams more often. They do not
        offer home loans.

        Arguments
        - screaming: screaming status
        """
        ...
