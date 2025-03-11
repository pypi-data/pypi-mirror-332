"""
Python module generated from Java source file org.bukkit.inventory.meta.components.JukeboxPlayableComponent

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import JukeboxSong
from org.bukkit import NamespacedKey
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory.meta.components import *
from typing import Any, Callable, Iterable, Tuple


class JukeboxPlayableComponent(ConfigurationSerializable):
    """
    Represents a component which can be inserted into a jukebox.
    """

    def getSong(self) -> "JukeboxSong":
        """
        Gets the song assigned to this component.

        Returns
        - song, or null if the song does not exist on the server
        """
        ...


    def getSongKey(self) -> "NamespacedKey":
        """
        Gets the key of the song assigned to this component.

        Returns
        - the song key
        """
        ...


    def setSong(self, song: "JukeboxSong") -> None:
        """
        Sets the song assigned to this component.

        Arguments
        - song: the song
        """
        ...


    def setSongKey(self, song: "NamespacedKey") -> None:
        """
        Sets the key of the song assigned to this component.

        Arguments
        - song: the song key
        """
        ...


    def isShowInTooltip(self) -> bool:
        """
        Gets if the song will show in the item tooltip.

        Returns
        - if the song will show in the tooltip
        """
        ...


    def setShowInTooltip(self, show: bool) -> None:
        """
        Sets if the song will show in the item tooltip.

        Arguments
        - show: True if the song will show in the tooltip
        """
        ...
