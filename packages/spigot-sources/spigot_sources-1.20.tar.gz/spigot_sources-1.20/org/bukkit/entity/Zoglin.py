"""
Python module generated from Java source file org.bukkit.entity.Zoglin

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Zoglin(Monster, Ageable):
    """
    Represents a Zoglin.
    """

    def isBaby(self) -> bool:
        """
        Gets whether the zoglin is a baby

        Returns
        - Whether the zoglin is a baby

        Deprecated
        - see Ageable.isAdult()
        """
        ...


    def setBaby(self, flag: bool) -> None:
        """
        Sets whether the zoglin is a baby

        Arguments
        - flag: Whether the zoglin is a baby

        Deprecated
        - see Ageable.setBaby() and Ageable.setAdult()
        """
        ...
