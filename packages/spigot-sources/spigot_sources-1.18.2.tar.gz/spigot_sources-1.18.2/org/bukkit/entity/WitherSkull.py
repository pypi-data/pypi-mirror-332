"""
Python module generated from Java source file org.bukkit.entity.WitherSkull

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class WitherSkull(Fireball):
    """
    Represents a wither skull Fireball.
    """

    def setCharged(self, charged: bool) -> None:
        """
        Sets the charged status of the wither skull.

        Arguments
        - charged: whether it should be charged
        """
        ...


    def isCharged(self) -> bool:
        """
        Gets whether or not the wither skull is charged.

        Returns
        - whether the wither skull is charged
        """
        ...
