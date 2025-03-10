"""
Python module generated from Java source file org.bukkit.conversations.ConversationPrefix

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ConversationPrefix:
    """
    A ConversationPrefix implementation prepends all output from the
    conversation to the player. The ConversationPrefix can be used to display
    the plugin name or conversation status as the conversation evolves.
    """

    def getPrefix(self, context: "ConversationContext") -> str:
        """
        Gets the prefix to use before each message to the player.

        Arguments
        - context: Context information about the conversation.

        Returns
        - The prefix text.
        """
        ...
