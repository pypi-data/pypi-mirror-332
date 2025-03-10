"""
Python module generated from Java source file org.bukkit.entity.Fireball

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class Fireball(Projectile, Explosive):
    """
    Represents a Fireball.
    """

    def setDirection(self, direction: "Vector") -> None:
        """
        Fireballs fly straight and do not take setVelocity(...) well.

        Arguments
        - direction: the direction this fireball is flying toward
        """
        ...


    def getDirection(self) -> "Vector":
        """
        Retrieve the direction this fireball is heading toward

        Returns
        - the direction
        """
        ...
