"""
Python module generated from Java source file com.google.gson.JsonObject

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.gson import *
from com.google.gson.internal import LinkedTreeMap
from typing import Any, Callable, Iterable, Tuple


class JsonObject(JsonElement):
    """
    A class representing an object type in JSON. An object consists of name-value pairs where names
    are strings, and values are any other type of JsonElement. This allows for a creating a
    tree of JsonElements. The member elements of this object are maintained in order they were added.
    This class does not support `null` values. If `null` is provided as value argument to
    any of the methods, it is converted to a JsonNull.
    
    `JsonObject` does not implement the Map interface, but a `Map` view of it
    can be obtained with .asMap().
    
    See the JsonElement documentation for details on how to convert `JsonObject` and
    generally any `JsonElement` from and to JSON.

    Author(s)
    - Joel Leitch
    """

    def __init__(self):
        """
        Creates an empty JsonObject.
        """
        ...


    def deepCopy(self) -> "JsonObject":
        """
        Creates a deep copy of this element and all its children.

        Since
        - 2.8.2
        """
        ...


    def add(self, property: str, value: "JsonElement") -> None:
        """
        Adds a member, which is a name-value pair, to self. The name must be a String, but the value
        can be an arbitrary JsonElement, thereby allowing you to build a full tree of
        JsonElements rooted at this node.

        Arguments
        - property: name of the member.
        - value: the member object.
        """
        ...


    def remove(self, property: str) -> "JsonElement":
        """
        Removes the `property` from this object.

        Arguments
        - property: name of the member that should be removed.

        Returns
        - the JsonElement object that is being removed, or `null` if no member with
            this name exists.

        Since
        - 1.3
        """
        ...


    def addProperty(self, property: str, value: str) -> None:
        """
        Convenience method to add a string member. The specified value is converted to a JsonPrimitive of String.

        Arguments
        - property: name of the member.
        - value: the string value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Number") -> None:
        """
        Convenience method to add a number member. The specified value is converted to a JsonPrimitive of Number.

        Arguments
        - property: name of the member.
        - value: the number value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Boolean") -> None:
        """
        Convenience method to add a boolean member. The specified value is converted to a JsonPrimitive of Boolean.

        Arguments
        - property: name of the member.
        - value: the boolean value associated with the member.
        """
        ...


    def addProperty(self, property: str, value: "Character") -> None:
        """
        Convenience method to add a char member. The specified value is converted to a JsonPrimitive of Character.

        Arguments
        - property: name of the member.
        - value: the char value associated with the member.
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

        Since
        - 2.7
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns True if the number of key/value pairs in the object is zero.

        Returns
        - True if the number of key/value pairs in the object is zero.

        Since
        - 2.10.1
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
        - the member matching the name, or `null` if no such member exists.
        """
        ...


    def getAsJsonPrimitive(self, memberName: str) -> "JsonPrimitive":
        """
        Convenience method to get the specified member as a JsonPrimitive.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the `JsonPrimitive` corresponding to the specified member, or `null` if no
            member with this name exists.

        Raises
        - ClassCastException: if the member is not of type `JsonPrimitive`.
        """
        ...


    def getAsJsonArray(self, memberName: str) -> "JsonArray":
        """
        Convenience method to get the specified member as a JsonArray.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the `JsonArray` corresponding to the specified member, or `null` if no
            member with this name exists.

        Raises
        - ClassCastException: if the member is not of type `JsonArray`.
        """
        ...


    def getAsJsonObject(self, memberName: str) -> "JsonObject":
        """
        Convenience method to get the specified member as a JsonObject.

        Arguments
        - memberName: name of the member being requested.

        Returns
        - the `JsonObject` corresponding to the specified member, or `null` if no
            member with this name exists.

        Raises
        - ClassCastException: if the member is not of type `JsonObject`.
        """
        ...


    def asMap(self) -> dict[str, "JsonElement"]:
        """
        Returns a mutable Map view of this `JsonObject`. Changes to the `Map` are
        visible in this `JsonObject` and the other way around.
        
        The `Map` does not permit `null` keys or values. Unlike `JsonObject`'s
        `null` handling, a NullPointerException is thrown when trying to add `null`. Use JsonNull for JSON null values.

        Returns
        - mutable `Map` view

        Since
        - 2.10
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Returns whether the other object is equal to this. This method only considers the other object
        to be equal if it is an instance of `JsonObject` and has equal members, ignoring order.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code of this object. This method calculates the hash code based on the members
        of this object, ignoring order.
        """
        ...
