"""
Python module generated from Java source file net.md_5.bungee.api.chat.ItemTag

Java source file obtained from artifact bungeecord-chat version 1.20-R0.1-20230802.100237-14

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonDeserializer
from com.google.gson import JsonElement
from com.google.gson import JsonParseException
from com.google.gson import JsonSerializationContext
from com.google.gson import JsonSerializer
from java.lang.reflect import Type
from net.md_5.bungee.api.chat import *
from typing import Any, Callable, Iterable, Tuple


class ItemTag:
    """
    Metadata for use in conjunction with HoverEvent.Action.SHOW_ITEM
    """

    @staticmethod
    def ofNbt(nbt: str) -> "ItemTag":
        ...


    class Serializer(JsonSerializer, JsonDeserializer):

        def deserialize(self, element: "JsonElement", type: "Type", context: "JsonDeserializationContext") -> "ItemTag":
            ...


        def serialize(self, itemTag: "ItemTag", type: "Type", context: "JsonSerializationContext") -> "JsonElement":
            ...
