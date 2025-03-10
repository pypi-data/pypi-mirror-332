"""
Python module generated from Java source file org.bukkit.conversations.Conversable

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import UUID
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class Conversable:
    """
    The Conversable interface is used to indicate objects that can have
    conversations.
    """

    def isConversing(self) -> bool:
        """
        Tests to see of a Conversable object is actively engaged in a
        conversation.

        Returns
        - True if a conversation is in progress
        """
        ...


    def acceptConversationInput(self, input: str) -> None:
        """
        Accepts input into the active conversation. If no conversation is in
        progress, this method does nothing.

        Arguments
        - input: The input message into the conversation
        """
        ...


    def beginConversation(self, conversation: "Conversation") -> bool:
        """
        Enters into a dialog with a Conversation object.

        Arguments
        - conversation: The conversation to begin

        Returns
        - True if the conversation should proceed, False if it has been
            enqueued
        """
        ...


    def abandonConversation(self, conversation: "Conversation") -> None:
        """
        Abandons an active conversation.

        Arguments
        - conversation: The conversation to abandon
        """
        ...


    def abandonConversation(self, conversation: "Conversation", details: "ConversationAbandonedEvent") -> None:
        """
        Abandons an active conversation.

        Arguments
        - conversation: The conversation to abandon
        - details: Details about why the conversation was abandoned
        """
        ...


    def sendRawMessage(self, message: str) -> None:
        """
        Sends this sender a message raw

        Arguments
        - message: Message to be displayed
        """
        ...


    def sendRawMessage(self, sender: "UUID", message: str) -> None:
        """
        Sends this sender a message raw

        Arguments
        - message: Message to be displayed
        - sender: The sender of this message
        """
        ...
