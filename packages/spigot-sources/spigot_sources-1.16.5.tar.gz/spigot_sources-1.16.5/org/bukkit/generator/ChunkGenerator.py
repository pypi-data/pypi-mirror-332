"""
Python module generated from Java source file org.bukkit.generator.ChunkGenerator

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import Bukkit
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import World
from org.bukkit.block import Biome
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.generator import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class ChunkGenerator:
    """
    A chunk generator is responsible for the initial shaping of an entire
    chunk. For example, the nether chunk generator should shape netherrack and
    soulsand.
    
    By default only one thread will call
    .generateChunkData(org.bukkit.World, java.util.Random, int, int, org.bukkit.generator.ChunkGenerator.BiomeGrid)
    at a time, although this may not necessarily be the main server thread.
    
    If your generator is capable of fully asynchronous generation, then
    .isParallelCapable() should be overridden accordingly to allow
    multiple concurrent callers.
    
    Some aspects of world generation can be delegated to the Vanilla generator.
    The methods ChunkGenerator.shouldGenerateCaves(), ChunkGenerator.shouldGenerateDecorations(),
    ChunkGenerator.shouldGenerateMobs() and ChunkGenerator.shouldGenerateStructures() can be
    overridden to enable this.
    """

    def generateChunkData(self, world: "World", random: "Random", x: int, z: int, biome: "BiomeGrid") -> "ChunkData":
        """
        Shapes the chunk for the given coordinates.
        
        This method must return a ChunkData.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at
        the passed coordinates, as doing so may cause an infinite loop
        
        This method should **never** modify a ChunkData after it has
        been returned.
        
        This method **must** return a ChunkData returned by ChunkGenerator.createChunkData(org.bukkit.World)

        Arguments
        - world: The world this chunk will be used for
        - random: The random generator to use
        - x: The X-coordinate of the chunk
        - z: The Z-coordinate of the chunk
        - biome: Proposed biome values for chunk - can be updated by
            generator

        Returns
        - ChunkData containing the types for each block created by this
            generator
        """
        ...


    def canSpawn(self, world: "World", x: int, z: int) -> bool:
        """
        Tests if the specified location is valid for a natural spawn position

        Arguments
        - world: The world we're testing on
        - x: X-coordinate of the block to test
        - z: Z-coordinate of the block to test

        Returns
        - True if the location is valid, otherwise False
        """
        ...


    def getDefaultPopulators(self, world: "World") -> list["BlockPopulator"]:
        """
        Gets a list of default BlockPopulators to apply to a given
        world

        Arguments
        - world: World to apply to

        Returns
        - List containing any amount of BlockPopulators
        """
        ...


    def getFixedSpawnLocation(self, world: "World", random: "Random") -> "Location":
        """
        Gets a fixed spawn location to use for a given world.
        
        A null value is returned if a world should not use a fixed spawn point,
        and will instead attempt to find one randomly.

        Arguments
        - world: The world to locate a spawn point for
        - random: Random generator to use in the calculation

        Returns
        - Location containing a new spawn point, otherwise null
        """
        ...


    def isParallelCapable(self) -> bool:
        """
        Gets if this ChunkGenerator is parallel capable.
        
        See ChunkGenerator for more information.

        Returns
        - parallel capable status
        """
        ...


    def shouldGenerateCaves(self) -> bool:
        """
        Gets if the server should generate Vanilla caves after this
        ChunkGenerator.

        Returns
        - True if the server should generate Vanilla caves
        """
        ...


    def shouldGenerateDecorations(self) -> bool:
        """
        Gets if the server should generate Vanilla decorations after this
        ChunkGenerator.

        Returns
        - True if the server should generate Vanilla decorations
        """
        ...


    def shouldGenerateMobs(self) -> bool:
        """
        Gets if the server should generate Vanilla mobs after this
        ChunkGenerator.

        Returns
        - True if the server should generate Vanilla mobs
        """
        ...


    def shouldGenerateStructures(self) -> bool:
        """
        Gets if the server should generate Vanilla structures after this
        ChunkGenerator.

        Returns
        - True if the server should generate Vanilla structures
        """
        ...


    class BiomeGrid:
        """
        Interface to biome section for chunk to be generated: initialized with
        default values for world type and seed.
        
        Custom generator is free to access and tailor values during
        generateBlockSections() or generateExtBlockSections().
        """

        def getBiome(self, x: int, z: int) -> "Biome":
            """
            Get biome at x, z within chunk being generated

            Arguments
            - x: - 0-15
            - z: - 0-15

            Returns
            - Biome value

            Deprecated
            - biomes are now 3-dimensional
            """
            ...


        def getBiome(self, x: int, y: int, z: int) -> "Biome":
            """
            Get biome at x, z within chunk being generated

            Arguments
            - x: - 0-15
            - y: - 0-255
            - z: - 0-15

            Returns
            - Biome value
            """
            ...


        def setBiome(self, x: int, z: int, bio: "Biome") -> None:
            """
            Set biome at x, z within chunk being generated

            Arguments
            - x: - 0-15
            - z: - 0-15
            - bio: - Biome value

            Deprecated
            - biomes are now 3-dimensional
            """
            ...


        def setBiome(self, x: int, y: int, z: int, bio: "Biome") -> None:
            """
            Set biome at x, z within chunk being generated

            Arguments
            - x: - 0-15
            - y: - 0-255
            - z: - 0-15
            - bio: - Biome value
            """
            ...


    class ChunkData:
        """
        Data for a Chunk.
        """

        def getMaxHeight(self) -> int:
            """
            Get the maximum height for the chunk.
            
            Setting blocks at or above this height will do nothing.

            Returns
            - the maximum height
            """
            ...


        def setBlock(self, x: int, y: int, z: int, material: "Material") -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            
            Note: setting blocks outside the chunk's bounds does nothing.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive
            - material: the type to set the block to
            """
            ...


        def setBlock(self, x: int, y: int, z: int, material: "MaterialData") -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            
            Setting blocks outside the chunk's bounds does nothing.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive
            - material: the type to set the block to
            """
            ...


        def setBlock(self, x: int, y: int, z: int, blockData: "BlockData") -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            
            Setting blocks outside the chunk's bounds does nothing.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive
            - blockData: the type to set the block to
            """
            ...


        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, material: "Material") -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive)
            to xMax, yMax, zMax (exclusive) to material.
            
            Setting blocks outside the chunk's bounds does nothing.

            Arguments
            - xMin: minimum x location (inclusive) in the chunk to set
            - yMin: minimum y location (inclusive) in the chunk to set
            - zMin: minimum z location (inclusive) in the chunk to set
            - xMax: maximum x location (exclusive) in the chunk to set
            - yMax: maximum y location (exclusive) in the chunk to set
            - zMax: maximum z location (exclusive) in the chunk to set
            - material: the type to set the blocks to
            """
            ...


        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, material: "MaterialData") -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive)
            to xMax, yMax, zMax (exclusive) to material.
            
            Setting blocks outside the chunk's bounds does nothing.

            Arguments
            - xMin: minimum x location (inclusive) in the chunk to set
            - yMin: minimum y location (inclusive) in the chunk to set
            - zMin: minimum z location (inclusive) in the chunk to set
            - xMax: maximum x location (exclusive) in the chunk to set
            - yMax: maximum y location (exclusive) in the chunk to set
            - zMax: maximum z location (exclusive) in the chunk to set
            - material: the type to set the blocks to
            """
            ...


        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, blockData: "BlockData") -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive) to xMax,
            yMax, zMax (exclusive) to material.
            
            Setting blocks outside the chunk's bounds does nothing.

            Arguments
            - xMin: minimum x location (inclusive) in the chunk to set
            - yMin: minimum y location (inclusive) in the chunk to set
            - zMin: minimum z location (inclusive) in the chunk to set
            - xMax: maximum x location (exclusive) in the chunk to set
            - yMax: maximum y location (exclusive) in the chunk to set
            - zMax: maximum z location (exclusive) in the chunk to set
            - blockData: the type to set the blocks to
            """
            ...


        def getType(self, x: int, y: int, z: int) -> "Material":
            """
            Get the type of the block at x, y, z.
            
            Getting blocks outside the chunk's bounds returns air.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - the type of the block or Material.AIR if x, y or z are outside the chunk's bounds
            """
            ...


        def getTypeAndData(self, x: int, y: int, z: int) -> "MaterialData":
            """
            Get the type and data of the block at x, y, z.
            
            Getting blocks outside the chunk's bounds returns air.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - the type and data of the block or the MaterialData for air if x, y or z are outside the chunk's bounds
            """
            ...


        def getBlockData(self, x: int, y: int, z: int) -> "BlockData":
            """
            Get the type and data of the block at x, y, z.
            
            Getting blocks outside the chunk's bounds returns air.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - the data of the block or the BlockData for air if x, y or z are outside the chunk's bounds
            """
            ...


        def getData(self, x: int, y: int, z: int) -> int:
            """
            Get the block data at x,y,z in the chunk data.
            
            Getting blocks outside the chunk's bounds returns 0.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from 0 (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - the block data value or air if x, y or z are outside the chunk's bounds

            Deprecated
            - Uses magic values
            """
            ...
