"""
Python module generated from Java source file net.md_5.bungee.api.chat.ClickEvent

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ClickEvent:

    class Action(Enum):

        OPEN_URL = 0
        """
        Open a url at the path given by
        net.md_5.bungee.api.chat.ClickEvent.value.
        """
        OPEN_FILE = 1
        """
        Open a file at the path given by
        net.md_5.bungee.api.chat.ClickEvent.value.
        """
        RUN_COMMAND = 2
        """
        Run the command given by
        net.md_5.bungee.api.chat.ClickEvent.value.
        """
        SUGGEST_COMMAND = 3
        """
        Inserts the string given by
        net.md_5.bungee.api.chat.ClickEvent.value into the player's
        text box.
        """
        CHANGE_PAGE = 4
        """
        Change to the page number given by
        net.md_5.bungee.api.chat.ClickEvent.value in a book.
        """
        COPY_TO_CLIPBOARD = 5
        """
        Copy the string given by
        net.md_5.bungee.api.chat.ClickEvent.value into the player's
        clipboard.
        """
