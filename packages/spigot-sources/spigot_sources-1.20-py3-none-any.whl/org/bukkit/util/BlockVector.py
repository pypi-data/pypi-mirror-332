"""
Python module generated from Java source file org.bukkit.util.BlockVector

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.configuration.serialization import SerializableAs
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class BlockVector(Vector):
    """
    A vector with a hash function that floors the X, Y, Z components, a la
    BlockVector in WorldEdit. BlockVectors can be used in hash sets and
    hash maps. Be aware that BlockVectors are mutable, but it is important
    that BlockVectors are never changed once put into a hash set or hash map.
    """

    def __init__(self):
        """
        Construct the vector with all components as 0.
        """
        ...


    def __init__(self, vec: "Vector"):
        """
        Construct the vector with another vector.

        Arguments
        - vec: The other vector.
        """
        ...


    def __init__(self, x: int, y: int, z: int):
        """
        Construct the vector with provided integer components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def __init__(self, x: float, y: float, z: float):
        """
        Construct the vector with provided double components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def __init__(self, x: float, y: float, z: float):
        """
        Construct the vector with provided float components.

        Arguments
        - x: X component
        - y: Y component
        - z: Z component
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Checks if another object is equivalent.

        Arguments
        - obj: The other object

        Returns
        - whether the other object is equivalent
        """
        ...


    def hashCode(self) -> int:
        """
        Returns a hash code for this vector.

        Returns
        - hash code
        """
        ...


    def clone(self) -> "BlockVector":
        """
        Get a new block vector.

        Returns
        - vector
        """
        ...


    @staticmethod
    def deserialize(args: dict[str, "Object"]) -> "BlockVector":
        ...
