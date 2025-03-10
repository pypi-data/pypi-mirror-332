"""
Python module generated from Java source file org.bukkit.command.CommandSender

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit import Server
from org.bukkit.command import *
from org.bukkit.permissions import Permissible
from typing import Any, Callable, Iterable, Tuple


class CommandSender(Permissible):

    def sendMessage(self, message: str) -> None:
        """
        Sends this sender a message

        Arguments
        - message: Message to be displayed
        """
        ...


    def sendMessage(self, *messages: Tuple[str, ...]) -> None:
        """
        Sends this sender multiple messages

        Arguments
        - messages: An array of messages to be displayed
        """
        ...


    def sendMessage(self, sender: "UUID", message: str) -> None:
        """
        Sends this sender a message

        Arguments
        - message: Message to be displayed
        - sender: The sender of this message
        """
        ...


    def sendMessage(self, sender: "UUID", *messages: Tuple[str, ...]) -> None:
        """
        Sends this sender multiple messages

        Arguments
        - messages: An array of messages to be displayed
        - sender: The sender of this message
        """
        ...


    def getServer(self) -> "Server":
        """
        Returns the server instance that this command is running on

        Returns
        - Server instance
        """
        ...


    def getName(self) -> str:
        """
        Gets the name of this command sender

        Returns
        - Name of the sender
        """
        ...


    def spigot(self) -> "Spigot":
        ...


    class Spigot:

        def sendMessage(self, component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            """
            Sends this sender a chat component.

            Arguments
            - component: the components to send
            """
            ...


        def sendMessage(self, *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            """
            Sends an array of components as a single message to the sender.

            Arguments
            - components: the components to send
            """
            ...


        def sendMessage(self, sender: "UUID", component: "net.md_5.bungee.api.chat.BaseComponent") -> None:
            """
            Sends this sender a chat component.

            Arguments
            - component: the components to send
            - sender: the sender of the message
            """
            ...


        def sendMessage(self, sender: "UUID", *components: Tuple["net.md_5.bungee.api.chat.BaseComponent", ...]) -> None:
            """
            Sends an array of components as a single message to the sender.

            Arguments
            - components: the components to send
            - sender: the sender of the message
            """
            ...
