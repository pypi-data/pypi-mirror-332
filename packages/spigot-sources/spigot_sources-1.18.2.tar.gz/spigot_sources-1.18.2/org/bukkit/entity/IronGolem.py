"""
Python module generated from Java source file org.bukkit.entity.IronGolem

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class IronGolem(Golem):
    """
    An iron Golem that protects Villages.
    """

    def isPlayerCreated(self) -> bool:
        """
        Gets whether this iron golem was built by a player.

        Returns
        - Whether this iron golem was built by a player
        """
        ...


    def setPlayerCreated(self, playerCreated: bool) -> None:
        """
        Sets whether this iron golem was built by a player or not.

        Arguments
        - playerCreated: True if you want to set the iron golem as being
            player created, False if you want it to be a natural village golem.
        """
        ...
