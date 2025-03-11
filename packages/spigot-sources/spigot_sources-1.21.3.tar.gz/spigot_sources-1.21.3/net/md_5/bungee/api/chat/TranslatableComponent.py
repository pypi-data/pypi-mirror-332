"""
Python module generated from Java source file net.md_5.bungee.api.chat.TranslatableComponent

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util.regex import Matcher
from java.util.regex import Pattern
from net.md_5.bungee.api.chat import *
from net.md_5.bungee.chat import TranslationRegistry
from typing import Any, Callable, Iterable, Tuple


class TranslatableComponent(BaseComponent):

    def __init__(self, original: "TranslatableComponent"):
        """
        Creates a translatable component from the original to clone it.

        Arguments
        - original: the original for the new translatable component.
        """
        ...


    def __init__(self, translate: str, *with: Tuple["Object", ...]):
        """
        Creates a translatable component with the passed substitutions

        Arguments
        - translate: the translation key
        - with: the java.lang.Strings and
        net.md_5.bungee.api.chat.BaseComponents to use into the
        translation

        See
        - .setWith(java.util.List)
        """
        ...


    def __init__(self, translatable: "TranslationProvider", *with: Tuple["Object", ...]):
        """
        Creates a translatable component with the passed substitutions

        Arguments
        - translatable: the translatable object
        - with: the java.lang.Strings and
        net.md_5.bungee.api.chat.BaseComponents to use into the
        translation

        See
        - .setWith(java.util.List)
        """
        ...


    def duplicate(self) -> "TranslatableComponent":
        """
        Creates a duplicate of this TranslatableComponent.

        Returns
        - the duplicate of this TranslatableComponent.
        """
        ...


    def setWith(self, components: list["BaseComponent"]) -> None:
        """
        Sets the translation substitutions to be used in this component. Removes
        any previously set substitutions

        Arguments
        - components: the components to substitute
        """
        ...


    def addWith(self, text: str) -> None:
        """
        Adds a text substitution to the component. The text will inherit this
        component's formatting

        Arguments
        - text: the text to substitute
        """
        ...


    def addWith(self, component: "BaseComponent") -> None:
        """
        Adds a component substitution to the component. The text will inherit
        this component's formatting

        Arguments
        - component: the component to substitute
        """
        ...
