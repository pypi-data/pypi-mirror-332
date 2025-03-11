"""
Python module generated from Java source file org.bukkit.event.player.AsyncPlayerChatPreviewEvent

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import Warning
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class AsyncPlayerChatPreviewEvent(AsyncPlayerChatEvent):
    """
    Used to format chat for chat preview. If this event is used, then the result
    of the corresponding AsyncPlayerChatEvent **must** be formatted in
    the same way.

    Deprecated
    - chat previews have been removed
    """

    def __init__(self, async: bool, who: "Player", message: str, players: set["Player"]):
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...
