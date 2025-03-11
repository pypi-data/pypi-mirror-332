"""
Python module generated from Java source file org.bukkit.entity.Parrot

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Parrot(Tameable, Sittable):
    """
    Represents a Parrot.
    """

    def getVariant(self) -> "Variant":
        """
        Get the variant of this parrot.

        Returns
        - parrot variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this parrot.

        Arguments
        - variant: parrot variant
        """
        ...


    def isDancing(self) -> bool:
        """
        Gets whether a parrot is dancing

        Returns
        - Whether the parrot is dancing
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a parrot - ie its color.
        """

        RED = 0
        """
        Classic parrot - red with colored wingtips.
        """
        BLUE = 1
        """
        Royal blue colored parrot.
        """
        GREEN = 2
        """
        Green colored parrot.
        """
        CYAN = 3
        """
        Cyan colored parrot.
        """
        GRAY = 4
        """
        Gray colored parrot.
        """
