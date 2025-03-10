"""
Python module generated from Java source file org.bukkit.block.data.Attachable

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import *
from typing import Any, Callable, Iterable, Tuple


class Attachable(BlockData):
    """
    'attached' denotes whether a tripwire hook or string forms a complete
    tripwire circuit and is ready to trigger.
    
    Updating the property on a tripwire hook will change the texture to indicate
    a connected string, but will not have any effect when used on the tripwire
    string itself. It may however still be used to check whether the string forms
    a circuit.
    """

    def isAttached(self) -> bool:
        """
        Gets the value of the 'attached' property.

        Returns
        - the 'attached' value
        """
        ...


    def setAttached(self, attached: bool) -> None:
        """
        Sets the value of the 'attached' property.

        Arguments
        - attached: the new 'attached' value
        """
        ...
