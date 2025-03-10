"""
Python module generated from Java source file org.bukkit.plugin.messaging.PluginMessageListener

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.entity import Player
from org.bukkit.plugin.messaging import *
from typing import Any, Callable, Iterable, Tuple


class PluginMessageListener:
    """
    A listener for a specific Plugin Channel, which will receive notifications
    of messages sent from a client.
    """

    def onPluginMessageReceived(self, channel: str, player: "Player", message: list[int]) -> None:
        """
        A method that will be thrown when a PluginMessageSource sends a plugin
        message on a registered channel.

        Arguments
        - channel: Channel that the message was sent through.
        - player: Source of the message.
        - message: The raw message that was sent.
        """
        ...
