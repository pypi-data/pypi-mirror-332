"""
Python module generated from Java source file org.bukkit.MusicInstrument

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.common.collect import Lists
from java.util import Collections
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class MusicInstrument(Keyed):

    PONDER = getInstrument("ponder_goat_horn")
    SING = getInstrument("sing_goat_horn")
    SEEK = getInstrument("seek_goat_horn")
    FEEL = getInstrument("feel_goat_horn")
    ADMIRE = getInstrument("admire_goat_horn")
    CALL = getInstrument("call_goat_horn")
    YEARN = getInstrument("yearn_goat_horn")
    DREAM = getInstrument("dream_goat_horn")


    @staticmethod
    def getByKey(namespacedKey: "NamespacedKey") -> "MusicInstrument":
        """
        Returns a MusicInstrument by a NamespacedKey.

        Arguments
        - namespacedKey: the key

        Returns
        - the event or null

        Deprecated
        - Use Registry.get(NamespacedKey) instead.
        """
        ...


    @staticmethod
    def values() -> Iterable["MusicInstrument"]:
        """
        Returns all known MusicInstruments.

        Returns
        - the memoryKeys

        Deprecated
        - use Registry.iterator().
        """
        ...
