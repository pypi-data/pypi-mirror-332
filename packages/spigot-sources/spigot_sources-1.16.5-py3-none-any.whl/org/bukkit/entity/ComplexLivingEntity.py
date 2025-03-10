"""
Python module generated from Java source file org.bukkit.entity.ComplexLivingEntity

Java source file obtained from artifact spigot-api version 1.16.5-R0.1-20210611.041013-99

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ComplexLivingEntity(LivingEntity):
    """
    Represents a complex living entity - one that is made up of various smaller
    parts
    """

    def getParts(self) -> set["ComplexEntityPart"]:
        """
        Gets a list of parts that belong to this complex entity

        Returns
        - List of parts
        """
        ...
