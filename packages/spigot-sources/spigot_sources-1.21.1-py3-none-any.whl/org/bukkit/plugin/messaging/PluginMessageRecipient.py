"""
Python module generated from Java source file org.bukkit.plugin.messaging.PluginMessageRecipient

Java source file obtained from artifact spigot-api version 1.21.1-R0.1-20241022.152140-54

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class PluginMessageRecipient:
    """
    Represents a possible recipient for a Plugin Message.
    """

    def sendPluginMessage(self, source: "Plugin", channel: str, message: list[int]) -> None:
        """
        Sends this recipient a Plugin Message on the specified outgoing
        channel.
        
        The message may not be larger than Messenger.MAX_MESSAGE_SIZE
        bytes, and the plugin must be registered to send messages on the
        specified channel.

        Arguments
        - source: The plugin that sent this message.
        - channel: The channel to send this message on.
        - message: The raw message to send.

        Raises
        - IllegalArgumentException: Thrown if the source plugin is
            disabled.
        - IllegalArgumentException: Thrown if source, channel or message
            is null.
        - MessageTooLargeException: Thrown if the message is too big.
        - ChannelNotRegisteredException: Thrown if the channel is not
            registered for this plugin.
        """
        ...


    def getListeningPluginChannels(self) -> set[str]:
        """
        Gets a set containing all the Plugin Channels that this client is
        listening on.

        Returns
        - Set containing all the channels that this client may accept.
        """
        ...
