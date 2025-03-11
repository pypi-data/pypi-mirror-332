"""
Python module generated from Java source file org.bukkit.inventory.meta.MusicInstrumentMeta

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import MusicInstrument
from org.bukkit.inventory.meta import *
from typing import Any, Callable, Iterable, Tuple


class MusicInstrumentMeta(ItemMeta):

    def setInstrument(self, instrument: "MusicInstrument") -> None:
        """
        Sets the goat horn's instrument.

        Arguments
        - instrument: the instrument to set
        """
        ...


    def getInstrument(self) -> "MusicInstrument":
        """
        Gets the instrument of the goat horn.

        Returns
        - The instrument of the goat horn
        """
        ...


    def clone(self) -> "MusicInstrumentMeta":
        ...
