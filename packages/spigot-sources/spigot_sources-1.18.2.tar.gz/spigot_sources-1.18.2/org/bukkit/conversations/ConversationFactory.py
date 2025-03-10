"""
Python module generated from Java source file org.bukkit.conversations.ConversationFactory

Java source file obtained from artifact spigot-api version 1.18.2-R0.1-20220607.160742-53

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class ConversationFactory:
    """
    A ConversationFactory is responsible for creating a Conversation
    from a predefined template. A ConversationFactory is typically created when
    a plugin is instantiated and builds a Conversation each time a user
    initiates a conversation with the plugin. Each Conversation maintains its
    own state and calls back as needed into the plugin.
    
    The ConversationFactory implements a fluid API, allowing parameters to be
    set as an extension to the constructor.
    """

    def __init__(self, plugin: "Plugin"):
        """
        Constructs a ConversationFactory.

        Arguments
        - plugin: The plugin that owns the factory.
        """
        ...


    def withModality(self, modal: bool) -> "ConversationFactory":
        """
        Sets the modality of all Conversations created by this factory.
        If a conversation is modal, all messages directed to the player are
        suppressed for the duration of the conversation.
        
        The default is True.

        Arguments
        - modal: The modality of all conversations to be created.

        Returns
        - This object.
        """
        ...


    def withLocalEcho(self, localEchoEnabled: bool) -> "ConversationFactory":
        """
        Sets the local echo status for all Conversations created by
        this factory. If local echo is enabled, any text submitted to a
        conversation gets echoed back into the submitter's chat window.

        Arguments
        - localEchoEnabled: The status of local echo.

        Returns
        - This object.
        """
        ...


    def withPrefix(self, prefix: "ConversationPrefix") -> "ConversationFactory":
        """
        Sets the ConversationPrefix that prepends all output from all
        generated conversations.
        
        The default is a NullConversationPrefix;

        Arguments
        - prefix: The ConversationPrefix to use.

        Returns
        - This object.
        """
        ...


    def withTimeout(self, timeoutSeconds: int) -> "ConversationFactory":
        """
        Sets the number of inactive seconds to wait before automatically
        abandoning all generated conversations.
        
        The default is 600 seconds (5 minutes).

        Arguments
        - timeoutSeconds: The number of seconds to wait.

        Returns
        - This object.
        """
        ...


    def withFirstPrompt(self, firstPrompt: "Prompt") -> "ConversationFactory":
        """
        Sets the first prompt to use in all generated conversations.
        
        The default is Prompt.END_OF_CONVERSATION.

        Arguments
        - firstPrompt: The first prompt.

        Returns
        - This object.
        """
        ...


    def withInitialSessionData(self, initialSessionData: dict["Object", "Object"]) -> "ConversationFactory":
        """
        Sets any initial data with which to populate the conversation context
        sessionData map.

        Arguments
        - initialSessionData: The conversation context's initial
            sessionData.

        Returns
        - This object.
        """
        ...


    def withEscapeSequence(self, escapeSequence: str) -> "ConversationFactory":
        """
        Sets the player input that, when received, will immediately terminate
        the conversation.

        Arguments
        - escapeSequence: Input to terminate the conversation.

        Returns
        - This object.
        """
        ...


    def withConversationCanceller(self, canceller: "ConversationCanceller") -> "ConversationFactory":
        """
        Adds a ConversationCanceller to constructed conversations.

        Arguments
        - canceller: The ConversationCanceller to add.

        Returns
        - This object.
        """
        ...


    def thatExcludesNonPlayersWithMessage(self, playerOnlyMessage: str) -> "ConversationFactory":
        """
        Prevents this factory from creating a conversation for non-player
        Conversable objects.

        Arguments
        - playerOnlyMessage: The message to return to a non-play in lieu of
            starting a conversation.

        Returns
        - This object.
        """
        ...


    def addConversationAbandonedListener(self, listener: "ConversationAbandonedListener") -> "ConversationFactory":
        """
        Adds a ConversationAbandonedListener to all conversations
        constructed by this factory.

        Arguments
        - listener: The listener to add.

        Returns
        - This object.
        """
        ...


    def buildConversation(self, forWhom: "Conversable") -> "Conversation":
        """
        Constructs a Conversation in accordance with the defaults set
        for this factory.

        Arguments
        - forWhom: The entity for whom the new conversation is mediating.

        Returns
        - A new conversation.
        """
        ...
