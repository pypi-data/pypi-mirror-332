"""
Python module generated from Java source file org.bukkit.entity.EntityFactory

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class EntityFactory:

    def createEntitySnapshot(self, input: str) -> "EntitySnapshot":
        """
        Create a new EntitySnapshot with the supplied input.
        Accepts strings in the format output by EntitySnapshot.getAsString().

        Arguments
        - input: the input string

        Returns
        - the created EntitySnapshot

        Raises
        - IllegalArgumentException: if the input string was provided in an invalid or unsupported format
        """
        ...
