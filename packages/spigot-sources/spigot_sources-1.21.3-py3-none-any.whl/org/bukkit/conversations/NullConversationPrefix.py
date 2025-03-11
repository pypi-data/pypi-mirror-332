"""
Python module generated from Java source file org.bukkit.conversations.NullConversationPrefix

Java source file obtained from artifact spigot-api version 1.21.3-R0.1-20241203.162251-46

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class NullConversationPrefix(ConversationPrefix):
    """
    NullConversationPrefix is a ConversationPrefix implementation that
    displays nothing in front of conversation output.
    """

    def getPrefix(self, context: "ConversationContext") -> str:
        """
        Prepends each conversation message with an empty string.

        Arguments
        - context: Context information about the conversation.

        Returns
        - An empty string.
        """
        ...
