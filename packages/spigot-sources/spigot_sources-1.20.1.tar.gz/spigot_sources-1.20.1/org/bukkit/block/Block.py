"""
Python module generated from Java source file org.bukkit.block.Block

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Chunk
from org.bukkit import FluidCollisionMode
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import Translatable
from org.bukkit import World
from org.bukkit.block import *
from org.bukkit.block.data import Bisected
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.inventory import ItemStack
from org.bukkit.metadata import Metadatable
from org.bukkit.util import BoundingBox
from org.bukkit.util import RayTraceResult
from org.bukkit.util import Vector
from org.bukkit.util import VoxelShape
from typing import Any, Callable, Iterable, Tuple


class Block(Metadatable, Translatable):
    """
    Represents a block. This is a live object, and only one Block may exist for
    any given location in a world. The state of the block may change
    concurrently to your own handling of it; use block.getState() to get a
    snapshot state of a block which will not be modified.
    
    
    Note that parts of this class which require access to the world at large
    (i.e. lighting and power) may not be able to be safely accessed during world
    generation when used in cases like BlockPhysicsEvent!!!!
    """

    def getData(self) -> int:
        """
        Gets the metadata for this block

        Returns
        - block specific metadata

        Deprecated
        - Magic value
        """
        ...


    def getBlockData(self) -> "BlockData":
        """
        Gets the complete block data for this block

        Returns
        - block specific data
        """
        ...


    def getRelative(self, modX: int, modY: int, modZ: int) -> "Block":
        """
        Gets the block at the given offsets

        Arguments
        - modX: X-coordinate offset
        - modY: Y-coordinate offset
        - modZ: Z-coordinate offset

        Returns
        - Block at the given offsets
        """
        ...


    def getRelative(self, face: "BlockFace") -> "Block":
        """
        Gets the block at the given face
        
        This method is equal to getRelative(face, 1)

        Arguments
        - face: Face of this block to return

        Returns
        - Block at the given face

        See
        - .getRelative(BlockFace, int)
        """
        ...


    def getRelative(self, face: "BlockFace", distance: int) -> "Block":
        """
        Gets the block at the given distance of the given face
        
        For example, the following method places water at 100,102,100; two
        blocks above 100,100,100.
        
        ```
        Block block = world.getBlockAt(100, 100, 100);
        Block shower = block.getRelative(BlockFace.UP, 2);
        shower.setType(Material.WATER);
        ```

        Arguments
        - face: Face of this block to return
        - distance: Distance to get the block at

        Returns
        - Block at the given face
        """
        ...


    def getType(self) -> "Material":
        """
        Gets the type of this block

        Returns
        - block type
        """
        ...


    def getLightLevel(self) -> int:
        """
        Gets the light level between 0-15

        Returns
        - light level
        """
        ...


    def getLightFromSky(self) -> int:
        """
        Get the amount of light at this block from the sky.
        
        Any light given from other sources (such as blocks like torches) will
        be ignored.

        Returns
        - Sky light level
        """
        ...


    def getLightFromBlocks(self) -> int:
        """
        Get the amount of light at this block from nearby blocks.
        
        Any light given from other sources (such as the sun) will be ignored.

        Returns
        - Block light level
        """
        ...


    def getWorld(self) -> "World":
        """
        Gets the world which contains this Block

        Returns
        - World containing this block
        """
        ...


    def getX(self) -> int:
        """
        Gets the x-coordinate of this block

        Returns
        - x-coordinate
        """
        ...


    def getY(self) -> int:
        """
        Gets the y-coordinate of this block

        Returns
        - y-coordinate
        """
        ...


    def getZ(self) -> int:
        """
        Gets the z-coordinate of this block

        Returns
        - z-coordinate
        """
        ...


    def getLocation(self) -> "Location":
        """
        Gets the Location of the block

        Returns
        - Location of block
        """
        ...


    def getLocation(self, loc: "Location") -> "Location":
        """
        Stores the location of the block in the provided Location object.
        
        If the provided Location is null this method does nothing and returns
        null.

        Arguments
        - loc: the location to copy into

        Returns
        - The Location object provided or null
        """
        ...


    def getChunk(self) -> "Chunk":
        """
        Gets the chunk which contains this block

        Returns
        - Containing Chunk
        """
        ...


    def setBlockData(self, data: "BlockData") -> None:
        """
        Sets the complete data for this block

        Arguments
        - data: new block specific data
        """
        ...


    def setBlockData(self, data: "BlockData", applyPhysics: bool) -> None:
        """
        Sets the complete data for this block
        
        
        Note that applyPhysics = False is not in general safe. It should only be
        used when you need to avoid triggering a physics update of neighboring
        blocks, for example when creating a Bisected block. If you are
        using a custom populator, then this parameter may also be required to
        prevent triggering infinite chunk loads on border blocks. This method
        should NOT be used to "hack" physics by placing blocks in impossible
        locations. Such blocks are liable to be removed on various events such as
        world upgrades. Furthermore setting large amounts of such blocks in close
        proximity may overload the server physics engine if an update is
        triggered at a later point. If this occurs, the resulting behavior is
        undefined.

        Arguments
        - data: new block specific data
        - applyPhysics: False to cancel physics from the changed block
        """
        ...


    def setType(self, type: "Material") -> None:
        """
        Sets the type of this block

        Arguments
        - type: Material to change this block to
        """
        ...


    def setType(self, type: "Material", applyPhysics: bool) -> None:
        """
        Sets the type of this block
        
        
        Note that applyPhysics = False is not in general safe. It should only be
        used when you need to avoid triggering a physics update of neighboring
        blocks, for example when creating a Bisected block. If you are
        using a custom populator, then this parameter may also be required to
        prevent triggering infinite chunk loads on border blocks. This method
        should NOT be used to "hack" physics by placing blocks in impossible
        locations. Such blocks are liable to be removed on various events such as
        world upgrades. Furthermore setting large amounts of such blocks in close
        proximity may overload the server physics engine if an update is
        triggered at a later point. If this occurs, the resulting behavior is
        undefined.

        Arguments
        - type: Material to change this block to
        - applyPhysics: False to cancel physics on the changed block.
        """
        ...


    def getFace(self, block: "Block") -> "BlockFace":
        """
        Gets the face relation of this block compared to the given block.
        
        For example:
        ````Block current = world.getBlockAt(100, 100, 100);
        Block target = world.getBlockAt(100, 101, 100);
        
        current.getFace(target) == BlockFace.Up;````
        
        If the given block is not connected to this block, null may be returned

        Arguments
        - block: Block to compare against this block

        Returns
        - BlockFace of this block which has the requested block, or null
        """
        ...


    def getState(self) -> "BlockState":
        """
        Captures the current state of this block. You may then cast that state
        into any accepted type, such as Furnace or Sign.
        
        The returned object will never be updated, and you are not guaranteed
        that (for example) a sign is still a sign after you capture its state.

        Returns
        - BlockState with the current state of this block.
        """
        ...


    def getBiome(self) -> "Biome":
        """
        Returns the biome that this block resides in

        Returns
        - Biome type containing this block
        """
        ...


    def setBiome(self, bio: "Biome") -> None:
        """
        Sets the biome that this block resides in

        Arguments
        - bio: new Biome type for this block
        """
        ...


    def isBlockPowered(self) -> bool:
        """
        Returns True if the block is being powered by Redstone.

        Returns
        - True if the block is powered.
        """
        ...


    def isBlockIndirectlyPowered(self) -> bool:
        """
        Returns True if the block is being indirectly powered by Redstone.

        Returns
        - True if the block is indirectly powered.
        """
        ...


    def isBlockFacePowered(self, face: "BlockFace") -> bool:
        """
        Returns True if the block face is being powered by Redstone.

        Arguments
        - face: The block face

        Returns
        - True if the block face is powered.
        """
        ...


    def isBlockFaceIndirectlyPowered(self, face: "BlockFace") -> bool:
        """
        Returns True if the block face is being indirectly powered by Redstone.

        Arguments
        - face: The block face

        Returns
        - True if the block face is indirectly powered.
        """
        ...


    def getBlockPower(self, face: "BlockFace") -> int:
        """
        Returns the redstone power being provided to this block face

        Arguments
        - face: the face of the block to query or BlockFace.SELF for the
            block itself

        Returns
        - The power level.
        """
        ...


    def getBlockPower(self) -> int:
        """
        Returns the redstone power being provided to this block

        Returns
        - The power level.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Checks if this block is empty.
        
        A block is considered empty when .getType() returns Material.AIR.

        Returns
        - True if this block is empty
        """
        ...


    def isLiquid(self) -> bool:
        """
        Checks if this block is liquid.
        
        A block is considered liquid when .getType() returns Material.WATER or Material.LAVA.

        Returns
        - True if this block is liquid
        """
        ...


    def getTemperature(self) -> float:
        """
        Gets the temperature of this block.
        
        If the raw biome temperature without adjusting for height effects is
        required then please use World.getTemperature(int, int).

        Returns
        - Temperature of this block
        """
        ...


    def getHumidity(self) -> float:
        """
        Gets the humidity of the biome of this block

        Returns
        - Humidity of this block
        """
        ...


    def getPistonMoveReaction(self) -> "PistonMoveReaction":
        """
        Returns the reaction of the block when moved by a piston

        Returns
        - reaction
        """
        ...


    def breakNaturally(self) -> bool:
        """
        Breaks the block and spawns items as if a player had digged it regardless
        of the tool.

        Returns
        - True if the block was destroyed
        """
        ...


    def breakNaturally(self, tool: "ItemStack") -> bool:
        """
        Breaks the block and spawns items as if a player had digged it with a
        specific tool

        Arguments
        - tool: The tool or item in hand used for digging

        Returns
        - True if the block was destroyed
        """
        ...


    def applyBoneMeal(self, face: "BlockFace") -> bool:
        """
        Simulate bone meal application to this block (if possible).

        Arguments
        - face: the face on which bonemeal should be applied

        Returns
        - True if the block was bonemealed, False otherwise
        """
        ...


    def getDrops(self) -> Iterable["ItemStack"]:
        """
        Returns a list of items which would drop by destroying this block

        Returns
        - a list of dropped items for this type of block
        """
        ...


    def getDrops(self, tool: "ItemStack") -> Iterable["ItemStack"]:
        """
        Returns a list of items which would drop by destroying this block with
        a specific tool

        Arguments
        - tool: The tool or item in hand used for digging

        Returns
        - a list of dropped items for this type of block
        """
        ...


    def getDrops(self, tool: "ItemStack", entity: "Entity") -> Iterable["ItemStack"]:
        """
        Returns a list of items which would drop by the entity destroying this
        block with a specific tool

        Arguments
        - tool: The tool or item in hand used for digging
        - entity: the entity destroying the block

        Returns
        - a list of dropped items for this type of block
        """
        ...


    def isPreferredTool(self, tool: "ItemStack") -> bool:
        """
        Returns if the given item is a preferred choice to break this Block.
        
        In some cases this determines if a block will drop anything or extra
        loot.

        Arguments
        - tool: The tool or item used for breaking this block

        Returns
        - True if the tool is preferred for breaking this block.
        """
        ...


    def getBreakSpeed(self, player: "Player") -> float:
        """
        Gets the speed at which the given player would break this block, taking
        into account tools, potion effects, whether or not the player is in
        water, enchantments, etc.
        
        The returned value is the amount of progress made in breaking the block
        each tick. When the total breaking progress reaches `1.0f`, the
        block is broken. Note that the break speed can change in the course of
        breaking a block, e.g. if a potion effect is applied or expires, or the
        player jumps/enters water.

        Arguments
        - player: player breaking the block

        Returns
        - the speed at which the player breaks this block
        """
        ...


    def isPassable(self) -> bool:
        """
        Checks if this block is passable.
        
        A block is passable if it has no colliding parts that would prevent
        players from moving through it.
        
        Examples: Tall grass, flowers, signs, etc. are passable, but open doors,
        fence gates, trap doors, etc. are not because they still have parts that
        can be collided with.

        Returns
        - `True` if passable
        """
        ...


    def rayTrace(self, start: "Location", direction: "Vector", maxDistance: float, fluidCollisionMode: "FluidCollisionMode") -> "RayTraceResult":
        """
        Performs a ray trace that checks for collision with this specific block
        in its current state using its precise collision shape.

        Arguments
        - start: the start location
        - direction: the ray direction
        - maxDistance: the maximum distance
        - fluidCollisionMode: the fluid collision mode

        Returns
        - the ray trace hit result, or `null` if there is no hit
        """
        ...


    def getBoundingBox(self) -> "BoundingBox":
        """
        Gets the approximate bounding box for this block.
        
        This isn't exact as some blocks org.bukkit.block.data.type.Stairs
        contain many bounding boxes to establish their complete form.
        
        Also, the box may not be exactly the same as the collision shape (such as
        cactus, which is 16/16 of a block with 15/16 collisional bounds).
        
        This method will return an empty bounding box if the geometric shape of
        the block is empty (such as air blocks).

        Returns
        - the approximate bounding box of the block
        """
        ...


    def getCollisionShape(self) -> "VoxelShape":
        """
        Gets the collision shape of this block.

        Returns
        - a VoxelShape representing the collision shape of this
        block.
        """
        ...


    def canPlace(self, data: "BlockData") -> bool:
        """
        Checks if this block is a valid placement location for the specified
        block data.

        Arguments
        - data: the block data to check

        Returns
        - `True` if the block data can be placed here
        """
        ...
