"""
Python module generated from Java source file org.bukkit.material.Chest

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class Chest(DirectionalContainer):
    """
    Represents a chest

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self):
        ...


    def __init__(self, direction: "BlockFace"):
        """
        Instantiate a chest facing in a particular direction.

        Arguments
        - direction: the direction the chest's lit opens towards
        """
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


    def clone(self) -> "Chest":
        ...
