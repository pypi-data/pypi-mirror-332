"""
Python module generated from Java source file org.bukkit.Instrument

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Instrument(Enum):

    PIANO = (0x0)
    """
    Piano is the standard instrument for a note block.
    """
    BASS_DRUM = (0x1)
    """
    Bass drum is normally played when a note block is on top of a
    stone-like block.
    """
    SNARE_DRUM = (0x2)
    """
    Snare drum is normally played when a note block is on top of a sandy
    block.
    """
    STICKS = (0x3)
    """
    Sticks are normally played when a note block is on top of a glass
    block.
    """
    BASS_GUITAR = (0x4)
    """
    Bass guitar is normally played when a note block is on top of a wooden
    block.
    """
    FLUTE = (0x5)
    """
    Flute is normally played when a note block is on top of a clay block.
    """
    BELL = (0x6)
    """
    Bell is normally played when a note block is on top of a gold block.
    """
    GUITAR = (0x7)
    """
    Guitar is normally played when a note block is on top of a woolen block.
    """
    CHIME = (0x8)
    """
    Chime is normally played when a note block is on top of a packed ice
    block.
    """
    XYLOPHONE = (0x9)
    """
    Xylophone is normally played when a note block is on top of a bone block.
    """
    IRON_XYLOPHONE = (0xA)
    """
    Iron Xylophone is normally played when a note block is on top of a iron block.
    """
    COW_BELL = (0xB)
    """
    Cow Bell is normally played when a note block is on top of a soul sand block.
    """
    DIDGERIDOO = (0xC)
    """
    Didgeridoo is normally played when a note block is on top of a pumpkin block.
    """
    BIT = (0xD)
    """
    Bit is normally played when a note block is on top of a emerald block.
    """
    BANJO = (0xE)
    """
    Banjo is normally played when a note block is on top of a hay block.
    """
    PLING = (0xF)
    """
    Pling is normally played when a note block is on top of a glowstone block.
    """


    def getType(self) -> int:
        """
        Returns
        - The type ID of this instrument.

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getByType(type: int) -> "Instrument":
        """
        Get an instrument by its type ID.

        Arguments
        - type: The type ID

        Returns
        - The instrument

        Deprecated
        - Magic value
        """
        ...
