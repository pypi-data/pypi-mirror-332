"""
Python module generated from Java source file org.bukkit.entity.Shulker

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.entity import *
from org.bukkit.material import Colorable
from typing import Any, Callable, Iterable, Tuple


class Shulker(Golem, Colorable):

    def getPeek(self) -> float:
        """
        Gets the peek state of the shulker between 0.0 and 1.0.

        Returns
        - the peek state of the shulker between 0.0 and 1.0
        """
        ...


    def setPeek(self, value: float) -> None:
        """
        Sets the peek state of the shulker, should be in between 0.0 and 1.0.

        Arguments
        - value: peek state of the shulker, should be in between 0.0 and 1.0

        Raises
        - IllegalArgumentException: thrown if the value exceeds the valid
        range in between of 0.0 and 1.0
        """
        ...


    def getAttachedFace(self) -> "BlockFace":
        """
        Gets the face to which the shulker is attached.

        Returns
        - the face to which the shulker is attached
        """
        ...


    def setAttachedFace(self, face: "BlockFace") -> None:
        """
        Sets the face to which the shulker is attached.

        Arguments
        - face: the face to attach the shulker to
        """
        ...
