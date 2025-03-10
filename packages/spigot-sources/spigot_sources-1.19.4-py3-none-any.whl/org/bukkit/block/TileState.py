"""
Python module generated from Java source file org.bukkit.block.TileState

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.persistence import PersistentDataContainer
from org.bukkit.persistence import PersistentDataHolder
from typing import Any, Callable, Iterable, Tuple


class TileState(BlockState, PersistentDataHolder):
    """
    Represents a block state that also hosts a tile entity at the given location.
    
    This interface alone is merely a marker that does not provide any data.
    
    Data about the tile entities is provided by the respective interface for each
    tile entity type.
    
    After modifying the data provided by a TileState, .update() needs to
    be called to store the data.
    """

    def getPersistentDataContainer(self) -> "PersistentDataContainer":
        """
        Returns a custom tag container capable of storing tags on the object.
        
        Note that the tags stored on this container are all stored under their
        own custom namespace therefore modifying default tags using this
        PersistentDataHolder is impossible.
        
        This PersistentDataHolder is only linked to the snapshot instance
        stored by the BlockState.
        
        When storing changes on the PersistentDataHolder, the updated
        content will only be applied to the actual tile entity after one of the
        .update() methods is called.

        Returns
        - the custom tag container
        """
        ...
