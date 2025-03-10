"""
Python module generated from Java source file org.bukkit.event.player.PlayerCommandPreprocessEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.apache.commons.lang import Validate
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerCommandPreprocessEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player runs a command (by placing a slash
    at the start of their message). It is called early in the command handling
    process, and modifications in this event (via .setMessage(String))
    will be shown in the behavior.
    
    Many plugins will have **no use for this event**, and you should
    attempt to avoid using it if it is not necessary.
    
    Some examples of valid uses for this event are:
    
    - Logging executed commands to a separate file
    - Variable substitution. For example, replacing
        `${nearbyPlayer}` with the name of the nearest other
        player, or simulating the `@a` and `@p`
        decorators used by Command Blocks in plugins that do not handle it.
    - Conditionally blocking commands belonging to other plugins. For
        example, blocking the use of the `/home` command in a
        combat arena.
    - Per-sender command aliases. For example, after a player runs the
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

    def __init__(self, player: "Player", message: str):
        ...


    def __init__(self, player: "Player", message: str, recipients: set["Player"]):
        ...


    def isCancelled(self) -> bool:
        ...


    def setCancelled(self, cancel: bool) -> None:
        ...


    def getMessage(self) -> str:
        """
        Gets the command that the player is attempting to send.
        
        All commands begin with a special character; implementations do not
        consider the first character when executing the content.

        Returns
        - Message the player is attempting to send
        """
        ...


    def setMessage(self, command: str) -> None:
        """
        Sets the command that the player will send.
        
        All commands begin with a special character; implementations do not
        consider the first character when executing the content.

        Arguments
        - command: New message that the player will send

        Raises
        - IllegalArgumentException: if command is null or empty
        """
        ...


    def setPlayer(self, player: "Player") -> None:
        """
        Sets the player that this command will be executed as.

        Arguments
        - player: New player which this event will execute as

        Raises
        - IllegalArgumentException: if the player provided is null
        """
        ...


    def getRecipients(self) -> set["Player"]:
        """
        Gets a set of recipients that this chat message will be displayed to.
        
        The set returned is not guaranteed to be mutable and may auto-populate
        on access. Any listener accessing the returned set should be aware that
        it may reduce performance for a lazy set implementation. Listeners
        should be aware that modifying the list may throw UnsupportedOperationException if the event caller provides an
        unmodifiable set.

        Returns
        - All Players who will see this chat message

        Deprecated
        - This method is provided for backward compatibility with no
            guarantee to the effect of viewing or modifying the set.
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
