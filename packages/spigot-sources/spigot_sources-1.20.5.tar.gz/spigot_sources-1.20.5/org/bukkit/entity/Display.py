"""
Python module generated from Java source file org.bukkit.entity.Display

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from org.bukkit import Color
from org.bukkit.entity import *
from org.bukkit.util import Transformation
from org.joml import Matrix4f
from typing import Any, Callable, Iterable, Tuple


class Display(Entity):
    """
    Represents a display entity which is designed to only have a visual function.
    """

    def getTransformation(self) -> "Transformation":
        """
        Gets the transformation applied to this display.

        Returns
        - the transformation
        """
        ...


    def setTransformation(self, transformation: "Transformation") -> None:
        """
        Sets the transformation applied to this display

        Arguments
        - transformation: the new transformation
        """
        ...


    def setTransformationMatrix(self, transformationMatrix: "Matrix4f") -> None:
        """
        Sets the raw transformation matrix applied to this display

        Arguments
        - transformationMatrix: the transformation matrix
        """
        ...


    def getInterpolationDuration(self) -> int:
        """
        Gets the interpolation duration of this display.

        Returns
        - interpolation duration
        """
        ...


    def setInterpolationDuration(self, duration: int) -> None:
        """
        Sets the interpolation duration of this display.

        Arguments
        - duration: new duration
        """
        ...


    def getTeleportDuration(self) -> int:
        """
        Gets the teleport duration of this display.
        
            - 0 means that updates are applied immediately.
            - 1 means that the display entity will move from current position to the updated one over one tick.
            - Higher values spread the movement over multiple ticks.

        Returns
        - teleport duration
        """
        ...


    def setTeleportDuration(self, duration: int) -> None:
        """
        Sets the teleport duration of this display.

        Arguments
        - duration: new duration

        Raises
        - IllegalArgumentException: if duration is not between 0 and 59

        See
        - .getTeleportDuration()
        """
        ...


    def getViewRange(self) -> float:
        """
        Gets the view distance/range of this display.

        Returns
        - view range
        """
        ...


    def setViewRange(self, range: float) -> None:
        """
        Sets the view distance/range of this display.

        Arguments
        - range: new range
        """
        ...


    def getShadowRadius(self) -> float:
        """
        Gets the shadow radius of this display.

        Returns
        - radius
        """
        ...


    def setShadowRadius(self, radius: float) -> None:
        """
        Sets the shadow radius of this display.

        Arguments
        - radius: new radius
        """
        ...


    def getShadowStrength(self) -> float:
        """
        Gets the shadow strength of this display.

        Returns
        - shadow strength
        """
        ...


    def setShadowStrength(self, strength: float) -> None:
        """
        Sets the shadow strength of this display.

        Arguments
        - strength: new strength
        """
        ...


    def getDisplayWidth(self) -> float:
        """
        Gets the width of this display.

        Returns
        - width
        """
        ...


    def setDisplayWidth(self, width: float) -> None:
        """
        Sets the width of this display.

        Arguments
        - width: new width
        """
        ...


    def getDisplayHeight(self) -> float:
        """
        Gets the height of this display.

        Returns
        - height
        """
        ...


    def setDisplayHeight(self, height: float) -> None:
        """
        Sets the height if this display.

        Arguments
        - height: new height
        """
        ...


    def getInterpolationDelay(self) -> int:
        """
        Gets the amount of ticks before client-side interpolation will commence.

        Returns
        - interpolation delay ticks
        """
        ...


    def setInterpolationDelay(self, ticks: int) -> None:
        """
        Sets the amount of ticks before client-side interpolation will commence.

        Arguments
        - ticks: interpolation delay ticks
        """
        ...


    def getBillboard(self) -> "Billboard":
        """
        Gets the billboard setting of this entity.
        
        The billboard setting controls the automatic rotation of the entity to
        face the player.

        Returns
        - billboard setting
        """
        ...


    def setBillboard(self, billboard: "Billboard") -> None:
        """
        Sets the billboard setting of this entity.
        
        The billboard setting controls the automatic rotation of the entity to
        face the player.

        Arguments
        - billboard: new setting
        """
        ...


    def getGlowColorOverride(self) -> "Color":
        """
        Gets the scoreboard team overridden glow color of this display.

        Returns
        - glow color
        """
        ...


    def setGlowColorOverride(self, color: "Color") -> None:
        """
        Sets the scoreboard team overridden glow color of this display.

        Arguments
        - color: new color
        """
        ...


    def getBrightness(self) -> "Brightness":
        """
        Gets the brightness override of the entity.

        Returns
        - brightness override, if set
        """
        ...


    def setBrightness(self, brightness: "Brightness") -> None:
        """
        Sets the brightness override of the entity.

        Arguments
        - brightness: new brightness override
        """
        ...


    class Brightness:
        """
        Represents the brightness rendering parameters of the entity.
        """

        def __init__(self, blockLight: int, skyLight: int):
            ...


        def getBlockLight(self) -> int:
            """
            Gets the block lighting component of this brightness.

            Returns
            - block light, between 0-15
            """
            ...


        def getSkyLight(self) -> int:
            """
            Gets the sky lighting component of this brightness.

            Returns
            - sky light, between 0-15
            """
            ...


        def hashCode(self) -> int:
            ...


        def equals(self, obj: "Object") -> bool:
            ...


        def toString(self) -> str:
            ...


    class Billboard(Enum):
        """
        Describes the axes/points around which the entity can pivot.
        """

        FIXED = 0
        """
        No rotation (default).
        """
        VERTICAL = 1
        """
        Can pivot around vertical axis.
        """
        HORIZONTAL = 2
        """
        Can pivot around horizontal axis.
        """
        CENTER = 3
        """
        Can pivot around center point.
        """
