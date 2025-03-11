"""
Python module generated from Java source file org.bukkit.block.PistonMoveReaction

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block import *
from typing import Any, Callable, Iterable, Tuple


class PistonMoveReaction(Enum):
    """
    Represents how a block or entity will react when interacting with a piston
    when it is extending or retracting.
    """

    MOVE = (0)
    """
    Indicates that the block can be pushed or pulled.
    """
    BREAK = (1)
    """
    Indicates the block is fragile and will break if pushed on.
    """
    BLOCK = (2)
    """
    Indicates that the block will resist being pushed or pulled.
    """
    IGNORE = (3)
    """
    Indicates that the entity will ignore any interaction(s) with
    pistons.
    
    Blocks should use PistonMoveReaction.BLOCK.
    """
    PUSH_ONLY = (4)
    """
    Indicates that the block can only be pushed by pistons, not pulled.
    """


    def getId(self) -> int:
        """
        Returns
        - The ID of the move reaction

        Deprecated
        - Magic value
        """
        ...


    @staticmethod
    def getById(id: int) -> "PistonMoveReaction":
        """
        Arguments
        - id: An ID

        Returns
        - The move reaction with that ID

        Deprecated
        - Magic value
        """
        ...
