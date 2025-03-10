"""
Python module generated from Java source file org.bukkit.event.entity.CreeperPowerEvent

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.entity import Creeper
from org.bukkit.entity import LightningStrike
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import *
from typing import Any, Callable, Iterable, Tuple


class CreeperPowerEvent(EntityEvent, Cancellable):
    """
    Called when a Creeper is struck by lightning.
    
    If a Creeper Power event is cancelled, the Creeper will not be powered.
    """

    def __init__(self, creeper: "Creeper", bolt: "LightningStrike", cause: "PowerCause"):
        ...


    def __init__(self, creeper: "Creeper", cause: "PowerCause"):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getEntity(self) -> "Creeper":
        ...


    def getLightning(self) -> "LightningStrike":
        """
        Gets the lightning bolt which is striking the Creeper.

        Returns
        - The Entity for the lightning bolt which is striking the Creeper
        """
        ...


    def getCause(self) -> "PowerCause":
        """
        Gets the cause of the creeper being (un)powered.

        Returns
        - A PowerCause value detailing the cause of change in power.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class PowerCause(Enum):
        """
        An enum to specify the cause of the change in power
        """

        LIGHTNING = 0
        """
        Power change caused by a lightning bolt
        
        Powered state: True
        """
        SET_ON = 1
        """
        Power change caused by something else (probably a plugin)
        
        Powered state: True
        """
        SET_OFF = 2
        """
        Power change caused by something else (probably a plugin)
        
        Powered state: False
        """
