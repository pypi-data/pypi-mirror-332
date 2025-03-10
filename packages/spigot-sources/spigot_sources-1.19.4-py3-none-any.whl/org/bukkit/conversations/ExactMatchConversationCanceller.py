"""
Python module generated from Java source file org.bukkit.conversations.ExactMatchConversationCanceller

Java source file obtained from artifact spigot-api version 1.19.4-R0.1-20230607.155743-88

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ExactMatchConversationCanceller(ConversationCanceller):
    """
    An ExactMatchConversationCanceller cancels a conversation if the user
    enters an exact input string
    """

    def __init__(self, escapeSequence: str):
        """
        Builds an ExactMatchConversationCanceller.

        Arguments
        - escapeSequence: The string that, if entered by the user, will
            cancel the conversation.
        """
        ...


    def setConversation(self, conversation: "Conversation") -> None:
        ...


    def cancelBasedOnInput(self, context: "ConversationContext", input: str) -> bool:
        ...


    def clone(self) -> "ConversationCanceller":
        ...
