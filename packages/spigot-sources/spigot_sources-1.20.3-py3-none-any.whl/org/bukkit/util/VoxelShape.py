"""
Python module generated from Java source file org.bukkit.util.VoxelShape

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class VoxelShape:
    """
    A shape made out of voxels.
    
    For example, used to represent the detailed collision shape of blocks.
    """

    def getBoundingBoxes(self) -> Iterable["BoundingBox"]:
        """
        Converts this shape into a collection of BoundingBox equivalent
        to the shape: a bounding box intersects with this block shape if it
        intersects with any of the shape's bounding boxes.

        Returns
        - shape converted to bounding boxes
        """
        ...


    def overlaps(self, other: "BoundingBox") -> bool:
        """
        Checks if the given bounding box intersects this block shape.

        Arguments
        - other: bounding box to test

        Returns
        - True if other overlaps this, False otherwise
        """
        ...
