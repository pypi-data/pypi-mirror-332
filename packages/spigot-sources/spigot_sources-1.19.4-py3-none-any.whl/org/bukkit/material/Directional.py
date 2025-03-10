"""
Python module generated from Java source file org.bukkit.material.Directional

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Directional:

    def setFacingDirection(self, face: "BlockFace") -> None:
        """
        Sets the direction that this block is facing in

        Arguments
        - face: The facing direction
        """
        ...


    def getFacing(self) -> "BlockFace":
        """
        Gets the direction this block is facing

        Returns
        - the direction this block is facing
        """
        ...
