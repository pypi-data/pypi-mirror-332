"""
Python module generated from Java source file org.bukkit.entity.ShulkerBullet

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ShulkerBullet(Projectile):

    def getTarget(self) -> "Entity":
        """
        Retrieve the target of this bullet.

        Returns
        - the targeted entity
        """
        ...


    def setTarget(self, target: "Entity") -> None:
        """
        Sets the target of this bullet

        Arguments
        - target: the entity to target
        """
        ...
