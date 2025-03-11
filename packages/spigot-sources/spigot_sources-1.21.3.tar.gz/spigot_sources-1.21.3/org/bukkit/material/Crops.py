"""
Python module generated from Java source file org.bukkit.material.Crops

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import CropState
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Crops(MaterialData):
    """
    Represents the different types of crops in different states of growth.

    See
    - Material.LEGACY_NETHER_WARTS

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        """
        Constructs a wheat crop block in the seeded state.
        """
        ...


    def __init__(self, state: "CropState"):
        """
        Constructs a wheat crop block in the given growth state

        Arguments
        - state: The growth state of the crops
        """
        ...


    def __init__(self, type: "Material", state: "CropState"):
        """
        Constructs a crop block of the given type and in the given growth state

        Arguments
        - type: The type of crops
        - state: The growth state of the crops
        """
        ...


    def __init__(self, type: "Material"):
        """
        Constructs a crop block of the given type and in the seeded state

        Arguments
        - type: The type of crops
        """
        ...


    def __init__(self, type: "Material", data: int):
        """
        Arguments
        - type: the type
        - data: the raw data value

        Deprecated
        - Magic value
        """
        ...


    def getState(self) -> "CropState":
        """
        Gets the current growth state of this crop
        
        For crops with only four growth states such as beetroot, only the values SEEDED, SMALL, TALL and RIPE will be
        returned.

        Returns
        - CropState of this crop
        """
        ...


    def setState(self, state: "CropState") -> None:
        """
        Sets the growth state of this crop
        
        For crops with only four growth states such as beetroot, the 8 CropStates are mapped into four states:
        
        SEEDED, SMALL, TALL and RIPE
        
        GERMINATED will change to SEEDED
        VERY_SMALL will change to SMALL
        MEDIUM will change to TALL
        VERY_TALL will change to RIPE

        Arguments
        - state: New growth state of this crop
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "Crops":
        ...
