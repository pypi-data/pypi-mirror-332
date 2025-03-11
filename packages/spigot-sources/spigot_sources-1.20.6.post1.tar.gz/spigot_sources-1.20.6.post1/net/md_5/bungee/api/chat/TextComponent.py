"""
Python module generated from Java source file net.md_5.bungee.api.chat.TextComponent

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from java.util.function import Consumer
from java.util.regex import Matcher
from java.util.regex import Pattern
from net.md_5.bungee.api import ChatColor
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class TextComponent(BaseComponent):

    def __init__(self):
        """
        Creates a TextComponent with blank text.
        """
        ...


    def __init__(self, textComponent: "TextComponent"):
        """
        Creates a TextComponent with formatting and text from the passed
        component

        Arguments
        - textComponent: the component to copy from
        """
        ...


    def __init__(self, *extras: Tuple["BaseComponent", ...]):
        """
        Creates a TextComponent with blank text and the extras set to the passed
        array

        Arguments
        - extras: the extras to set
        """
        ...


    @staticmethod
    def fromLegacy(message: str) -> "BaseComponent":
        """
        Converts the old formatting system that used
        net.md_5.bungee.api.ChatColor.COLOR_CHAR into the new json based
        system.

        Arguments
        - message: the text to convert

        Returns
        - the components needed to print the message to the client
        """
        ...


    @staticmethod
    def fromLegacy(message: str, defaultColor: "ChatColor") -> "BaseComponent":
        """
        Converts the old formatting system that used
        net.md_5.bungee.api.ChatColor.COLOR_CHAR into the new json based
        system.

        Arguments
        - message: the text to convert
        - defaultColor: color to use when no formatting is to be applied
        (i.e. after ChatColor.RESET).

        Returns
        - the components needed to print the message to the client
        """
        ...


    @staticmethod
    def fromLegacyText(message: str) -> list["BaseComponent"]:
        """
        Converts the old formatting system that used
        net.md_5.bungee.api.ChatColor.COLOR_CHAR into the new json based
        system.

        Arguments
        - message: the text to convert

        Returns
        - the components needed to print the message to the client

        Deprecated
        - .fromLegacy(String) is preferred as it will
        consolidate all components into a single BaseComponent with extra
        contents as opposed to an array of components which is non-standard and
        may result in unexpected behavior.
        """
        ...


    @staticmethod
    def fromLegacyText(message: str, defaultColor: "ChatColor") -> list["BaseComponent"]:
        """
        Converts the old formatting system that used
        net.md_5.bungee.api.ChatColor.COLOR_CHAR into the new json based
        system.

        Arguments
        - message: the text to convert
        - defaultColor: color to use when no formatting is to be applied
        (i.e. after ChatColor.RESET).

        Returns
        - the components needed to print the message to the client

        Deprecated
        - .fromLegacy(String, ChatColor) is preferred as it
        will consolidate all components into a single BaseComponent with extra
        contents as opposed to an array of components which is non-standard and
        may result in unexpected behavior.
        """
        ...


    @staticmethod
    def fromArray(*components: Tuple["BaseComponent", ...]) -> "BaseComponent":
        """
        Internal compatibility method to transform an array of components to a
        single component.

        Arguments
        - components: array

        Returns
        - single component
        """
        ...


    def duplicate(self) -> "TextComponent":
        """
        Creates a duplicate of this TextComponent.

        Returns
        - the duplicate of this TextComponent.
        """
        ...


    def toString(self) -> str:
        ...
