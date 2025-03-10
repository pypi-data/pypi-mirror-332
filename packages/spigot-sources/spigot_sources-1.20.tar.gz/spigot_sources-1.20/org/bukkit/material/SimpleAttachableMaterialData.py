"""
Python module generated from Java source file org.bukkit.material.SimpleAttachableMaterialData

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import *
from typing import Any, Callable, Iterable, Tuple


class SimpleAttachableMaterialData(MaterialData, Attachable):
    """
    Simple utility class for attachable MaterialData subclasses

    Deprecated
    - all usage of MaterialData is deprecated and subject to removal.
    Use org.bukkit.block.data.BlockData.
    """

    def __init__(self, type: "Material", direction: "BlockFace"):
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


    def getFacing(self) -> "BlockFace":
        ...


    def toString(self) -> str:
        ...


    def clone(self) -> "SimpleAttachableMaterialData":
        ...
