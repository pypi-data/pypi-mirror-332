"""
Python module generated from Java source file org.bukkit.event.player.AsyncPlayerPreLoginEvent

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.net import InetAddress
from java.util import UUID
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.event.player import *
from typing import Any, Callable, Iterable, Tuple


class AsyncPlayerPreLoginEvent(Event):
    """
    Stores details for players attempting to log in.
    
    This event is asynchronous, and not run using main thread.
    """

    def __init__(self, name: str, ipAddress: "InetAddress"):
        ...


    def __init__(self, name: str, ipAddress: "InetAddress", uniqueId: "UUID"):
        ...


    def getLoginResult(self) -> "Result":
        """
        Gets the current result of the login, as an enum

        Returns
        - Current Result of the login
        """
        ...


    def getResult(self) -> "PlayerPreLoginEvent.Result":
        """
        Gets the current result of the login, as an enum

        Returns
        - Current Result of the login

        See
        - .getLoginResult()

        Deprecated
        - This method uses a deprecated enum from PlayerPreLoginEvent
        """
        ...


    def setLoginResult(self, result: "Result") -> None:
        """
        Sets the new result of the login, as an enum

        Arguments
        - result: New result to set
        """
        ...


    def setResult(self, result: "PlayerPreLoginEvent.Result") -> None:
        """
        Sets the new result of the login, as an enum

        Arguments
        - result: New result to set

        See
        - .setLoginResult(Result)

        Deprecated
        - This method uses a deprecated enum from PlayerPreLoginEvent
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


    def disallow(self, result: "PlayerPreLoginEvent.Result", message: str) -> None:
        """
        Disallows the player from logging in, with the given reason

        Arguments
        - result: New result for disallowing the player
        - message: Kick message to display to the user

        See
        - .disallow(Result, String)

        Deprecated
        - This method uses a deprecated enum from PlayerPreLoginEvent
        """
        ...


    def getName(self) -> str:
        """
        Gets the player's name.

        Returns
        - the player's name
        """
        ...


    def getAddress(self) -> "InetAddress":
        """
        Gets the player IP address.

        Returns
        - The IP address
        """
        ...


    def getUniqueId(self) -> "UUID":
        """
        Gets the player's unique ID.

        Returns
        - The unique ID
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
