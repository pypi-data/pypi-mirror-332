"""
Python module generated from Java source file org.bukkit.event.server.TabCompleteEvent

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerCommandSendEvent
from org.bukkit.event.server import *
from typing import Any, Callable, Iterable, Tuple


class TabCompleteEvent(Event, Cancellable):
    """
    Called when a CommandSender of any description (ie: player or
    console) attempts to tab complete.
    
    Note that due to client changes, if the sender is a Player, this event will
    only begin to fire once command arguments are specified, not commands
    themselves. Plugins wishing to remove commands from tab completion are
    advised to ensure the client does not have permission for the relevant
    commands, or use PlayerCommandSendEvent.
    """

    def __init__(self, sender: "CommandSender", buffer: str, completions: list[str]):
        ...


    def getSender(self) -> "CommandSender":
        """
        Get the sender completing this command.

        Returns
        - the CommandSender instance
        """
        ...


    def getBuffer(self) -> str:
        """
        Return the entire buffer which formed the basis of this completion.

        Returns
        - command buffer, as entered
        """
        ...


    def getCompletions(self) -> list[str]:
        """
        The list of completions which will be offered to the sender, in order.
        This list is mutable and reflects what will be offered.

        Returns
        - a list of offered completions
        """
        ...


    def setCompletions(self, completions: list[str]) -> None:
        """
        Set the completions offered, overriding any already set.

        Arguments
        - completions: the new completions
        """
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancelled: bool) -> None:
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
