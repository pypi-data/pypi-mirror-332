"""
Python module generated from Java source file org.bukkit.entity.Firework

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.inventory.meta import FireworkMeta
from typing import Any, Callable, Iterable, Tuple


class Firework(Projectile):

    def getFireworkMeta(self) -> "FireworkMeta":
        """
        Get a copy of the fireworks meta

        Returns
        - A copy of the current Firework meta
        """
        ...


    def setFireworkMeta(self, meta: "FireworkMeta") -> None:
        """
        Apply the provided meta to the fireworks

        Arguments
        - meta: The FireworkMeta to apply
        """
        ...


    def detonate(self) -> None:
        """
        Cause this firework to explode at earliest opportunity, as if it has no
        remaining fuse.
        """
        ...


    def isShotAtAngle(self) -> bool:
        """
        Gets if the firework was shot at an angle (i.e. from a crossbow).
        
        A firework which was not shot at an angle will fly straight upwards.

        Returns
        - shot at angle status
        """
        ...


    def setShotAtAngle(self, shotAtAngle: bool) -> None:
        """
        Sets if the firework was shot at an angle (i.e. from a crossbow).
        
        A firework which was not shot at an angle will fly straight upwards.

        Arguments
        - shotAtAngle: the new shotAtAngle
        """
        ...
