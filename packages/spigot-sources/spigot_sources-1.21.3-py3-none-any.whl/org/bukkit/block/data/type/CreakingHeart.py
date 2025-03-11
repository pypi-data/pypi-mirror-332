"""
Python module generated from Java source file org.bukkit.block.data.type.CreakingHeart

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import MinecraftExperimental
from org.bukkit.block.data import Orientable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class CreakingHeart(Orientable):
    """
    'creaking' is the creaking status of this block.
    """

    def getCreaking(self) -> "Creaking":
        """
        Gets the value of the 'creaking' property.

        Returns
        - the 'creaking' value
        """
        ...


    def setCreaking(self, creaking: "Creaking") -> None:
        """
        Sets the value of the 'creaking' property.

        Arguments
        - creaking: the new 'creaking' value
        """
        ...


    class Creaking(Enum):
        """
        Creaking status.
        """

        DISABLED = 0
        """
        The block is disabled.
        """
        DORMANT = 1
        """
        The block is dormant.
        """
        ACTIVE = 2
        """
        The block is active.
        """
