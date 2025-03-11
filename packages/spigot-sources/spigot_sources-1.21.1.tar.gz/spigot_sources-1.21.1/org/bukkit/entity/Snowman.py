"""
Python module generated from Java source file org.bukkit.entity.Snowman

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Snowman(Golem):
    """
    Represents a snowman entity
    """

    def isDerp(self) -> bool:
        """
        Gets whether this snowman is in "derp mode", meaning it is not wearing a
        pumpkin.

        Returns
        - True if the snowman is bald, False if it is wearing a pumpkin
        """
        ...


    def setDerp(self, derpMode: bool) -> None:
        """
        Sets whether this snowman is in "derp mode", meaning it is not wearing a
        pumpkin. NOTE: This value is not persisted to disk and will therefore
        reset when the chunk is reloaded.

        Arguments
        - derpMode: True to remove the pumpkin, False to add a pumpkin
        """
        ...
