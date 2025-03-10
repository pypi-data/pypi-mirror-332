"""
Python module generated from Java source file org.bukkit.conversations.MessagePrompt

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class MessagePrompt(Prompt):
    """
    MessagePrompt is the base class for any prompt that only displays a message
    to the user and requires no input.
    """

    def __init__(self):
        ...


    def blocksForInput(self, context: "ConversationContext") -> bool:
        """
        Message prompts never wait for user input before continuing.

        Arguments
        - context: Context information about the conversation.

        Returns
        - Always False.
        """
        ...


    def acceptInput(self, context: "ConversationContext", input: str) -> "Prompt":
        """
        Accepts and ignores any user input, returning the next prompt in the
        prompt graph instead.

        Arguments
        - context: Context information about the conversation.
        - input: Ignored.

        Returns
        - The next prompt in the prompt graph.
        """
        ...
