"""
Python module generated from Java source file org.bukkit.World

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.io import File
from java.util.function import Consumer
from java.util.function import Predicate
from org.bukkit import *
from org.bukkit.block import Biome
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.boss import DragonBattle
from org.bukkit.entity import AbstractArrow
from org.bukkit.entity import Arrow
from org.bukkit.entity import Entity
from org.bukkit.entity import FallingBlock
from org.bukkit.entity import Item
from org.bukkit.entity import LightningStrike
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import Player
from org.bukkit.entity import SpawnCategory
from org.bukkit.generator import BiomeProvider
from org.bukkit.generator import BlockPopulator
from org.bukkit.generator import ChunkGenerator
from org.bukkit.generator import WorldInfo
from org.bukkit.generator.structure import Structure
from org.bukkit.generator.structure import StructureType
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from org.bukkit.metadata import Metadatable
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import PluginMessageRecipient
from org.bukkit.util import BiomeSearchResult
from org.bukkit.util import BoundingBox
from org.bukkit.util import RayTraceResult
from org.bukkit.util import StructureSearchResult
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class World(RegionAccessor, WorldInfo, PluginMessageRecipient, Metadatable, PersistentDataHolder, Keyed):
    """
    Represents a world, which may contain entities, chunks and blocks
    """

    def getBlockAt(self, x: int, y: int, z: int) -> "Block":
        """
        Gets the Block at the given coordinates

        Arguments
        - x: X-coordinate of the block
        - y: Y-coordinate of the block
        - z: Z-coordinate of the block

        Returns
        - Block at the given coordinates
        """
        ...


    def getBlockAt(self, location: "Location") -> "Block":
        """
        Gets the Block at the given Location

        Arguments
        - location: Location of the block

        Returns
        - Block at the given location
        """
        ...


    def getHighestBlockAt(self, x: int, z: int) -> "Block":
        """
        Gets the highest non-empty (impassable) block at the given coordinates.

        Arguments
        - x: X-coordinate of the block
        - z: Z-coordinate of the block

        Returns
        - Highest non-empty block
        """
        ...


    def getHighestBlockAt(self, location: "Location") -> "Block":
        """
        Gets the highest non-empty (impassable) block at the given coordinates.

        Arguments
        - location: Coordinates to get the highest block

        Returns
        - Highest non-empty block
        """
        ...


    def getHighestBlockAt(self, x: int, z: int, heightMap: "HeightMap") -> "Block":
        """
        Gets the highest block corresponding to the HeightMap at the
        given coordinates.

        Arguments
        - x: X-coordinate of the block
        - z: Z-coordinate of the block
        - heightMap: the heightMap that is used to determine the highest
        point

        Returns
        - Highest block corresponding to the HeightMap
        """
        ...


    def getHighestBlockAt(self, location: "Location", heightMap: "HeightMap") -> "Block":
        """
        Gets the highest block corresponding to the HeightMap at the
        given coordinates.

        Arguments
        - location: Coordinates to get the highest block
        - heightMap: the heightMap that is used to determine the highest
        point

        Returns
        - Highest block corresponding to the HeightMap
        """
        ...


    def getChunkAt(self, x: int, z: int) -> "Chunk":
        """
        Gets the Chunk at the given coordinates

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - Chunk at the given coordinates
        """
        ...


    def getChunkAt(self, x: int, z: int, generate: bool) -> "Chunk":
        """
        Gets the Chunk at the given coordinates

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - generate: Whether the chunk should be fully generated or not

        Returns
        - Chunk at the given coordinates
        """
        ...


    def getChunkAt(self, location: "Location") -> "Chunk":
        """
        Gets the Chunk at the given Location

        Arguments
        - location: Location of the chunk

        Returns
        - Chunk at the given location
        """
        ...


    def getChunkAt(self, block: "Block") -> "Chunk":
        """
        Gets the Chunk that contains the given Block

        Arguments
        - block: Block to get the containing chunk from

        Returns
        - The chunk that contains the given block
        """
        ...


    def isChunkLoaded(self, chunk: "Chunk") -> bool:
        """
        Checks if the specified Chunk is loaded

        Arguments
        - chunk: The chunk to check

        Returns
        - True if the chunk is loaded, otherwise False
        """
        ...


    def getLoadedChunks(self) -> list["Chunk"]:
        """
        Gets an array of all loaded Chunks

        Returns
        - Chunk[] containing all loaded chunks
        """
        ...


    def loadChunk(self, chunk: "Chunk") -> None:
        """
        Loads the specified Chunk.
        
        **This method will keep the specified chunk loaded until one of the
        unload methods is manually called. Callers are advised to instead use
        getChunkAt which will only temporarily load the requested chunk.**

        Arguments
        - chunk: The chunk to load
        """
        ...


    def isChunkLoaded(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is loaded

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - True if the chunk is loaded, otherwise False
        """
        ...


    def isChunkGenerated(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is generated

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - True if the chunk is generated, otherwise False
        """
        ...


    def isChunkInUse(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is loaded and
        in use by one or more players

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - True if the chunk is loaded and in use by one or more players,
            otherwise False

        Deprecated
        - This method was added to facilitate chunk garbage collection.
            As of the current Minecraft version chunks are now strictly managed and
            will not be loaded for more than 1 tick unless they are in use.
        """
        ...


    def loadChunk(self, x: int, z: int) -> None:
        """
        Loads the Chunk at the specified coordinates.
        
        **This method will keep the specified chunk loaded until one of the
        unload methods is manually called. Callers are advised to instead use
        getChunkAt which will only temporarily load the requested chunk.**
        
        If the chunk does not exist, it will be generated.
        
        This method is analogous to .loadChunk(int, int, boolean) where
        generate is True.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        """
        ...


    def loadChunk(self, x: int, z: int, generate: bool) -> bool:
        """
        Loads the Chunk at the specified coordinates.
        
        **This method will keep the specified chunk loaded until one of the
        unload methods is manually called. Callers are advised to instead use
        getChunkAt which will only temporarily load the requested chunk.**

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - generate: Whether or not to generate a chunk if it doesn't
            already exist

        Returns
        - True if the chunk has loaded successfully, otherwise False
        """
        ...


    def unloadChunk(self, chunk: "Chunk") -> bool:
        """
        Safely unloads and saves the Chunk at the specified coordinates
        
        This method is analogous to .unloadChunk(int, int, boolean)
        where save is True.

        Arguments
        - chunk: the chunk to unload

        Returns
        - True if the chunk has unloaded successfully, otherwise False
        """
        ...


    def unloadChunk(self, x: int, z: int) -> bool:
        """
        Safely unloads and saves the Chunk at the specified coordinates
        
        This method is analogous to .unloadChunk(int, int, boolean)
        where save is True.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - True if the chunk has unloaded successfully, otherwise False
        """
        ...


    def unloadChunk(self, x: int, z: int, save: bool) -> bool:
        """
        Safely unloads and optionally saves the Chunk at the specified
        coordinates.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - save: Whether or not to save the chunk

        Returns
        - True if the chunk has unloaded successfully, otherwise False
        """
        ...


    def unloadChunkRequest(self, x: int, z: int) -> bool:
        """
        Safely queues the Chunk at the specified coordinates for
        unloading.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - True is the queue attempt was successful, otherwise False
        """
        ...


    def regenerateChunk(self, x: int, z: int) -> bool:
        """
        Regenerates the Chunk at the specified coordinates

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - Whether the chunk was actually regenerated

        Deprecated
        - regenerating a single chunk is not likely to produce the same
        chunk as before as terrain decoration may be spread across chunks. Use of
        this method should be avoided as it is known to produce buggy results.
        """
        ...


    def refreshChunk(self, x: int, z: int) -> bool:
        """
        Resends the Chunk to all clients

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - Whether the chunk was actually refreshed

        Deprecated
        - This method is not guaranteed to work suitably across all client implementations.
        """
        ...


    def isChunkForceLoaded(self, x: int, z: int) -> bool:
        """
        Gets whether the chunk at the specified chunk coordinates is force
        loaded.
        
        A force loaded chunk will not be unloaded due to lack of player activity.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - force load status
        """
        ...


    def setChunkForceLoaded(self, x: int, z: int, forced: bool) -> None:
        """
        Sets whether the chunk at the specified chunk coordinates is force
        loaded.
        
        A force loaded chunk will not be unloaded due to lack of player activity.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - forced: force load status
        """
        ...


    def getForceLoadedChunks(self) -> Iterable["Chunk"]:
        """
        Returns all force loaded chunks in this world.
        
        A force loaded chunk will not be unloaded due to lack of player activity.

        Returns
        - unmodifiable collection of force loaded chunks
        """
        ...


    def addPluginChunkTicket(self, x: int, z: int, plugin: "Plugin") -> bool:
        """
        Adds a plugin ticket for the specified chunk, loading the chunk if it is
        not already loaded.
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - plugin: Plugin which owns the ticket

        Returns
        - `True` if a plugin ticket was added, `False` if the
        ticket already exists for the plugin

        Raises
        - IllegalStateException: If the specified plugin is not enabled

        See
        - .removePluginChunkTicket(int, int, Plugin)
        """
        ...


    def removePluginChunkTicket(self, x: int, z: int, plugin: "Plugin") -> bool:
        """
        Removes the specified plugin's ticket for the specified chunk
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk
        - plugin: Plugin which owns the ticket

        Returns
        - `True` if the plugin ticket was removed, `False` if
        there is no plugin ticket for the chunk

        See
        - .addPluginChunkTicket(int, int, Plugin)
        """
        ...


    def removePluginChunkTickets(self, plugin: "Plugin") -> None:
        """
        Removes all plugin tickets for the specified plugin
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - plugin: Specified plugin

        See
        - .removePluginChunkTicket(int, int, Plugin)
        """
        ...


    def getPluginChunkTickets(self, x: int, z: int) -> Iterable["Plugin"]:
        """
        Retrieves a collection specifying which plugins have tickets for the
        specified chunk. This collection is not updated when plugin tickets are
        added or removed to the chunk.
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Arguments
        - x: X-coordinate of the chunk
        - z: Z-coordinate of the chunk

        Returns
        - unmodifiable collection containing which plugins have tickets for
        the chunk

        See
        - .removePluginChunkTicket(int, int, Plugin)
        """
        ...


    def getPluginChunkTickets(self) -> dict["Plugin", Iterable["Chunk"]]:
        """
        Returns a map of which plugins have tickets for what chunks. The returned
        map is not updated when plugin tickets are added or removed to chunks. If
        a plugin has no tickets, it will be absent from the map.
        
        A plugin ticket will prevent a chunk from unloading until it is
        explicitly removed. A plugin instance may only have one ticket per chunk,
        but each chunk can have multiple plugin tickets.

        Returns
        - unmodifiable map containing which plugins have tickets for what
        chunks

        See
        - .removePluginChunkTicket(int, int, Plugin)
        """
        ...


    def dropItem(self, location: "Location", item: "ItemStack") -> "Item":
        """
        Drops an item at the specified Location

        Arguments
        - location: Location to drop the item
        - item: ItemStack to drop

        Returns
        - ItemDrop entity created as a result of this method
        """
        ...


    def dropItem(self, location: "Location", item: "ItemStack", function: "Consumer"["Item"]) -> "Item":
        """
        Drops an item at the specified Location
        Note that functions will run before the entity is spawned

        Arguments
        - location: Location to drop the item
        - item: ItemStack to drop
        - function: the function to be run before the entity is spawned.

        Returns
        - ItemDrop entity created as a result of this method
        """
        ...


    def dropItemNaturally(self, location: "Location", item: "ItemStack") -> "Item":
        """
        Drops an item at the specified Location with a random offset

        Arguments
        - location: Location to drop the item
        - item: ItemStack to drop

        Returns
        - ItemDrop entity created as a result of this method
        """
        ...


    def dropItemNaturally(self, location: "Location", item: "ItemStack", function: "Consumer"["Item"]) -> "Item":
        """
        Drops an item at the specified Location with a random offset
        Note that functions will run before the entity is spawned

        Arguments
        - location: Location to drop the item
        - item: ItemStack to drop
        - function: the function to be run before the entity is spawned.

        Returns
        - ItemDrop entity created as a result of this method
        """
        ...


    def spawnArrow(self, location: "Location", direction: "Vector", speed: float, spread: float) -> "Arrow":
        """
        Creates an Arrow entity at the given Location

        Arguments
        - location: Location to spawn the arrow
        - direction: Direction to shoot the arrow in
        - speed: Speed of the arrow. A recommend speed is 0.6
        - spread: Spread of the arrow. A recommend spread is 12

        Returns
        - Arrow entity spawned as a result of this method
        """
        ...


    def spawnArrow(self, location: "Location", direction: "Vector", speed: float, spread: float, clazz: type["T"]) -> "T":
        """
        Creates an arrow entity of the given class at the given Location
        
        Type `<T>`: type of arrow to spawn

        Arguments
        - location: Location to spawn the arrow
        - direction: Direction to shoot the arrow in
        - speed: Speed of the arrow. A recommend speed is 0.6
        - spread: Spread of the arrow. A recommend spread is 12
        - clazz: the Entity class for the arrow
        org.bukkit.entity.SpectralArrow,org.bukkit.entity.Arrow,org.bukkit.entity.TippedArrow

        Returns
        - Arrow entity spawned as a result of this method
        """
        ...


    def generateTree(self, location: "Location", type: "TreeType") -> bool:
        """
        Creates a tree at the given Location

        Arguments
        - location: Location to spawn the tree
        - type: Type of the tree to create

        Returns
        - True if the tree was created successfully, otherwise False
        """
        ...


    def generateTree(self, loc: "Location", type: "TreeType", delegate: "BlockChangeDelegate") -> bool:
        """
        Creates a tree at the given Location

        Arguments
        - loc: Location to spawn the tree
        - type: Type of the tree to create
        - delegate: A class to call for each block changed as a result of
            this method

        Returns
        - True if the tree was created successfully, otherwise False

        See
        - .generateTree(org.bukkit.Location, java.util.Random, org.bukkit.TreeType, java.util.function.Consumer)

        Deprecated
        - this method does not handle tile entities (bee nests)
        """
        ...


    def strikeLightning(self, loc: "Location") -> "LightningStrike":
        """
        Strikes lightning at the given Location

        Arguments
        - loc: The location to strike lightning

        Returns
        - The lightning entity.
        """
        ...


    def strikeLightningEffect(self, loc: "Location") -> "LightningStrike":
        """
        Strikes lightning at the given Location without doing damage

        Arguments
        - loc: The location to strike lightning

        Returns
        - The lightning entity.
        """
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Get a list of all entities in this World

        Returns
        - A List of all Entities currently residing in this world
        """
        ...


    def getLivingEntities(self) -> list["LivingEntity"]:
        """
        Get a list of all living entities in this World

        Returns
        - A List of all LivingEntities currently residing in this world
        """
        ...


    def getEntitiesByClass(self, *classes: Tuple[type["T"], ...]) -> Iterable["T"]:
        """
        Get a collection of all entities in this World matching the given
        class/interface
        
        Type `<T>`: an entity subclass

        Arguments
        - classes: The classes representing the types of entity to match

        Returns
        - A List of all Entities currently residing in this world that
            match the given class/interface
        """
        ...


    def getEntitiesByClass(self, cls: type["T"]) -> Iterable["T"]:
        """
        Get a collection of all entities in this World matching the given
        class/interface
        
        Type `<T>`: an entity subclass

        Arguments
        - cls: The class representing the type of entity to match

        Returns
        - A List of all Entities currently residing in this world that
            match the given class/interface
        """
        ...


    def getEntitiesByClasses(self, *classes: Tuple[type[Any], ...]) -> Iterable["Entity"]:
        """
        Get a collection of all entities in this World matching any of the
        given classes/interfaces

        Arguments
        - classes: The classes representing the types of entity to match

        Returns
        - A List of all Entities currently residing in this world that
            match one or more of the given classes/interfaces
        """
        ...


    def getPlayers(self) -> list["Player"]:
        """
        Get a list of all players in this World

        Returns
        - A list of all Players currently residing in this world
        """
        ...


    def getNearbyEntities(self, location: "Location", x: float, y: float, z: float) -> Iterable["Entity"]:
        """
        Returns a list of entities within a bounding box centered around a
        Location.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the size of the
        search bounding box.

        Arguments
        - location: The center of the bounding box
        - x: 1/2 the size of the box along x axis
        - y: 1/2 the size of the box along y axis
        - z: 1/2 the size of the box along z axis

        Returns
        - the collection of entities near location. This will always be a
             non-null collection.
        """
        ...


    def getNearbyEntities(self, location: "Location", x: float, y: float, z: float, filter: "Predicate"["Entity"]) -> Iterable["Entity"]:
        """
        Returns a list of entities within a bounding box centered around a
        Location.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the size of the
        search bounding box.

        Arguments
        - location: The center of the bounding box
        - x: 1/2 the size of the box along x axis
        - y: 1/2 the size of the box along y axis
        - z: 1/2 the size of the box along z axis
        - filter: only entities that fulfill this predicate are considered,
            or `null` to consider all entities

        Returns
        - the collection of entities near location. This will always be a
            non-null collection.
        """
        ...


    def getNearbyEntities(self, boundingBox: "BoundingBox") -> Iterable["Entity"]:
        """
        Returns a list of entities within the given bounding box.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the size of the
        search bounding box.

        Arguments
        - boundingBox: the bounding box

        Returns
        - the collection of entities within the bounding box, will always
            be a non-null collection
        """
        ...


    def getNearbyEntities(self, boundingBox: "BoundingBox", filter: "Predicate"["Entity"]) -> Iterable["Entity"]:
        """
        Returns a list of entities within the given bounding box.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the size of the
        search bounding box.

        Arguments
        - boundingBox: the bounding box
        - filter: only entities that fulfill this predicate are considered,
            or `null` to consider all entities

        Returns
        - the collection of entities within the bounding box, will always
            be a non-null collection
        """
        ...


    def rayTraceEntities(self, start: "Location", direction: "Vector", maxDistance: float) -> "RayTraceResult":
        """
        Performs a ray trace that checks for entity collisions.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the maximum
        distance.
        
        **Note:** Due to display entities having a zero size hitbox, this method will not detect them.
        To detect display entities use .rayTraceEntities(Location, Vector, double, double) with a positive raySize

        Arguments
        - start: the start position
        - direction: the ray direction
        - maxDistance: the maximum distance

        Returns
        - the closest ray trace hit result, or `null` if there
            is no hit

        See
        - .rayTraceEntities(Location, Vector, double, double, Predicate)
        """
        ...


    def rayTraceEntities(self, start: "Location", direction: "Vector", maxDistance: float, raySize: float) -> "RayTraceResult":
        """
        Performs a ray trace that checks for entity collisions.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the maximum
        distance.

        Arguments
        - start: the start position
        - direction: the ray direction
        - maxDistance: the maximum distance
        - raySize: entity bounding boxes will be uniformly expanded (or
            shrunk) by this value before doing collision checks

        Returns
        - the closest ray trace hit result, or `null` if there
            is no hit

        See
        - .rayTraceEntities(Location, Vector, double, double, Predicate)
        """
        ...


    def rayTraceEntities(self, start: "Location", direction: "Vector", maxDistance: float, filter: "Predicate"["Entity"]) -> "RayTraceResult":
        """
        Performs a ray trace that checks for entity collisions.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the maximum
        distance.
        
        **Note:** Due to display entities having a zero size hitbox, this method will not detect them.
        To detect display entities use .rayTraceEntities(Location, Vector, double, double, Predicate) with a positive raySize

        Arguments
        - start: the start position
        - direction: the ray direction
        - maxDistance: the maximum distance
        - filter: only entities that fulfill this predicate are considered,
            or `null` to consider all entities

        Returns
        - the closest ray trace hit result, or `null` if there
            is no hit

        See
        - .rayTraceEntities(Location, Vector, double, double, Predicate)
        """
        ...


    def rayTraceEntities(self, start: "Location", direction: "Vector", maxDistance: float, raySize: float, filter: "Predicate"["Entity"]) -> "RayTraceResult":
        """
        Performs a ray trace that checks for entity collisions.
        
        This may not consider entities in currently unloaded chunks. Some
        implementations may impose artificial restrictions on the maximum
        distance.

        Arguments
        - start: the start position
        - direction: the ray direction
        - maxDistance: the maximum distance
        - raySize: entity bounding boxes will be uniformly expanded (or
            shrunk) by this value before doing collision checks
        - filter: only entities that fulfill this predicate are considered,
            or `null` to consider all entities

        Returns
        - the closest ray trace hit result, or `null` if there
            is no hit
        """
        ...


    def rayTraceBlocks(self, start: "Location", direction: "Vector", maxDistance: float) -> "RayTraceResult":
        """
        Performs a ray trace that checks for block collisions using the blocks'
        precise collision shapes.
        
        This takes collisions with passable blocks into account, but ignores
        fluids.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - start: the start location
        - direction: the ray direction
        - maxDistance: the maximum distance

        Returns
        - the ray trace hit result, or `null` if there is no hit

        See
        - .rayTraceBlocks(Location, Vector, double, FluidCollisionMode, boolean)
        """
        ...


    def rayTraceBlocks(self, start: "Location", direction: "Vector", maxDistance: float, fluidCollisionMode: "FluidCollisionMode") -> "RayTraceResult":
        """
        Performs a ray trace that checks for block collisions using the blocks'
        precise collision shapes.
        
        This takes collisions with passable blocks into account.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - start: the start location
        - direction: the ray direction
        - maxDistance: the maximum distance
        - fluidCollisionMode: the fluid collision mode

        Returns
        - the ray trace hit result, or `null` if there is no hit

        See
        - .rayTraceBlocks(Location, Vector, double, FluidCollisionMode, boolean)
        """
        ...


    def rayTraceBlocks(self, start: "Location", direction: "Vector", maxDistance: float, fluidCollisionMode: "FluidCollisionMode", ignorePassableBlocks: bool) -> "RayTraceResult":
        """
        Performs a ray trace that checks for block collisions using the blocks'
        precise collision shapes.
        
        If collisions with passable blocks are ignored, fluid collisions are
        ignored as well regardless of the fluid collision mode.
        
        Portal blocks are only considered passable if the ray starts within
        them. Apart from that collisions with portal blocks will be considered
        even if collisions with passable blocks are otherwise ignored.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - start: the start location
        - direction: the ray direction
        - maxDistance: the maximum distance
        - fluidCollisionMode: the fluid collision mode
        - ignorePassableBlocks: whether to ignore passable but collidable
            blocks (ex. tall grass, signs, fluids, ..)

        Returns
        - the ray trace hit result, or `null` if there is no hit
        """
        ...


    def rayTrace(self, start: "Location", direction: "Vector", maxDistance: float, fluidCollisionMode: "FluidCollisionMode", ignorePassableBlocks: bool, raySize: float, filter: "Predicate"["Entity"]) -> "RayTraceResult":
        """
        Performs a ray trace that checks for both block and entity collisions.
        
        Block collisions use the blocks' precise collision shapes. The
        `raySize` parameter is only taken into account for entity
        collision checks.
        
        If collisions with passable blocks are ignored, fluid collisions are
        ignored as well regardless of the fluid collision mode.
        
        Portal blocks are only considered passable if the ray starts within them.
        Apart from that collisions with portal blocks will be considered even if
        collisions with passable blocks are otherwise ignored.
        
        This may cause loading of chunks! Some implementations may impose
        artificial restrictions on the maximum distance.

        Arguments
        - start: the start location
        - direction: the ray direction
        - maxDistance: the maximum distance
        - fluidCollisionMode: the fluid collision mode
        - ignorePassableBlocks: whether to ignore passable but collidable
            blocks (ex. tall grass, signs, fluids, ..)
        - raySize: entity bounding boxes will be uniformly expanded (or
            shrunk) by this value before doing collision checks
        - filter: only entities that fulfill this predicate are considered,
            or `null` to consider all entities

        Returns
        - the closest ray trace hit result with either a block or an
            entity, or `null` if there is no hit
        """
        ...


    def getSpawnLocation(self) -> "Location":
        """
        Gets the default spawn Location of this world

        Returns
        - The spawn location of this world
        """
        ...


    def setSpawnLocation(self, location: "Location") -> bool:
        """
        Sets the spawn location of the world.
        
        The location provided must be equal to this world.

        Arguments
        - location: The Location to set the spawn for this world at.

        Returns
        - True if it was successfully set.
        """
        ...


    def setSpawnLocation(self, x: int, y: int, z: int, angle: float) -> bool:
        """
        Sets the spawn location of the world

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - angle: the angle

        Returns
        - True if it was successfully set.
        """
        ...


    def setSpawnLocation(self, x: int, y: int, z: int) -> bool:
        """
        Sets the spawn location of the world

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - True if it was successfully set.
        """
        ...


    def getTime(self) -> int:
        """
        Gets the relative in-game time of this world.
        
        The relative time is analogous to hours * 1000

        Returns
        - The current relative time

        See
        - .getFullTime() Returns an absolute time of this world
        """
        ...


    def setTime(self, time: int) -> None:
        """
        Sets the relative in-game time on the server.
        
        The relative time is analogous to hours * 1000
        
        Note that setting the relative time below the current relative time
        will actually move the clock forward a day. If you require to rewind
        time, please see .setFullTime(long)

        Arguments
        - time: The new relative time to set the in-game time to (in
            hours*1000)

        See
        - .setFullTime(long) Sets the absolute time of this world
        """
        ...


    def getFullTime(self) -> int:
        """
        Gets the full in-game time on this world

        Returns
        - The current absolute time

        See
        - .getTime() Returns a relative time of this world
        """
        ...


    def setFullTime(self, time: int) -> None:
        """
        Sets the in-game time on the server
        
        Note that this sets the full time of the world, which may cause adverse
        effects such as breaking redstone clocks and any scheduled events

        Arguments
        - time: The new absolute time to set this world to

        See
        - .setTime(long) Sets the relative time of this world
        """
        ...


    def getGameTime(self) -> int:
        """
        Gets the full in-game time on this world since the world generation

        Returns
        - The current absolute time since the world generation

        See
        - .getFullTime() Returns an absolute time of this world
        """
        ...


    def hasStorm(self) -> bool:
        """
        Returns whether the world has an ongoing storm.

        Returns
        - Whether there is an ongoing storm
        """
        ...


    def setStorm(self, hasStorm: bool) -> None:
        """
        Set whether there is a storm. A duration will be set for the new
        current conditions.
        
        This will implicitly call .setClearWeatherDuration(int) with 0
        ticks to reset the world's clear weather.

        Arguments
        - hasStorm: Whether there is rain and snow
        """
        ...


    def getWeatherDuration(self) -> int:
        """
        Get the remaining time in ticks of the current conditions.

        Returns
        - Time in ticks
        """
        ...


    def setWeatherDuration(self, duration: int) -> None:
        """
        Set the remaining time in ticks of the current conditions.

        Arguments
        - duration: Time in ticks
        """
        ...


    def isThundering(self) -> bool:
        """
        Returns whether there is thunder.

        Returns
        - Whether there is thunder
        """
        ...


    def setThundering(self, thundering: bool) -> None:
        """
        Set whether it is thundering.
        
        This will implicitly call .setClearWeatherDuration(int) with 0
        ticks to reset the world's clear weather.

        Arguments
        - thundering: Whether it is thundering
        """
        ...


    def getThunderDuration(self) -> int:
        """
        Get the thundering duration.

        Returns
        - Duration in ticks
        """
        ...


    def setThunderDuration(self, duration: int) -> None:
        """
        Set the thundering duration.

        Arguments
        - duration: Duration in ticks
        """
        ...


    def isClearWeather(self) -> bool:
        """
        Returns whether the world has clear weather.
        
        This will be True such that .isThundering() and
        .hasStorm() are both False.

        Returns
        - True if clear weather
        """
        ...


    def setClearWeatherDuration(self, duration: int) -> None:
        """
        Set the clear weather duration.
        
        The clear weather ticks determine whether or not the world will be
        allowed to rain or storm. If clear weather ticks are &gt; 0, the world will
        not naturally do either until the duration has elapsed.
        
        This method is equivalent to calling `/weather clear` with a set
        amount of ticks.

        Arguments
        - duration: duration in ticks
        """
        ...


    def getClearWeatherDuration(self) -> int:
        """
        Get the clear weather duration.

        Returns
        - duration in ticks
        """
        ...


    def createExplosion(self, x: float, y: float, z: float, power: float) -> bool:
        """
        Creates explosion at given coordinates with given power

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - power: The power of explosion, where 4F is TNT

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, x: float, y: float, z: float, power: float, setFire: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, x: float, y: float, z: float, power: float, setFire: bool, breakBlocks: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire or breaking blocks.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire
        - breakBlocks: Whether or not to have blocks be destroyed

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, x: float, y: float, z: float, power: float, setFire: bool, breakBlocks: bool, source: "Entity") -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire or breaking blocks.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire
        - breakBlocks: Whether or not to have blocks be destroyed
        - source: the source entity, used for tracking damage

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, loc: "Location", power: float) -> bool:
        """
        Creates explosion at given coordinates with given power

        Arguments
        - loc: Location to blow up
        - power: The power of explosion, where 4F is TNT

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, loc: "Location", power: float, setFire: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire.

        Arguments
        - loc: Location to blow up
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, loc: "Location", power: float, setFire: bool, breakBlocks: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire or breaking blocks.

        Arguments
        - loc: Location to blow up
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire
        - breakBlocks: Whether or not to have blocks be destroyed

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def createExplosion(self, loc: "Location", power: float, setFire: bool, breakBlocks: bool, source: "Entity") -> bool:
        """
        Creates explosion at given coordinates with given power and optionally
        setting blocks on fire or breaking blocks.

        Arguments
        - loc: Location to blow up
        - power: The power of explosion, where 4F is TNT
        - setFire: Whether or not to set blocks on fire
        - breakBlocks: Whether or not to have blocks be destroyed
        - source: the source entity, used for tracking damage

        Returns
        - False if explosion was canceled, otherwise True
        """
        ...


    def getPVP(self) -> bool:
        """
        Gets the current PVP setting for this world.

        Returns
        - True if PVP is enabled
        """
        ...


    def setPVP(self, pvp: bool) -> None:
        """
        Sets the PVP setting for this world.

        Arguments
        - pvp: True/False whether PVP should be Enabled.
        """
        ...


    def getGenerator(self) -> "ChunkGenerator":
        """
        Gets the chunk generator for this world

        Returns
        - ChunkGenerator associated with this world
        """
        ...


    def getBiomeProvider(self) -> "BiomeProvider":
        """
        Gets the biome provider for this world

        Returns
        - BiomeProvider associated with this world
        """
        ...


    def save(self) -> None:
        """
        Saves world to disk
        """
        ...


    def getPopulators(self) -> list["BlockPopulator"]:
        """
        Gets a list of all applied BlockPopulators for this World

        Returns
        - List containing any or none BlockPopulators
        """
        ...


    def spawnFallingBlock(self, location: "Location", data: "MaterialData") -> "FallingBlock":
        """
        Spawn a FallingBlock entity at the given Location of
        the specified MaterialData. The MaterialData dictates what is falling.
        When the FallingBlock hits the ground, it will place that block.
        
        The Material must be a block type, check with Material.isBlock()
        data.getItemType().isBlock(). The Material may not be air.

        Arguments
        - location: The Location to spawn the FallingBlock
        - data: The block data

        Returns
        - The spawned FallingBlock instance

        Raises
        - IllegalArgumentException: if Location or MaterialData are null or Material of the MaterialData is not a block
        """
        ...


    def spawnFallingBlock(self, location: "Location", data: "BlockData") -> "FallingBlock":
        """
        Spawn a FallingBlock entity at the given Location of
        the specified BlockData. The BlockData dictates what is falling.
        When the FallingBlock hits the ground, it will place that block.

        Arguments
        - location: The Location to spawn the FallingBlock
        - data: The BlockData of the FallingBlock to spawn

        Returns
        - The spawned FallingBlock instance

        Raises
        - IllegalArgumentException: if Location or BlockData are null
        """
        ...


    def spawnFallingBlock(self, location: "Location", material: "Material", data: int) -> "FallingBlock":
        """
        Spawn a FallingBlock entity at the given Location of the
        specified Material. The material dictates what is falling.
        When the FallingBlock hits the ground, it will place that block.
        
        The Material must be a block type, check with Material.isBlock()
        material.isBlock(). The Material may not be air.

        Arguments
        - location: The Location to spawn the FallingBlock
        - material: The block Material type
        - data: The block data

        Returns
        - The spawned FallingBlock instance

        Raises
        - IllegalArgumentException: if Location or Material are null or Material is not a block

        Deprecated
        - Magic value
        """
        ...


    def playEffect(self, location: "Location", effect: "Effect", data: int) -> None:
        """
        Plays an effect to all players within a default radius around a given
        location.

        Arguments
        - location: the Location around which players must be to
            hear the sound
        - effect: the Effect
        - data: a data bit needed for some effects
        """
        ...


    def playEffect(self, location: "Location", effect: "Effect", data: int, radius: int) -> None:
        """
        Plays an effect to all players within a given radius around a location.

        Arguments
        - location: the Location around which players must be to
            hear the effect
        - effect: the Effect
        - data: a data bit needed for some effects
        - radius: the radius around the location
        """
        ...


    def playEffect(self, location: "Location", effect: "Effect", data: "T") -> None:
        """
        Plays an effect to all players within a default radius around a given
        location.
        
        Type `<T>`: data dependant on the type of effect

        Arguments
        - location: the Location around which players must be to
            hear the sound
        - effect: the Effect
        - data: a data bit needed for some effects
        """
        ...


    def playEffect(self, location: "Location", effect: "Effect", data: "T", radius: int) -> None:
        """
        Plays an effect to all players within a given radius around a location.
        
        Type `<T>`: data dependant on the type of effect

        Arguments
        - location: the Location around which players must be to
            hear the effect
        - effect: the Effect
        - data: a data bit needed for some effects
        - radius: the radius around the location
        """
        ...


    def getEmptyChunkSnapshot(self, x: int, z: int, includeBiome: bool, includeBiomeTemp: bool) -> "ChunkSnapshot":
        """
        Get empty chunk snapshot (equivalent to all air blocks), optionally
        including valid biome data. Used for representing an ungenerated chunk,
        or for fetching only biome data without loading a chunk.

        Arguments
        - x: - chunk x coordinate
        - z: - chunk z coordinate
        - includeBiome: - if True, snapshot includes per-coordinate biome
            type
        - includeBiomeTemp: - if True, snapshot includes per-coordinate
            raw biome temperature

        Returns
        - The empty snapshot.
        """
        ...


    def setSpawnFlags(self, allowMonsters: bool, allowAnimals: bool) -> None:
        """
        Sets the spawn flags for this.

        Arguments
        - allowMonsters: - if True, monsters are allowed to spawn in this
            world.
        - allowAnimals: - if True, animals are allowed to spawn in this
            world.
        """
        ...


    def getAllowAnimals(self) -> bool:
        """
        Gets whether animals can spawn in this world.

        Returns
        - whether animals can spawn in this world.
        """
        ...


    def getAllowMonsters(self) -> bool:
        """
        Gets whether monsters can spawn in this world.

        Returns
        - whether monsters can spawn in this world.
        """
        ...


    def getBiome(self, x: int, z: int) -> "Biome":
        """
        Gets the biome for the given block coordinates.

        Arguments
        - x: X coordinate of the block
        - z: Z coordinate of the block

        Returns
        - Biome of the requested block

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def setBiome(self, x: int, z: int, bio: "Biome") -> None:
        """
        Sets the biome for the given block coordinates

        Arguments
        - x: X coordinate of the block
        - z: Z coordinate of the block
        - bio: new Biome type for this block

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def getTemperature(self, x: int, z: int) -> float:
        """
        Gets the temperature for the given block coordinates.
        
        It is safe to run this method when the block does not exist, it will
        not create the block.
        
        This method will return the raw temperature without adjusting for block
        height effects.

        Arguments
        - x: X coordinate of the block
        - z: Z coordinate of the block

        Returns
        - Temperature of the requested block

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def getTemperature(self, x: int, y: int, z: int) -> float:
        """
        Gets the temperature for the given block coordinates.
        
        It is safe to run this method when the block does not exist, it will
        not create the block.
        
        This method will return the raw temperature without adjusting for block
        height effects.

        Arguments
        - x: X coordinate of the block
        - y: Y coordinate of the block
        - z: Z coordinate of the block

        Returns
        - Temperature of the requested block
        """
        ...


    def getHumidity(self, x: int, z: int) -> float:
        """
        Gets the humidity for the given block coordinates.
        
        It is safe to run this method when the block does not exist, it will
        not create the block.

        Arguments
        - x: X coordinate of the block
        - z: Z coordinate of the block

        Returns
        - Humidity of the requested block

        Deprecated
        - biomes are now 3-dimensional
        """
        ...


    def getHumidity(self, x: int, y: int, z: int) -> float:
        """
        Gets the humidity for the given block coordinates.
        
        It is safe to run this method when the block does not exist, it will
        not create the block.

        Arguments
        - x: X coordinate of the block
        - y: Y coordinate of the block
        - z: Z coordinate of the block

        Returns
        - Humidity of the requested block
        """
        ...


    def getLogicalHeight(self) -> int:
        """
        Gets the maximum height to which chorus fruits and nether portals can
        bring players within this dimension.
        
        This excludes portals that were already built above the limit as they
        still connect normally. May not be greater than .getMaxHeight().

        Returns
        - maximum logical height for chorus fruits and nether portals
        """
        ...


    def isNatural(self) -> bool:
        """
        Gets if this world is natural.
        
        When False, compasses spin randomly, and using a bed to set the respawn
        point or sleep, is disabled. When True, nether portals can spawn
        zombified piglins.

        Returns
        - True if world is natural
        """
        ...


    def isBedWorks(self) -> bool:
        """
        Gets if beds work in this world.
        
        A non-working bed will blow up when trying to sleep. .isNatural()
        defines if a bed can be used to set spawn point.

        Returns
        - True if beds work in this world
        """
        ...


    def hasSkyLight(self) -> bool:
        """
        Gets if this world has skylight access.

        Returns
        - True if this world has skylight access
        """
        ...


    def hasCeiling(self) -> bool:
        """
        Gets if this world has a ceiling.

        Returns
        - True if this world has a bedrock ceiling
        """
        ...


    def isPiglinSafe(self) -> bool:
        """
        Gets if this world allow to piglins to survive without shaking and
        transforming to zombified piglins.

        Returns
        - True if piglins will not transform to zombified piglins
        """
        ...


    def isRespawnAnchorWorks(self) -> bool:
        """
        Gets if this world allows players to charge and use respawn anchors.

        Returns
        - True if players can charge and use respawn anchors
        """
        ...


    def hasRaids(self) -> bool:
        """
        Gets if players with the bad omen effect in this world will trigger a
        raid.

        Returns
        - True if raids will be triggered
        """
        ...


    def isUltraWarm(self) -> bool:
        """
        Gets if various water/lava mechanics will be triggered in this world, eg:
        
        
        - Water is evaporated
        - Sponges dry
        - Lava spreads faster and further

        Returns
        - True if this world has the above mechanics
        """
        ...


    def getSeaLevel(self) -> int:
        """
        Gets the sea level for this world.
        
        This is often half of .getMaxHeight()

        Returns
        - Sea level
        """
        ...


    def getKeepSpawnInMemory(self) -> bool:
        """
        Gets whether the world's spawn area should be kept loaded into memory
        or not.

        Returns
        - True if the world's spawn area will be kept loaded into memory.
        """
        ...


    def setKeepSpawnInMemory(self, keepLoaded: bool) -> None:
        """
        Sets whether the world's spawn area should be kept loaded into memory
        or not.

        Arguments
        - keepLoaded: if True then the world's spawn area will be kept
            loaded into memory.
        """
        ...


    def isAutoSave(self) -> bool:
        """
        Gets whether or not the world will automatically save

        Returns
        - True if the world will automatically save, otherwise False
        """
        ...


    def setAutoSave(self, value: bool) -> None:
        """
        Sets whether or not the world will automatically save

        Arguments
        - value: True if the world should automatically save, otherwise
            False
        """
        ...


    def setDifficulty(self, difficulty: "Difficulty") -> None:
        """
        Sets the Difficulty of the world.

        Arguments
        - difficulty: the new difficulty you want to set the world to
        """
        ...


    def getDifficulty(self) -> "Difficulty":
        """
        Gets the Difficulty of the world.

        Returns
        - The difficulty of the world.
        """
        ...


    def getWorldFolder(self) -> "File":
        """
        Gets the folder of this world on disk.

        Returns
        - The folder of this world.
        """
        ...


    def getWorldType(self) -> "WorldType":
        """
        Gets the type of this world.

        Returns
        - Type of this world.

        Deprecated
        - world type is only used to select the default word generation
        settings and is not stored in Vanilla worlds, making it impossible for
        this method to always return the correct value.
        """
        ...


    def canGenerateStructures(self) -> bool:
        """
        Gets whether or not structures are being generated.

        Returns
        - True if structures are being generated.
        """
        ...


    def isHardcore(self) -> bool:
        """
        Gets whether the world is hardcore or not.
        
        In a hardcore world the difficulty is locked to hard.

        Returns
        - hardcore status
        """
        ...


    def setHardcore(self, hardcore: bool) -> None:
        """
        Sets whether the world is hardcore or not.
        
        In a hardcore world the difficulty is locked to hard.

        Arguments
        - hardcore: Whether the world is hardcore
        """
        ...


    def getTicksPerAnimalSpawns(self) -> int:
        """
        Gets the world's ticks per animal spawns value
        
        This value determines how many ticks there are between attempts to
        spawn animals.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn animals in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn animals
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, animal spawning will be disabled for this world. We
        recommend using .setSpawnFlags(boolean, boolean) to control
        this instead.
        
        Minecraft default: 400.

        Returns
        - The world's ticks per animal spawns value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerAnimalSpawns(self, ticksPerAnimalSpawns: int) -> None:
        """
        Sets the world's ticks per animal spawns value
        
        This value determines how many ticks there are between attempts to
        spawn animals.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn animals in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn animals
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, animal spawning will be disabled for this world. We
        recommend using .setSpawnFlags(boolean, boolean) to control
        this instead.
        
        Minecraft default: 400.

        Arguments
        - ticksPerAnimalSpawns: the ticks per animal spawns value you want
            to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerMonsterSpawns(self) -> int:
        """
        Gets the world's ticks per monster spawns value
        
        This value determines how many ticks there are between attempts to
        spawn monsters.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn monsters in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn monsters
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, monsters spawning will be disabled for this world. We
        recommend using .setSpawnFlags(boolean, boolean) to control
        this instead.
        
        Minecraft default: 1.

        Returns
        - The world's ticks per monster spawns value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerMonsterSpawns(self, ticksPerMonsterSpawns: int) -> None:
        """
        Sets the world's ticks per monster spawns value
        
        This value determines how many ticks there are between attempts to
        spawn monsters.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn monsters in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn monsters
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, monsters spawning will be disabled for this world. We
        recommend using .setSpawnFlags(boolean, boolean) to control
        this instead.
        
        Minecraft default: 1.

        Arguments
        - ticksPerMonsterSpawns: the ticks per monster spawns value you
            want to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerWaterSpawns(self) -> int:
        """
        Gets the world's ticks per water mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn water mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water mobs in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn water mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, water mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Returns
        - The world's ticks per water mob spawns value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerWaterSpawns(self, ticksPerWaterSpawns: int) -> None:
        """
        Sets the world's ticks per water mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn water mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water mobs in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn water mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, water mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - ticksPerWaterSpawns: the ticks per water mob spawns value you
            want to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerWaterAmbientSpawns(self) -> int:
        """
        Gets the default ticks per water ambient mob spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water ambient mobs
            every tick.
        - A value of 400 will mean the server will attempt to spawn water ambient mobs
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, ambient mobs spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per water ambient mobs spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerWaterAmbientSpawns(self, ticksPerAmbientSpawns: int) -> None:
        """
        Sets the world's ticks per water ambient mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn water ambient mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water ambient mobs in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn water ambient mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, water ambient mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - ticksPerAmbientSpawns: the ticks per water ambient mob spawns value you
            want to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerWaterUndergroundCreatureSpawns(self) -> int:
        """
        Gets the default ticks per water underground creature spawns value.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water underground creature
            every tick.
        - A value of 400 will mean the server will attempt to spawn water underground creature
            every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:** If set to 0, water underground creature spawning will be disabled.
        
        Minecraft default: 1.

        Returns
        - the default ticks per water underground creature spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerWaterUndergroundCreatureSpawns(self, ticksPerWaterUndergroundCreatureSpawns: int) -> None:
        """
        Sets the world's ticks per water underground creature spawns value
        
        This value determines how many ticks there are between attempts to
        spawn water underground creature.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn water underground creature in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn water underground creature
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, water underground creature spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - ticksPerWaterUndergroundCreatureSpawns: the ticks per water underground creature spawns value you
            want to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerAmbientSpawns(self) -> int:
        """
        Gets the world's ticks per ambient mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn ambient mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn ambient mobs in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn ambient mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, ambient mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Returns
        - the default ticks per ambient mobs spawn value

        Deprecated
        - Deprecated in favor of .getTicksPerSpawns(SpawnCategory)
        """
        ...


    def setTicksPerAmbientSpawns(self, ticksPerAmbientSpawns: int) -> None:
        """
        Sets the world's ticks per ambient mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn ambient mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn ambient mobs in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn ambient mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, ambient mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - ticksPerAmbientSpawns: the ticks per ambient mob spawns value you
            want to set the world to

        Deprecated
        - Deprecated in favor of .setTicksPerSpawns(SpawnCategory, int)
        """
        ...


    def getTicksPerSpawns(self, spawnCategory: "SpawnCategory") -> int:
        """
        Gets the world's ticks per SpawnCategory mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn SpawnCategory mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn SpawnCategory mobs in
            this world every tick.
        - A value of 400 will mean the server will attempt to spawn SpawnCategory mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, SpawnCategory mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - spawnCategory: the category spawn

        Returns
        - The world's ticks per SpawnCategory mob spawns value
        """
        ...


    def setTicksPerSpawns(self, spawnCategory: "SpawnCategory", ticksPerCategorySpawn: int) -> None:
        """
        Sets the world's ticks per SpawnCategory mob spawns value
        
        This value determines how many ticks there are between attempts to
        spawn SpawnCategory mobs.
        
        **Example Usage:**
        
        - A value of 1 will mean the server will attempt to spawn SpawnCategory mobs in
            this world on every tick.
        - A value of 400 will mean the server will attempt to spawn SpawnCategory mobs
            in this world every 400th tick.
        - A value below 0 will be reset back to Minecraft's default.
        
        
        **Note:**
        If set to 0, SpawnCategory mobs spawning will be disabled for this world.
        
        Minecraft default: 1.

        Arguments
        - spawnCategory: the category spawn
        - ticksPerCategorySpawn: the ticks per SpawnCategory mob spawns value you
            want to set the world to
        """
        ...


    def getMonsterSpawnLimit(self) -> int:
        """
        Gets limit for number of monsters that can spawn in a chunk in this
        world

        Returns
        - The monster spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setMonsterSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of monsters that can spawn in a chunk in this
        world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .setSpawnLimit(SpawnCategory, int)
        """
        ...


    def getAnimalSpawnLimit(self) -> int:
        """
        Gets the limit for number of animals that can spawn in a chunk in this
        world

        Returns
        - The animal spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setAnimalSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of animals that can spawn in a chunk in this
        world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def getWaterAnimalSpawnLimit(self) -> int:
        """
        Gets the limit for number of water animals that can spawn in a chunk in
        this world

        Returns
        - The water animal spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setWaterAnimalSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of water animals that can spawn in a chunk in
        this world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .setSpawnLimit(SpawnCategory, int)
        """
        ...


    def getWaterUndergroundCreatureSpawnLimit(self) -> int:
        """
        Gets the limit for number of water underground creature that can spawn in a chunk in
        this world

        Returns
        - The water underground creature spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setWaterUndergroundCreatureSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of water underground creature that can spawn in a chunk in
        this world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .setSpawnLimit(SpawnCategory, int)
        """
        ...


    def getWaterAmbientSpawnLimit(self) -> int:
        """
        Gets user-specified limit for number of water ambient mobs that can spawn
        in a chunk.

        Returns
        - the water ambient spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setWaterAmbientSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of water ambient mobs that can spawn in a chunk
        in this world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .setSpawnLimit(SpawnCategory, int)
        """
        ...


    def getAmbientSpawnLimit(self) -> int:
        """
        Gets the limit for number of ambient mobs that can spawn in a chunk in
        this world

        Returns
        - The ambient spawn limit

        Deprecated
        - Deprecated in favor of .getSpawnLimit(SpawnCategory)
        """
        ...


    def setAmbientSpawnLimit(self, limit: int) -> None:
        """
        Sets the limit for number of ambient mobs that can spawn in a chunk in
        this world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - limit: the new mob limit

        Deprecated
        - Deprecated in favor of .setSpawnLimit(SpawnCategory, int)
        """
        ...


    def getSpawnLimit(self, spawnCategory: "SpawnCategory") -> int:
        """
        Gets the limit for number of SpawnCategory entities that can spawn in a chunk in
        this world

        Arguments
        - spawnCategory: the entity category

        Returns
        - The ambient spawn limit
        """
        ...


    def setSpawnLimit(self, spawnCategory: "SpawnCategory", limit: int) -> None:
        """
        Sets the limit for number of SpawnCategory entities that can spawn in a chunk in
        this world
        
        **Note:** If set to a negative number the world will use the
        server-wide spawn limit instead.

        Arguments
        - spawnCategory: the entity category
        - limit: the new mob limit
        """
        ...


    def playNote(self, loc: "Location", instrument: "Instrument", note: "Note") -> None:
        """
        Play a note at the provided Location in the World. 
        This *will* work with cake.
        
        This method will fail silently when called with Instrument.CUSTOM_HEAD.

        Arguments
        - loc: The location to play the note
        - instrument: The instrument
        - note: The note
        """
        ...


    def playSound(self, location: "Location", sound: "Sound", volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.
        
        This function will fail silently if Location or Sound are null.

        Arguments
        - location: The location to play the sound
        - sound: The sound to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: str, volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.
        
        This function will fail silently if Location or Sound are null. No
        sound will be heard by the players if their clients do not have the
        respective sound for the value passed.

        Arguments
        - location: The location to play the sound
        - sound: The internal sound name to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: "Sound", category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.
        
        This function will fail silently if Location or Sound are null.

        Arguments
        - location: The location to play the sound
        - sound: The sound to play
        - category: the category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: str, category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.
        
        This function will fail silently if Location or Sound are null. No sound
        will be heard by the players if their clients do not have the respective
        sound for the value passed.

        Arguments
        - location: The location to play the sound
        - sound: The internal sound name to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, location: "Location", sound: "Sound", category: "SoundCategory", volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the provided Location in the World. For sounds with multiple
        variations passing the same seed will always play the same variation.
        
        This function will fail silently if Location or Sound are null.

        Arguments
        - location: The location to play the sound
        - sound: The sound to play
        - category: the category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        - seed: The seed for the sound
        """
        ...


    def playSound(self, location: "Location", sound: str, category: "SoundCategory", volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the provided Location in the World. For sounds with multiple
        variations passing the same seed will always play the same variation.
        
        This function will fail silently if Location or Sound are null. No sound will
        be heard by the players if their clients do not have the respective sound for
        the value passed.

        Arguments
        - location: The location to play the sound
        - sound: The internal sound name to play
        - category: the category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        - seed: The seed for the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: "Sound", volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: str, volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: "Sound", category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: str, category: "SoundCategory", volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: "Sound", category: "SoundCategory", volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the location of the provided entity in the World. For sounds
        with multiple variations passing the same seed will always play the same
        variation.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        - seed: The seed for the sound
        """
        ...


    def playSound(self, entity: "Entity", sound: str, category: "SoundCategory", volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the location of the provided entity in the World. For sounds
        with multiple variations passing the same seed will always play the same
        variation.
        
        This function will fail silently if Entity or Sound are null.

        Arguments
        - entity: The entity to play the sound
        - sound: The sound to play
        - category: The category of the sound
        - volume: The volume of the sound
        - pitch: The pitch of the sound
        - seed: The seed for the sound
        """
        ...


    def getGameRules(self) -> list[str]:
        """
        Get an array containing the names of all the GameRules.

        Returns
        - An array of GameRule names.
        """
        ...


    def getGameRuleValue(self, rule: str) -> str:
        """
        Gets the current state of the specified rule
        
        Will return null if rule passed is null

        Arguments
        - rule: Rule to look up value of

        Returns
        - String value of rule

        Deprecated
        - use .getGameRuleValue(GameRule) instead
        """
        ...


    def setGameRuleValue(self, rule: str, value: str) -> bool:
        """
        Set the specified gamerule to specified value.
        
        The rule may attempt to validate the value passed, will return True if
        value was set.
        
        If rule is null, the function will return False.

        Arguments
        - rule: Rule to set
        - value: Value to set rule to

        Returns
        - True if rule was set

        Deprecated
        - use .setGameRule(GameRule, Object) instead.
        """
        ...


    def isGameRule(self, rule: str) -> bool:
        """
        Checks if string is a valid game rule

        Arguments
        - rule: Rule to check

        Returns
        - True if rule exists
        """
        ...


    def getGameRuleValue(self, rule: "GameRule"["T"]) -> "T":
        """
        Get the current value for a given GameRule.
        
        Type `<T>`: the GameRule's type

        Arguments
        - rule: the GameRule to check

        Returns
        - the current value
        """
        ...


    def getGameRuleDefault(self, rule: "GameRule"["T"]) -> "T":
        """
        Get the default value for a given GameRule. This value is not
        guaranteed to match the current value.
        
        Type `<T>`: the type of GameRule

        Arguments
        - rule: the rule to return a default value for

        Returns
        - the default value
        """
        ...


    def setGameRule(self, rule: "GameRule"["T"], newValue: "T") -> bool:
        """
        Set the given GameRule's new value.
        
        Type `<T>`: the value type of the GameRule

        Arguments
        - rule: the GameRule to update
        - newValue: the new value

        Returns
        - True if the value was successfully set
        """
        ...


    def getWorldBorder(self) -> "WorldBorder":
        """
        Gets the world border for this world.

        Returns
        - The world border for this world.
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T") -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        """
        ...


    def spawnParticle(self, particle: "Particle", location: "Location", count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T", force: bool) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - location: the location to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        - force: whether to send the particle to players within an extended
                     range and encourage their client to render it regardless of
                     settings
        """
        ...


    def spawnParticle(self, particle: "Particle", x: float, y: float, z: float, count: int, offsetX: float, offsetY: float, offsetZ: float, extra: float, data: "T", force: bool) -> None:
        """
        Spawns the particle (the number of times specified by count)
        at the target location. The position of each particle will be
        randomized positively and negatively by the offset parameters
        on each axis.
        
        Type `<T>`: type of particle data (see Particle.getDataType()

        Arguments
        - particle: the particle to spawn
        - x: the position on the x axis to spawn at
        - y: the position on the y axis to spawn at
        - z: the position on the z axis to spawn at
        - count: the number of particles
        - offsetX: the maximum random offset on the X axis
        - offsetY: the maximum random offset on the Y axis
        - offsetZ: the maximum random offset on the Z axis
        - extra: the extra data for this particle, depends on the
                     particle used (normally speed)
        - data: the data to use for the particle or null,
                    the type of this depends on Particle.getDataType()
        - force: whether to send the particle to players within an extended
                     range and encourage their client to render it regardless of
                     settings
        """
        ...


    def locateNearestStructure(self, origin: "Location", structureType: "org.bukkit.StructureType", radius: int, findUnexplored: bool) -> "Location":
        """
        Find the closest nearby structure of a given StructureType.
        Finding unexplored structures can, and will, block if the world is
        looking in chunks that gave not generated yet. This can lead to the world
        temporarily freezing while locating an unexplored structure.
        
        The `radius` is not a rigid square radius. Each structure may alter
        how many chunks to check for each iteration. Do not assume that only a
        radius x radius chunk area will be checked. For example,
        StructureType.WOODLAND_MANSION can potentially check up to 20,000
        blocks away (or more) regardless of the radius used.
        
        This will *not* load or generate chunks. This can also lead to
        instances where the server can hang if you are only looking for
        unexplored structures. This is because it will keep looking further and
        further out in order to find the structure.

        Arguments
        - origin: where to start looking for a structure
        - structureType: the type of structure to find
        - radius: the radius, in chunks, around which to search
        - findUnexplored: True to only find unexplored structures

        Returns
        - the closest Location, or null if no structure of the
        specified type exists.

        See
        - .locateNearestStructure(Location, StructureType, int, boolean)

        Deprecated
        - Use
        .locateNearestStructure(Location, Structure, int, boolean) or
        .locateNearestStructure(Location, StructureType, int, boolean)
        instead.
        """
        ...


    def locateNearestStructure(self, origin: "Location", structureType: "StructureType", radius: int, findUnexplored: bool) -> "StructureSearchResult":
        """
        Find the closest nearby structure of a given StructureType.
        Finding unexplored structures can, and will, block if the world is
        looking in chunks that gave not generated yet. This can lead to the world
        temporarily freezing while locating an unexplored structure.
        
        The `radius` is not a rigid square radius. Each structure may alter
        how many chunks to check for each iteration. Do not assume that only a
        radius x radius chunk area will be checked. For example,
        StructureType.WOODLAND_MANSION can potentially check up to 20,000
        blocks away (or more) regardless of the radius used.
        
        This will *not* load or generate chunks. This can also lead to
        instances where the server can hang if you are only looking for
        unexplored structures. This is because it will keep looking further and
        further out in order to find the structure.
        
        The difference between searching for a StructureType and a
        Structure is, that a StructureType can refer to multiple
        Structure Structures while searching for a Structure
        while only search for the given Structure.

        Arguments
        - origin: where to start looking for a structure
        - structureType: the type of structure to find
        - radius: the radius, in chunks, around which to search
        - findUnexplored: True to only find unexplored structures

        Returns
        - the closest Location and Structure, or null if no
        structure of the specified type exists.

        See
        - .locateNearestStructure(Location, Structure, int, boolean)
        """
        ...


    def locateNearestStructure(self, origin: "Location", structure: "Structure", radius: int, findUnexplored: bool) -> "StructureSearchResult":
        """
        Find the closest nearby structure of a given Structure. Finding
        unexplored structures can, and will, block if the world is looking in
        chunks that gave not generated yet. This can lead to the world
        temporarily freezing while locating an unexplored structure.
        
        The `radius` is not a rigid square radius. Each structure may alter
        how many chunks to check for each iteration. Do not assume that only a
        radius x radius chunk area will be checked. For example,
        Structure.MANSION can potentially check up to 20,000 blocks away
        (or more) regardless of the radius used.
        
        This will *not* load or generate chunks. This can also lead to
        instances where the server can hang if you are only looking for
        unexplored structures. This is because it will keep looking further and
        further out in order to find the structure.
        
        The difference between searching for a StructureType and a
        Structure is, that a StructureType can refer to multiple
        Structure Structures while searching for a Structure
        while only search for the given Structure.

        Arguments
        - origin: where to start looking for a structure
        - structure: the structure to find
        - radius: the radius, in chunks, around which to search
        - findUnexplored: True to only find unexplored structures

        Returns
        - the closest Location and Structure, or null if no
        structure was found.

        See
        - .locateNearestStructure(Location, StructureType, int, boolean)
        """
        ...


    def getViewDistance(self) -> int:
        """
        Returns the view distance used for this world.

        Returns
        - the view distance used for this world
        """
        ...


    def getSimulationDistance(self) -> int:
        """
        Returns the simulation distance used for this world.

        Returns
        - the simulation distance used for this world
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    def locateNearestBiome(self, origin: "Location", radius: int, *biomes: Tuple["Biome", ...]) -> "BiomeSearchResult":
        """
        Find the closest nearby location with a biome matching the provided
        Biome(s). Finding biomes can, and will, block if the world is looking
        in chunks that have not generated yet. This can lead to the world temporarily
        freezing while locating a biome.
        
        **Note:** This will *not* reflect changes made to the world after
        generation, this method only sees the biome at the time of world generation.
        This will *not* load or generate chunks.
        
        If multiple biomes are provided BiomeSearchResult.getBiome() will
        indicate which one was located.
        
        This method will use a horizontal interval of 32 and a vertical interval of
        64, equal to the /locate command.

        Arguments
        - origin: where to start looking for a biome
        - radius: the radius, in blocks, around which to search
        - biomes: the biomes to search for

        Returns
        - a BiomeSearchResult containing the closest Location and
                Biome, or null if no biome was found.

        See
        - .locateNearestBiome(Location, int, int, int, Biome...)
        """
        ...


    def locateNearestBiome(self, origin: "Location", radius: int, horizontalInterval: int, verticalInterval: int, *biomes: Tuple["Biome", ...]) -> "BiomeSearchResult":
        """
        Find the closest nearby location with a biome matching the provided
        Biome(s). Finding biomes can, and will, block if the world is looking
        in chunks that have not generated yet. This can lead to the world temporarily
        freezing while locating a biome.
        
        **Note:** This will *not* reflect changes made to the world after
        generation, this method only sees the biome at the time of world generation.
        This will *not* load or generate chunks.
        
        If multiple biomes are provided BiomeSearchResult.getBiome() will
        indicate which one was located. Higher values for `horizontalInterval`
        and `verticalInterval` will result in faster searches, but may lead to
        small biomes being missed.

        Arguments
        - origin: where to start looking for a biome
        - radius: the radius, in blocks, around which to search
        - horizontalInterval: the horizontal distance between each check
        - verticalInterval: the vertical distance between each check
        - biomes: the biomes to search for

        Returns
        - a BiomeSearchResult containing the closest Location and
                Biome, or null if no biome was found.

        See
        - .locateNearestBiome(Location, int, Biome...)
        """
        ...


    def locateNearestRaid(self, location: "Location", radius: int) -> "Raid":
        """
        Finds the nearest raid close to the given location.

        Arguments
        - location: the origin location
        - radius: the radius

        Returns
        - the closest Raid, or null if no raids were found
        """
        ...


    def getRaids(self) -> list["Raid"]:
        """
        Gets all raids that are going on over this world.

        Returns
        - the list of all active raids
        """
        ...


    def getEnderDragonBattle(self) -> "DragonBattle":
        """
        Get the DragonBattle associated with this world.
        
        If this world's environment is not Environment.THE_END, null will
        be returned.
        
        If an end world, a dragon battle instance will be returned regardless of
        whether or not a dragon is present in the world or a fight sequence has
        been activated. The dragon battle instance acts as a state holder.

        Returns
        - the dragon battle instance
        """
        ...


    def getFeatureFlags(self) -> set["FeatureFlag"]:
        """
        Get all FeatureFlag enabled in this world.

        Returns
        - all enabled FeatureFlag
        """
        ...


    class Spigot:

        def strikeLightning(self, loc: "Location", isSilent: bool) -> "LightningStrike":
            """
            Strikes lightning at the given Location and possibly without sound

            Arguments
            - loc: The location to strike lightning
            - isSilent: Whether this strike makes no sound

            Returns
            - The lightning entity.
            """
            ...


        def strikeLightningEffect(self, loc: "Location", isSilent: bool) -> "LightningStrike":
            """
            Strikes lightning at the given Location without doing damage and possibly without sound

            Arguments
            - loc: The location to strike lightning
            - isSilent: Whether this strike makes no sound

            Returns
            - The lightning entity.
            """
            ...


    class Environment(Enum):
        """
        Represents various map environment types that a world may be
        """

        NORMAL = (0)
        """
        Represents the "normal"/"surface world" map
        """
        NETHER = (-1)
        """
        Represents a nether based map ("hell")
        """
        THE_END = (1)
        """
        Represents the "end" map
        """
        CUSTOM = (-999)
        """
        Represents a custom dimension
        """


        def getId(self) -> int:
            """
            Gets the dimension ID of this environment

            Returns
            - dimension ID

            Deprecated
            - Magic value
            """
            ...


        @staticmethod
        def getEnvironment(id: int) -> "Environment":
            """
            Get an environment by ID

            Arguments
            - id: The ID of the environment

            Returns
            - The environment

            Deprecated
            - Magic value
            """
            ...
