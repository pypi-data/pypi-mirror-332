"""
Python module generated from Java source file org.bukkit.event.server.ServerListPingEvent

Java source file obtained from artifact spigot-api version 1.20.6-R0.1-20240613.150924-57

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from java.net import InetAddress
from java.util import Iterator
from org.bukkit import Bukkit
from org.bukkit import UndefinedNullability
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.server import *
from org.bukkit.util import CachedServerIcon
from typing import Any, Callable, Iterable, Tuple


class ServerListPingEvent(ServerEvent, Iterable):
    """
    Called when a server list ping is coming in. Displayed players can be
    checked and removed by .iterator() iterating over this event.
    
    **Note:** The players in .iterator() will not be shown in the
    server info if Bukkit.getHideOnlinePlayers() is True.
    """

    def __init__(self, hostname: str, address: "InetAddress", motd: str, numPlayers: int, maxPlayers: int):
        ...


    def getHostname(self) -> str:
        """
        Gets the hostname that the player used to connect to the server, or
        blank if unknown

        Returns
        - The hostname
        """
        ...


    def getAddress(self) -> "InetAddress":
        """
        Get the address the ping is coming from.

        Returns
        - the address
        """
        ...


    def getMotd(self) -> str:
        """
        Get the message of the day message.

        Returns
        - the message of the day
        """
        ...


    def setMotd(self, motd: str) -> None:
        """
        Change the message of the day message.

        Arguments
        - motd: the message of the day
        """
        ...


    def getNumPlayers(self) -> int:
        """
        Get the number of players sent.

        Returns
        - the number of players
        """
        ...


    def getMaxPlayers(self) -> int:
        """
        Get the maximum number of players sent.

        Returns
        - the maximum number of players
        """
        ...


    def shouldSendChatPreviews(self) -> bool:
        """
        Gets whether the server needs to send a preview of the chat to the
        client.

        Returns
        - True if chat preview is enabled, False otherwise

        Deprecated
        - chat previews have been removed
        """
        ...


    def setMaxPlayers(self, maxPlayers: int) -> None:
        """
        Set the maximum number of players sent.

        Arguments
        - maxPlayers: the maximum number of player
        """
        ...


    def setServerIcon(self, icon: "CachedServerIcon") -> None:
        """
        Sets the server-icon sent to the client.

        Arguments
        - icon: the icon to send to the client

        Raises
        - IllegalArgumentException: if the CachedServerIcon is not
            created by the caller of this event; null may be accepted for some
            implementations
        - UnsupportedOperationException: if the caller of this event does
            not support setting the server icon
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    def iterator(self) -> Iterator["Player"]:
        """
        
        
        Calling the Iterator.remove() method will force that particular
        player to not be displayed on the player list, decrease the size
        returned by .getNumPlayers(), and will not be returned again by
        any new iterator.
        
        **Note:** The players here will not be shown in the server info if
        Bukkit.getHideOnlinePlayers() is True.

        Raises
        - UnsupportedOperationException: if the caller of this event does
            not support removing players
        """
        ...
