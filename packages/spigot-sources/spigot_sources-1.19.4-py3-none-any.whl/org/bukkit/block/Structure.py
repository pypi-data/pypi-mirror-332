"""
Python module generated from Java source file org.bukkit.block.Structure

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.block.structure import Mirror
from org.bukkit.block.structure import StructureRotation
from org.bukkit.block.structure import UsageMode
from org.bukkit.entity import LivingEntity
from org.bukkit.util import BlockVector
from typing import Any, Callable, Iterable, Tuple


class Structure(TileState):
    """
    Represents a structure block that can save and load blocks from a file. They
    can only be used by OPs, and are not obtainable in survival.
    """

    def getStructureName(self) -> str:
        """
        The name of this structure.

        Returns
        - structure name
        """
        ...


    def setStructureName(self, name: str) -> None:
        """
        Set the name of this structure. This is case-sensitive. The name of the
        structure in the UsageMode.SAVE structure block MUST match the
        name within the UsageMode.CORNER block or the size calculation
        will fail.

        Arguments
        - name: the case-sensitive name of this structure
        """
        ...


    def getAuthor(self) -> str:
        """
        Get the name of who created this structure.

        Returns
        - the name of whoever created this structure.
        """
        ...


    def setAuthor(self, author: str) -> None:
        """
        Set the name of whoever created this structure.

        Arguments
        - author: whoever created this structure (not empty)
        """
        ...


    def setAuthor(self, livingEntity: "LivingEntity") -> None:
        """
        Set the name of whoever created this structure using a
        LivingEntity.

        Arguments
        - livingEntity: the entity who created this structure
        """
        ...


    def getRelativePosition(self) -> "BlockVector":
        """
        The relative position of the structure outline based on the position of
        the structure block. Maximum allowed distance is 48 blocks in any
        direction.

        Returns
        - a Location which contains the relative distance this structure is
        from the structure block.
        """
        ...


    def setRelativePosition(self, vector: "BlockVector") -> None:
        """
        Set the relative position from the structure block. Maximum allowed
        distance is 48 blocks in any direction.

        Arguments
        - vector: the BlockVector containing the relative origin
        coordinates of this structure.
        """
        ...


    def getStructureSize(self) -> "BlockVector":
        """
        The distance to the opposite corner of this structure. The maximum
        structure size is 48x48x48. When a structure has successfully been
        calculated (i.e. it is within the maximum allowed distance) a white
        border surrounds the structure.

        Returns
        - a BlockVector which contains the total size of the
        structure.
        """
        ...


    def setStructureSize(self, vector: "BlockVector") -> None:
        """
        Set the maximum size of this structure from the origin point. Maximum
        allowed size is 48x48x48.

        Arguments
        - vector: the BlockVector containing the size of this
        structure, based off of the origin coordinates.
        """
        ...


    def setMirror(self, mirror: "Mirror") -> None:
        """
        Sets the mirroring of the structure.

        Arguments
        - mirror: the new mirroring method
        """
        ...


    def getMirror(self) -> "Mirror":
        """
        How this structure is mirrored.

        Returns
        - the current mirroring method
        """
        ...


    def setRotation(self, rotation: "StructureRotation") -> None:
        """
        Set how this structure is rotated.

        Arguments
        - rotation: the new rotation
        """
        ...


    def getRotation(self) -> "StructureRotation":
        """
        Get how this structure is rotated.

        Returns
        - the new rotation
        """
        ...


    def setUsageMode(self, mode: "UsageMode") -> None:
        """
        Set the UsageMode of this structure block.

        Arguments
        - mode: the new mode to set.
        """
        ...


    def getUsageMode(self) -> "UsageMode":
        """
        Get the UsageMode of this structure block.

        Returns
        - the mode this block is currently in.
        """
        ...


    def setIgnoreEntities(self, ignoreEntities: bool) -> None:
        """
        While in UsageMode.SAVE mode, this will ignore any entities when
        saving the structure.
        
        While in UsageMode.LOAD mode this will ignore any entities that
        were saved to file.

        Arguments
        - ignoreEntities: the flag to set
        """
        ...


    def isIgnoreEntities(self) -> bool:
        """
        Get if this structure block should ignore entities.

        Returns
        - True if the appropriate UsageMode should ignore entities.
        """
        ...


    def setShowAir(self, showAir: bool) -> None:
        """
        Set if the structure outline should show air blocks.

        Arguments
        - showAir: if the structure block should show air blocks
        """
        ...


    def isShowAir(self) -> bool:
        """
        Check if this structure block is currently showing all air blocks

        Returns
        - True if the structure block is showing all air blocks
        """
        ...


    def setBoundingBoxVisible(self, showBoundingBox: bool) -> None:
        """
        Set if this structure box should show the bounding box.

        Arguments
        - showBoundingBox: if the structure box should be shown
        """
        ...


    def isBoundingBoxVisible(self) -> bool:
        """
        Get if this structure block is currently showing the bounding box.

        Returns
        - True if the bounding box is shown
        """
        ...


    def setIntegrity(self, integrity: float) -> None:
        """
        Set the integrity of the structure. Integrity must be between 0.0 and 1.0
        Lower integrity values will result in more blocks being removed when
        loading a structure. Integrity and .getSeed() are used together
        to determine which blocks are randomly removed to mimic "decay."

        Arguments
        - integrity: the integrity of this structure
        """
        ...


    def getIntegrity(self) -> float:
        """
        Get the integrity of this structure.

        Returns
        - the integrity of this structure
        """
        ...


    def setSeed(self, seed: int) -> None:
        """
        The seed used to determine which blocks will be removed upon loading.
        .getIntegrity() and seed are used together to determine which
        blocks are randomly removed to mimic "decay."

        Arguments
        - seed: the seed used to determine how many blocks will be removed
        """
        ...


    def getSeed(self) -> int:
        """
        The seed used to determine how many blocks are removed upon loading of
        this structure.

        Returns
        - the seed used
        """
        ...


    def setMetadata(self, metadata: str) -> None:
        """
        Only applicable while in UsageMode.DATA. Metadata are specific
        functions that can be applied to the structure location. Consult the
        <a href="https://minecraft.gamepedia.com/Structure_Block#Data">Minecraft
        wiki</a> for more information.

        Arguments
        - metadata: the function to perform on the selected location
        """
        ...


    def getMetadata(self) -> str:
        """
        Get the metadata function this structure block will perform when
        activated. Consult the
        <a href="https://minecraft.gamepedia.com/Structure_Block#Data">Minecraft
        Wiki</a> for more information.

        Returns
        - the function that will be performed when this block is activated
        """
        ...
