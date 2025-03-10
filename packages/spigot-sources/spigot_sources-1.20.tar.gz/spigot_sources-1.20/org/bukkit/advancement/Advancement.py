"""
Python module generated from Java source file org.bukkit.advancement.Advancement

Java source file obtained from artifact spigot-api version 1.20-R0.1-20230612.113428-32

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Keyed
from org.bukkit.advancement import *
from typing import Any, Callable, Iterable, Tuple


class Advancement(Keyed):
    """
    Represents an advancement that may be awarded to a player. This class is not
    reference safe as the underlying advancement may be reloaded.
    """

    def getCriteria(self) -> Iterable[str]:
        """
        Get all the criteria present in this advancement.

        Returns
        - a unmodifiable copy of all criteria
        """
        ...


    def getDisplay(self) -> "AdvancementDisplay":
        """
        Returns the display information for this advancement.
        
        This includes it's name, description and other visible tags.

        Returns
        - a AdvancementDisplay object, or null if not set.
        """
        ...
