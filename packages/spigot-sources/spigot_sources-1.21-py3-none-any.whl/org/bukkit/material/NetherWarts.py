"""
Python module generated from Java source file org.bukkit.material.NetherWarts

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit import NetherWartsState
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class NetherWarts(MaterialData):
    """
    Represents nether wart

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, state: "NetherWartsState"):
        ...


    def __init__(self, type: "Material"):
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


    def getState(self) -> "NetherWartsState":
        """
        Gets the current growth state of this nether wart

        Returns
        - NetherWartsState of this nether wart
        """
        ...


    def setState(self, state: "NetherWartsState") -> None:
        """
        Sets the growth state of this nether wart

        Arguments
        - state: New growth state of this nether wart
        """
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "NetherWarts":
        ...
