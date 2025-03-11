"""
Python module generated from Java source file org.bukkit.block.data.type.NoteBlock

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Instrument
from org.bukkit import Note
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class NoteBlock(Powerable):
    """
    'instrument' is the type of sound made when this note block is activated.
    
    'note' is the specified tuned pitch that the instrument will be played in.
    """

    def getInstrument(self) -> "Instrument":
        """
        Gets the value of the 'instrument' property.

        Returns
        - the 'instrument' value
        """
        ...


    def setInstrument(self, instrument: "Instrument") -> None:
        """
        Sets the value of the 'instrument' property.

        Arguments
        - instrument: the new 'instrument' value
        """
        ...


    def getNote(self) -> "Note":
        """
        Gets the value of the 'note' property.

        Returns
        - the 'note' value
        """
        ...


    def setNote(self, note: "Note") -> None:
        """
        Sets the value of the 'note' property.

        Arguments
        - note: the new 'note' value
        """
        ...
