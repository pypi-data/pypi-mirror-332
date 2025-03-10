"""
Python module generated from Java source file org.bukkit.Chunk

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import *
from org.bukkit.block import Biome
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Entity
from org.bukkit.generator.structure import GeneratedStructure
from org.bukkit.generator.structure import Structure
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class Chunk(PersistentDataHolder):
    """
    Represents a chunk of blocks.
    
    If the chunk is not yet fully generated and data is requested from the chunk,
    then the chunk will only be generated as far as it needs to provide the
    requested data.
    """

    def getX(self) -> int:
        """
        Gets the X-coordinate of this chunk

        Returns
        - X-coordinate
        """
        ...


    def getZ(self) -> int:
        """
        Gets the Z-coordinate of this chunk

        Returns
        - Z-coordinate
        """
        ...


    def getWorld(self) -> "World":
        """
        Gets the world containing this chunk

        Returns
        - Parent World
        """
        ...


    def getBlock(self, x: int, y: int, z: int) -> "Block":
        """
        Gets a block from this chunk

        Arguments
        - x: 0-15
        - y: world minHeight (inclusive) - world maxHeight (exclusive)
        - z: 0-15

        Returns
        - the Block
        """
        ...


    def getChunkSnapshot(self) -> "ChunkSnapshot":
        """
        Capture thread-safe read-only snapshot of chunk data

        Returns
        - ChunkSnapshot
        """
        ...


    def getChunkSnapshot(self, includeMaxblocky: bool, includeBiome: bool, includeBiomeTempRain: bool) -> "ChunkSnapshot":
        """
        Capture thread-safe read-only snapshot of chunk data

        Arguments
        - includeMaxblocky: - if True, snapshot includes per-coordinate
            maximum Y values
        - includeBiome: - if True, snapshot includes per-coordinate biome
            type
        - includeBiomeTempRain: - if True, snapshot includes per-coordinate
            raw biome temperature and rainfall

        Returns
        - ChunkSnapshot
        """
        ...


    def isEntitiesLoaded(self) -> bool:
        """
        Checks if entities in this chunk are loaded.

        Returns
        - True if entities are loaded.
        """
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Get a list of all entities in the chunk.
        This will force load any entities, which are not loaded.

        Returns
        - The entities.
        """
        ...


    def getTileEntities(self) -> list["BlockState"]:
        """
        Get a list of all tile entities in the chunk.

        Returns
        - The tile entities.
        """
        ...


    def isGenerated(self) -> bool:
        """
        Checks if the chunk is fully generated.

        Returns
        - True if it is fully generated.
        """
        ...


    def isLoaded(self) -> bool:
        """
        Checks if the chunk is loaded.

        Returns
        - True if it is loaded.
        """
        ...


    def load(self, generate: bool) -> bool:
        """
        Loads the chunk.

        Arguments
        - generate: Whether or not to generate a chunk if it doesn't
            already exist

        Returns
        - True if the chunk has loaded successfully, otherwise False
        """
        ...


    def load(self) -> bool:
        """
        Loads the chunk.

        Returns
        - True if the chunk has loaded successfully, otherwise False
        """
        ...


    def unload(self, save: bool) -> bool:
        """
        Unloads and optionally saves the Chunk

        Arguments
        - save: Controls whether the chunk is saved

        Returns
        - True if the chunk has unloaded successfully, otherwise False
        """
        ...


    def unload(self) -> bool:
        """
        Unloads and optionally saves the Chunk

        Returns
        - True if the chunk has unloaded successfully, otherwise False
        """
        ...


    def isSlimeChunk(self) -> bool:
        """
        Checks if this chunk can spawn slimes without being a swamp biome.

        Returns
        - True if slimes are able to spawn in this chunk
        """
        ...


    def isForceLoaded(self) -> bool:
        """
        Gets whether the chunk at the specified chunk coordinates is force
        loaded.
        
        A force loaded chunk will not be unloaded due to lack of player activity.

        Returns
        - force load status

        See
        - World.isChunkForceLoaded(int, int)
        """
        ...


    def setForceLoaded(self, forced: bool) -> None:
        """
        Sets whether the chunk at the specified chunk coordinates is force
        loaded.
        
        A force loaded chunk will not be unloaded due to lack of player activity.

        Arguments
        - forced: force load status

        See
        - World.setChunkForceLoaded(int, int, boolean)
        """
        ...


    def addPluginChunkTicket(self, plugin: "Plugin") -> bool:
        """
        Adds a plugin ticket for this chunk, loading this chunk if it is not
        already loaded.
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - plugin: Plugin which owns the ticket

        Returns
        - `True` if a plugin ticket was added, `False` if the
        ticket already exists for the plugin

        Raises
        - IllegalStateException: If the specified plugin is not enabled

        See
        - World.addPluginChunkTicket(int, int, Plugin)
        """
        ...


    def removePluginChunkTicket(self, plugin: "Plugin") -> bool:
        """
        Removes the specified plugin's ticket for this chunk
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - plugin: Plugin which owns the ticket

        Returns
        - `True` if the plugin ticket was removed, `False` if
        there is no plugin ticket for the chunk

        See
        - World.removePluginChunkTicket(int, int, Plugin)
        """
        ...


    def getPluginChunkTickets(self) -> Iterable["Plugin"]:
        """
        Retrieves a collection specifying which plugins have tickets for this
        chunk. This collection is not updated when plugin tickets are added or
        removed to this chunk.
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Returns
        - unmodifiable collection containing which plugins have tickets for
        this chunk

        See
        - World.getPluginChunkTickets(int, int)
        """
        ...


    def getInhabitedTime(self) -> int:
        """
        Gets the amount of time in ticks that this chunk has been inhabited.
        
        Note that the time is incremented once per tick per player within mob
        spawning distance of this chunk.

        Returns
        - inhabited time
        """
        ...


    def setInhabitedTime(self, ticks: int) -> None:
        """
        Sets the amount of time in ticks that this chunk has been inhabited.

        Arguments
        - ticks: new inhabited time
        """
        ...


    def contains(self, block: "BlockData") -> bool:
        """
        Tests if this chunk contains the specified block.

        Arguments
        - block: block to test

        Returns
        - if the block is contained within
        """
        ...


    def contains(self, biome: "Biome") -> bool:
        """
        Tests if this chunk contains the specified biome.

        Arguments
        - biome: biome to test

        Returns
        - if the biome is contained within
        """
        ...


    def getLoadLevel(self) -> "LoadLevel":
        """
        Gets the load level of this chunk, which determines what game logic is
        processed.

        Returns
        - the load level
        """
        ...


    def getStructures(self) -> Iterable["GeneratedStructure"]:
        """
        Gets all generated structures that intersect this chunk. 
        If no structures are present an empty collection will be returned.

        Returns
        - a collection of placed structures in this chunk
        """
        ...


    def getStructures(self, structure: "Structure") -> Iterable["GeneratedStructure"]:
        """
        Gets all generated structures of a given Structure that intersect
        this chunk. 
        If no structures are present an empty collection will be returned.

        Arguments
        - structure: the structure to find

        Returns
        - a collection of placed structures in this chunk
        """
        ...


    class LoadLevel(Enum):
        """
        An enum to specify the load level of a chunk.
        """

        INACCESSIBLE = 0
        """
        No game logic is processed, world generation may still occur.
        """
        BORDER = 1
        """
        Most game logic is not processed, including entities and redstone.
        """
        TICKING = 2
        """
        All game logic except entities is processed.
        """
        ENTITY_TICKING = 3
        """
        All game logic is processed.
        """
        UNLOADED = 4
        """
        This chunk is not loaded.
        """
