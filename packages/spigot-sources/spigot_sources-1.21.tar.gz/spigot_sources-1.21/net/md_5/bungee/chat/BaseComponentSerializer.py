"""
Python module generated from Java source file net.md_5.bungee.chat.BaseComponentSerializer

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonElement
from com.google.gson import JsonObject
from com.google.gson import JsonSerializationContext
from java.util import Arrays
from java.util import Collections
from java.util import IdentityHashMap
from java.util import Locale
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import ClickEvent
from net.md_5.bungee.api.chat import ComponentStyle
from net.md_5.bungee.api.chat import HoverEvent
from net.md_5.bungee.api.chat.hover.content import Content
from net.md_5.bungee.chat import *
from typing import Any, Callable, Iterable, Tuple


class BaseComponentSerializer:


