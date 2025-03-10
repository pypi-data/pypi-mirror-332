"""
Python module generated from Java source file org.bukkit.block.Conduit

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block import *
from org.bukkit.entity import LivingEntity
from org.bukkit.util import BoundingBox
from typing import Any, Callable, Iterable, Tuple


class Conduit(TileState):
    """
    Represents a captured state of a conduit.
    """

    def isActive(self) -> bool:
        """
        Checks whether or not this conduit is active.
        
        A conduit is considered active if there are at least 16 valid frame
        blocks surrounding it and the conduit is surrounded by a 3x3x3 area of
        water source blocks (or waterlogged blocks), at which point its animation
        will activate, start spinning, and apply effects to nearby players.

        Returns
        - True if active, False otherwise
        """
        ...


    def isHunting(self) -> bool:
        """
        Get whether or not this conduit is actively hunting for nearby hostile
        creatures.
        
        A conduit will hunt if it is active (see .isActive()) and its
        frame is complete (it is surrounded by at least 42 valid frame blocks).
        While hunting, the .getTarget()
        conduit's target, if within its .getHuntingArea() hunting area,
        will be damaged every 2 seconds.

        Returns
        - True if hunting, False otherwise
        """
        ...


    def getFrameBlocks(self) -> Iterable["Block"]:
        """
        Get a Collection of all Block Blocks that make up the
        frame of this conduit. The returned collection will contain only blocks
        that match the types required by the conduit to make up a valid frame,
        <strong>not</strong> the blocks at which the conduit is searching,
        meaning it will be of variable size depending on how many valid frames
        are surrounding the conduit at the time of invocation.

        Returns
        - the frame blocks
        """
        ...


    def getFrameBlockCount(self) -> int:
        """
        Get the amount of valid frame blocks that are currently surrounding the
        conduit.

        Returns
        - the frame block count
        """
        ...


    def getRange(self) -> int:
        """
        Get the range (measured in blocks) within which players will receive the
        conduit's benefits.

        Returns
        - the conduit range
        """
        ...


    def setTarget(self, target: "LivingEntity") -> bool:
        """
        Set the conduit's hunting target.
        
        Note that the value set by this method may be overwritten by the
        conduit's periodic hunting logic. If the target is ever set to
        `null`, the conduit will continue to look for a new target.
        Additionally, if the target is set to an entity that does not meet a
        conduit's hunting conditions (e.g. the entity is not within the
        .getHuntingArea() hunting area, has already been killed, etc.)
        then the passed entity will be ignored and the conduit will also continue
        to look for a new target.

        Arguments
        - target: the target entity, or null to remove the target

        Returns
        - True if the target was changed, False if the target was the same
        """
        ...


    def getTarget(self) -> "LivingEntity":
        """
        Get the conduit's hunting target.

        Returns
        - the hunting target, or null if the conduit does not have a target
        """
        ...


    def hasTarget(self) -> bool:
        """
        Check whether or not this conduit has an active (alive) hunting target.

        Returns
        - True if has a hunting target, False otherwise
        """
        ...


    def getHuntingArea(self) -> "BoundingBox":
        """
        Get a BoundingBox (relative to real-world coordinates) in which
        the conduit will search for hostile entities to target.

        Returns
        - the hunting area bounding box
        """
        ...
