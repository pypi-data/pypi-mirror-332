"""
Python module generated from Java source file org.bukkit.entity.Boat

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit import Material
from org.bukkit import TreeSpecies
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Boat(Vehicle):
    """
    Represents a boat entity.
    """

    def getWoodType(self) -> "TreeSpecies":
        """
        Gets the wood type of the boat.

        Returns
        - the wood type

        Deprecated
        - deprecated in favor of .getBoatType()
        """
        ...


    def setWoodType(self, species: "TreeSpecies") -> None:
        """
        Sets the wood type of the boat.

        Arguments
        - species: the new wood type

        Deprecated
        - deprecated in favor of .setBoatType(Type)
        """
        ...


    def getBoatType(self) -> "Type":
        """
        Gets the type of the boat.

        Returns
        - the boat type

        Deprecated
        - different boats types are now different entity types
        """
        ...


    def setBoatType(self, type: "Type") -> None:
        """
        Sets the type of the boat.

        Arguments
        - type: the new type

        Deprecated
        - different boats types are now different entity types
        """
        ...


    def getMaxSpeed(self) -> float:
        """
        Gets the maximum speed of a boat. The speed is unrelated to the
        velocity.

        Returns
        - The max speed.

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def setMaxSpeed(self, speed: float) -> None:
        """
        Sets the maximum speed of a boat. Must be nonnegative. Default is 0.4D.

        Arguments
        - speed: The max speed.

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def getOccupiedDeceleration(self) -> float:
        """
        Gets the deceleration rate (newSpeed = curSpeed * rate) of occupied
        boats. The default is 0.2.

        Returns
        - The rate of deceleration

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def setOccupiedDeceleration(self, rate: float) -> None:
        """
        Sets the deceleration rate (newSpeed = curSpeed * rate) of occupied
        boats. Setting this to a higher value allows for quicker acceleration.
        The default is 0.2.

        Arguments
        - rate: deceleration rate

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def getUnoccupiedDeceleration(self) -> float:
        """
        Gets the deceleration rate (newSpeed = curSpeed * rate) of unoccupied
        boats. The default is -1. Values below 0 indicate that no additional
        deceleration is imposed.

        Returns
        - The rate of deceleration

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def setUnoccupiedDeceleration(self, rate: float) -> None:
        """
        Sets the deceleration rate (newSpeed = curSpeed * rate) of unoccupied
        boats. Setting this to a higher value allows for quicker deceleration
        of boats when a player disembarks. The default is -1. Values below 0
        indicate that no additional deceleration is imposed.

        Arguments
        - rate: deceleration rate

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def getWorkOnLand(self) -> bool:
        """
        Get whether boats can work on land.

        Returns
        - whether boats can work on land

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def setWorkOnLand(self, workOnLand: bool) -> None:
        """
        Set whether boats can work on land.

        Arguments
        - workOnLand: whether boats can work on land

        Deprecated
        - boats are complex and many of these methods do not work correctly across multiple versions.
        """
        ...


    def getStatus(self) -> "Status":
        """
        Gets the status of the boat.

        Returns
        - the status
        """
        ...


    class Type(Enum):
        """
        Represents the type of boats.

        Deprecated
        - different boats types are now different entity types
        """

        OAK = (Material.OAK_PLANKS)
        SPRUCE = (Material.SPRUCE_PLANKS)
        BIRCH = (Material.BIRCH_PLANKS)
        JUNGLE = (Material.JUNGLE_PLANKS)
        ACACIA = (Material.ACACIA_PLANKS)
        CHERRY = (Material.CHERRY_PLANKS)
        DARK_OAK = (Material.DARK_OAK_PLANKS)
        MANGROVE = (Material.MANGROVE_PLANKS)
        BAMBOO = (Material.BAMBOO_PLANKS)


        def getMaterial(self) -> "Material":
            """
            Gets the material of the boat type.

            Returns
            - a material
            """
            ...


    class Status(Enum):
        """
        Represents the status of the boat.
        """

        IN_WATER = 0
        UNDER_WATER = 1
        UNDER_FLOWING_WATER = 2
        ON_LAND = 3
        IN_AIR = 4
