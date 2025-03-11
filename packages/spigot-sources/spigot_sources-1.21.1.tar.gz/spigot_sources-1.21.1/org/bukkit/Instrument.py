"""
Python module generated from Java source file org.bukkit.Instrument

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import Maps
from enum import Enum
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Instrument(Enum):

    PIANO = (0x0, Sound.BLOCK_NOTE_BLOCK_HARP)
    """
    Piano is the standard instrument for a note block.
    """
    BASS_DRUM = (0x1, Sound.BLOCK_NOTE_BLOCK_BASEDRUM)
    """
    Bass drum is normally played when a note block is on top of a
    stone-like block.
    """
    SNARE_DRUM = (0x2, Sound.BLOCK_NOTE_BLOCK_SNARE)
    """
    Snare drum is normally played when a note block is on top of a sandy
    block.
    """
    STICKS = (0x3, Sound.BLOCK_NOTE_BLOCK_HAT)
    """
    Sticks are normally played when a note block is on top of a glass
    block.
    """
    BASS_GUITAR = (0x4, Sound.BLOCK_NOTE_BLOCK_BASS)
    """
    Bass guitar is normally played when a note block is on top of a wooden
    block.
    """
    FLUTE = (0x5, Sound.BLOCK_NOTE_BLOCK_FLUTE)
    """
    Flute is normally played when a note block is on top of a clay block.
    """
    BELL = (0x6, Sound.BLOCK_NOTE_BLOCK_BELL)
    """
    Bell is normally played when a note block is on top of a gold block.
    """
    GUITAR = (0x7, Sound.BLOCK_NOTE_BLOCK_GUITAR)
    """
    Guitar is normally played when a note block is on top of a woolen block.
    """
    CHIME = (0x8, Sound.BLOCK_NOTE_BLOCK_CHIME)
    """
    Chime is normally played when a note block is on top of a packed ice
    block.
    """
    XYLOPHONE = (0x9, Sound.BLOCK_NOTE_BLOCK_XYLOPHONE)
    """
    Xylophone is normally played when a note block is on top of a bone block.
    """
    IRON_XYLOPHONE = (0xA, Sound.BLOCK_NOTE_BLOCK_IRON_XYLOPHONE)
    """
    Iron Xylophone is normally played when a note block is on top of a iron block.
    """
    COW_BELL = (0xB, Sound.BLOCK_NOTE_BLOCK_COW_BELL)
    """
    Cow Bell is normally played when a note block is on top of a soul sand block.
    """
    DIDGERIDOO = (0xC, Sound.BLOCK_NOTE_BLOCK_DIDGERIDOO)
    """
    Didgeridoo is normally played when a note block is on top of a pumpkin block.
    """
    BIT = (0xD, Sound.BLOCK_NOTE_BLOCK_BIT)
    """
    Bit is normally played when a note block is on top of a emerald block.
    """
    BANJO = (0xE, Sound.BLOCK_NOTE_BLOCK_BANJO)
    """
    Banjo is normally played when a note block is on top of a hay block.
    """
    PLING = (0xF, Sound.BLOCK_NOTE_BLOCK_PLING)
    """
    Pling is normally played when a note block is on top of a glowstone block.
    """
    ZOMBIE = (Sound.BLOCK_NOTE_BLOCK_IMITATE_ZOMBIE)
    """
    Zombie is normally played when a Zombie Head is on top of the note block.
    """
    SKELETON = (Sound.BLOCK_NOTE_BLOCK_IMITATE_SKELETON)
    """
    Skeleton is normally played when a Skeleton Head is on top of the note block.
    """
    CREEPER = (Sound.BLOCK_NOTE_BLOCK_IMITATE_CREEPER)
    """
    Creeper is normally played when a Creeper Head is on top of the note block.
    """
    DRAGON = (Sound.BLOCK_NOTE_BLOCK_IMITATE_ENDER_DRAGON)
    """
    Dragon is normally played when a Dragon Head is on top of the note block.
    """
    WITHER_SKELETON = (Sound.BLOCK_NOTE_BLOCK_IMITATE_WITHER_SKELETON)
    """
    Wither Skeleton is normally played when a Wither Skeleton Head is on top of the note block.
    """
    PIGLIN = (Sound.BLOCK_NOTE_BLOCK_IMITATE_PIGLIN)
    """
    Piglin is normally played when a Piglin Head is on top of the note block.
    """
    CUSTOM_HEAD = (None)
    """
    Custom Sound is normally played when a Player Head with the required data is on top of the note block.
    """


    def getSound(self) -> "Sound":
        """
        Gets the sound associated with this instrument. 
        Will be null for Instrument.CUSTOM_HEAD

        Returns
        - the sound or null
        """
        ...


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
