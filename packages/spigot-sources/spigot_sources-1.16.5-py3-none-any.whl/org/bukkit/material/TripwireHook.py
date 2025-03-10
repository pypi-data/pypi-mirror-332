"""
Python module generated from Java source file org.bukkit.material.TripwireHook

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class TripwireHook(SimpleAttachableMaterialData, Redstone):
    """
    Represents the tripwire hook

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
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


    def __init__(self, dir: "BlockFace"):
        ...


    def isConnected(self) -> bool:
        """
        Test if tripwire is connected

        Returns
        - True if connected, False if not
        """
        ...


    def setConnected(self, connected: bool) -> None:
        """
        Set tripwire connection state

        Arguments
        - connected: - True if connected, False if not
        """
        ...


    def isActivated(self) -> bool:
        """
        Test if hook is currently activated

        Returns
        - True if activated, False if not
        """
        ...


    def setActivated(self, act: bool) -> None:
        """
        Set hook activated state

        Arguments
        - act: - True if activated, False if not
        """
        ...


    def setFacingDirection(self, face: "BlockFace") -> None:
        ...


    def getAttachedFace(self) -> "BlockFace":
        ...


    def isPowered(self) -> bool:
        ...


    def clone(self) -> "TripwireHook":
        ...


    def toString(self) -> str:
        ...
