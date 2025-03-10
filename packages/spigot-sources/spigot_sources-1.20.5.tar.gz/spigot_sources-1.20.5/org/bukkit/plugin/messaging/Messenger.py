"""
Python module generated from Java source file org.bukkit.plugin.messaging.Messenger

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import NamespacedKey
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class Messenger:
    """
    A class responsible for managing the registrations of plugin channels and
    their listeners.
    
    Channel names must contain a colon separator and consist of only [a-z0-9/._-]
    - i.e. they MUST be valid NamespacedKey. The "BungeeCord" channel is
    an exception and may only take this form.
    """

    MAX_MESSAGE_SIZE = 32766
    """
    Represents the largest size that an individual Plugin Message may be.
    """
    MAX_CHANNEL_SIZE = 64
    """
    Represents the largest size that a Plugin Channel may be.
    """


    def isReservedChannel(self, channel: str) -> bool:
        """
        Checks if the specified channel is a reserved name.
        
        All channels within the "minecraft" namespace except for
        "minecraft:brand" are reserved.

        Arguments
        - channel: Channel name to check.

        Returns
        - True if the channel is reserved, otherwise False.

        Raises
        - IllegalArgumentException: Thrown if channel is null.
        """
        ...


    def registerOutgoingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        """
        Registers the specific plugin to the requested outgoing plugin channel,
        allowing it to send messages through that channel to any clients.

        Arguments
        - plugin: Plugin that wishes to send messages through the channel.
        - channel: Channel to register.

        Raises
        - IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...


    def unregisterOutgoingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        """
        Unregisters the specific plugin from the requested outgoing plugin
        channel, no longer allowing it to send messages through that channel to
        any clients.

        Arguments
        - plugin: Plugin that no longer wishes to send messages through the
            channel.
        - channel: Channel to unregister.

        Raises
        - IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...


    def unregisterOutgoingPluginChannel(self, plugin: "Plugin") -> None:
        """
        Unregisters the specific plugin from all outgoing plugin channels, no
        longer allowing it to send any plugin messages.

        Arguments
        - plugin: Plugin that no longer wishes to send plugin messages.

        Raises
        - IllegalArgumentException: Thrown if plugin is null.
        """
        ...


    def registerIncomingPluginChannel(self, plugin: "Plugin", channel: str, listener: "PluginMessageListener") -> "PluginMessageListenerRegistration":
        """
        Registers the specific plugin for listening on the requested incoming
        plugin channel, allowing it to act upon any plugin messages.

        Arguments
        - plugin: Plugin that wishes to register to this channel.
        - channel: Channel to register.
        - listener: Listener to receive messages on.

        Returns
        - The resulting registration that was made as a result of this
            method.

        Raises
        - IllegalArgumentException: Thrown if plugin, channel or listener
            is null, or the listener is already registered for this channel.
        """
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin", channel: str, listener: "PluginMessageListener") -> None:
        """
        Unregisters the specific plugin's listener from listening on the
        requested incoming plugin channel, no longer allowing it to act upon
        any plugin messages.

        Arguments
        - plugin: Plugin that wishes to unregister from this channel.
        - channel: Channel to unregister.
        - listener: Listener to stop receiving messages on.

        Raises
        - IllegalArgumentException: Thrown if plugin, channel or listener
            is null.
        """
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin", channel: str) -> None:
        """
        Unregisters the specific plugin from listening on the requested
        incoming plugin channel, no longer allowing it to act upon any plugin
        messages.

        Arguments
        - plugin: Plugin that wishes to unregister from this channel.
        - channel: Channel to unregister.

        Raises
        - IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...


    def unregisterIncomingPluginChannel(self, plugin: "Plugin") -> None:
        """
        Unregisters the specific plugin from listening on all plugin channels
        through all listeners.

        Arguments
        - plugin: Plugin that wishes to unregister from this channel.

        Raises
        - IllegalArgumentException: Thrown if plugin is null.
        """
        ...


    def getOutgoingChannels(self) -> set[str]:
        """
        Gets a set containing all the outgoing plugin channels.

        Returns
        - List of all registered outgoing plugin channels.
        """
        ...


    def getOutgoingChannels(self, plugin: "Plugin") -> set[str]:
        """
        Gets a set containing all the outgoing plugin channels that the
        specified plugin is registered to.

        Arguments
        - plugin: Plugin to retrieve channels for.

        Returns
        - List of all registered outgoing plugin channels that a plugin
            is registered to.

        Raises
        - IllegalArgumentException: Thrown if plugin is null.
        """
        ...


    def getIncomingChannels(self) -> set[str]:
        """
        Gets a set containing all the incoming plugin channels.

        Returns
        - List of all registered incoming plugin channels.
        """
        ...


    def getIncomingChannels(self, plugin: "Plugin") -> set[str]:
        """
        Gets a set containing all the incoming plugin channels that the
        specified plugin is registered for.

        Arguments
        - plugin: Plugin to retrieve channels for.

        Returns
        - List of all registered incoming plugin channels that the plugin
            is registered for.

        Raises
        - IllegalArgumentException: Thrown if plugin is null.
        """
        ...


    def getIncomingChannelRegistrations(self, plugin: "Plugin") -> set["PluginMessageListenerRegistration"]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that the specified plugin has.

        Arguments
        - plugin: Plugin to retrieve registrations for.

        Returns
        - List of all registrations that the plugin has.

        Raises
        - IllegalArgumentException: Thrown if plugin is null.
        """
        ...


    def getIncomingChannelRegistrations(self, channel: str) -> set["PluginMessageListenerRegistration"]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that are on the requested channel.

        Arguments
        - channel: Channel to retrieve registrations for.

        Returns
        - List of all registrations that are on the channel.

        Raises
        - IllegalArgumentException: Thrown if channel is null.
        """
        ...


    def getIncomingChannelRegistrations(self, plugin: "Plugin", channel: str) -> set["PluginMessageListenerRegistration"]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that the specified plugin has on the requested channel.

        Arguments
        - plugin: Plugin to retrieve registrations for.
        - channel: Channel to filter registrations by.

        Returns
        - List of all registrations that the plugin has.

        Raises
        - IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...


    def isRegistrationValid(self, registration: "PluginMessageListenerRegistration") -> bool:
        """
        Checks if the specified plugin message listener registration is valid.
        
        A registration is considered valid if it has not be unregistered and
        that the plugin is still enabled.

        Arguments
        - registration: Registration to check.

        Returns
        - True if the registration is valid, otherwise False.
        """
        ...


    def isIncomingChannelRegistered(self, plugin: "Plugin", channel: str) -> bool:
        """
        Checks if the specified plugin has registered to receive incoming
        messages through the requested channel.

        Arguments
        - plugin: Plugin to check registration for.
        - channel: Channel to test for.

        Returns
        - True if the channel is registered, else False.
        """
        ...


    def isOutgoingChannelRegistered(self, plugin: "Plugin", channel: str) -> bool:
        """
        Checks if the specified plugin has registered to send outgoing messages
        through the requested channel.

        Arguments
        - plugin: Plugin to check registration for.
        - channel: Channel to test for.

        Returns
        - True if the channel is registered, else False.
        """
        ...


    def dispatchIncomingMessage(self, source: "Player", channel: str, message: list[int]) -> None:
        """
        Dispatches the specified incoming message to any registered listeners.

        Arguments
        - source: Source of the message.
        - channel: Channel that the message was sent by.
        - message: Raw payload of the message.
        """
        ...
