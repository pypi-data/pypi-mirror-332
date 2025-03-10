"""
Python module generated from Java source file org.bukkit.conversations.StringPrompt

Java source file obtained from artifact spigot-api version 1.20.3-R0.1-20231207.085553-9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class StringPrompt(Prompt):
    """
    StringPrompt is the base class for any prompt that accepts an arbitrary
    string from the user.
    """

    def blocksForInput(self, context: "ConversationContext") -> bool:
        """
        Ensures that the prompt waits for the user to provide input.

        Arguments
        - context: Context information about the conversation.

        Returns
        - True.
        """
        ...
