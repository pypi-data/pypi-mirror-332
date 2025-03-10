"""
Python module generated from Java source file org.bukkit.entity.EvokerFangs

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class EvokerFangs(Entity):
    """
    Represents Evoker Fangs.
    """

    def getOwner(self) -> "LivingEntity":
        """
        Gets the LivingEntity which summoned the fangs.

        Returns
        - the LivingEntity which summoned the fangs
        """
        ...


    def setOwner(self, owner: "LivingEntity") -> None:
        """
        Sets the LivingEntity which summoned the fangs.

        Arguments
        - owner: the LivingEntity which summoned the fangs
        """
        ...
