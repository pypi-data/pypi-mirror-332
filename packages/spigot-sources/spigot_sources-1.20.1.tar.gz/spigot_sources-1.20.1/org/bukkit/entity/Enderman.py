"""
Python module generated from Java source file org.bukkit.entity.Enderman

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.entity import *
from org.bukkit.material import MaterialData
from typing import Any, Callable, Iterable, Tuple


class Enderman(Monster):
    """
    Represents an Enderman.
    """

    def getCarriedMaterial(self) -> "MaterialData":
        """
        Gets the id and data of the block that the Enderman is carrying.

        Returns
        - MaterialData containing the id and data of the block
        """
        ...


    def setCarriedMaterial(self, material: "MaterialData") -> None:
        """
        Sets the id and data of the block that the Enderman is carrying.

        Arguments
        - material: data to set the carried block to
        """
        ...


    def getCarriedBlock(self) -> "BlockData":
        """
        Gets the data of the block that the Enderman is carrying.

        Returns
        - BlockData containing the carried block, or null if none
        """
        ...


    def setCarriedBlock(self, blockData: "BlockData") -> None:
        """
        Sets the data of the block that the Enderman is carrying.

        Arguments
        - blockData: data to set the carried block to, or null to remove
        """
        ...


    def teleport(self) -> bool:
        """
        Randomly teleports the Enderman in a 64x64x64 block cuboid region.
        
        If the randomly selected point is in the ground, the point is moved 1 block
        down until air is found or until it goes under
        org.bukkit.World.getMinHeight().
        
        This method will return False if this Enderman is not alive, or if the
        teleport location was obstructed, or if the teleport location is in water.

        Returns
        - True if the teleport succeeded.
        """
        ...


    def teleportTowards(self, entity: "Entity") -> bool:
        """
        Randomly teleports the Enderman towards the given `entity`.
        
        The point is selected by drawing a vector between this enderman and the
        given `entity`. That vector's length is set to 16 blocks.
        That point is then moved within a 8x8x8 cuboid region. If the randomly
        selected point is in the ground, the point is moved 1 block down until
        air is found or until it goes under
        org.bukkit.World.getMinHeight().
        
        This method will return False if this Enderman is not alive, or if the
        teleport location was obstructed, or if the teleport location is in water.

        Arguments
        - entity: The entity to teleport towards.

        Returns
        - True if the teleport succeeded.
        """
        ...
