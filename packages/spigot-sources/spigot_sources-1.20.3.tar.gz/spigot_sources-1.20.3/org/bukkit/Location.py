"""
Python module generated from Java source file org.bukkit.Location

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.lang.ref import Reference
from java.lang.ref import WeakReference
from org.bukkit import *
from org.bukkit.block import Block
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.util import NumberConversions
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class Location(Cloneable, ConfigurationSerializable):
    """
    Represents a 3-dimensional position in a world.
    
    No constraints are placed on any angular values other than that they be
    specified in degrees. This means that negative angles or angles of greater
    magnitude than 360 are valid, but may be normalized to any other equivalent
    representation by the implementation.
    """

    def __init__(self, world: "World", x: float, y: float, z: float):
        """
        Constructs a new Location with the given coordinates

        Arguments
        - world: The world in which this location resides
        - x: The x-coordinate of this new location
        - y: The y-coordinate of this new location
        - z: The z-coordinate of this new location
        """
        ...


    def __init__(self, world: "World", x: float, y: float, z: float, yaw: float, pitch: float):
        """
        Constructs a new Location with the given coordinates and direction

        Arguments
        - world: The world in which this location resides
        - x: The x-coordinate of this new location
        - y: The y-coordinate of this new location
        - z: The z-coordinate of this new location
        - yaw: The absolute rotation on the x-plane, in degrees
        - pitch: The absolute rotation on the y-plane, in degrees
        """
        ...


    def setWorld(self, world: "World") -> None:
        """
        Sets the world that this location resides in

        Arguments
        - world: New world that this location resides in
        """
        ...


    def isWorldLoaded(self) -> bool:
        """
        Checks if world in this location is present and loaded.

        Returns
        - True if is loaded, otherwise False
        """
        ...


    def getWorld(self) -> "World":
        """
        Gets the world that this location resides in

        Returns
        - World that contains this location, or `null` if it is not set

        Raises
        - IllegalArgumentException: when world is unloaded

        See
        - .isWorldLoaded()
        """
        ...


    def getChunk(self) -> "Chunk":
        """
        Gets the chunk at the represented location

        Returns
        - Chunk at the represented location
        """
        ...


    def getBlock(self) -> "Block":
        """
        Gets the block at the represented location

        Returns
        - Block at the represented location
        """
        ...


    def setX(self, x: float) -> None:
        """
        Sets the x-coordinate of this location

        Arguments
        - x: X-coordinate
        """
        ...


    def getX(self) -> float:
        """
        Gets the x-coordinate of this location

        Returns
        - x-coordinate
        """
        ...


    def getBlockX(self) -> int:
        """
        Gets the floored value of the X component, indicating the block that
        this location is contained with.

        Returns
        - block X
        """
        ...


    def setY(self, y: float) -> None:
        """
        Sets the y-coordinate of this location

        Arguments
        - y: y-coordinate
        """
        ...


    def getY(self) -> float:
        """
        Gets the y-coordinate of this location

        Returns
        - y-coordinate
        """
        ...


    def getBlockY(self) -> int:
        """
        Gets the floored value of the Y component, indicating the block that
        this location is contained with.

        Returns
        - block y
        """
        ...


    def setZ(self, z: float) -> None:
        """
        Sets the z-coordinate of this location

        Arguments
        - z: z-coordinate
        """
        ...


    def getZ(self) -> float:
        """
        Gets the z-coordinate of this location

        Returns
        - z-coordinate
        """
        ...


    def getBlockZ(self) -> int:
        """
        Gets the floored value of the Z component, indicating the block that
        this location is contained with.

        Returns
        - block z
        """
        ...


    def setYaw(self, yaw: float) -> None:
        """
        Sets the yaw of this location, measured in degrees.
        
        - A yaw of 0 or 360 represents the positive z direction.
        - A yaw of 180 represents the negative z direction.
        - A yaw of 90 represents the negative x direction.
        - A yaw of 270 represents the positive x direction.
        
        Increasing yaw values are the equivalent of turning to your
        right-facing, increasing the scale of the next respective axis, and
        decreasing the scale of the previous axis.

        Arguments
        - yaw: new rotation's yaw
        """
        ...


    def getYaw(self) -> float:
        """
        Gets the yaw of this location, measured in degrees.
        
        - A yaw of 0 or 360 represents the positive z direction.
        - A yaw of 180 represents the negative z direction.
        - A yaw of 90 represents the negative x direction.
        - A yaw of 270 represents the positive x direction.
        
        Increasing yaw values are the equivalent of turning to your
        right-facing, increasing the scale of the next respective axis, and
        decreasing the scale of the previous axis.

        Returns
        - the rotation's yaw
        """
        ...


    def setPitch(self, pitch: float) -> None:
        """
        Sets the pitch of this location, measured in degrees.
        
        - A pitch of 0 represents level forward facing.
        - A pitch of 90 represents downward facing, or negative y
            direction.
        - A pitch of -90 represents upward facing, or positive y direction.
        
        Increasing pitch values the equivalent of looking down.

        Arguments
        - pitch: new incline's pitch
        """
        ...


    def getPitch(self) -> float:
        """
        Gets the pitch of this location, measured in degrees.
        
        - A pitch of 0 represents level forward facing.
        - A pitch of 90 represents downward facing, or negative y
            direction.
        - A pitch of -90 represents upward facing, or positive y direction.
        
        Increasing pitch values the equivalent of looking down.

        Returns
        - the incline's pitch
        """
        ...


    def getDirection(self) -> "Vector":
        """
        Gets a unit-vector pointing in the direction that this Location is
        facing.

        Returns
        - a vector pointing the direction of this location's .getPitch() pitch and .getYaw() yaw
        """
        ...


    def setDirection(self, vector: "Vector") -> "Location":
        """
        Sets the .getYaw() yaw and .getPitch() pitch to point
        in the direction of the vector.

        Arguments
        - vector: the direction vector

        Returns
        - the same location
        """
        ...


    def add(self, vec: "Location") -> "Location":
        """
        Adds the location by another.

        Arguments
        - vec: The other location

        Returns
        - the same location

        Raises
        - IllegalArgumentException: for differing worlds

        See
        - Vector
        """
        ...


    def add(self, vec: "Vector") -> "Location":
        """
        Adds the location by a vector.

        Arguments
        - vec: Vector to use

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def add(self, x: float, y: float, z: float) -> "Location":
        """
        Adds the location by another. Not world-aware.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def subtract(self, vec: "Location") -> "Location":
        """
        Subtracts the location by another.

        Arguments
        - vec: The other location

        Returns
        - the same location

        Raises
        - IllegalArgumentException: for differing worlds

        See
        - Vector
        """
        ...


    def subtract(self, vec: "Vector") -> "Location":
        """
        Subtracts the location by a vector.

        Arguments
        - vec: The vector to use

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def subtract(self, x: float, y: float, z: float) -> "Location":
        """
        Subtracts the location by another. Not world-aware and
        orientation independent.

        Arguments
        - x: X coordinate
        - y: Y coordinate
        - z: Z coordinate

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def length(self) -> float:
        """
        Gets the magnitude of the location, defined as sqrt(x^2+y^2+z^2). The
        value of this method is not cached and uses a costly square-root
        function, so do not repeatedly call this method to get the location's
        magnitude. NaN will be returned if the inner result of the sqrt()
        function overflows, which will be caused if the length is too long. Not
        world-aware and orientation independent.

        Returns
        - the magnitude

        See
        - Vector
        """
        ...


    def lengthSquared(self) -> float:
        """
        Gets the magnitude of the location squared. Not world-aware and
        orientation independent.

        Returns
        - the magnitude

        See
        - Vector
        """
        ...


    def distance(self, o: "Location") -> float:
        """
        Get the distance between this location and another. The value of this
        method is not cached and uses a costly square-root function, so do not
        repeatedly call this method to get the location's magnitude. NaN will
        be returned if the inner result of the sqrt() function overflows, which
        will be caused if the distance is too long.

        Arguments
        - o: The other location

        Returns
        - the distance

        Raises
        - IllegalArgumentException: for differing worlds

        See
        - Vector
        """
        ...


    def distanceSquared(self, o: "Location") -> float:
        """
        Get the squared distance between this location and another.

        Arguments
        - o: The other location

        Returns
        - the distance

        Raises
        - IllegalArgumentException: for differing worlds

        See
        - Vector
        """
        ...


    def multiply(self, m: float) -> "Location":
        """
        Performs scalar multiplication, multiplying all components with a
        scalar. Not world-aware.

        Arguments
        - m: The factor

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def zero(self) -> "Location":
        """
        Zero this location's components. Not world-aware.

        Returns
        - the same location

        See
        - Vector
        """
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...


    def toString(self) -> str:
        ...


    def toVector(self) -> "Vector":
        """
        Constructs a new Vector based on this Location

        Returns
        - New Vector containing the coordinates represented by this
            Location
        """
        ...


    def clone(self) -> "Location":
        ...


    def checkFinite(self) -> None:
        """
        Check if each component of this Location is finite.

        Raises
        - IllegalArgumentException: if any component is not finite
        """
        ...


    @staticmethod
    def locToBlock(loc: float) -> int:
        """
        Safely converts a double (location coordinate) to an int (block
        coordinate)

        Arguments
        - loc: Precise coordinate

        Returns
        - Block coordinate
        """
        ...


    def serialize(self) -> dict[str, "Object"]:
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "Location":
        """
        Required method for deserialization

        Arguments
        - args: map to deserialize

        Returns
        - deserialized location

        Raises
        - IllegalArgumentException: if the world don't exists

        See
        - ConfigurationSerializable
        """
        ...


    @staticmethod
    def normalizeYaw(yaw: float) -> float:
        """
        Normalizes the given yaw angle to a value between `+/-180`
        degrees.

        Arguments
        - yaw: the yaw in degrees

        Returns
        - the normalized yaw in degrees

        See
        - Location.getYaw()
        """
        ...


    @staticmethod
    def normalizePitch(pitch: float) -> float:
        """
        Normalizes the given pitch angle to a value between `+/-90`
        degrees.

        Arguments
        - pitch: the pitch in degrees

        Returns
        - the normalized pitch in degrees

        See
        - Location.getPitch()
        """
        ...
