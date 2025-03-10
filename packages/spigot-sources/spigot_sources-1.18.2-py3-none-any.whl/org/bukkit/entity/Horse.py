"""
Python module generated from Java source file org.bukkit.entity.Horse

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import *
from org.bukkit.inventory import HorseInventory
from typing import Any, Callable, Iterable, Tuple


class Horse(AbstractHorse):
    """
    Represents a Horse.
    """

    def getColor(self) -> "Color":
        """
        Gets the horse's color.
        
        Colors only apply to horses, not to donkeys, mules, skeleton horses
        or undead horses.

        Returns
        - a Color representing the horse's group
        """
        ...


    def setColor(self, color: "Color") -> None:
        """
        Sets the horse's color.
        
        Attempting to set a color for any donkey, mule, skeleton horse or
        undead horse will not result in a change.

        Arguments
        - color: a Color for this horse
        """
        ...


    def getStyle(self) -> "Style":
        """
        Gets the horse's style.
        Styles determine what kind of markings or patterns a horse has.
        
        Styles only apply to horses, not to donkeys, mules, skeleton horses
        or undead horses.

        Returns
        - a Style representing the horse's style
        """
        ...


    def setStyle(self, style: "Style") -> None:
        """
        Sets the style of this horse.
        Styles determine what kind of markings or patterns a horse has.
        
        Attempting to set a style for any donkey, mule, skeleton horse or
        undead horse will not result in a change.

        Arguments
        - style: a Style for this horse
        """
        ...


    def isCarryingChest(self) -> bool:
        """
        Returns
        - carrying chest status

        Deprecated
        - see ChestedHorse
        """
        ...


    def setCarryingChest(self, chest: bool) -> None:
        """
        Arguments
        - chest: chest

        Deprecated
        - see ChestedHorse
        """
        ...


    def getInventory(self) -> "HorseInventory":
        ...


    class Variant(Enum):
        """
        Deprecated
        - different variants are differing classes
        """

        HORSE = 0
        """
        A normal horse
        """
        DONKEY = 1
        """
        A donkey
        """
        MULE = 2
        """
        A mule
        """
        UNDEAD_HORSE = 3
        """
        An undead horse
        """
        SKELETON_HORSE = 4
        """
        A skeleton horse
        """
        LLAMA = 5
        """
        Not really a horse :)
        """


    class Color(Enum):
        """
        Represents the base color that the horse has.
        """

        WHITE = 0
        """
        Snow white
        """
        CREAMY = 1
        """
        Very light brown
        """
        CHESTNUT = 2
        """
        Chestnut
        """
        BROWN = 3
        """
        Light brown
        """
        BLACK = 4
        """
        Pitch black
        """
        GRAY = 5
        """
        Gray
        """
        DARK_BROWN = 6
        """
        Dark brown
        """


    class Style(Enum):
        """
        Represents the style, or markings, that the horse has.
        """

        NONE = 0
        """
        No markings
        """
        WHITE = 1
        """
        White socks or stripes
        """
        WHITEFIELD = 2
        """
        Milky splotches
        """
        WHITE_DOTS = 3
        """
        Round white dots
        """
        BLACK_DOTS = 4
        """
        Small black dots
        """
