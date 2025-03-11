"""
Python module generated from Java source file org.bukkit.event.server.ServerCommandEvent

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.server import *
from typing import Any, Callable, Iterable, Tuple


class ServerCommandEvent(ServerEvent, Cancellable):
    """
    This event is called when a command is run by a non-player. It is
    called early in the command handling process, and modifications in this
    event (via .setCommand(String)) will be shown in the behavior.
    
    Many plugins will have **no use for this event**, and you should
    attempt to avoid using it if it is not necessary.
    
    Some examples of valid uses for this event are:
    
    - Logging executed commands to a separate file
    - Variable substitution. For example, replacing `${ip:Steve}`
        with the connection IP of the player named Steve, or simulating the
        `@a` and `@p` decorators used by Command Blocks
        for plugins that do not handle it.
    - Conditionally blocking commands belonging to other plugins.
    - Per-sender command aliases. For example, after the console runs the
        command `/calias cr gamemode creative`, the next time they
        run `/cr`, it gets replaced into
        `/gamemode creative`. (Global command aliases should be
        done by registering the alias.)
    
    
    Examples of incorrect uses are:
    
    - Using this event to run command logic
    
    
    If the event is cancelled, processing of the command will halt.
    
    The state of whether or not there is a slash (`/`) at the
    beginning of the message should be preserved. If a slash is added or
    removed, unexpected behavior may result.
    """

    def __init__(self, sender: "CommandSender", command: str):
        ...


    def getCommand(self) -> str:
        """
        Gets the command that the user is attempting to execute from the
        console

        Returns
        - Command the user is attempting to execute
        """
        ...


    def setCommand(self, message: str) -> None:
        """
        Sets the command that the server will execute

        Arguments
        - message: New message that the server will execute
        """
        ...


    def getSender(self) -> "CommandSender":
        """
        Get the command sender.

        Returns
        - The sender
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...
