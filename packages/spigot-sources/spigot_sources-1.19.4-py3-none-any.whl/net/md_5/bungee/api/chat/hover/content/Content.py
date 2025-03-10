"""
Python module generated from Java source file net.md_5.bungee.api.chat.hover.content.Content

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import HoverEvent
from net.md_5.bungee.api.chat.hover.content import *
from typing import Any, Callable, Iterable, Tuple


class Content:

    def requiredAction(self) -> "HoverEvent.Action":
        """
        Required action for this content type.

        Returns
        - action
        """
        ...


    def assertAction(self, input: "HoverEvent.Action") -> None:
        """
        Tests this content against an action

        Arguments
        - input: input to test

        Raises
        - UnsupportedOperationException: if action incompatible
        """
        ...
