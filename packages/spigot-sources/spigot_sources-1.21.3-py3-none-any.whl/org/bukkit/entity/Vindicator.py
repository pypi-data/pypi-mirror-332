"""
Python module generated from Java source file org.bukkit.entity.Vindicator

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Vindicator(Illager):
    """
    Represents a Vindicator.
    """

    def isJohnny(self) -> bool:
        """
        Returns whether a vindicator is in "Johnny" mode.
        
        When this mode is active, vindicators will be hostile to all mobs.

        Returns
        - True if johnny
        """
        ...


    def setJohnny(self, johnny: bool) -> None:
        """
        Sets the Johnny state of a vindicator.

        Arguments
        - johnny: new johnny state
        """
        ...
