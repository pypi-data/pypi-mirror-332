"""
Python module generated from Java source file org.bukkit.util.EulerAngle

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class EulerAngle:
    """
    EulerAngle is used to represent 3 angles, one for each
    axis (x, y, z). The angles are in radians
    """

    ZERO = EulerAngle(0, 0, 0)
    """
    A EulerAngle with every axis set to 0
    """


    def __init__(self, x: float, y: float, z: float):
        """
        Creates a EularAngle with each axis set to the
        passed angle in radians

        Arguments
        - x: the angle for the x axis in radians
        - y: the angle for the y axis in radians
        - z: the angle for the z axis in radians
        """
        ...


    def getX(self) -> float:
        """
        Returns the angle on the x axis in radians

        Returns
        - the angle in radians
        """
        ...


    def getY(self) -> float:
        """
        Returns the angle on the y axis in radians

        Returns
        - the angle in radians
        """
        ...


    def getZ(self) -> float:
        """
        Returns the angle on the z axis in radians

        Returns
        - the angle in radians
        """
        ...


    def setX(self, x: float) -> "EulerAngle":
        """
        Return a EulerAngle which is the result of changing
        the x axis to the passed angle

        Arguments
        - x: the angle in radians

        Returns
        - the resultant EulerAngle
        """
        ...


    def setY(self, y: float) -> "EulerAngle":
        """
        Return a EulerAngle which is the result of changing
        the y axis to the passed angle

        Arguments
        - y: the angle in radians

        Returns
        - the resultant EulerAngle
        """
        ...


    def setZ(self, z: float) -> "EulerAngle":
        """
        Return a EulerAngle which is the result of changing
        the z axis to the passed angle

        Arguments
        - z: the angle in radians

        Returns
        - the resultant EulerAngle
        """
        ...


    def add(self, x: float, y: float, z: float) -> "EulerAngle":
        """
        Creates a new EulerAngle which is the result of adding
        the x, y, z components to this EulerAngle

        Arguments
        - x: the angle to add to the x axis in radians
        - y: the angle to add to the y axis in radians
        - z: the angle to add to the z axis in radians

        Returns
        - the resultant EulerAngle
        """
        ...


    def subtract(self, x: float, y: float, z: float) -> "EulerAngle":
        """
        Creates a new EulerAngle which is the result of subtracting
        the x, y, z components to this EulerAngle

        Arguments
        - x: the angle to subtract to the x axis in radians
        - y: the angle to subtract to the y axis in radians
        - z: the angle to subtract to the z axis in radians

        Returns
        - the resultant EulerAngle
        """
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
