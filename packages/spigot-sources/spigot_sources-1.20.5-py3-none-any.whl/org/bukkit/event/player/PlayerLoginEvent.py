"""
Python module generated from Java source file org.bukkit.event.player.PlayerLoginEvent

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.net import InetAddress
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class PlayerLoginEvent(PlayerEvent):
    """
    Stores details for players attempting to log in.
    
    Note that this event is called *early* in the player initialization
    process. It is recommended that most options involving the Player
    *entity* be postponed to the PlayerJoinEvent instead.
    """

    def __init__(self, player: "Player", hostname: str, address: "InetAddress", realAddress: "InetAddress"):
        """
        This constructor defaults message to an empty string, and result to
        ALLOWED

        Arguments
        - player: The Player for this event
        - hostname: The hostname that was used to connect to the server
        - address: The address the player used to connect, provided for
            timing issues
        - realAddress: the actual, unspoofed connecting address
        """
        ...


    def __init__(self, player: "Player", hostname: str, address: "InetAddress"):
        """
        This constructor defaults message to an empty string, and result to
        ALLOWED

        Arguments
        - player: The Player for this event
        - hostname: The hostname that was used to connect to the server
        - address: The address the player used to connect, provided for
            timing issues
        """
        ...


    def __init__(self, player: "Player", hostname: str, address: "InetAddress", result: "Result", message: str, realAddress: "InetAddress"):
        """
        This constructor pre-configures the event with a result and message

        Arguments
        - player: The Player for this event
        - hostname: The hostname that was used to connect to the server
        - address: The address the player used to connect, provided for
            timing issues
        - result: The result status for this event
        - message: The message to be displayed if result denies login
        - realAddress: the actual, unspoofed connecting address
        """
        ...


    def getResult(self) -> "Result":
        """
        Gets the current result of the login, as an enum

        Returns
        - Current Result of the login
        """
        ...


    def setResult(self, result: "Result") -> None:
        """
        Sets the new result of the login, as an enum

        Arguments
        - result: New result to set
        """
        ...


    def getKickMessage(self) -> str:
        """
        Gets the current kick message that will be used if getResult() !=
        Result.ALLOWED

        Returns
        - Current kick message
        """
        ...


    def setKickMessage(self, message: str) -> None:
        """
        Sets the kick message to display if getResult() != Result.ALLOWED

        Arguments
        - message: New kick message
        """
        ...


    def getHostname(self) -> str:
        """
        Gets the hostname that the player used to connect to the server, or
        blank if unknown

        Returns
        - The hostname
        """
        ...


    def allow(self) -> None:
        """
        Allows the player to log in
        """
        ...


    def disallow(self, result: "Result", message: str) -> None:
        """
        Disallows the player from logging in, with the given reason

        Arguments
        - result: New result for disallowing the player
        - message: Kick message to display to the user
        """
        ...


    def getAddress(self) -> "InetAddress":
        """
        Gets the InetAddress for the Player associated with this event.
        This method is provided as a workaround for player.getAddress()
        returning null during PlayerLoginEvent.

        Returns
        - The address for this player. For legacy compatibility, this may
            be null.
        """
        ...


    def getRealAddress(self) -> "InetAddress":
        """
        Gets the connection address of this player, regardless of whether it has
        been spoofed or not.

        Returns
        - the player's connection address

        See
        - .getAddress()
        """
        ...


    def getHandlers(self) -> "HandlerList":
        ...


    @staticmethod
    def getHandlerList() -> "HandlerList":
        ...


    class Result(Enum):
        """
        Basic kick reasons for communicating to plugins
        """

        ALLOWED = 0
        """
        The player is allowed to log in
        """
        KICK_FULL = 1
        """
        The player is not allowed to log in, due to the server being full
        """
        KICK_BANNED = 2
        """
        The player is not allowed to log in, due to them being banned
        """
        KICK_WHITELIST = 3
        """
        The player is not allowed to log in, due to them not being on the
        white list
        """
        KICK_OTHER = 4
        """
        The player is not allowed to log in, for reasons undefined
        """
