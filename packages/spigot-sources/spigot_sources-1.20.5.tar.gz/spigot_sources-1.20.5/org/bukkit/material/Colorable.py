"""
Python module generated from Java source file org.bukkit.material.Colorable

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import DyeColor
from org.bukkit import UndefinedNullability
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Colorable:
    """
    An object that can be colored.
    """

    def getColor(self) -> "DyeColor":
        """
        Gets the color of this object.
        
        This may be null to represent the default color of an object, if the
        object has a special default color (e.g Shulkers).

        Returns
        - The DyeColor of this object.
        """
        ...


    def setColor(self, color: "DyeColor") -> None:
        """
        Sets the color of this object to the specified DyeColor.
        
        This may be null to represent the default color of an object, if the
        object has a special default color (e.g Shulkers).

        Arguments
        - color: The color of the object, as a DyeColor.

        Raises
        - NullPointerException: if argument is null and this implementation does not support null
        """
        ...
