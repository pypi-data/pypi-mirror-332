"""
Python module generated from Java source file org.bukkit.entity.Minecart

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import BlockData
from org.bukkit.entity import *
from org.bukkit.material import MaterialData
from org.bukkit.util import Vector
from typing import Any, Callable, Iterable, Tuple


class Minecart(Vehicle):
    """
    Represents a minecart entity.
    """

    def setDamage(self, damage: float) -> None:
        """
        Sets a minecart's damage.

        Arguments
        - damage: over 40 to "kill" a minecart
        """
        ...


    def getDamage(self) -> float:
        """
        Gets a minecart's damage.

        Returns
        - The damage
        """
        ...


    def getMaxSpeed(self) -> float:
        """
        Gets the maximum speed of a minecart. The speed is unrelated to the
        velocity.

        Returns
        - The max speed
        """
        ...


    def setMaxSpeed(self, speed: float) -> None:
        """
        Sets the maximum speed of a minecart. Must be nonnegative. Default is
        0.4D.

        Arguments
        - speed: The max speed
        """
        ...


    def isSlowWhenEmpty(self) -> bool:
        """
        Returns whether this minecart will slow down faster without a passenger
        occupying it

        Returns
        - Whether it decelerates faster
        """
        ...


    def setSlowWhenEmpty(self, slow: bool) -> None:
        """
        Sets whether this minecart will slow down faster without a passenger
        occupying it

        Arguments
        - slow: Whether it will decelerate faster
        """
        ...


    def getFlyingVelocityMod(self) -> "Vector":
        """
        Gets the flying velocity modifier. Used for minecarts that are in
        mid-air. A flying minecart's velocity is multiplied by this factor each
        tick.

        Returns
        - The vector factor
        """
        ...


    def setFlyingVelocityMod(self, flying: "Vector") -> None:
        """
        Sets the flying velocity modifier. Used for minecarts that are in
        mid-air. A flying minecart's velocity is multiplied by this factor each
        tick.

        Arguments
        - flying: velocity modifier vector
        """
        ...


    def getDerailedVelocityMod(self) -> "Vector":
        """
        Gets the derailed velocity modifier. Used for minecarts that are on the
        ground, but not on rails.
        
        A derailed minecart's velocity is multiplied by this factor each tick.

        Returns
        - derailed visible speed
        """
        ...


    def setDerailedVelocityMod(self, derailed: "Vector") -> None:
        """
        Sets the derailed velocity modifier. Used for minecarts that are on the
        ground, but not on rails. A derailed minecart's velocity is multiplied
        by this factor each tick.

        Arguments
        - derailed: visible speed
        """
        ...


    def setDisplayBlock(self, material: "MaterialData") -> None:
        """
        Sets the display block for this minecart.
        Passing a null value will set the minecart to have no display block.

        Arguments
        - material: the material to set as display block.
        """
        ...


    def getDisplayBlock(self) -> "MaterialData":
        """
        Gets the display block for this minecart.
        This function will return the type AIR if none is set.

        Returns
        - the block displayed by this minecart.
        """
        ...


    def setDisplayBlockData(self, blockData: "BlockData") -> None:
        """
        Sets the display block for this minecart.
        Passing a null value will set the minecart to have no display block.

        Arguments
        - blockData: the material to set as display block.
        """
        ...


    def getDisplayBlockData(self) -> "BlockData":
        """
        Gets the display block for this minecart.
        This function will return the type AIR if none is set.

        Returns
        - the block displayed by this minecart.
        """
        ...


    def setDisplayBlockOffset(self, offset: int) -> None:
        """
        Sets the offset of the display block.

        Arguments
        - offset: the block offset to set for this minecart.
        """
        ...


    def getDisplayBlockOffset(self) -> int:
        """
        Gets the offset of the display block.

        Returns
        - the current block offset for this minecart.
        """
        ...
