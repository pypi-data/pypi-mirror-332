"""
Python module generated from Java source file org.bukkit.conversations.ConversationAbandonedListener

Java source file obtained from artifact spigot-api version 1.17.1-R0.1-20211121.234319-104

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import EventListener
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ConversationAbandonedListener(EventListener):
    """

    """

    def conversationAbandoned(self, abandonedEvent: "ConversationAbandonedEvent") -> None:
        """
        Called whenever a Conversation is abandoned.

        Arguments
        - abandonedEvent: Contains details about the abandoned
            conversation.
        """
        ...
