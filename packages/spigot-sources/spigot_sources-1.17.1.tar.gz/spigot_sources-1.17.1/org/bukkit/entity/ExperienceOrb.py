"""
Python module generated from Java source file org.bukkit.entity.ExperienceOrb

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class ExperienceOrb(Entity):
    """
    Represents an Experience Orb.
    """

    def getExperience(self) -> int:
        """
        Gets how much experience is contained within this orb

        Returns
        - Amount of experience
        """
        ...


    def setExperience(self, value: int) -> None:
        """
        Sets how much experience is contained within this orb

        Arguments
        - value: Amount of experience
        """
        ...
