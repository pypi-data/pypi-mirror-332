"""
Python module generated from Java source file org.bukkit.WorldBorder

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.concurrent import TimeUnit
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class WorldBorder:

    def getWorld(self) -> "World":
        """
        Get the World in which the border resides.

        Returns
        - the associated world, or null if this world border is not associated
        with any specific world, such as those created via Server.createWorldBorder()
        """
        ...


    def reset(self) -> None:
        """
        Resets the border to default values.
        """
        ...


    def getSize(self) -> float:
        """
        Gets the current side length of the border.

        Returns
        - The current side length of the border.
        """
        ...


    def setSize(self, newSize: float) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Arguments
        - newSize: The new size of the border.

        Raises
        - IllegalArgumentException: if newSize is less than 1.0D or greater than .getMaxSize()
        """
        ...


    def setSize(self, newSize: float, seconds: int) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Arguments
        - newSize: The new side length of the border.
        - seconds: The time in seconds in which the border grows or shrinks from the previous size to that being set.

        Raises
        - IllegalArgumentException: if newSize is less than 1.0D or greater than .getMaxSize()
        """
        ...


    def setSize(self, newSize: float, unit: "TimeUnit", time: int) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Arguments
        - newSize: The new side length of the border.
        - unit: The time unit.
        - time: The time in which the border grows or shrinks from the previous size to that being set.

        Raises
        - IllegalArgumentException: if unit is `null` or newSize is less than 1.0D or greater than .getMaxSize()
        """
        ...


    def getCenter(self) -> "Location":
        """
        Gets the current border center.

        Returns
        - The current border center.
        """
        ...


    def setCenter(self, x: float, z: float) -> None:
        """
        Sets the new border center.

        Arguments
        - x: The new center x-coordinate.
        - z: The new center z-coordinate.

        Raises
        - IllegalArgumentException: if the absolute value of x or z is higher than .getMaxCenterCoordinate()
        """
        ...


    def setCenter(self, location: "Location") -> None:
        """
        Sets the new border center.

        Arguments
        - location: The new location of the border center. (Only x/z used)

        Raises
        - IllegalArgumentException: if location is `null` or the absolute value of Location.getX() or Location.getZ() is higher than .getMaxCenterCoordinate()
        """
        ...


    def getDamageBuffer(self) -> float:
        """
        Gets the current border damage buffer.

        Returns
        - The current border damage buffer.
        """
        ...


    def setDamageBuffer(self, blocks: float) -> None:
        """
        Sets the amount of blocks a player may safely be outside the border before taking damage.

        Arguments
        - blocks: The amount of blocks. (The default is 5 blocks.)
        """
        ...


    def getDamageAmount(self) -> float:
        """
        Gets the current border damage amount.

        Returns
        - The current border damage amount.
        """
        ...


    def setDamageAmount(self, damage: float) -> None:
        """
        Sets the amount of damage a player takes when outside the border plus the border buffer.

        Arguments
        - damage: The amount of damage. (The default is 0.2 damage per second per block.)
        """
        ...


    def getWarningTime(self) -> int:
        """
        Gets the current border warning time in seconds.

        Returns
        - The current border warning time in seconds.
        """
        ...


    def setWarningTime(self, seconds: int) -> None:
        """
        Sets the warning time that causes the screen to be tinted red when a contracting border will reach the player within the specified time.

        Arguments
        - seconds: The amount of time in seconds. (The default is 15 seconds.)
        """
        ...


    def getWarningDistance(self) -> int:
        """
        Gets the current border warning distance.

        Returns
        - The current border warning distance.
        """
        ...


    def setWarningDistance(self, distance: int) -> None:
        """
        Sets the warning distance that causes the screen to be tinted red when the player is within the specified number of blocks from the border.

        Arguments
        - distance: The distance in blocks. (The default is 5 blocks.)
        """
        ...


    def isInside(self, location: "Location") -> bool:
        """
        Check if the specified location is inside this border.

        Arguments
        - location: the location to check

        Returns
        - if this location is inside the border or not
        """
        ...


    def getMaxSize(self) -> float:
        """
        Gets the maximum possible size of a WorldBorder.

        Returns
        - The maximum size the WorldBorder
        """
        ...


    def getMaxCenterCoordinate(self) -> float:
        """
        Gets the absolute value of the maximum x/z center coordinate of a
        WorldBorder.

        Returns
        - The absolute maximum center coordinate of the WorldBorder
        """
        ...
