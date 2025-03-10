"""
Python module generated from Java source file org.bukkit.entity.Projectile

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from org.bukkit.projectiles import ProjectileSource
from typing import Any, Callable, Iterable, Tuple


class Projectile(Entity):
    """
    Represents a shootable entity.
    """

    def getShooter(self) -> "ProjectileSource":
        """
        Retrieve the shooter of this projectile.

        Returns
        - the ProjectileSource that shot this projectile
        """
        ...


    def setShooter(self, source: "ProjectileSource") -> None:
        """
        Set the shooter of this projectile.

        Arguments
        - source: the ProjectileSource that shot this projectile
        """
        ...


    def doesBounce(self) -> bool:
        """
        Determine if this projectile should bounce or not when it hits.
        
        If a small fireball does not bounce it will set the target on fire.

        Returns
        - True if it should bounce.
        """
        ...


    def setBounce(self, doesBounce: bool) -> None:
        """
        Set whether or not this projectile should bounce or not when it hits
        something.

        Arguments
        - doesBounce: whether or not it should bounce.
        """
        ...
