"""
Python module generated from Java source file org.bukkit.Art

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Locale
from org.bukkit import *
from org.bukkit.packs import DataPack
from org.bukkit.util import OldEnum
from typing import Any, Callable, Iterable, Tuple


class Art(OldEnum, Keyed):
    """
    Represents the art on a painting.
    
    The arts listed in this interface are present in the default server
    or can be enabled via a FeatureFlag.
    There may be additional arts present in the server, for example from a DataPack
    which can be accessed via Registry.ART.
    """

    KEBAB = getArt("kebab")
    AZTEC = getArt("aztec")
    ALBAN = getArt("alban")
    AZTEC2 = getArt("aztec2")
    BOMB = getArt("bomb")
    PLANT = getArt("plant")
    WASTELAND = getArt("wasteland")
    POOL = getArt("pool")
    COURBET = getArt("courbet")
    SEA = getArt("sea")
    SUNSET = getArt("sunset")
    CREEBET = getArt("creebet")
    WANDERER = getArt("wanderer")
    GRAHAM = getArt("graham")
    MATCH = getArt("match")
    BUST = getArt("bust")
    STAGE = getArt("stage")
    VOID = getArt("void")
    SKULL_AND_ROSES = getArt("skull_and_roses")
    WITHER = getArt("wither")
    FIGHTERS = getArt("fighters")
    POINTER = getArt("pointer")
    PIGSCENE = getArt("pigscene")
    BURNING_SKULL = getArt("burning_skull")
    SKELETON = getArt("skeleton")
    DONKEY_KONG = getArt("donkey_kong")
    EARTH = getArt("earth")
    WIND = getArt("wind")
    WATER = getArt("water")
    FIRE = getArt("fire")
    BAROQUE = getArt("baroque")
    HUMBLE = getArt("humble")
    MEDITATIVE = getArt("meditative")
    PRAIRIE_RIDE = getArt("prairie_ride")
    UNPACKED = getArt("unpacked")
    BACKYARD = getArt("backyard")
    BOUQUET = getArt("bouquet")
    CAVEBIRD = getArt("cavebird")
    CHANGING = getArt("changing")
    COTAN = getArt("cotan")
    ENDBOSS = getArt("endboss")
    FERN = getArt("fern")
    FINDING = getArt("finding")
    LOWMIST = getArt("lowmist")
    ORB = getArt("orb")
    OWLEMONS = getArt("owlemons")
    PASSAGE = getArt("passage")
    POND = getArt("pond")
    SUNFLOWERS = getArt("sunflowers")
    TIDES = getArt("tides")


    @staticmethod
    def getArt(key: str) -> "Art":
        ...


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
        
        This ignores capitalization

        Arguments
        - name: The name

        Returns
        - The painting

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def valueOf(name: str) -> "Art":
        """
        Arguments
        - name: of the art.

        Returns
        - the art with the given name.

        Deprecated
        - only for backwards compatibility, use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> list["Art"]:
        """
        Returns
        - an array of all known arts.

        Deprecated
        - use Registry.iterator().
        """
        ...
