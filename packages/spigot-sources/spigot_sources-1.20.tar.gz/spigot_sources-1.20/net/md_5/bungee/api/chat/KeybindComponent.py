"""
Python module generated from Java source file net.md_5.bungee.api.chat.KeybindComponent

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class KeybindComponent(BaseComponent):

    def __init__(self, original: "KeybindComponent"):
        """
        Creates a keybind component from the original to clone it.

        Arguments
        - original: the original for the new keybind component.
        """
        ...


    def __init__(self, keybind: str):
        """
        Creates a keybind component with the passed internal keybind value.

        Arguments
        - keybind: the keybind value

        See
        - Keybinds
        """
        ...


    def duplicate(self) -> "KeybindComponent":
        ...
