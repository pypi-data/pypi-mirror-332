"""
Python module generated from Java source file org.bukkit.block.Jukebox

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import *
from org.bukkit.inventory import BlockInventoryHolder
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import JukeboxInventory
from typing import Any, Callable, Iterable, Tuple


class Jukebox(TileState, BlockInventoryHolder):
    """
    Represents a captured state of a jukebox.
    """

    def getPlaying(self) -> "Material":
        """
        Gets the record inserted into the jukebox.

        Returns
        - The record Material, or AIR if none is inserted
        """
        ...


    def setPlaying(self, record: "Material") -> None:
        """
        Sets the record being played.

        Arguments
        - record: The record Material, or null/AIR to stop playing
        """
        ...


    def hasRecord(self) -> bool:
        """
        Gets whether or not this jukebox has a record.
        
        A jukebox can have a record but not .isPlaying() be playing
        if it was stopped with .stopPlaying() or if a record has
        finished playing.

        Returns
        - True if this jukebox has a record, False if it the jukebox
        is empty
        """
        ...


    def getRecord(self) -> "ItemStack":
        """
        Gets the record item inserted into the jukebox.

        Returns
        - a copy of the inserted record, or an air stack if none
        """
        ...


    def setRecord(self, record: "ItemStack") -> None:
        """
        Sets the record being played. The jukebox will start playing automatically.

        Arguments
        - record: the record to insert or null/AIR to empty
        """
        ...


    def isPlaying(self) -> bool:
        """
        Checks if the jukebox is playing a record.

        Returns
        - True if there is a record playing
        """
        ...


    def startPlaying(self) -> bool:
        """
        Starts the jukebox playing if there is a record.

        Returns
        - True if the jukebox had a record and was able to start playing, False
        if the jukebox was already playing or did not have a record
        """
        ...


    def stopPlaying(self) -> None:
        """
        Stops the jukebox playing without ejecting the record.
        """
        ...


    def eject(self) -> bool:
        """
        Stops the jukebox playing and ejects the current record.
        
        If the block represented by this state is no longer a jukebox, this will
        do nothing and return False.

        Returns
        - True if a record was ejected; False if there was none playing

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def getInventory(self) -> "JukeboxInventory":
        """
        Returns
        - inventory

        See
        - Container.getInventory()
        """
        ...


    def getSnapshotInventory(self) -> "JukeboxInventory":
        """
        Returns
        - snapshot inventory

        See
        - Container.getSnapshotInventory()
        """
        ...
