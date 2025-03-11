"""
Python module generated from Java source file org.bukkit.Art

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Maps
from enum import Enum
from java.util import Locale
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
    EARTH = (26, 2, 2)
    WIND = (27, 2, 2)
    WATER = (28, 2, 2)
    FIRE = (29, 2, 2)
    BAROQUE = (30, 2, 2)
    HUMBLE = (31, 2, 2)
    MEDITATIVE = (32, 1, 1)
    PRAIRIE_RIDE = (33, 1, 2)
    UNPACKED = (34, 4, 4)
    BACKYARD = (35, 3, 4)
    BOUQUET = (36, 3, 3)
    CAVEBIRD = (37, 3, 3)
    CHANGING = (38, 4, 2)
    COTAN = (39, 3, 3)
    ENDBOSS = (40, 3, 3)
    FERN = (41, 3, 3)
    FINDING = (42, 4, 2)
    LOWMIST = (43, 4, 2)
    ORB = (44, 4, 4)
    OWLEMONS = (45, 3, 3)
    PASSAGE = (46, 4, 2)
    POND = (47, 3, 4)
    SUNFLOWERS = (48, 3, 3)
    TIDES = (49, 3, 3)


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
