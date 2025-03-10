"""
Python module generated from Java source file org.bukkit.entity.PufferFish

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class PufferFish(Fish):
    """
    Represents a puffer fish.
    """

    def getPuffState(self) -> int:
        """
        Returns the current puff state of this fish (i.e. how inflated it is).

        Returns
        - current puff state
        """
        ...


    def setPuffState(self, state: int) -> None:
        """
        Sets the current puff state of this fish (i.e. how inflated it is).

        Arguments
        - state: new puff state
        """
        ...
