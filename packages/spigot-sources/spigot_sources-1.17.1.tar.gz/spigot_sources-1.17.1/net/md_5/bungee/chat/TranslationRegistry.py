"""
Python module generated from Java source file net.md_5.bungee.chat.TranslationRegistry

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Charsets
from com.google.gson import Gson
from com.google.gson import JsonElement
from com.google.gson import JsonObject
from java.io import IOException
from java.io import InputStreamReader
from java.util import ResourceBundle
from net.md_5.bungee.chat import *
from typing import Any, Callable, Iterable, Tuple


class TranslationRegistry:

    INSTANCE = TranslationRegistry()


    def translate(self, s: str) -> str:
        ...
