"""
Python module generated from Java source file org.bukkit.entity.Enderman

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

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
