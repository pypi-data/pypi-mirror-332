"""
Python module generated from Java source file org.bukkit.conversations.ConversationAbandonedEvent

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import EventObject
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ConversationAbandonedEvent(EventObject):
    """
    ConversationAbandonedEvent contains information about an abandoned
    conversation.
    """

    def __init__(self, conversation: "Conversation"):
        ...


    def __init__(self, conversation: "Conversation", canceller: "ConversationCanceller"):
        ...


    def getCanceller(self) -> "ConversationCanceller":
        """
        Gets the object that caused the conversation to be abandoned.

        Returns
        - The object that abandoned the conversation.
        """
        ...


    def getContext(self) -> "ConversationContext":
        """
        Gets the abandoned conversation's conversation context.

        Returns
        - The abandoned conversation's conversation context.
        """
        ...


    def gracefulExit(self) -> bool:
        """
        Indicates how the conversation was abandoned - naturally as part of the
        prompt chain or prematurely via a ConversationCanceller.

        Returns
        - True if the conversation is abandoned gracefully by a Prompt returning null or the next prompt. False of the
            conversations is abandoned prematurely by a ConversationCanceller.
        """
        ...
