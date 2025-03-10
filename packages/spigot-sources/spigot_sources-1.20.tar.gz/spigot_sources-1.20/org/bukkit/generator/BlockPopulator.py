"""
Python module generated from Java source file org.bukkit.generator.BlockPopulator

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import Chunk
from org.bukkit import World
from org.bukkit.event.world import WorldInitEvent
from org.bukkit.generator import *
from typing import Any, Callable, Iterable, Tuple


class BlockPopulator:
    """
    A block populator is responsible for generating a small area of blocks.
    
    For example, generating glowstone inside the nether or generating dungeons
    full of treasure
    
    A BlockPopulator can be used in combination with a custom ChunkGenerator
    by returning it in the method ChunkGenerator.getDefaultPopulators(World)
    or by adding it manually to the worlds populator list returned by World.getPopulators().
    
    When adding a BlockPopulator manually to a world it is recommended to do so during
    the WorldInitEvent.
    """

    def populate(self, world: "World", random: "Random", source: "Chunk") -> None:
        """
        Populates an area of blocks at or around the given chunk.
        
        The chunks on each side of the specified chunk must already exist; that
        is, there must be one north, east, south and west of the specified
        chunk. The "corner" chunks may not exist, in which scenario the
        populator should record any changes required for those chunks and
        perform the changes when they are ready.

        Arguments
        - world: The world to generate in
        - random: The random generator to use
        - source: The chunk to generate for

        Deprecated
        - Use .populate(WorldInfo, Random, int, int, LimitedRegion)
        """
        ...


    def populate(self, worldInfo: "WorldInfo", random: "Random", chunkX: int, chunkZ: int, limitedRegion: "LimitedRegion") -> None:
        """
        Populates an area of blocks at or around the given chunk.
        
        Notes:
        
        This method should **never** attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop
        
        This method should **never** modify a LimitedRegion at a later
        point of time.
        
        This method **must** be completely thread safe and able to handle
        multiple concurrent callers.
        
        No physics are applied, whether or not it is set to True in
        org.bukkit.block.BlockState.update(boolean, boolean)
        
        **Only** use the org.bukkit.block.BlockState returned by
        LimitedRegion,
        **never** use methods from a World to modify the chunk.

        Arguments
        - worldInfo: The world info of the world to generate in
        - random: The random generator to use
        - chunkX: The X-coordinate of the chunk
        - chunkZ: The Z-coordinate of the chunk
        - limitedRegion: The chunk region to populate
        """
        ...
