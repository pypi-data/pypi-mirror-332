"""
Python module generated from Java source file org.bukkit.conversations.Prompt

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class Prompt(Cloneable):
    """
    A Prompt is the main constituent of a Conversation. Each prompt
    displays text to the user and optionally waits for a user's response.
    Prompts are chained together into a directed graph that represents the
    conversation flow. To halt a conversation, END_OF_CONVERSATION is returned
    in liu of another Prompt object.
    """

    END_OF_CONVERSATION = None
    """
    A convenience constant for indicating the end of a conversation.
    """


    def getPromptText(self, context: "ConversationContext") -> str:
        """
        Gets the text to display to the user when this prompt is first
        presented.

        Arguments
        - context: Context information about the conversation.

        Returns
        - The text to display.
        """
        ...


    def blocksForInput(self, context: "ConversationContext") -> bool:
        """
        Checks to see if this prompt implementation should wait for user input
        or immediately display the next prompt.

        Arguments
        - context: Context information about the conversation.

        Returns
        - If True, the Conversation will wait for input before
            continuing. If False, .acceptInput(ConversationContext, String) will be called immediately with `null` input.
        """
        ...


    def acceptInput(self, context: "ConversationContext", input: str) -> "Prompt":
        """
        Accepts and processes input from the user. Using the input, the next
        Prompt in the prompt graph is returned.

        Arguments
        - context: Context information about the conversation.
        - input: The input text from the user.

        Returns
        - The next Prompt in the prompt graph.
        """
        ...
