"""
Python module generated from Java source file org.bukkit.entity.Hanging

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import BlockFace
from org.bukkit.entity import *
from org.bukkit.material import Attachable
from typing import Any, Callable, Iterable, Tuple


class Hanging(Entity, Attachable):
    """
    Represents a Hanging entity
    """

    def setFacingDirection(self, face: "BlockFace", force: bool) -> bool:
        """
        Sets the direction of the hanging entity, potentially overriding rules
        of placement. Note that if the result is not valid the object would
        normally drop as an item.

        Arguments
        - face: The new direction.
        - force: Whether to force it.

        Returns
        - False if force was False and there was no block for it to
            attach to in order to face the given direction.
        """
        ...
