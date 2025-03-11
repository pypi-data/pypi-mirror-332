"""
Python module generated from Java source file org.bukkit.plugin.messaging.StandardMessenger

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.collect import ImmutableSet
from com.google.common.collect.ImmutableSet import Builder
from java.util import Locale
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class StandardMessenger(Messenger):
    """
    Standard implementation to Messenger
    """

    def isReservedChannel(self, channel: str) -> bool:
        ...


    def registerOutgoingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        ...


    def unregisterOutgoingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        ...


    def unregisterOutgoingPluginChannel(self, plugin: "Plugin") -> None:
        ...


    def registerIncomingPluginChannel(self, plugin: "Plugin", channel: str, listener: "PluginMessageListener") -> "PluginMessageListenerRegistration":
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin", channel: str, listener: "PluginMessageListener") -> None:
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin") -> None:
        ...


    def getOutgoingChannels(self) -> set[str]:
        ...


    def getOutgoingChannels(self, plugin: "Plugin") -> set[str]:
        ...


    def getIncomingChannels(self) -> set[str]:
        ...


    def getIncomingChannels(self, plugin: "Plugin") -> set[str]:
        ...


    def getIncomingChannelRegistrations(self, plugin: "Plugin") -> set["PluginMessageListenerRegistration"]:
        ...


    def getIncomingChannelRegistrations(self, channel: str) -> set["PluginMessageListenerRegistration"]:
        ...


    def getIncomingChannelRegistrations(self, plugin: "Plugin", channel: str) -> set["PluginMessageListenerRegistration"]:
        ...


    def isRegistrationValid(self, registration: "PluginMessageListenerRegistration") -> bool:
        ...


    def isIncomingChannelRegistered(self, plugin: "Plugin", channel: str) -> bool:
        ...


    def isOutgoingChannelRegistered(self, plugin: "Plugin", channel: str) -> bool:
        ...


    def dispatchIncomingMessage(self, source: "Player", channel: str, message: list[int]) -> None:
        ...


    @staticmethod
    def validateChannel(channel: str) -> None:
        """
        Validates a Plugin Channel name.

        Arguments
        - channel: Channel name to validate.

        Deprecated
        - not an API method
        """
        ...


    @staticmethod
    def validateAndCorrectChannel(channel: str) -> str:
        """
        Validates and corrects a Plugin Channel name. Method is not reentrant / idempotent.

        Arguments
        - channel: Channel name to validate.

        Returns
        - corrected channel name

        Deprecated
        - not an API method
        """
        ...


    @staticmethod
    def validatePluginMessage(messenger: "Messenger", source: "Plugin", channel: str, message: list[int]) -> None:
        """
        Validates the input of a Plugin Message, ensuring the arguments are all
        valid.

        Arguments
        - messenger: Messenger to use for validation.
        - source: Source plugin of the Message.
        - channel: Plugin Channel to send the message by.
        - message: Raw message payload to send.

        Raises
        - IllegalArgumentException: Thrown if the source plugin is
            disabled.
        - IllegalArgumentException: Thrown if source, channel or message
            is null.
        - MessageTooLargeException: Thrown if the message is too big.
        - ChannelNameTooLongException: Thrown if the channel name is too
            long.
        - ChannelNotRegisteredException: Thrown if the channel is not
            registered for this plugin.
        """
        ...
