"""
Python module generated from Java source file org.bukkit.conversations.RegexPrompt

Java source file obtained from artifact spigot-api version 1.20.5-R0.1-20240429.101539-37

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Pattern
from org.bukkit.conversations import *
from typing import Any, Callable, Iterable, Tuple


class RegexPrompt(ValidatingPrompt):
    """
    RegexPrompt is the base class for any prompt that requires an input
    validated by a regular expression.
    """

    def __init__(self, regex: str):
        ...


    def __init__(self, pattern: "Pattern"):
        ...
