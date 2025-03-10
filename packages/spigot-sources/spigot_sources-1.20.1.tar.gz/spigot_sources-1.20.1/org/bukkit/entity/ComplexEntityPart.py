"""
Python module generated from Java source file org.bukkit.entity.ComplexEntityPart

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ComplexEntityPart(Entity):
    """
    Represents a single part of a ComplexLivingEntity
    """

    def getParent(self) -> "ComplexLivingEntity":
        """
        Gets the parent ComplexLivingEntity of this part.

        Returns
        - Parent complex entity
        """
        ...
