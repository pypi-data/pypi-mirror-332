"""
Python module generated from Java source file org.bukkit.util.EntityTransformer

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Entity
from org.bukkit.generator import LimitedRegion
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class EntityTransformer:
    """
    A EntityTransformer is used to modify entities that are spawned by structure.
    """

    def transform(self, region: "LimitedRegion", x: int, y: int, z: int, entity: "Entity", allowedToSpawn: bool) -> bool:
        """
        Transforms a entity in a structure.

        Arguments
        - region: the accessible region
        - x: the x position of the entity
        - y: the y position of the entity
        - z: the z position of the entity
        - entity: the entity
        - allowedToSpawn: if the entity is allowed to spawn

        Returns
        - `True` if the entity should be spawned otherwise
        `False`
        """
        ...
