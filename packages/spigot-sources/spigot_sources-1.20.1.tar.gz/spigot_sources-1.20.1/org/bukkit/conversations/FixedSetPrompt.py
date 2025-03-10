"""
Python module generated from Java source file org.bukkit.conversations.FixedSetPrompt

Java source file obtained from artifact spigot-api version 1.20.1-R0.1-20230921.163938-66

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Joiner
from java.util import Arrays
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class FixedSetPrompt(ValidatingPrompt):
    """
    FixedSetPrompt is the base class for any prompt that requires a fixed set
    response from the user.
    """

    def __init__(self, *fixedSet: Tuple[str, ...]):
        """
        Creates a FixedSetPrompt from a set of strings.
        
        foo = new FixedSetPrompt("bar", "cheese", "panda");

        Arguments
        - fixedSet: A fixed set of strings, one of which the user must
            type.
        """
        ...
