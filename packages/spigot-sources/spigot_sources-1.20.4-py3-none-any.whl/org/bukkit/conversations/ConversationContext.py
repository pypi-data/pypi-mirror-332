"""
Python module generated from Java source file org.bukkit.conversations.ConversationContext

Java source file obtained from artifact spigot-api version 1.20.4-R0.1-20240423.152506-123

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class ConversationContext:
    """
    A ConversationContext provides continuity between nodes in the prompt graph
    by giving the developer access to the subject of the conversation and a
    generic map for storing values that are shared between all Prompt
    invocations.
    """

    def __init__(self, plugin: "Plugin", forWhom: "Conversable", initialSessionData: dict["Object", "Object"]):
        """
        Arguments
        - plugin: The owning plugin.
        - forWhom: The subject of the conversation.
        - initialSessionData: Any initial values to put in the sessionData
            map.
        """
        ...


    def getPlugin(self) -> "Plugin":
        """
        Gets the plugin that owns this conversation.

        Returns
        - The owning plugin.
        """
        ...


    def getForWhom(self) -> "Conversable":
        """
        Gets the subject of the conversation.

        Returns
        - The subject of the conversation.
        """
        ...


    def getAllSessionData(self) -> dict["Object", "Object"]:
        """
        Gets the underlying sessionData map.
        
        May be directly modified to manipulate session data.

        Returns
        - The full sessionData map.
        """
        ...


    def getSessionData(self, key: "Object") -> "Object":
        """
        Gets session data shared between all Prompt invocations. Use
        this as a way to pass data through each Prompt as the conversation
        develops.

        Arguments
        - key: The session data key.

        Returns
        - The requested session data.
        """
        ...


    def setSessionData(self, key: "Object", value: "Object") -> None:
        """
        Sets session data shared between all Prompt invocations. Use
        this as a way to pass data through each prompt as the conversation
        develops.

        Arguments
        - key: The session data key.
        - value: The session data value.
        """
        ...
