"""
Python module generated from Java source file org.bukkit.material.DetectorRail

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class DetectorRail(ExtendedRails, PressureSensor):
    """
    Represents a detector rail

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
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


    def isPressed(self) -> bool:
        ...


    def setPressed(self, isPressed: bool) -> None:
        ...


    def clone(self) -> "DetectorRail":
        ...
