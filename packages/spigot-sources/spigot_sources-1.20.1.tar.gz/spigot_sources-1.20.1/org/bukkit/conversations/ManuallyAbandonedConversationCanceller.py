"""
Python module generated from Java source file org.bukkit.conversations.ManuallyAbandonedConversationCanceller

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ManuallyAbandonedConversationCanceller(ConversationCanceller):
    """
    The ManuallyAbandonedConversationCanceller is only used as part of a ConversationAbandonedEvent to indicate that the conversation was manually
    abandoned by programmatically calling the abandon() method on it.
    """

    def setConversation(self, conversation: "Conversation") -> None:
        ...


    def cancelBasedOnInput(self, context: "ConversationContext", input: str) -> bool:
        ...


    def clone(self) -> "ConversationCanceller":
        ...
