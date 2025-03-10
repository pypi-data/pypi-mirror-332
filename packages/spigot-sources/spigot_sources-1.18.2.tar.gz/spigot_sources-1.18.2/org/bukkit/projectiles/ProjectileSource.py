"""
Python module generated from Java source file org.bukkit.projectiles.ProjectileSource

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Projectile
from org.bukkit.projectiles import *
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class ProjectileSource:
    """
    Represents a valid source of a projectile.
    """

    def launchProjectile(self, projectile: type["T"]) -> "T":
        """
        Launches a Projectile from the ProjectileSource.
        
        Type `<T>`: a projectile subclass

        Arguments
        - projectile: class of the projectile to launch

        Returns
        - the launched projectile
        """
        ...


    def launchProjectile(self, projectile: type["T"], velocity: "Vector") -> "T":
        """
        Launches a Projectile from the ProjectileSource with an
        initial velocity.
        
        Type `<T>`: a projectile subclass

        Arguments
        - projectile: class of the projectile to launch
        - velocity: the velocity with which to launch

        Returns
        - the launched projectile
        """
        ...
