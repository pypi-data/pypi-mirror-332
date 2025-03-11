"""
Python module generated from Java source file org.bukkit.inventory.JukeboxInventory

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import Jukebox
from org.bukkit.inventory import *
from typing import Any, Callable, Iterable, Tuple


class JukeboxInventory(Inventory):
    """
    Interface to the inventory of a Jukebox.
    """

    def setRecord(self, item: "ItemStack") -> None:
        """
        Set the record in the jukebox.
        
        This will immediately start playing the inserted item or stop playing if the
        item provided is null.

        Arguments
        - item: the new record
        """
        ...


    def getRecord(self) -> "ItemStack":
        """
        Get the record in the jukebox.

        Returns
        - the current record
        """
        ...


    def getHolder(self) -> "Jukebox":
        ...
