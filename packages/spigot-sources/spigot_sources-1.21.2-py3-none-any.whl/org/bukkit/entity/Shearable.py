"""
Python module generated from Java source file org.bukkit.entity.Shearable

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Shearable:
    """
    Represents an entity which can be shorn with shears.
    """

    def isSheared(self) -> bool:
        """
        Gets whether the entity is in its sheared state.

        Returns
        - Whether the entity is sheared.
        """
        ...


    def setSheared(self, flag: bool) -> None:
        """
        Sets whether the entity is in its sheared state.

        Arguments
        - flag: Whether to shear the entity
        """
        ...
