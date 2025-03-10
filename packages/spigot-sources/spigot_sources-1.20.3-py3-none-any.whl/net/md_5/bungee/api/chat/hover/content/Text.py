"""
Python module generated from Java source file net.md_5.bungee.api.chat.hover.content.Text

Java source file obtained from artifact bungeecord-chat version 1.20-R0.1-20230802.100237-14

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import HoverEvent
from net.md_5.bungee.api.chat.hover.content import *
from typing import Any, Callable, Iterable, Tuple


class Text(Content):

    def __init__(self, value: list["BaseComponent"]):
        ...


    def __init__(self, value: str):
        ...


    def requiredAction(self) -> "HoverEvent.Action":
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
