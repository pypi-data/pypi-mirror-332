"""
Python module generated from Java source file org.bukkit.block.BlockState

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import World
from org.bukkit.block import *
from org.bukkit.block.data import BlockData
from org.bukkit.material import MaterialData
from org.bukkit.metadata import Metadatable
from typing import Any, Callable, Iterable, Tuple


class BlockState(Metadatable):
    """
    Represents a captured state of a block, which will not change
    automatically.
    
    Unlike Block, which only one object can exist per coordinate, BlockState
    can exist multiple times for any given Block. Note that another plugin may
    change the state of the block and you will not know, or they may change the
    block to another type entirely, causing your BlockState to become invalid.
    """

    def getBlock(self) -> "Block":
        """
        Gets the block represented by this block state.

        Returns
        - the block represented by this block state

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def getData(self) -> "MaterialData":
        """
        Gets the metadata for this block state.

        Returns
        - block specific metadata
        """
        ...


    def getBlockData(self) -> "BlockData":
        """
        Gets the data for this block state.

        Returns
        - block specific data
        """
        ...


    def copy(self) -> "BlockState":
        """
        Returns a copy of this BlockState as an unplaced BlockState.

        Returns
        - a copy of the block state
        """
        ...


    def getType(self) -> "Material":
        """
        Gets the type of this block state.

        Returns
        - block type
        """
        ...


    def getLightLevel(self) -> int:
        """
        Gets the current light level of the block represented by this block state.

        Returns
        - the light level between 0-15

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def getWorld(self) -> "World":
        """
        Gets the world which contains the block represented by this block state.

        Returns
        - the world containing the block represented by this block state

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def getX(self) -> int:
        """
        Gets the x-coordinate of this block state.

        Returns
        - x-coordinate
        """
        ...


    def getY(self) -> int:
        """
        Gets the y-coordinate of this block state.

        Returns
        - y-coordinate
        """
        ...


    def getZ(self) -> int:
        """
        Gets the z-coordinate of this block state.

        Returns
        - z-coordinate
        """
        ...


    def getLocation(self) -> "Location":
        """
        Gets the location of this block state.
        
        If this block state is not placed the location's world will be null!

        Returns
        - the location
        """
        ...


    def getLocation(self, loc: "Location") -> "Location":
        """
        Stores the location of this block state in the provided Location object.
        
        If the provided Location is null this method does nothing and returns
        null.
        
        If this block state is not placed the location's world will be null!

        Arguments
        - loc: the location to copy into

        Returns
        - The Location object provided or null
        """
        ...


    def getChunk(self) -> "Chunk":
        """
        Gets the chunk which contains the block represented by this block state.

        Returns
        - the containing Chunk

        Raises
        - IllegalStateException: if this block state is not placed
        """
        ...


    def setData(self, data: "MaterialData") -> None:
        """
        Sets the metadata for this block state.

        Arguments
        - data: New block specific metadata
        """
        ...


    def setBlockData(self, data: "BlockData") -> None:
        """
        Sets the data for this block state.

        Arguments
        - data: New block specific data
        """
        ...


    def setType(self, type: "Material") -> None:
        """
        Sets the type of this block state.

        Arguments
        - type: Material to change this block state to
        """
        ...


    def update(self) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        
        This has the same effect as calling update(False). That is to say,
        this will not modify the state of a block if it is no longer the same
        type as it was when this state was taken. It will return False in this
        eventuality.

        Returns
        - True if the update was successful, otherwise False

        See
        - .update(boolean)
        """
        ...


    def update(self, force: bool) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        
        This has the same effect as calling update(force, True). That is to
        say, this will trigger a physics update to surrounding blocks.

        Arguments
        - force: True to forcefully set the state

        Returns
        - True if the update was successful, otherwise False
        """
        ...


    def update(self, force: bool, applyPhysics: bool) -> bool:
        """
        Attempts to update the block represented by this state, setting it to
        the new values as defined by this state.
        
        If this state is not placed, this will have no effect and return True.
        
        Unless force is True, this will not modify the state of a block if it
        is no longer the same type as it was when this state was taken. It will
        return False in this eventuality.
        
        If force is True, it will set the type of the block to match the new
        state, set the state data and then return True.
        
        If applyPhysics is True, it will trigger a physics update on
        surrounding blocks which could cause them to update or disappear.

        Arguments
        - force: True to forcefully set the state
        - applyPhysics: False to cancel updating physics on surrounding
            blocks

        Returns
        - True if the update was successful, otherwise False
        """
        ...


    def getRawData(self) -> int:
        """
        Returns
        - The data as a raw byte.

        Deprecated
        - Magic value
        """
        ...


    def setRawData(self, data: int) -> None:
        """
        Arguments
        - data: The new data value for the block.

        Deprecated
        - Magic value
        """
        ...


    def isPlaced(self) -> bool:
        """
        Returns whether this state is placed in the world.
        
        Some methods will not work if the block state isn't
        placed in the world.

        Returns
        - whether the state is placed in the world
                or 'virtual' (e.g. on an itemstack)
        """
        ...
