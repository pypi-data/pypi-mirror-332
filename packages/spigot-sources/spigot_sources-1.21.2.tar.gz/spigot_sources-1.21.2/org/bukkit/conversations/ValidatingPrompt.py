"""
Python module generated from Java source file org.bukkit.conversations.ValidatingPrompt

Java source file obtained from artifact spigot-api version 1.21.2-R0.1-20241023.084343-5

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit import ChatColor
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class ValidatingPrompt(Prompt):
    """
    ValidatingPrompt is the base class for any prompt that requires validation.
    ValidatingPrompt will keep replaying the prompt text until the user enters
    a valid response.
    """

    def __init__(self):
        ...


    def acceptInput(self, context: "ConversationContext", input: str) -> "Prompt":
        """
        Accepts and processes input from the user and validates it. If
        validation fails, this prompt is returned for re-execution, otherwise
        the next Prompt in the prompt graph is returned.

        Arguments
        - context: Context information about the conversation.
        - input: The input text from the user.

        Returns
        - This prompt or the next Prompt in the prompt graph.
        """
        ...


    def blocksForInput(self, context: "ConversationContext") -> bool:
        """
        Ensures that the prompt waits for the user to provide input.

        Arguments
        - context: Context information about the conversation.

        Returns
        - True.
        """
        ...
