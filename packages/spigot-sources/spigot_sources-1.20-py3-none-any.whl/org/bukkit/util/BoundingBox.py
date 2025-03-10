"""
Python module generated from Java source file org.bukkit.util.BoundingBox

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Objects
from org.bukkit import Location
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class BoundingBox(Cloneable, ConfigurationSerializable):
    """
    A mutable axis aligned bounding box (AABB).
    
    This basically represents a rectangular box (specified by minimum and maximum
    corners) that can for example be used to describe the position and extents of
    an object (such as an entity, block, or rectangular region) in 3D space. Its
    edges and faces are parallel to the axes of the cartesian coordinate system.
    
    The bounding box may be degenerate (one or more sides having the length 0).
    
    Because bounding boxes are mutable, storing them long term may be dangerous
    if they get modified later. If you want to keep around a bounding box, it may
    be wise to call .clone() in order to get a copy.
    """

    def __init__(self):
        """
        Creates a new (degenerate) bounding box with all corner coordinates at
        `0`.
        """
        ...


    def __init__(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float):
        """
        Creates a new bounding box from the given corner coordinates.

        Arguments
        - x1: the first corner's x value
        - y1: the first corner's y value
        - z1: the first corner's z value
        - x2: the second corner's x value
        - y2: the second corner's y value
        - z2: the second corner's z value
        """
        ...


    @staticmethod
    def of(corner1: "Vector", corner2: "Vector") -> "BoundingBox":
        """
        Creates a new bounding box using the coordinates of the given vectors as
        corners.

        Arguments
        - corner1: the first corner
        - corner2: the second corner

        Returns
        - the bounding box
        """
        ...


    @staticmethod
    def of(corner1: "Location", corner2: "Location") -> "BoundingBox":
        """
        Creates a new bounding box using the coordinates of the given locations
        as corners.

        Arguments
        - corner1: the first corner
        - corner2: the second corner

        Returns
        - the bounding box
        """
        ...


    @staticmethod
    def of(corner1: "Block", corner2: "Block") -> "BoundingBox":
        """
        Creates a new bounding box using the coordinates of the given blocks as
        corners.
        
        The bounding box will be sized to fully contain both blocks.

        Arguments
        - corner1: the first corner block
        - corner2: the second corner block

        Returns
        - the bounding box
        """
        ...


    @staticmethod
    def of(block: "Block") -> "BoundingBox":
        """
        Creates a new 1x1x1 sized bounding box containing the given block.

        Arguments
        - block: the block

        Returns
        - the bounding box
        """
        ...


    @staticmethod
    def of(center: "Vector", x: float, y: float, z: float) -> "BoundingBox":
        """
        Creates a new bounding box using the given center and extents.

        Arguments
        - center: the center
        - x: 1/2 the size of the bounding box along the x axis
        - y: 1/2 the size of the bounding box along the y axis
        - z: 1/2 the size of the bounding box along the z axis

        Returns
        - the bounding box
        """
        ...


    @staticmethod
    def of(center: "Location", x: float, y: float, z: float) -> "BoundingBox":
        """
        Creates a new bounding box using the given center and extents.

        Arguments
        - center: the center
        - x: 1/2 the size of the bounding box along the x axis
        - y: 1/2 the size of the bounding box along the y axis
        - z: 1/2 the size of the bounding box along the z axis

        Returns
        - the bounding box
        """
        ...


    def resize(self, x1: float, y1: float, z1: float, x2: float, y2: float, z2: float) -> "BoundingBox":
        """
        Resizes this bounding box.

        Arguments
        - x1: the first corner's x value
        - y1: the first corner's y value
        - z1: the first corner's z value
        - x2: the second corner's x value
        - y2: the second corner's y value
        - z2: the second corner's z value

        Returns
        - this bounding box (resized)
        """
        ...


    def getMinX(self) -> float:
        """
        Gets the minimum x value.

        Returns
        - the minimum x value
        """
        ...


    def getMinY(self) -> float:
        """
        Gets the minimum y value.

        Returns
        - the minimum y value
        """
        ...


    def getMinZ(self) -> float:
        """
        Gets the minimum z value.

        Returns
        - the minimum z value
        """
        ...


    def getMin(self) -> "Vector":
        """
        Gets the minimum corner as vector.

        Returns
        - the minimum corner as vector
        """
        ...


    def getMaxX(self) -> float:
        """
        Gets the maximum x value.

        Returns
        - the maximum x value
        """
        ...


    def getMaxY(self) -> float:
        """
        Gets the maximum y value.

        Returns
        - the maximum y value
        """
        ...


    def getMaxZ(self) -> float:
        """
        Gets the maximum z value.

        Returns
        - the maximum z value
        """
        ...


    def getMax(self) -> "Vector":
        """
        Gets the maximum corner as vector.

        Returns
        - the maximum corner vector
        """
        ...


    def getWidthX(self) -> float:
        """
        Gets the width of the bounding box in the x direction.

        Returns
        - the width in the x direction
        """
        ...


    def getWidthZ(self) -> float:
        """
        Gets the width of the bounding box in the z direction.

        Returns
        - the width in the z direction
        """
        ...


    def getHeight(self) -> float:
        """
        Gets the height of the bounding box.

        Returns
        - the height
        """
        ...


    def getVolume(self) -> float:
        """
        Gets the volume of the bounding box.

        Returns
        - the volume
        """
        ...


    def getCenterX(self) -> float:
        """
        Gets the x coordinate of the center of the bounding box.

        Returns
        - the center's x coordinate
        """
        ...


    def getCenterY(self) -> float:
        """
        Gets the y coordinate of the center of the bounding box.

        Returns
        - the center's y coordinate
        """
        ...


    def getCenterZ(self) -> float:
        """
        Gets the z coordinate of the center of the bounding box.

        Returns
        - the center's z coordinate
        """
        ...


    def getCenter(self) -> "Vector":
        """
        Gets the center of the bounding box.

        Returns
        - the center
        """
        ...


    def copy(self, other: "BoundingBox") -> "BoundingBox":
        """
        Copies another bounding box.

        Arguments
        - other: the other bounding box

        Returns
        - this bounding box
        """
        ...


    def expand(self, negativeX: float, negativeY: float, negativeZ: float, positiveX: float, positiveY: float, positiveZ: float) -> "BoundingBox":
        """
        Expands this bounding box by the given values in the corresponding
        directions.
        
        Negative values will shrink the bounding box in the corresponding
        direction. Shrinking will be limited to the point where the affected
        opposite faces would meet if the they shrank at uniform speeds.

        Arguments
        - negativeX: the amount of expansion in the negative x direction
        - negativeY: the amount of expansion in the negative y direction
        - negativeZ: the amount of expansion in the negative z direction
        - positiveX: the amount of expansion in the positive x direction
        - positiveY: the amount of expansion in the positive y direction
        - positiveZ: the amount of expansion in the positive z direction

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, x: float, y: float, z: float) -> "BoundingBox":
        """
        Expands this bounding box uniformly by the given values in both positive
        and negative directions.
        
        Negative values will shrink the bounding box. Shrinking will be limited
        to the bounding box's current size.

        Arguments
        - x: the amount of expansion in both positive and negative x
        direction
        - y: the amount of expansion in both positive and negative y
        direction
        - z: the amount of expansion in both positive and negative z
        direction

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, expansion: "Vector") -> "BoundingBox":
        """
        Expands this bounding box uniformly by the given values in both positive
        and negative directions.
        
        Negative values will shrink the bounding box. Shrinking will be limited
        to the bounding box's current size.

        Arguments
        - expansion: the expansion values

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, expansion: float) -> "BoundingBox":
        """
        Expands this bounding box uniformly by the given value in all directions.
        
        A negative value will shrink the bounding box. Shrinking will be limited
        to the bounding box's current size.

        Arguments
        - expansion: the amount of expansion

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, dirX: float, dirY: float, dirZ: float, expansion: float) -> "BoundingBox":
        """
        Expands this bounding box in the specified direction.
        
        The magnitude of the direction will scale the expansion. A negative
        expansion value will shrink the bounding box in this direction. Shrinking
        will be limited to the bounding box's current size.

        Arguments
        - dirX: the x direction component
        - dirY: the y direction component
        - dirZ: the z direction component
        - expansion: the amount of expansion

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, direction: "Vector", expansion: float) -> "BoundingBox":
        """
        Expands this bounding box in the specified direction.
        
        The magnitude of the direction will scale the expansion. A negative
        expansion value will shrink the bounding box in this direction. Shrinking
        will be limited to the bounding box's current size.

        Arguments
        - direction: the direction
        - expansion: the amount of expansion

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expand(self, blockFace: "BlockFace", expansion: float) -> "BoundingBox":
        """
        Expands this bounding box in the direction specified by the given block
        face.
        
        A negative expansion value will shrink the bounding box in this
        direction. Shrinking will be limited to the bounding box's current size.

        Arguments
        - blockFace: the block face
        - expansion: the amount of expansion

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expandDirectional(self, dirX: float, dirY: float, dirZ: float) -> "BoundingBox":
        """
        Expands this bounding box in the specified direction.
        
        Negative values will expand the bounding box in the negative direction,
        positive values will expand it in the positive direction. The magnitudes
        of the direction components determine the corresponding amounts of
        expansion.

        Arguments
        - dirX: the x direction component
        - dirY: the y direction component
        - dirZ: the z direction component

        Returns
        - this bounding box (now expanded)
        """
        ...


    def expandDirectional(self, direction: "Vector") -> "BoundingBox":
        """
        Expands this bounding box in the specified direction.
        
        Negative values will expand the bounding box in the negative direction,
        positive values will expand it in the positive direction. The magnitude
        of the direction vector determines the amount of expansion.

        Arguments
        - direction: the direction and magnitude of the expansion

        Returns
        - this bounding box (now expanded)
        """
        ...


    def union(self, posX: float, posY: float, posZ: float) -> "BoundingBox":
        """
        Expands this bounding box to contain (or border) the specified position.

        Arguments
        - posX: the x position value
        - posY: the y position value
        - posZ: the z position value

        Returns
        - this bounding box (now expanded)

        See
        - .contains(double, double, double)
        """
        ...


    def union(self, position: "Vector") -> "BoundingBox":
        """
        Expands this bounding box to contain (or border) the specified position.

        Arguments
        - position: the position

        Returns
        - this bounding box (now expanded)

        See
        - .contains(double, double, double)
        """
        ...


    def union(self, position: "Location") -> "BoundingBox":
        """
        Expands this bounding box to contain (or border) the specified position.

        Arguments
        - position: the position

        Returns
        - this bounding box (now expanded)

        See
        - .contains(double, double, double)
        """
        ...


    def union(self, other: "BoundingBox") -> "BoundingBox":
        """
        Expands this bounding box to contain both this and the given bounding
        box.

        Arguments
        - other: the other bounding box

        Returns
        - this bounding box (now expanded)
        """
        ...


    def intersection(self, other: "BoundingBox") -> "BoundingBox":
        """
        Resizes this bounding box to represent the intersection of this and the
        given bounding box.

        Arguments
        - other: the other bounding box

        Returns
        - this bounding box (now representing the intersection)

        Raises
        - IllegalArgumentException: if the bounding boxes don't overlap
        """
        ...


    def shift(self, shiftX: float, shiftY: float, shiftZ: float) -> "BoundingBox":
        """
        Shifts this bounding box by the given amounts.

        Arguments
        - shiftX: the shift in x direction
        - shiftY: the shift in y direction
        - shiftZ: the shift in z direction

        Returns
        - this bounding box (now shifted)
        """
        ...


    def shift(self, shift: "Vector") -> "BoundingBox":
        """
        Shifts this bounding box by the given amounts.

        Arguments
        - shift: the shift

        Returns
        - this bounding box (now shifted)
        """
        ...


    def shift(self, shift: "Location") -> "BoundingBox":
        """
        Shifts this bounding box by the given amounts.

        Arguments
        - shift: the shift

        Returns
        - this bounding box (now shifted)
        """
        ...


    def overlaps(self, other: "BoundingBox") -> bool:
        """
        Checks if this bounding box overlaps with the given bounding box.
        
        Bounding boxes that are only intersecting at the borders are not
        considered overlapping.

        Arguments
        - other: the other bounding box

        Returns
        - `True` if overlapping
        """
        ...


    def overlaps(self, min: "Vector", max: "Vector") -> bool:
        """
        Checks if this bounding box overlaps with the bounding box that is
        defined by the given corners.
        
        Bounding boxes that are only intersecting at the borders are not
        considered overlapping.

        Arguments
        - min: the first corner
        - max: the second corner

        Returns
        - `True` if overlapping
        """
        ...


    def contains(self, x: float, y: float, z: float) -> bool:
        """
        Checks if this bounding box contains the specified position.
        
        Positions exactly on the minimum borders of the bounding box are
        considered to be inside the bounding box, while positions exactly on the
        maximum borders are considered to be outside. This allows bounding boxes
        to reside directly next to each other with positions always only residing
        in exactly one of them.

        Arguments
        - x: the position's x coordinates
        - y: the position's y coordinates
        - z: the position's z coordinates

        Returns
        - `True` if the bounding box contains the position
        """
        ...


    def contains(self, position: "Vector") -> bool:
        """
        Checks if this bounding box contains the specified position.
        
        Positions exactly on the minimum borders of the bounding box are
        considered to be inside the bounding box, while positions exactly on the
        maximum borders are considered to be outside. This allows bounding boxes
        to reside directly next to each other with positions always only residing
        in exactly one of them.

        Arguments
        - position: the position

        Returns
        - `True` if the bounding box contains the position
        """
        ...


    def contains(self, other: "BoundingBox") -> bool:
        """
        Checks if this bounding box fully contains the given bounding box.

        Arguments
        - other: the other bounding box

        Returns
        - `True` if the bounding box contains the given bounding
        box
        """
        ...


    def contains(self, min: "Vector", max: "Vector") -> bool:
        """
        Checks if this bounding box fully contains the bounding box that is
        defined by the given corners.

        Arguments
        - min: the first corner
        - max: the second corner

        Returns
        - `True` if the bounding box contains the specified
            bounding box
        """
        ...


    def rayTrace(self, start: "Vector", direction: "Vector", maxDistance: float) -> "RayTraceResult":
        """
        Calculates the intersection of this bounding box with the specified line
        segment.
        
        Intersections at edges and corners yield one of the affected block faces
        as hit result, but it is not defined which of them.

        Arguments
        - start: the start position
        - direction: the ray direction
        - maxDistance: the maximum distance

        Returns
        - the ray trace hit result, or `null` if there is no hit
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "BoundingBox":
        """
        Creates a copy of this bounding box.

        Returns
        - the cloned bounding box
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "BoundingBox":
        ...
