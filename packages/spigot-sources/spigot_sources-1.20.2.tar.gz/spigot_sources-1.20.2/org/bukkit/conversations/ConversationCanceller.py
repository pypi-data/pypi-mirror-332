"""
Python module generated from Java source file org.bukkit.conversations.ConversationCanceller

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ConversationCanceller(Cloneable):
    """
    A ConversationCanceller is a class that cancels an active Conversation. A Conversation can have more than one ConversationCanceller.
    """

    def setConversation(self, conversation: "Conversation") -> None:
        """
        Sets the conversation this ConversationCanceller can optionally cancel.

        Arguments
        - conversation: A conversation.
        """
        ...


    def cancelBasedOnInput(self, context: "ConversationContext", input: str) -> bool:
        """
        Cancels a conversation based on user input.

        Arguments
        - context: Context information about the conversation.
        - input: The input text from the user.

        Returns
        - True to cancel the conversation, False otherwise.
        """
        ...


    def clone(self) -> "ConversationCanceller":
        """
        Allows the ConversationFactory to duplicate this
        ConversationCanceller when creating a new Conversation.
        
        Implementing this method should reset any internal object state.

        Returns
        - A clone.
        """
        ...
