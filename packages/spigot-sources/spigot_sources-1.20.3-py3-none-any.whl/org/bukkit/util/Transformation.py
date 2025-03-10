"""
Python module generated from Java source file org.bukkit.util.Transformation

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.util import Objects
from org.bukkit.util import *
from org.joml import AxisAngle4f
from org.joml import Quaternionf
from org.joml import Vector3f
from typing import Any, Callable, Iterable, Tuple


class Transformation:
    """
    Represents an arbitrary affine transformation.
    """

    def __init__(self, translation: "Vector3f", leftRotation: "AxisAngle4f", scale: "Vector3f", rightRotation: "AxisAngle4f"):
        ...


    def __init__(self, translation: "Vector3f", leftRotation: "Quaternionf", scale: "Vector3f", rightRotation: "Quaternionf"):
        ...


    def getTranslation(self) -> "Vector3f":
        """
        Gets the translation component of this transformation.

        Returns
        - translation component
        """
        ...


    def getLeftRotation(self) -> "Quaternionf":
        """
        Gets the left rotation component of this transformation.

        Returns
        - left rotation component
        """
        ...


    def getScale(self) -> "Vector3f":
        """
        Gets the scale component of this transformation.

        Returns
        - scale component
        """
        ...


    def getRightRotation(self) -> "Quaternionf":
        """
        Gets the right rotation component of this transformation.

        Returns
        - right rotation component
        """
        ...


    def hashCode(self) -> int:
        ...


    def equals(self, obj: "Object") -> bool:
        ...


    def toString(self) -> str:
        ...
