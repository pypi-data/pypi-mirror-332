"""
Python module generated from Java source file org.bukkit.entity.Bat

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import *
from typing import Any, Callable, Iterable, Tuple


class Bat(Ambient):
    """
    Represents a Bat
    """

    def isAwake(self) -> bool:
        """
        Checks the current waking state of this bat.
        
        This does not imply any persistence of state past the method call.

        Returns
        - True if the bat is awake or False if it is currently hanging
            from a block
        """
        ...


    def setAwake(self, state: bool) -> None:
        """
        This method modifies the current waking state of this bat.
        
        This does not prevent a bat from spontaneously awaking itself, or from
        reattaching itself to a block.

        Arguments
        - state: the new state
        """
        ...
