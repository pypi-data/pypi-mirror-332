"""
Python module generated from Java source file org.bukkit.entity.AnimalTamer

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class AnimalTamer:

    def getName(self) -> str:
        """
        This is the name of the specified AnimalTamer.

        Returns
        - The name to reference on tamed animals or null if a name cannot be obtained
        """
        ...


    def getUniqueId(self) -> "UUID":
        """
        This is the UUID of the specified AnimalTamer.

        Returns
        - The UUID to reference on tamed animals
        """
        ...
