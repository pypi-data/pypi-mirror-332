"""
Python module generated from Java source file net.md_5.bungee.api.chat.hover.content.Entity

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from lombok import NonNull
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import HoverEvent
from net.md_5.bungee.api.chat.hover.content import *
from typing import Any, Callable, Iterable, Tuple


class Entity(Content):

    def requiredAction(self) -> "HoverEvent.Action":
        ...
