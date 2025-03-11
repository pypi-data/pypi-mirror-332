"""
Python module generated from Java source file org.bukkit.structure.Structure

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Random
from org.bukkit import Location
from org.bukkit import RegionAccessor
from org.bukkit.block.structure import Mirror
from org.bukkit.block.structure import StructureRotation
from org.bukkit.entity import Entity
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.structure import *
from org.bukkit.util import BlockTransformer
from org.bukkit.util import BlockVector
from org.bukkit.util import EntityTransformer
from typing import Any, Callable, Iterable, Tuple


class Structure(PersistentDataHolder):
    """
    Represents a structure.
    
    A structure is a mutable template of captured blocks and entities that can be
    copied back into the world. The StructureManager, retrieved via
    org.bukkit.Server.getStructureManager(), allows you to create new
    structures, load existing structures, and save structures.
    
    In order for a structure to be usable by structure blocks, it needs to be
    null StructureManager.registerStructure(org.bukkit.NamespacedKey, Structure)
    registered with the StructureManager, or located in the primary
    world folder, a DataPack, or the server's own default resources, so that the
    StructureManager can find it.
    """

    def getSize(self) -> "BlockVector":
        """
        Gets the current size of the structure.
        
        The size of the structure may not be fixed.

        Returns
        - A new vector that represents the size of the structure along each
        axis.
        """
        ...


    def getPalettes(self) -> list["Palette"]:
        """
        Gets a list of available block palettes.

        Returns
        - a list of available variants of this structure.
        """
        ...


    def getPaletteCount(self) -> int:
        """
        Gets the number of palettes in this structure.

        Returns
        - The number of palettes in this structure
        """
        ...


    def getEntities(self) -> list["Entity"]:
        """
        Gets a list of entities that have been included in the Structure.
        
        The entity positions are offsets relative to the structure's position
        that is provided once the structure is placed into the world.

        Returns
        - a list of Entities included in the Structure.
        """
        ...


    def getEntityCount(self) -> int:
        """
        Gets the number of entities in this structure.

        Returns
        - The number of entities in this structure
        """
        ...


    def place(self, location: "Location", includeEntities: bool, structureRotation: "StructureRotation", mirror: "Mirror", palette: int, integrity: float, random: "Random") -> None:
        """
        Place a structure in the world.

        Arguments
        - location: The location to place the structure at.
        - includeEntities: If the entities present in the structure should be
        spawned.
        - structureRotation: The rotation of the structure.
        - mirror: The mirror settings of the structure.
        - palette: The palette index of the structure to use, starting at
        `0`, or `-1` to pick a random palette.
        - integrity: Determines how damaged the building should look by
        randomly skipping blocks to place. This value can range from 0 to 1. With
        0 removing all blocks and 1 spawning the structure in pristine condition.
        - random: The randomizer used for setting the structure's
        org.bukkit.loot.LootTables and integrity.
        """
        ...


    def place(self, location: "Location", includeEntities: bool, structureRotation: "StructureRotation", mirror: "Mirror", palette: int, integrity: float, random: "Random", blockTransformers: Iterable["BlockTransformer"], entityTransformers: Iterable["EntityTransformer"]) -> None:
        """
        Place a structure in the world.

        Arguments
        - location: The location to place the structure at.
        - includeEntities: If the entities present in the structure should be
        spawned.
        - structureRotation: The rotation of the structure.
        - mirror: The mirror settings of the structure.
        - palette: The palette index of the structure to use, starting at
        `0`, or `-1` to pick a random palette.
        - integrity: Determines how damaged the building should look by
        randomly skipping blocks to place. This value can range from 0 to 1. With
        0 removing all blocks and 1 spawning the structure in pristine condition.
        - random: The randomizer used for setting the structure's
        org.bukkit.loot.LootTables and integrity.
        - blockTransformers: A collection of BlockTransformers to apply to the structure.
        - entityTransformers: A collection of EntityTransformers to apply to the structure.
        """
        ...


    def place(self, regionAccessor: "RegionAccessor", location: "BlockVector", includeEntities: bool, structureRotation: "StructureRotation", mirror: "Mirror", palette: int, integrity: float, random: "Random") -> None:
        """
        Place a structure in the world.

        Arguments
        - regionAccessor: The world to place the structure in.
        - location: The location to place the structure at.
        - includeEntities: If the entities present in the structure should be
        spawned.
        - structureRotation: The rotation of the structure.
        - mirror: The mirror settings of the structure.
        - palette: The palette index of the structure to use, starting at
        `0`, or `-1` to pick a random palette.
        - integrity: Determines how damaged the building should look by
        randomly skipping blocks to place. This value can range from 0 to 1. With
        0 removing all blocks and 1 spawning the structure in pristine condition.
        - random: The randomizer used for setting the structure's
        org.bukkit.loot.LootTables and integrity.
        """
        ...


    def place(self, regionAccessor: "RegionAccessor", location: "BlockVector", includeEntities: bool, structureRotation: "StructureRotation", mirror: "Mirror", palette: int, integrity: float, random: "Random", blockTransformers: Iterable["BlockTransformer"], entityTransformers: Iterable["EntityTransformer"]) -> None:
        """
        Place a structure in the world.

        Arguments
        - regionAccessor: The world to place the structure in.
        - location: The location to place the structure at.
        - includeEntities: If the entities present in the structure should be
        spawned.
        - structureRotation: The rotation of the structure.
        - mirror: The mirror settings of the structure.
        - palette: The palette index of the structure to use, starting at
        `0`, or `-1` to pick a random palette.
        - integrity: Determines how damaged the building should look by
        randomly skipping blocks to place. This value can range from 0 to 1. With
        0 removing all blocks and 1 spawning the structure in pristine condition.
        - random: The randomizer used for setting the structure's
        org.bukkit.loot.LootTables and integrity.
        - blockTransformers: A collection of BlockTransformers to apply to the structure.
        - entityTransformers: A collection of EntityTransformers to apply to the structure.
        """
        ...


    def fill(self, corner1: "Location", corner2: "Location", includeEntities: bool) -> None:
        """
        Fills the structure from an area in a world. The origin and size will be
        calculated automatically from the two corners provided.
        
        Be careful as this will override the current data of the structure.
        
        Be aware that this method allows for creating structures larger than the
        48x48x48 size that Minecraft's Structure blocks support. Any structures
        saved this way can not be loaded by using a structure block. Using the
        API however will still work.

        Arguments
        - corner1: A corner of the structure.
        - corner2: The corner opposite from corner1.
        - includeEntities: True if entities should be included in the saved
        structure.
        """
        ...


    def fill(self, origin: "Location", size: "BlockVector", includeEntities: bool) -> None:
        """
        Fills the Structure from an area in a world, starting at the specified
        origin and extending in each axis according to the specified size vector.
        
        Be careful as this will override the current data of the structure.
        
        Be aware that this method allows for saving structures larger than the
        48x48x48 size that Minecraft's Structure blocks support. Any structures
        saved this way can not be loaded by using a structure block. Using the
        API however will still work.

        Arguments
        - origin: The origin of the structure.
        - size: The size of the structure, must be at least 1x1x1.
        - includeEntities: True if entities should be included in the saved
        structure.

        Raises
        - IllegalArgumentException: Thrown if size is smaller than 1x1x1
        """
        ...
