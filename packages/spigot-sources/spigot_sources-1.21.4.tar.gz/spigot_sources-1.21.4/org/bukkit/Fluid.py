"""
Python module generated from Java source file org.bukkit.Fluid

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import *
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Fluid(OldEnum, Keyed, RegistryAware):
    """
    Represents a fluid type.
    """

    EMPTY = getFluid("empty")
    """
    No fluid.
    """
    WATER = getFluid("water")
    """
    Stationary water.
    """
    FLOWING_WATER = getFluid("flowing_water")
    """
    Flowing water.
    """
    LAVA = getFluid("lava")
    """
    Stationary lava.
    """
    FLOWING_LAVA = getFluid("flowing_lava")
    """
    Flowing lava.
    """


    @staticmethod
    def getFluid(key: str) -> "Fluid":
        ...


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...


    @staticmethod
    def valueOf(name: str) -> "Fluid":
        """
        Arguments
        - name: of the fluid.

        Returns
        - the fluid with the given name.

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["Fluid"]:
        """
        Returns
        - an array of all known fluids.

        Deprecated
        - use Registry.iterator().
        """
        ...
