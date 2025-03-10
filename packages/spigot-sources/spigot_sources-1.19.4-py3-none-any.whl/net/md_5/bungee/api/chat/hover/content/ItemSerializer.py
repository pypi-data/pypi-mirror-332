"""
Python module generated from Java source file net.md_5.bungee.api.chat.hover.content.ItemSerializer

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonDeserializer
from com.google.gson import JsonElement
from com.google.gson import JsonObject
from com.google.gson import JsonParseException
from com.google.gson import JsonPrimitive
from com.google.gson import JsonSerializationContext
from com.google.gson import JsonSerializer
from java.lang.reflect import Type
from net.md_5.bungee.api.chat import ItemTag
from net.md_5.bungee.api.chat.hover.content import *
from typing import Any, Callable, Iterable, Tuple


class ItemSerializer(JsonSerializer, JsonDeserializer):

    def deserialize(self, element: "JsonElement", type: "Type", context: "JsonDeserializationContext") -> "Item":
        ...


    def serialize(self, content: "Item", type: "Type", context: "JsonSerializationContext") -> "JsonElement":
        ...
