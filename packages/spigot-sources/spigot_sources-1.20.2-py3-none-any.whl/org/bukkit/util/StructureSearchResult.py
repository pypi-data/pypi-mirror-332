"""
Python module generated from Java source file org.bukkit.util.StructureSearchResult

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Location
from org.bukkit import World
from org.bukkit.generator.structure import Structure
from org.bukkit.generator.structure import StructureType
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class StructureSearchResult:
    """
    Holds the result of searching for a structure.

    See
    - World.locateNearestStructure(Location, StructureType, int, boolean)
    """

    def getStructure(self) -> "Structure":
        """
        Return the structure which was found.

        Returns
        - the found structure.
        """
        ...


    def getLocation(self) -> "Location":
        """
        Return the location of the structure.

        Returns
        - the location the structure was found.
        """
        ...
