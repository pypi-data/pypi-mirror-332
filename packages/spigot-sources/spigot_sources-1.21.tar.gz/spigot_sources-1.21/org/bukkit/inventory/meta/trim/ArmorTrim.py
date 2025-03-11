"""
Python module generated from Java source file org.bukkit.inventory.meta.trim.ArmorTrim

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Objects
from org.bukkit.inventory.meta import ArmorMeta
from org.bukkit.inventory.meta.trim import *
from typing import Any, Callable, Iterable, Tuple


class ArmorTrim:
    """
    Represents an armor trim that may be applied to an item.

    See
    - ArmorMeta.setTrim(ArmorTrim)
    """

    def __init__(self, material: "TrimMaterial", pattern: "TrimPattern"):
        """
        Create a new ArmorTrim given a TrimMaterial and
        TrimPattern.

        Arguments
        - material: the material
        - pattern: the pattern
        """
        ...


    def getMaterial(self) -> "TrimMaterial":
        """
        Get the TrimMaterial for this armor trim.

        Returns
        - the material
        """
        ...


    def getPattern(self) -> "TrimPattern":
        """
        Get the TrimPattern for this armor trim.

        Returns
        - the pattern
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
