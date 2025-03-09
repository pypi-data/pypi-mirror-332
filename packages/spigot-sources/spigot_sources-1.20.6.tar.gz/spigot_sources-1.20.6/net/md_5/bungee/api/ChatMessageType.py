"""
Python module generated from Java source file net.md_5.bungee.api.ChatMessageType

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from net.md_5.bungee.api import *
from typing import Any, Callable, Iterable, Tuple


class ChatMessageType(Enum):
    """
    Represents the position on the screen where a message will appear.
    """

    CHAT = 0
    SYSTEM = 1
    ACTION_BAR = 2
