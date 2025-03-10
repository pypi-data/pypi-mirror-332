"""
Python module generated from Java source file org.bukkit.conversations.PluginNameConversationPrefix

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ChatColor
from org.bukkit.conversations import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class PluginNameConversationPrefix(ConversationPrefix):
    """
    PluginNameConversationPrefix is a ConversationPrefix implementation
    that displays the plugin name in front of conversation output.
    """

    def __init__(self, plugin: "Plugin"):
        ...


    def __init__(self, plugin: "Plugin", separator: str, prefixColor: "ChatColor"):
        ...


    def getPrefix(self, context: "ConversationContext") -> str:
        """
        Prepends each conversation message with the plugin name.

        Arguments
        - context: Context information about the conversation.

        Returns
        - An empty string.
        """
        ...
