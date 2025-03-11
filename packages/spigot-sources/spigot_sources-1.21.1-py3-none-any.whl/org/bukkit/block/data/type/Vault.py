"""
Python module generated from Java source file org.bukkit.block.data.type.Vault

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import Directional
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class Vault(Directional):
    """
    'vault_state' indicates the current operational phase of the vault block.
    
    'ominous' indicates if the block has ominous effects.
    """

    def getTrialSpawnerState(self) -> "State":
        """
        Gets the value of the 'vault_state' property.

        Returns
        - the 'vault_state' value
        """
        ...


    def setTrialSpawnerState(self, state: "State") -> None:
        """
        Sets the value of the 'vault_state' property.

        Arguments
        - state: the new 'vault_state' value
        """
        ...


    def isOminous(self) -> bool:
        """
        Gets the value of the 'ominous' property.

        Returns
        - the 'ominous' value
        """
        ...


    def setOminous(self, ominous: bool) -> None:
        """
        Sets the value of the 'ominous' property.

        Arguments
        - ominous: the new 'ominous' value
        """
        ...


    class State(Enum):

        INACTIVE = 0
        ACTIVE = 1
        UNLOCKING = 2
        EJECTING = 3
