"""
Python module generated from Java source file org.bukkit.WorldType

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class WorldType(Enum):
    """
    Represents various types of worlds that may exist
    """

    NORMAL = ("DEFAULT")
    FLAT = ("FLAT")
    LARGE_BIOMES = ("LARGEBIOMES")
    AMPLIFIED = ("AMPLIFIED")


    def getName(self) -> str:
        """
        Gets the name of this WorldType

        Returns
        - Name of this type
        """
        ...


    @staticmethod
    def getByName(name: str) -> "WorldType":
        """
        Gets a WorldType by its name

        Arguments
        - name: Name of the WorldType to get

        Returns
        - Requested WorldType, or null if not found
        """
        ...
