"""
Python module generated from Java source file org.bukkit.event.player.PlayerCommandSendEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerCommandSendEvent(PlayerEvent):
    """
    This event is called when the list of available server commands is sent to
    the player.
    
    Commands may be removed from display using this event, but implementations
    are not required to securely remove all traces of the command. If secure
    removal of commands is required, then the command should be assigned a
    permission which is not granted to the player.
    """

    def __init__(self, player: "Player", commands: Iterable[str]):
        ...


    def getCommands(self) -> Iterable[str]:
        """
        Returns a mutable collection of all top level commands to be sent.
        
        It is not legal to add entries to this collection, only remove them.
        Behaviour of adding entries is undefined.

        Returns
        - collection of all commands
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
