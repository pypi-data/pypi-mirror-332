"""
Python module generated from Java source file org.bukkit.Nameable

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import *
from typing import Any, Callable, Iterable, Tuple


class Nameable:
    """
    Represents a block, entity, or other object that may receive a custom name.
    """

    def getCustomName(self) -> str:
        """
        Gets the custom name on a mob or block. If there is no name this method
        will return null.
        
        This value has no effect on players, they will always use their real
        name.

        Returns
        - name of the mob/block or null
        """
        ...


    def setCustomName(self, name: str) -> None:
        """
        Sets a custom name on a mob or block. This name will be used in death
        messages and can be sent to the client as a nameplate over the mob.
        
        Setting the name to null or an empty string will clear it.
        
        This value has no effect on players, they will always use their real
        name.

        Arguments
        - name: the name to set
        """
        ...
