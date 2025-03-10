"""
Python module generated from Java source file net.md_5.bungee.chat.ComponentSerializer

Java source file obtained from artifact bungeecord-chat version 1.16-R0.5-20210527.222444-33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import GsonBuilder
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonDeserializer
from com.google.gson import JsonElement
from com.google.gson import JsonObject
from com.google.gson import JsonParseException
from com.google.gson import JsonParser
from java.lang.reflect import Type
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import ItemTag
from net.md_5.bungee.api.chat import KeybindComponent
from net.md_5.bungee.api.chat import ScoreComponent
from net.md_5.bungee.api.chat import SelectorComponent
from net.md_5.bungee.api.chat import TextComponent
from net.md_5.bungee.api.chat import TranslatableComponent
from net.md_5.bungee.api.chat.hover.content import Entity
from net.md_5.bungee.api.chat.hover.content import EntitySerializer
from net.md_5.bungee.api.chat.hover.content import Item
from net.md_5.bungee.api.chat.hover.content import ItemSerializer
from net.md_5.bungee.api.chat.hover.content import Text
from net.md_5.bungee.api.chat.hover.content import TextSerializer
from net.md_5.bungee.chat import *
from typing import Any, Callable, Iterable, Tuple


class ComponentSerializer(JsonDeserializer):

    serializedComponents = ThreadLocal<Set<BaseComponent>>()


    @staticmethod
    def parse(json: str) -> list["BaseComponent"]:
        ...


    @staticmethod
    def toString(object: "Object") -> str:
        ...


    @staticmethod
    def toString(component: "BaseComponent") -> str:
        ...


    @staticmethod
    def toString(*components: Tuple["BaseComponent", ...]) -> str:
        ...


    def deserialize(self, json: "JsonElement", typeOfT: "Type", context: "JsonDeserializationContext") -> "BaseComponent":
        ...
