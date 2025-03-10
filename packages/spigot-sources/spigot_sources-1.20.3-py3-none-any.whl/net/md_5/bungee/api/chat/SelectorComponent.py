"""
Python module generated from Java source file net.md_5.bungee.api.chat.SelectorComponent

Java source file obtained from artifact bungeecord-chat version 1.20-R0.1-20230802.100237-14

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class SelectorComponent(BaseComponent):
    """
    This component processes a target selector into a pre-formatted set of
    discovered names.
    
    Multiple targets may be obtained, and with commas separating each one and a
    final "and" for the last target. The resulting format cannot be overwritten.
    This includes all styling from team prefixes, insertions, click events, and
    hover events.
    
    These values are filled in by the server-side implementation.
    
    As of 1.12.2, a bug ( MC-56373 ) prevents full usage within hover events.
    """

    def __init__(self, original: "SelectorComponent"):
        """
        Creates a selector component from the original to clone it.

        Arguments
        - original: the original for the new selector component
        """
        ...


    def duplicate(self) -> "SelectorComponent":
        ...
