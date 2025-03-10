"""
Python module generated from Java source file org.bukkit.entity.AbstractSkeleton

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class AbstractSkeleton(Monster):
    """
    This interface defines or represents the abstract concept of skeleton-like
    entities on the server. The interface is hence not a direct representation
    of an entity but rather serves as a parent to interfaces/entity types like
    Skeleton, WitherSkeleton or Stray.
    
    To compute what specific type of skeleton is present in a variable/field
    of this type, instanceOf checks against the specific subtypes listed prior
    are recommended.
    """

    def getSkeletonType(self) -> "Skeleton.SkeletonType":
        """
        Gets the current type of this skeleton.

        Returns
        - Current type

        Deprecated
        - should check what class instance this is.
        """
        ...


    def setSkeletonType(self, type: "Skeleton.SkeletonType") -> None:
        """
        Arguments
        - type: type

        Deprecated
        - Must spawn a new subtype variant
        """
        ...
