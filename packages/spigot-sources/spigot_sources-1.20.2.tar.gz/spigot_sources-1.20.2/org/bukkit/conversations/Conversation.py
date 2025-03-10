"""
Python module generated from Java source file org.bukkit.conversations.Conversation

Java source file obtained from artifact spigot-api version 1.20.2-R0.1-20231205.164257-71

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.bukkit.conversations import *
from org.bukkit.plugin import Plugin
from typing import Any, Callable, Iterable, Tuple


class Conversation:
    """
    The Conversation class is responsible for tracking the current state of a
    conversation, displaying prompts to the user, and dispatching the user's
    response to the appropriate place. Conversation objects are not typically
    instantiated directly. Instead a ConversationFactory is used to
    construct identical conversations on demand.
    
    Conversation flow consists of a directed graph of Prompt objects.
    Each time a prompt gets input from the user, it must return the next prompt
    in the graph. Since each Prompt chooses the next Prompt, complex
    conversation trees can be implemented where the nature of the player's
    response directs the flow of the conversation.
    
    Each conversation has a ConversationPrefix that prepends all output
    from the conversation to the player. The ConversationPrefix can be used to
    display the plugin name or conversation status as the conversation evolves.
    
    Each conversation has a timeout measured in the number of inactive seconds
    to wait before abandoning the conversation. If the inactivity timeout is
    reached, the conversation is abandoned and the user's incoming and outgoing
    chat is returned to normal.
    
    You should not construct a conversation manually. Instead, use the ConversationFactory for access to all available options.
    """

    def __init__(self, plugin: "Plugin", forWhom: "Conversable", firstPrompt: "Prompt"):
        """
        Initializes a new Conversation.

        Arguments
        - plugin: The plugin that owns this conversation.
        - forWhom: The entity for whom this conversation is mediating.
        - firstPrompt: The first prompt in the conversation graph.
        """
        ...


    def __init__(self, plugin: "Plugin", forWhom: "Conversable", firstPrompt: "Prompt", initialSessionData: dict["Object", "Object"]):
        """
        Initializes a new Conversation.

        Arguments
        - plugin: The plugin that owns this conversation.
        - forWhom: The entity for whom this conversation is mediating.
        - firstPrompt: The first prompt in the conversation graph.
        - initialSessionData: Any initial values to put in the conversation
            context sessionData map.
        """
        ...


    def getForWhom(self) -> "Conversable":
        """
        Gets the entity for whom this conversation is mediating.

        Returns
        - The entity.
        """
        ...


    def isModal(self) -> bool:
        """
        Gets the modality of this conversation. If a conversation is modal, all
        messages directed to the player are suppressed for the duration of the
        conversation.

        Returns
        - The conversation modality.
        """
        ...


    def isLocalEchoEnabled(self) -> bool:
        """
        Gets the status of local echo for this conversation. If local echo is
        enabled, any text submitted to a conversation gets echoed back into the
        submitter's chat window.

        Returns
        - The status of local echo.
        """
        ...


    def setLocalEchoEnabled(self, localEchoEnabled: bool) -> None:
        """
        Sets the status of local echo for this conversation. If local echo is
        enabled, any text submitted to a conversation gets echoed back into the
        submitter's chat window.

        Arguments
        - localEchoEnabled: The status of local echo.
        """
        ...


    def getPrefix(self) -> "ConversationPrefix":
        """
        Gets the ConversationPrefix that prepends all output from this
        conversation.

        Returns
        - The ConversationPrefix in use.
        """
        ...


    def getCancellers(self) -> list["ConversationCanceller"]:
        """
        Gets the list of ConversationCancellers

        Returns
        - The list.
        """
        ...


    def getContext(self) -> "ConversationContext":
        """
        Returns the Conversation's ConversationContext.

        Returns
        - The ConversationContext.
        """
        ...


    def begin(self) -> None:
        """
        Displays the first prompt of this conversation and begins redirecting
        the user's chat responses.
        """
        ...


    def getState(self) -> "ConversationState":
        """
        Returns Returns the current state of the conversation.

        Returns
        - The current state of the conversation.
        """
        ...


    def acceptInput(self, input: str) -> None:
        """
        Passes player input into the current prompt. The next prompt (as
        determined by the current prompt) is then displayed to the user.

        Arguments
        - input: The user's chat text.
        """
        ...


    def addConversationAbandonedListener(self, listener: "ConversationAbandonedListener") -> None:
        """
        Adds a ConversationAbandonedListener.

        Arguments
        - listener: The listener to add.
        """
        ...


    def removeConversationAbandonedListener(self, listener: "ConversationAbandonedListener") -> None:
        """
        Removes a ConversationAbandonedListener.

        Arguments
        - listener: The listener to remove.
        """
        ...


    def abandon(self) -> None:
        """
        Abandons and resets the current conversation. Restores the user's
        normal chat behavior.
        """
        ...


    def abandon(self, details: "ConversationAbandonedEvent") -> None:
        """
        Abandons and resets the current conversation. Restores the user's
        normal chat behavior.

        Arguments
        - details: Details about why the conversation was abandoned
        """
        ...


    def outputNextPrompt(self) -> None:
        """
        Displays the next user prompt and abandons the conversation if the next
        prompt is null.
        """
        ...


    class ConversationState(Enum):

        UNSTARTED = 0
        STARTED = 1
        ABANDONED = 2
