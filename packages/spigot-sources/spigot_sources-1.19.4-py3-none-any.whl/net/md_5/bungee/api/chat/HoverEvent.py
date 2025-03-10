"""
Python module generated from Java source file net.md_5.bungee.api.chat.HoverEvent

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from enum import Enum
from java.util import Collections
from net.md_5.bungee.api.chat import *
from net.md_5.bungee.api.chat.hover.content import Content
from net.md_5.bungee.api.chat.hover.content import Entity
from net.md_5.bungee.api.chat.hover.content import Item
from net.md_5.bungee.api.chat.hover.content import Text
from net.md_5.bungee.chat import ComponentSerializer
from typing import Any, Callable, Iterable, Tuple


class HoverEvent:

    def __init__(self, action: "Action", *contents: Tuple["Content", ...]):
        """
        Creates event with an action and a list of contents.

        Arguments
        - action: action of this event
        - contents: array of contents, provide at least one
        """
        ...


    def __init__(self, action: "Action", value: list["BaseComponent"]):
        """
        Legacy constructor to create hover event.

        Arguments
        - action: the action
        - value: the value

        Deprecated
        - .HoverEvent(Action, Content[])
        """
        ...


    def getValue(self) -> list["BaseComponent"]:
        ...


    def addContent(self, content: "Content") -> None:
        """
        Adds a content to this hover event.

        Arguments
        - content: the content add

        Raises
        - IllegalArgumentException: if is a legacy component and already has
        a content
        - UnsupportedOperationException: if content action does not match
        hover event action
        """
        ...


    @staticmethod
    def getClass(action: "HoverEvent.Action", array: bool) -> type[Any]:
        """
        Gets the appropriate Content class for an Action for the
        GSON serialization

        Arguments
        - action: the action to get for
        - array: if to return the arrayed class

        Returns
        - the class
        """
        ...


    class Action(Enum):

        SHOW_TEXT = 0
        SHOW_ITEM = 1
        SHOW_ENTITY = 2
        SHOW_ACHIEVEMENT = 3
        """
        Removed since 1.12. Advancements instead simply use show_text. The ID
        of an achievement or statistic to display. Example: new
        ComponentText( "achievement.openInventory" )
        """
