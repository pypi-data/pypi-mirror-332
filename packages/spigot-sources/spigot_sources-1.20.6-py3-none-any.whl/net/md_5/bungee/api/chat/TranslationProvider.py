"""
Python module generated from Java source file net.md_5.bungee.api.chat.TranslationProvider

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class TranslationProvider:
    """
    An object capable of being translated by the client in a
    TranslatableComponent.
    """

    def getTranslationKey(self) -> str:
        """
        Get the translation key.

        Returns
        - the translation key
        """
        ...


    def asTranslatableComponent(self) -> "TranslatableComponent":
        """
        Get this translatable object as a TranslatableComponent.

        Returns
        - the translatable component
        """
        ...


    def asTranslatableComponent(self, *with: Tuple["Object", ...]) -> "TranslatableComponent":
        """
        Get this translatable object as a TranslatableComponent.

        Arguments
        - with: the String Strings and
        BaseComponent BaseComponents to use in the translation

        Returns
        - the translatable component
        """
        ...
