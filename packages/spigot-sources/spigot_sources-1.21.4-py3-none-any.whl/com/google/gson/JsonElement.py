"""
Python module generated from Java source file com.google.gson.JsonElement

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.gson import *
from com.google.gson.internal import Streams
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.io import Reader
from java.io import StringWriter
from java.math import BigDecimal
from java.math import BigInteger
from typing import Any, Callable, Iterable, Tuple


class JsonElement:
    """
    A class representing an element of JSON. It could either be a JsonObject, a JsonArray, a JsonPrimitive or a JsonNull.
    
    This class provides multiple `getAs` methods which allow
    
    
      - obtaining the represented primitive value, for example .getAsString()
      - casting to the `JsonElement` subclasses in a convenient way, for example .getAsJsonObject()
    
    
    <h2>Converting `JsonElement` from / to JSON</h2>
    
    There are two ways to parse JSON data as a JsonElement:
    
    
      - JsonParser, for example:
          ```
    JsonObject jsonObject = JsonParser.parseString("{}").getAsJsonObject();
    ```
      - Gson.fromJson(Reader, Class) Gson.fromJson(..., JsonElement.class)
          It is possible to directly specify a `JsonElement` subclass, for example:
          ```
    JsonObject jsonObject = gson.fromJson("{}", JsonObject.class);
    ```
    
    
    To convert a `JsonElement` to JSON either .toString() JsonElement.toString() or the
    method Gson.toJson(JsonElement) and its overloads can be used.
    
    It is also possible to obtain the TypeAdapter for `JsonElement` from a Gson instance and then use it for conversion from and to JSON:
    
    ````TypeAdapter<JsonElement> adapter = gson.getAdapter(JsonElement.class);
    
    JsonElement value = adapter.fromJson("{`");
    String json = adapter.toJson(value);
    }```
    
    <h2>`JsonElement` as JSON data</h2>
    
    `JsonElement` can also be treated as JSON data, allowing to deserialize from a `JsonElement` and serializing to a `JsonElement`. The Gson class offers these
    methods for this:
    
    
      - Gson.fromJson(JsonElement, Class) Gson.fromJson(JsonElement, ...), for example:
          ```
    JsonObject jsonObject = ...;
    MyClass myObj = gson.fromJson(jsonObject, MyClass.class);
    ```
      - Gson.toJsonTree(Object), for example:
          ```
    MyClass myObj = ...;
    JsonElement json = gson.toJsonTree(myObj);
    ```
    
    
    The TypeAdapter class provides corresponding methods as well:
    
    
      - TypeAdapter.fromJsonTree(JsonElement)
      - TypeAdapter.toJsonTree(Object)

    Author(s)
    - Joel Leitch
    """

    def __init__(self):
        """
        Deprecated
        - Creating custom `JsonElement` subclasses is highly discouraged and can lead
            to undefined behavior.
            This constructor is only kept for backward compatibility.
        """
        ...


    def deepCopy(self) -> "JsonElement":
        """
        Returns a deep copy of this element. Immutable elements like primitives and nulls are not
        copied.

        Since
        - 2.8.2
        """
        ...


    def isJsonArray(self) -> bool:
        """
        Provides a check for verifying if this element is a JSON array or not.

        Returns
        - True if this element is of type JsonArray, False otherwise.
        """
        ...


    def isJsonObject(self) -> bool:
        """
        Provides a check for verifying if this element is a JSON object or not.

        Returns
        - True if this element is of type JsonObject, False otherwise.
        """
        ...


    def isJsonPrimitive(self) -> bool:
        """
        Provides a check for verifying if this element is a primitive or not.

        Returns
        - True if this element is of type JsonPrimitive, False otherwise.
        """
        ...


    def isJsonNull(self) -> bool:
        """
        Provides a check for verifying if this element represents a null value or not.

        Returns
        - True if this element is of type JsonNull, False otherwise.

        Since
        - 1.2
        """
        ...


    def getAsJsonObject(self) -> "JsonObject":
        """
        Convenience method to get this element as a JsonObject. If this element is of some
        other type, an IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonObject()
        first.

        Returns
        - this element as a JsonObject.

        Raises
        - IllegalStateException: if this element is of another type.
        """
        ...


    def getAsJsonArray(self) -> "JsonArray":
        """
        Convenience method to get this element as a JsonArray. If this element is of some other
        type, an IllegalStateException will result. Hence it is best to use this method after
        ensuring that this element is of the desired type by calling .isJsonArray() first.

        Returns
        - this element as a JsonArray.

        Raises
        - IllegalStateException: if this element is of another type.
        """
        ...


    def getAsJsonPrimitive(self) -> "JsonPrimitive":
        """
        Convenience method to get this element as a JsonPrimitive. If this element is of some
        other type, an IllegalStateException will result. Hence it is best to use this method
        after ensuring that this element is of the desired type by calling .isJsonPrimitive()
        first.

        Returns
        - this element as a JsonPrimitive.

        Raises
        - IllegalStateException: if this element is of another type.
        """
        ...


    def getAsJsonNull(self) -> "JsonNull":
        """
        Convenience method to get this element as a JsonNull. If this element is of some other
        type, an IllegalStateException will result. Hence it is best to use this method after
        ensuring that this element is of the desired type by calling .isJsonNull() first.

        Returns
        - this element as a JsonNull.

        Raises
        - IllegalStateException: if this element is of another type.

        Since
        - 1.2
        """
        ...


    def getAsBoolean(self) -> bool:
        """
        Convenience method to get this element as a boolean value.

        Returns
        - this element as a primitive boolean value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsNumber(self) -> "Number":
        """
        Convenience method to get this element as a Number.

        Returns
        - this element as a Number.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray, or cannot be converted to a number.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsString(self) -> str:
        """
        Convenience method to get this element as a string value.

        Returns
        - this element as a string value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsDouble(self) -> float:
        """
        Convenience method to get this element as a primitive double value.

        Returns
        - this element as a primitive double value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid double.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsFloat(self) -> float:
        """
        Convenience method to get this element as a primitive float value.

        Returns
        - this element as a primitive float value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid float.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsLong(self) -> int:
        """
        Convenience method to get this element as a primitive long value.

        Returns
        - this element as a primitive long value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid long.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsInt(self) -> int:
        """
        Convenience method to get this element as a primitive integer value.

        Returns
        - this element as a primitive integer value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid integer.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def getAsByte(self) -> int:
        """
        Convenience method to get this element as a primitive byte value.

        Returns
        - this element as a primitive byte value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid byte.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.

        Since
        - 1.3
        """
        ...


    def getAsCharacter(self) -> str:
        """
        Convenience method to get the first character of the string value of this element.

        Returns
        - the first character of the string value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray, or if its string value is empty.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.

        Since
        - 1.3

        Deprecated
        - This method is misleading, as it does not get this element as a char but rather as
            a string's first character.
        """
        ...


    def getAsBigDecimal(self) -> "BigDecimal":
        """
        Convenience method to get this element as a BigDecimal.

        Returns
        - this element as a BigDecimal.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if this element is not a valid BigDecimal.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.

        Since
        - 1.2
        """
        ...


    def getAsBigInteger(self) -> "BigInteger":
        """
        Convenience method to get this element as a BigInteger.

        Returns
        - this element as a BigInteger.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if this element is not a valid BigInteger.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.

        Since
        - 1.2
        """
        ...


    def getAsShort(self) -> int:
        """
        Convenience method to get this element as a primitive short value.

        Returns
        - this element as a primitive short value.

        Raises
        - UnsupportedOperationException: if this element is not a JsonPrimitive or JsonArray.
        - NumberFormatException: if the value contained is not a valid short.
        - IllegalStateException: if this element is of the type JsonArray but contains
            more than a single element.
        """
        ...


    def toString(self) -> str:
        """
        Converts this element to a JSON string.
        
        For example:
        
        ```
        JsonObject object = new JsonObject();
        object.add("a", JsonNull.INSTANCE);
        JsonArray array = new JsonArray();
        array.add(1);
        object.add("b", array);
        
        String json = object.toString();
        // json: {"a":null,"b":[1]}
        ```
        
        If this element or any nested elements contain Double.NaN NaN or Double.isInfinite() Infinity that value is written to JSON, even though the JSON specification
        does not permit these values.
        
        To customize formatting or to directly write to an Appendable instead of creating an
        intermediate `String` first, use Gson.toJson(JsonElement, Appendable)
        Gson.toJson(JsonElement, ...).
        
        To get the contained String value (without enclosing `"` and without escaping), use
        .getAsString() instead:
        
        ```
        JsonPrimitive jsonPrimitive = new JsonPrimitive("with \" quote");
        String json = jsonPrimitive.toString();
        // json: "with \" quote"
        String value = jsonPrimitive.getAsString();
        // value: with " quote
        ```
        """
        ...
