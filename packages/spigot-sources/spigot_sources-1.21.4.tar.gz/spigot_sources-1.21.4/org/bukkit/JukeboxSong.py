"""
Python module generated from Java source file org.bukkit.JukeboxSong

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from org.bukkit.registry import RegistryAware
from typing import Any, Callable, Iterable, Tuple


class JukeboxSong(Keyed, Translatable, RegistryAware):
    """
    Represents a song which may play in a Jukebox.
    """

    THIRTEEN = get("13")
    CAT = get("cat")
    BLOCKS = get("blocks")
    CHIRP = get("chirp")
    FAR = get("far")
    MALL = get("mall")
    MELLOHI = get("mellohi")
    STAL = get("stal")
    STRAD = get("strad")
    WARD = get("ward")
    ELEVEN = get("11")
    WAIT = get("wait")
    PIGSTEP = get("pigstep")
    OTHERSIDE = get("otherside")
    FIVE = get("5")
    RELIC = get("relic")
    PRECIPICE = get("precipice")
    CREATOR = get("creator")
    CREATOR_MUSIC_BOX = get("creator_music_box")


    @staticmethod
    def get(key: str) -> "JukeboxSong":
        ...


    def getKey(self) -> "NamespacedKey":
        """
        See
        - .isRegistered()

        Deprecated
        - A key might not always be present, use .getKeyOrThrow() instead.
        """
        ...
