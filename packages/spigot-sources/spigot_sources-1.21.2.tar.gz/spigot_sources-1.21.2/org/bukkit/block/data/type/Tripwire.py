"""
Python module generated from Java source file org.bukkit.block.data.type.Tripwire

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.block.data import Attachable
from org.bukkit.block.data import MultipleFacing
from org.bukkit.block.data import Powerable
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Tripwire(Attachable, MultipleFacing, Powerable):
    """
    'disarmed' denotes that the tripwire was broken with shears and will not
    subsequently produce a current when destroyed.
    """

    def isDisarmed(self) -> bool:
        """
        Gets the value of the 'disarmed' property.

        Returns
        - the 'disarmed' value
        """
        ...


    def setDisarmed(self, disarmed: bool) -> None:
        """
        Sets the value of the 'disarmed' property.

        Arguments
        - disarmed: the new 'disarmed' value
        """
        ...
