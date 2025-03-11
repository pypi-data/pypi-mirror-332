"""
Python module generated from Java source file org.bukkit.block.data.type.TrialSpawner

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.block.data import BlockData
from org.bukkit.block.data.type import *
from typing import Any, Callable, Iterable, Tuple


class TrialSpawner(BlockData):
    """
    'trial_spawner_state' indicates the current operational phase of the spawner.
    
    'ominous' indicates if the block has ominous effects.
    """

    def getTrialSpawnerState(self) -> "State":
        """
        Gets the value of the 'trial_spawner_state' property.

        Returns
        - the 'trial_spawner_state' value
        """
        ...


    def setTrialSpawnerState(self, state: "State") -> None:
        """
        Sets the value of the 'trial_spawner_state' property.

        Arguments
        - state: the new 'trial_spawner_state' value
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
        WAITING_FOR_PLAYERS = 1
        ACTIVE = 2
        WAITING_FOR_REWARD_EJECTION = 3
        EJECTING_REWARD = 4
        COOLDOWN = 5
