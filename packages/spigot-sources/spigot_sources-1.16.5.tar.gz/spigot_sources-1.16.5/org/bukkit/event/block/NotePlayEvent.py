"""
Python module generated from Java source file org.bukkit.event.block.NotePlayEvent

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Instrument
from org.bukkit import Note
from org.bukkit.block import Block
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import *
from typing import Any, Callable, Iterable, Tuple


class NotePlayEvent(BlockEvent, Cancellable):
    """
    Called when a note block is being played through player interaction or a
    redstone current.
    """

    def __init__(self, block: "Block", instrument: "Instrument", note: "Note"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getInstrument(self) -> "Instrument":
        """
        Gets the Instrument to be used.

        Returns
        - the Instrument
        """
        ...


    def getNote(self) -> "Note":
        """
        Gets the Note to be played.

        Returns
        - the Note
        """
        ...


    def setInstrument(self, instrument: "Instrument") -> None:
        """
        Overrides the Instrument to be used.

        Arguments
        - instrument: the Instrument. Has no effect if null.

        Deprecated
        - no effect on newer Minecraft versions
        """
        ...


    def setNote(self, note: "Note") -> None:
        """
        Overrides the Note to be played.

        Arguments
        - note: the Note. Has no effect if null.

        Deprecated
        - no effect on newer Minecraft versions
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
