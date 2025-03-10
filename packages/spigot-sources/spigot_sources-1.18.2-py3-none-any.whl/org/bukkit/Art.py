"""
Python module generated from Java source file org.bukkit.Art

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.apache.commons.lang import Validate
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Art(Enum):
    """
    Represents the art on a painting
    """

    KEBAB = (0, 1, 1)
    AZTEC = (1, 1, 1)
    ALBAN = (2, 1, 1)
    AZTEC2 = (3, 1, 1)
    BOMB = (4, 1, 1)
    PLANT = (5, 1, 1)
    WASTELAND = (6, 1, 1)
    POOL = (7, 2, 1)
    COURBET = (8, 2, 1)
    SEA = (9, 2, 1)
    SUNSET = (10, 2, 1)
    CREEBET = (11, 2, 1)
    WANDERER = (12, 1, 2)
    GRAHAM = (13, 1, 2)
    MATCH = (14, 2, 2)
    BUST = (15, 2, 2)
    STAGE = (16, 2, 2)
    VOID = (17, 2, 2)
    SKULL_AND_ROSES = (18, 2, 2)
    WITHER = (19, 2, 2)
    FIGHTERS = (20, 4, 2)
    POINTER = (21, 4, 4)
    PIGSCENE = (22, 4, 4)
    BURNING_SKULL = (23, 4, 4)
    SKELETON = (24, 4, 3)
    DONKEY_KONG = (25, 4, 3)


    def getBlockWidth(self) -> int:
        """
        Gets the width of the painting, in blocks

        Returns
        - The width of the painting, in blocks
        """
        ...


    def getBlockHeight(self) -> int:
        """
        Gets the height of the painting, in blocks

        Returns
        - The height of the painting, in blocks
        """
        ...


    def getId(self) -> int:
        """
        Get the ID of this painting.

        Returns
        - The ID of this painting

        Deprecated
        - Magic value
        """
        ...


    def getKey(self) -> "NamespacedKey":
        ...


    @staticmethod
    def getById(id: int) -> "Art":
        """
        Get a painting by its numeric ID

        Arguments
        - id: The ID

        Returns
        - The painting

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByName(name: str) -> "Art":
        """
        Get a painting by its unique name
        
        This ignores underscores and capitalization

        Arguments
        - name: The name

        Returns
        - The painting
        """
        ...
