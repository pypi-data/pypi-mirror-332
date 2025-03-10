"""
Python module generated from Java source file com.google.gson.JsonObject

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import LinkedTreeMap
from typing import Any, Callable, Iterable, Tuple


class JsonObject(JsonElement):
    """
    A class representing an object type in Json. An object consists of name-value pairs where names
    are strings, and values are any other type of JsonElement. This allows for a creating a
    tree of JsonElements. The member elements of this object are maintained in order they were added.

    Author(s)
    - Joel Leitch
    """

    def deepCopy(self) -> "JsonObject":
        """
        Creates a deep copy of this element and all its children

        Since
        - 2.8.2
        """
        ...


    def add(self, property: str, value: "JsonElement") -> None:
        """
        Adds a member, which is a name-value pair, to self. The name must be a String, but the value
        can be an arbitrary JsonElement, thereby allowing you to build a full tree of JsonElements
        rooted at this node.

        Arguments
        - property: name of the member.
        - value: the member object.
        """
        ...


    def remove(self, property: str) -> "JsonElement":
        """
        Removes the `property` from this JsonObject.

        Arguments
        - property: name of the member that should be removed.

        Returns
        - the JsonElement object that is being removed.

        Since
        - 1.3
        """
        ...


    def addProperty(self, property: str, value: str) -> None:
        """
        Convenience method to add a primitive member. The specified value is converted to a
        JsonPrimitive of String.

        Arguments
        - property: name of the member.
        - value: the string value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Number") -> None:
        """
        Convenience method to add a primitive member. The specified value is converted to a
        JsonPrimitive of Number.

        Arguments
        - property: name of the member.
        - value: the number value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Boolean") -> None:
        """
        Convenience method to add a boolean member. The specified value is converted to a
        JsonPrimitive of Boolean.

        Arguments
        - property: name of the member.
        - value: the number value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Character") -> None:
        """
        Convenience method to add a char member. The specified value is converted to a
        JsonPrimitive of Character.

        Arguments
        - property: name of the member.
        - value: the number value associated with the member.
        """
        ...


    def entrySet(self) -> set["Map.Entry"[str, "JsonElement"]]:
        """
        Returns a set of members of this object. The set is ordered, and the order is in which the
        elements were added.

        Returns
        - a set of members of this object.
        """
        ...


    def keySet(self) -> set[str]:
        """
        Returns a set of members key values.

        Returns
        - a set of member keys as Strings

        Since
        - 2.8.1
        """
        ...


    def size(self) -> int:
        """
        Returns the number of key/value pairs in the object.

        Returns
        - the number of key/value pairs in the object.
        """
        ...


    def has(self, memberName: str) -> bool:
        """
        Convenience method to check if a member with the specified name is present in this object.

        Arguments
        - memberName: name of the member that is being checked for presence.

        Returns
        - True if there is a member with the specified name, False otherwise.
        """
        ...


    def get(self, memberName: str) -> "JsonElement":
        """
        Returns the member with the specified name.

        Arguments
        - memberName: name of the member that is being requested.

        Returns
        - the member matching the name. Null if no such member exists.
        """
        ...


    def getAsJsonPrimitive(self, memberName: str) -> "JsonPrimitive":
        """
        Convenience method to get the specified member as a JsonPrimitive element.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the JsonPrimitive corresponding to the specified member.
        """
        ...


    def getAsJsonArray(self, memberName: str) -> "JsonArray":
        """
        Convenience method to get the specified member as a JsonArray.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the JsonArray corresponding to the specified member.
        """
        ...


    def getAsJsonObject(self, memberName: str) -> "JsonObject":
        """
        Convenience method to get the specified member as a JsonObject.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the JsonObject corresponding to the specified member.
        """
        ...


    def equals(self, o: "Object") -> bool:
        ...


    def hashCode(self) -> int:
        ...
