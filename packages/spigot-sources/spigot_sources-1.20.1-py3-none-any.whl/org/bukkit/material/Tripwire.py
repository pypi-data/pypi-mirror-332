"""
Python module generated from Java source file org.bukkit.material.Tripwire

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Tripwire(MaterialData):
    """
    Represents the tripwire

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


    def isActivated(self) -> bool:
        """
        Test if tripwire is currently activated

        Returns
        - True if activated, False if not
        """
        ...


    def setActivated(self, act: bool) -> None:
        """
        Set tripwire activated state

        Arguments
        - act: - True if activated, False if not
        """
        ...


    def isObjectTriggering(self) -> bool:
        """
        Test if object triggering this tripwire directly

        Returns
        - True if object activating tripwire, False if not
        """
        ...


    def setObjectTriggering(self, trig: bool) -> None:
        """
        Set object triggering state for this tripwire

        Arguments
        - trig: - True if object activating tripwire, False if not
        """
        ...


    def clone(self) -> "Tripwire":
        ...


    def toString(self) -> str:
        ...
