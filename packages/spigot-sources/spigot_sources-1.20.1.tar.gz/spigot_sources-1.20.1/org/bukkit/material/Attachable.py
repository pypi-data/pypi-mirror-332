"""
Python module generated from Java source file org.bukkit.material.Attachable

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Attachable(Directional):
    """
    Indicates that a block can be attached to another block
    """

    def getAttachedFace(self) -> "BlockFace":
        """
        Gets the face that this block is attached on

        Returns
        - BlockFace attached to
        """
        ...
