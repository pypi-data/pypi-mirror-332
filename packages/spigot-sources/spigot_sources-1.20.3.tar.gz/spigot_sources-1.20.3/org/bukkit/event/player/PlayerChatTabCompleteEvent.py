"""
Python module generated from Java source file org.bukkit.event.player.PlayerChatTabCompleteEvent

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit import Warning
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerChatTabCompleteEvent(PlayerEvent):
    """
    Called when a player attempts to tab-complete a chat message.

    Deprecated
    - This event is no longer fired due to client changes
    """

    def __init__(self, who: "Player", message: str, completions: Iterable[str]):
        ...


    def getChatMessage(self) -> str:
        """
        Gets the chat message being tab-completed.

        Returns
        - the chat message
        """
        ...


    def getLastToken(self) -> str:
        """
        Gets the last 'token' of the message being tab-completed.
        
        The token is the substring starting with the character after the last
        space in the message.

        Returns
        - The last token for the chat message
        """
        ...


    def getTabCompletions(self) -> Iterable[str]:
        """
        This is the collection of completions for this event.

        Returns
        - the current completions
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
