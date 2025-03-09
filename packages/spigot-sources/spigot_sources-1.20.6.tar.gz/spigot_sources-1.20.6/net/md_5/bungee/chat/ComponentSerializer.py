"""
Python module generated from Java source file net.md_5.bungee.chat.ComponentSerializer

Java source file obtained from artifact bungeecord-chat version 1.20-R0.2-20240119.213604-65

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import GsonBuilder
from com.google.gson import JsonArray
from com.google.gson import JsonDeserializationContext
from com.google.gson import JsonDeserializer
from com.google.gson import JsonElement
from com.google.gson import JsonObject
from com.google.gson import JsonParseException
from com.google.gson import JsonParser
from com.google.gson import JsonPrimitive
from java.lang.reflect import Type
from net.md_5.bungee.api.chat import BaseComponent
from net.md_5.bungee.api.chat import ComponentStyle
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
        """
        Parse a JSON-compliant String as an array of base components. The input
        can be one of either an array of components, or a single component
        object. If the input is an array, each component will be parsed
        individually and returned in the order that they were parsed. If the
        input is a single component object, a single-valued array with the
        component will be returned.
        
        <strong>NOTE:</strong> .deserialize(String) is preferred as it
        will parse only one component as opposed to an array of components which
        is non- standard behavior. This method is still appropriate for parsing
        multiple components at once, although such use case is rarely (if at all)
        exhibited in vanilla Minecraft.

        Arguments
        - json: the component json to parse

        Returns
        - an array of all parsed components
        """
        ...


    @staticmethod
    def deserialize(json: str) -> "BaseComponent":
        """
        Deserialize a JSON-compliant String as a single component.

        Arguments
        - json: the component json to parse

        Returns
        - the deserialized component

        Raises
        - IllegalArgumentException: if anything other than a valid JSON
        component string is passed as input
        """
        ...


    @staticmethod
    def deserialize(jsonElement: "JsonElement") -> "BaseComponent":
        """
        Deserialize a JSON element as a single component.

        Arguments
        - jsonElement: the component json to parse

        Returns
        - the deserialized component

        Raises
        - IllegalArgumentException: if anything other than a valid JSON
        component is passed as input
        """
        ...


    @staticmethod
    def deserializeStyle(json: str) -> "ComponentStyle":
        """
        Deserialize a JSON-compliant String as a component style.

        Arguments
        - json: the component style json to parse

        Returns
        - the deserialized component style

        Raises
        - IllegalArgumentException: if anything other than a valid JSON
        component style string is passed as input
        """
        ...


    @staticmethod
    def deserializeStyle(jsonElement: "JsonElement") -> "ComponentStyle":
        """
        Deserialize a JSON element as a component style.

        Arguments
        - jsonElement: the component style json to parse

        Returns
        - the deserialized component style

        Raises
        - IllegalArgumentException: if anything other than a valid JSON
        component style is passed as input
        """
        ...


    @staticmethod
    def toJson(component: "BaseComponent") -> "JsonElement":
        ...


    @staticmethod
    def toJson(style: "ComponentStyle") -> "JsonElement":
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


    @staticmethod
    def toString(style: "ComponentStyle") -> str:
        ...


    def deserialize(self, json: "JsonElement", typeOfT: "Type", context: "JsonDeserializationContext") -> "BaseComponent":
        ...
