"""
Python module generated from Java source file org.bukkit.entity.Axolotl

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Axolotl(Animals):
    """
    An Axolotl.
    """

    def isPlayingDead(self) -> bool:
        """
        Gets if this axolotl is playing dead.
        
        An axolotl may play dead when it is damaged underwater.

        Returns
        - playing dead status
        """
        ...


    def setPlayingDead(self, playingDead: bool) -> None:
        """
        Sets if this axolotl is playing dead.
        
        An axolotl may play dead when it is damaged underwater.

        Arguments
        - playingDead: playing dead status
        """
        ...


    def getVariant(self) -> "Variant":
        """
        Get the variant of this axolotl.

        Returns
        - axolotl variant
        """
        ...


    def setVariant(self, variant: "Variant") -> None:
        """
        Set the variant of this axolotl.

        Arguments
        - variant: axolotl variant
        """
        ...


    class Variant(Enum):
        """
        Represents the variant of a axolotl - ie its color.
        """

        LUCY = 0
        """
        Leucistic (pink) axolotl.
        """
        WILD = 1
        """
        Brown axolotl.
        """
        GOLD = 2
        """
        Gold axolotl.
        """
        CYAN = 3
        """
        Cyan axolotl.
        """
        BLUE = 4
        """
        Blue axolotl.
        """
