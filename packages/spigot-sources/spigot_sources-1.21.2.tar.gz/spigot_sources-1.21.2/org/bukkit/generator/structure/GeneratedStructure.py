"""
Python module generated from Java source file org.bukkit.generator.structure.GeneratedStructure

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.generator.structure import *
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.util import BoundingBox
from typing import Any, Callable, Iterable, Tuple


class GeneratedStructure(PersistentDataHolder):
    """
    Represents a structure placed in the world.

    See
    - StructurePiece
    """

    def getBoundingBox(self) -> "BoundingBox":
        """
        Gets the bounding box of this placed structure.

        Returns
        - bounding box of this placed structure
        """
        ...


    def getStructure(self) -> "Structure":
        """
        Gets the structure that this PlacedStructure represents.

        Returns
        - the structure that this PlacedStructure represents
        """
        ...


    def getPieces(self) -> Iterable["StructurePiece"]:
        """
        Gets all the StructurePiece that make up this PlacedStructure.

        Returns
        - a collection of all the StructurePieces
        """
        ...
