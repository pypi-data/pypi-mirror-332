"""
Python module generated from Java source file org.bukkit.conversations.InactivityConversationCanceller

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class InactivityConversationCanceller(ConversationCanceller):
    """
    An InactivityConversationCanceller will cancel a Conversation after
    a period of inactivity by the user.
    """

    def __init__(self, plugin: "Plugin", timeoutSeconds: int):
        """
        Creates an InactivityConversationCanceller.

        Arguments
        - plugin: The owning plugin.
        - timeoutSeconds: The number of seconds of inactivity to wait.
        """
        ...


    def setConversation(self, conversation: "Conversation") -> None:
        ...


    def cancelBasedOnInput(self, context: "ConversationContext", input: str) -> bool:
        ...


    def clone(self) -> "ConversationCanceller":
        ...
