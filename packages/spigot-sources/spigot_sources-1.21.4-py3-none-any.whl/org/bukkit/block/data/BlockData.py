"""
Python module generated from Java source file org.bukkit.block.data.BlockData

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Color
from org.bukkit import Location
from org.bukkit import Material
from org.bukkit import Server
from org.bukkit import SoundGroup
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.block import BlockState
from org.bukkit.block import BlockSupport
from org.bukkit.block import PistonMoveReaction
from org.bukkit.block.data import *
from org.bukkit.block.structure import Mirror
from org.bukkit.block.structure import StructureRotation
from org.bukkit.inventory import ItemStack
from typing import Any, Callable, Iterable, Tuple


class BlockData(Cloneable):

    def getMaterial(self) -> "Material":
        """
        Get the Material represented by this block data.

        Returns
        - the material
        """
        ...


    def getAsString(self) -> str:
        """
        Gets a string, which when passed into a method such as
        Server.createBlockData(java.lang.String) will unambiguously
        recreate this instance.

        Returns
        - serialized data string for this block
        """
        ...


    def getAsString(self, hideUnspecified: bool) -> str:
        """
        Gets a string, which when passed into a method such as
        Server.createBlockData(java.lang.String) will recreate this or a
        similar instance where unspecified states (if any) may be optionally
        omitted. If this instance was parsed and states are omitted, this exact
        instance will be creatable when parsed again, else their equality cannot
        be guaranteed.
        
        This method will only take effect for BlockData instances created by
        methods such as Server.createBlockData(String) or any similar
        method whereby states are optionally defined. If otherwise, the result of
        .getAsString() will be returned. The following behaviour would be
        expected:
        ````String dataString = "minecraft:chest[waterlogged=True]"
        BlockData data = Bukkit.createBlockData(dataString);
        dataString.equals(data.getAsString(True)); // This would return True
        dataString.equals(data.getAsString(False)); // This would return False as all states are present
        dataString.equals(data.getAsString()); // This is equivalent to the above, "getAsString(False)"````

        Arguments
        - hideUnspecified: True if unspecified states should be omitted,
        False if they are to be shown as performed by .getAsString().

        Returns
        - serialized data string for this block
        """
        ...


    def merge(self, data: "BlockData") -> "BlockData":
        """
        Merges all explicitly set states from the given data with this BlockData.
        
        Note that the given data MUST have been created from one of the String
        parse methods, e.g. Server.createBlockData(java.lang.String) and
        not have been subsequently modified.
        
        Note also that the block types must match identically.

        Arguments
        - data: the data to merge from

        Returns
        - a new instance of this blockdata with the merged data
        """
        ...


    def matches(self, data: "BlockData") -> bool:
        """
        Checks if the specified BlockData matches this block data.
        
        The semantics of this method are such that for manually created or
        modified BlockData it has the same effect as
        Object.equals(java.lang.Object), whilst for parsed data (that to
        which .merge(org.bukkit.block.data.BlockData) applies, it will
        return True when the type and all explicitly set states match.
        
        **Note that these semantics mean that a.matches(b) may not be the same
        as b.matches(a)**

        Arguments
        - data: the data to match against (normally a parsed constant)

        Returns
        - if there is a match
        """
        ...


    def clone(self) -> "BlockData":
        """
        Returns a copy of this BlockData.

        Returns
        - a copy of the block data
        """
        ...


    def getSoundGroup(self) -> "SoundGroup":
        """
        Gets the block's SoundGroup which can be used to get its step
        sound, hit sound, and others.

        Returns
        - the sound effect group
        """
        ...


    def getLightEmission(self) -> int:
        """
        Get the amount of light emitted by this state when in the world.

        Returns
        - the light emission
        """
        ...


    def isOccluding(self) -> bool:
        """
        Check whether or not this state will occlude other blocks.
        
        Block state occlusion affects visual features of other blocks (e.g. leaves and
        wet sponges will not spawn dripping water particles if an occluding state is
        below it), or whether light will pass through it.

        Returns
        - True if occluding, False otherwise
        """
        ...


    def requiresCorrectToolForDrops(self) -> bool:
        """
        Check whether or not this state requires a specific item to be used to drop
        items when broken. For example, diamond ore requires an iron pickaxe and will
        not drop diamonds when broken with a wooden or stone pickaxe.

        Returns
        - True if a more specific item is required for drops, False if any item
        (or an empty hand) will drop items
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


    def getPistonMoveReaction(self) -> "PistonMoveReaction":
        """
        Returns the reaction of the block when moved by a piston

        Returns
        - reaction
        """
        ...


    def isSupported(self, block: "Block") -> bool:
        """
        Checks if this state would be properly supported if it were placed at
        the given Block.
        
        This may be useful, for instance, to check whether or not a wall torch is
        capable of surviving on its neighbouring block states.

        Arguments
        - block: the block position at which the state would be placed

        Returns
        - True if the block is supported, False if this state would not survive
        the world conditions
        """
        ...


    def isSupported(self, location: "Location") -> bool:
        """
        Checks if this state would be properly supported if it were placed at
        the block at the given Location.
        
        This may be useful, for instance, to check whether or not a wall torch is
        capable of surviving on its neighbouring block states.

        Arguments
        - location: the location at which the state would be placed

        Returns
        - True if the block is supported, False if this state would not survive
        the world conditions
        """
        ...


    def isFaceSturdy(self, face: "BlockFace", support: "BlockSupport") -> bool:
        """
        Checks if a state's BlockFace is capable of providing a given level
        of BlockSupport for neighbouring block states.
        
        Any given state may support either none, one, or more than one level of block
        support depending on its states. A common example would be a wall's ability to support
        torches only on the center of the upper block face, whereas a grass block would
        support all levels of block support on all block faces.

        Arguments
        - face: the face to check
        - support: the possible support level

        Returns
        - True if the face is sturdy and can support a block, False otherwise
        """
        ...


    def getMapColor(self) -> "Color":
        """
        Gets the color this block should appear as when rendered on a map.

        Returns
        - the color associated with this BlockData
        """
        ...


    def getPlacementMaterial(self) -> "Material":
        """
        Gets the material that a player would use to place this block.
        
        For most blocks this is the same as .getMaterial() but some blocks
        have different materials used to place them.
        
        For example:
        ```
        Material.REDSTONE_WIRE -> Material.REDSTONE
        Material.CARROTS -> Material.CARROT
        ```

        Returns
        - placement material
        """
        ...


    def rotate(self, rotation: "StructureRotation") -> None:
        """
        Rotates this blockdata by the specified StructureRotation.
        
        This has no effect on blocks that do not have any rotatable states.

        Arguments
        - rotation: the rotation
        """
        ...


    def mirror(self, mirror: "Mirror") -> None:
        """
        Mirrors this blockdata using the specified Mirror.
        
        This has no effect on blocks that do not have any mirrorable states.

        Arguments
        - mirror: the mirror
        """
        ...


    def copyTo(self, other: "BlockData") -> None:
        """
        Copies all applicable properties from this BlockData to the provided
        BlockData.
        
        Only modifies properties that both blocks share in common.

        Arguments
        - other: the BlockData to copy properties to
        """
        ...


    def createBlockState(self) -> "BlockState":
        """
        Creates a new default BlockState for this type of Block, not
        bound to a location.

        Returns
        - a new BlockState
        """
        ...
