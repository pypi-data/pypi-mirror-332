"""
Python module generated from Java source file org.bukkit.generator.ChunkGenerator

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import Bukkit
from org.bukkit import HeightMap
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
    
    A chunk is generated in multiple steps, those steps are always in the same
    order. Between those steps however an unlimited time may pass. This means, a
    chunk may generated until the surface step and continue with the bedrock step
    after one or multiple server restarts or even after multiple Minecraft
    versions.
    
    The order of generation is as follows
    <ol>
    - .generateNoise(WorldInfo, Random, int, int, ChunkData)
    - .generateSurface(WorldInfo, Random, int, int, ChunkData)
    - .generateBedrock(WorldInfo, Random, int, int, ChunkData)
    - .generateCaves(WorldInfo, Random, int, int, ChunkData)
    </ol>
    
    Every method listed above as well as
    .getBaseHeight(WorldInfo, Random, int, int, HeightMap)
    **must** be completely thread safe and able to handle multiple concurrent
    callers.
    
    Some aspects of world generation can be delegated to the Vanilla generator.
    The following methods can be overridden to enable this:
    
    - ChunkGenerator.shouldGenerateNoise() or ChunkGenerator.shouldGenerateNoise(WorldInfo, Random, int, int)
    - ChunkGenerator.shouldGenerateSurface() or ChunkGenerator.shouldGenerateSurface(WorldInfo, Random, int, int)
    - ChunkGenerator.shouldGenerateCaves() or ChunkGenerator.shouldGenerateCaves(WorldInfo, Random, int, int)
    - ChunkGenerator.shouldGenerateDecorations() or ChunkGenerator.shouldGenerateDecorations(WorldInfo, Random, int, int)
    - ChunkGenerator.shouldGenerateMobs() or ChunkGenerator.shouldGenerateMobs(WorldInfo, Random, int, int)
    - ChunkGenerator.shouldGenerateStructures() or ChunkGenerator.shouldGenerateStructures(WorldInfo, Random, int, int)
    """

    def generateNoise(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int, chunkData: "ChunkData") -> None:
        """
        Shapes the Chunk noise for the given coordinates.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        
        This method should **never** modify the ChunkData at a later
        point of time.
        
        The Y-coordinate range should **never** be hardcoded, to get the
        Y-coordinate range use the methods ChunkData.getMinHeight() and
        ChunkData.getMaxHeight().
        
        If .shouldGenerateNoise() is set to True, the given
        ChunkData contains already the Vanilla noise generation.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk
        - chunkData: To modify
        """
        ...


    def generateSurface(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int, chunkData: "ChunkData") -> None:
        """
        Shapes the Chunk surface for the given coordinates.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        
        This method should **never** modify the ChunkData at a later
        point of time.
        
        The Y-coordinate range should **never** be hardcoded, to get the
        Y-coordinate range use the methods ChunkData.getMinHeight() and
        ChunkData.getMaxHeight().
        
        If .shouldGenerateSurface() is set to True, the given
        ChunkData contains already the Vanilla surface generation.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk
        - chunkData: To modify
        """
        ...


    def generateBedrock(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int, chunkData: "ChunkData") -> None:
        """
        Shapes the Chunk bedrock layer for the given coordinates.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        
        This method should **never** modify the ChunkData at a later
        point of time.
        
        The Y-coordinate range should **never** be hardcoded, to get the
        Y-coordinate range use the methods ChunkData.getMinHeight() and
        ChunkData.getMaxHeight().

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk
        - chunkData: To modify
        """
        ...


    def generateCaves(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int, chunkData: "ChunkData") -> None:
        """
        Shapes the Chunk caves for the given coordinates.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        
        This method should **never** modify the ChunkData at a later
        point of time.
        
        The Y-coordinate range should **never** be hardcoded, to get the
        Y-coordinate range use the methods ChunkData.getMinHeight() and
        ChunkData.getMaxHeight().
        
        If .shouldGenerateCaves() is set to True, the given
        ChunkData contains already the Vanilla cave generation.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk
        - chunkData: To modify
        """
        ...


    def getDefaultBiomeProvider(self, worldInfo: "WorldInfo") -> "BiomeProvider":
        """
        Gets called when no BiomeProvider is set in
        org.bukkit.WorldCreator or via the server configuration files. It
        is therefore possible that one plugin can provide the Biomes and another
        one the generation.
        
        Notes:
        
        If `null` is returned, than Vanilla biomes are used.
        
        This method only gets called once when the world is loaded. Returning
        another BiomeProvider later one is not respected.

        Arguments
        - worldInfo: The world info of the world the biome provider will be
        used for

        Returns
        - BiomeProvider to use to fill the biomes of a chunk
        """
        ...


    def getBaseHeight(self, worldInfo: "WorldInfo", random: "Random", x: int, z: int, heightMap: "HeightMap") -> int:
        """
        This method is similar to
        World.getHighestBlockAt(int, int, HeightMap). With the difference
        being, that the highest y coordinate should be the block before any
        surface, bedrock, caves or decoration is applied. Or in other words the
        highest block when only the noise is present at the chunk.
        
        Notes:
        
        When this method is not overridden, the Vanilla base height is used.
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, or use the method
        World.getHighestBlockAt(int, int, HeightMap), as doing so may
        cause an infinite loop.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - x: The X-coordinate from world origin
        - z: The Z-coordinate from world origin
        - heightMap: From the highest block should be get

        Returns
        - The y coordinate of the highest block at the given location
        """
        ...


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

        Deprecated
        - The generation is now split up and the new methods should be used, see ChunkGenerator
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

        Deprecated
        - the chunk generation code should be thread safe
        """
        ...


    def shouldGenerateNoise(self) -> bool:
        """
        Gets if the server should generate Vanilla noise.
        
        The Vanilla noise is generated **before**
        .generateNoise(WorldInfo, Random, int, int, ChunkData) is called.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateNoise(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla noise

        See
        - .shouldGenerateNoise(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateNoise(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla noise.
        
        The Vanilla noise is generated **before**
        .generateNoise(WorldInfo, Random, int, int, ChunkData) is called.
        
        Only this method is called if both this and
        .shouldGenerateNoise() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla noise

        See
        - .shouldGenerateNoise()
        """
        ...


    def shouldGenerateSurface(self) -> bool:
        """
        Gets if the server should generate Vanilla surface.
        
        The Vanilla surface is generated **before**
        .generateSurface(WorldInfo, Random, int, int, ChunkData) is
        called.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateSurface(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla surface

        See
        - .shouldGenerateSurface(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateSurface(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla surface.
        
        The Vanilla surface is generated **before**
        .generateSurface(WorldInfo, Random, int, int, ChunkData) is
        called.
        
        Only this method is called if both this and
        .shouldGenerateSurface() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla surface

        See
        - .shouldGenerateSurface()
        """
        ...


    def shouldGenerateBedrock(self) -> bool:
        """
        Gets if the server should generate Vanilla bedrock.
        
        The Vanilla bedrock is generated **before**
        .generateBedrock(WorldInfo, Random, int, int, ChunkData) is
        called.

        Returns
        - True if the server should generate Vanilla bedrock

        Deprecated
        - has no effect, bedrock generation is part of the surface step, see .shouldGenerateSurface()
        """
        ...


    def shouldGenerateCaves(self) -> bool:
        """
        Gets if the server should generate Vanilla caves.
        
        The Vanilla caves are generated **before**
        .generateCaves(WorldInfo, Random, int, int, ChunkData) is called.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateCaves(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla caves

        See
        - .shouldGenerateCaves(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateCaves(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla caves.
        
        The Vanilla caves are generated **before**
        .generateCaves(WorldInfo, Random, int, int, ChunkData) is called.
        
        Only this method is called if both this and
        .shouldGenerateCaves() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla caves

        See
        - .shouldGenerateCaves()
        """
        ...


    def shouldGenerateDecorations(self) -> bool:
        """
        Gets if the server should generate Vanilla decorations after this
        ChunkGenerator.
        
        The Vanilla decoration are generated **before** any
        BlockPopulator are called.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateDecorations(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla decorations

        See
        - .shouldGenerateDecorations(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateDecorations(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla decorations after this
        ChunkGenerator.
        
        The Vanilla decoration are generated **before** any
        BlockPopulator are called.
        
        Only this method is called if both this and
        .shouldGenerateDecorations() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla decorations

        See
        - .shouldGenerateDecorations()
        """
        ...


    def shouldGenerateMobs(self) -> bool:
        """
        Gets if the server should generate Vanilla mobs after this
        ChunkGenerator.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateMobs(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla mobs

        See
        - .shouldGenerateMobs(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateMobs(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla mobs after this
        ChunkGenerator.
        
        Only this method is called if both this and
        .shouldGenerateMobs() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla mobs

        See
        - .shouldGenerateMobs()
        """
        ...


    def shouldGenerateStructures(self) -> bool:
        """
        Gets if the server should generate Vanilla structures after this
        ChunkGenerator.
        
        This is method is not called (and has therefore no effect), if
        .shouldGenerateStructures(WorldInfo, Random, int, int) is overridden.

        Returns
        - True if the server should generate Vanilla structures

        See
        - .shouldGenerateStructures(WorldInfo, Random, int, int)
        """
        ...


    def shouldGenerateStructures(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla structures after this
        ChunkGenerator.
        
        Only this method is called if both this and
        .shouldGenerateStructures() are overridden.

        Arguments
        - worldInfo: The world info of the world this chunk will be used for
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk

        Returns
        - True if the server should generate Vanilla structures

        See
        - .shouldGenerateStructures()
        """
        ...


    class BiomeGrid:
        """
        Interface to biome section for chunk to be generated: initialized with
        default values for world type and seed.
        
        Custom generator is free to access and tailor values during
        generateBlockSections() or generateExtBlockSections().

        Deprecated
        - Biomes are now set with BiomeProvider
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
            - y: - world minHeight (inclusive) - world maxHeight (exclusive)
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
            - y: - world minHeight (inclusive) - world maxHeight (exclusive)
            - z: - 0-15
            - bio: - Biome value
            """
            ...


    class ChunkData:
        """
        Data for a Chunk.
        """

        def getMinHeight(self) -> int:
            """
            Get the minimum height for this ChunkData.
            
            It is not guaranteed that this method will return the same value as
            World.getMinHeight().
            
            Setting blocks below this height will do nothing.

            Returns
            - the minimum height
            """
            ...


        def getMaxHeight(self) -> int:
            """
            Get the maximum height for this ChunkData.
            
            It is not guaranteed that this method will return the same value as
            World.getMaxHeight().
            
            Setting blocks at or above this height will do nothing.

            Returns
            - the maximum height
            """
            ...


        def getBiome(self, x: int, y: int, z: int) -> "Biome":
            """
            Get the biome at x, y, z within chunk being generated

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from minimum (inclusive) -
            maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - Biome value
            """
            ...


        def setBlock(self, x: int, y: int, z: int, material: "Material") -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            
            Note: setting blocks outside the chunk's bounds does nothing.

            Arguments
            - x: the x location in the chunk from 0-15 inclusive
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
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
            - y: the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            - z: the z location in the chunk from 0-15 inclusive

            Returns
            - the block data value or air if x, y or z are outside the chunk's bounds

            Deprecated
            - Uses magic values
            """
            ...
