"""
Python module generated from Java source file org.bukkit.entity.Camel

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MinecraftExperimental
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Camel(AbstractHorse, Sittable):
    """
    Represents a Camel.

    Unknown Tags
    - This entity is part of an experimental feature of Minecraft and
    hence subject to change.
    """

    def isDashing(self) -> bool:
        """
        Gets whether this camel is dashing (sprinting).

        Returns
        - dashing status
        """
        ...


    def setDashing(self, dashing: bool) -> None:
        """
        Sets whether this camel is dashing (sprinting).

        Arguments
        - dashing: new dashing status
        """
        ...
