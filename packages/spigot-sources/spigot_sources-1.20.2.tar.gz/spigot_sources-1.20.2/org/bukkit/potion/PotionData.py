"""
Python module generated from Java source file org.bukkit.potion.PotionData

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.potion import *
from typing import Any, Callable, Iterable, Tuple


class PotionData:
    """
    Deprecated
    - Upgraded / extended potions are now their own PotionType use them instead.
    """

    def __init__(self, type: "PotionType", extended: bool, upgraded: bool):
        """
        Instantiates a final PotionData object to contain information about a
        Potion

        Arguments
        - type: the type of the Potion
        - extended: whether the potion is extended PotionType#isExtendable()
        must be True
        - upgraded: whether the potion is upgraded PotionType#isUpgradable()
        must be True
        """
        ...


    def __init__(self, type: "PotionType"):
        ...


    def getType(self) -> "PotionType":
        """
        Gets the type of the potion, Type matches up with each kind of craftable
        potion

        Returns
        - the potion type
        """
        ...


    def isUpgraded(self) -> bool:
        """
        Checks if the potion is in an upgraded state. This refers to whether or
        not the potion is Tier 2, such as Potion of Fire Resistance II.

        Returns
        - True if the potion is upgraded;
        """
        ...


    def isExtended(self) -> bool:
        """
        Checks if the potion is in an extended state. This refers to the extended
        duration potions

        Returns
        - True if the potion is extended
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...
