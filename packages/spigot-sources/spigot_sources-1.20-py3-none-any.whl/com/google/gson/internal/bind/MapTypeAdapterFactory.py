"""
Python module generated from Java source file com.google.gson.internal.bind.MapTypeAdapterFactory

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import JsonElement
from com.google.gson import JsonPrimitive
from com.google.gson import JsonSyntaxException
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import $Gson$Types
from com.google.gson.internal import ConstructorConstructor
from com.google.gson.internal import JsonReaderInternalAccess
from com.google.gson.internal import ObjectConstructor
from com.google.gson.internal import Streams
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class MapTypeAdapterFactory(TypeAdapterFactory):
    """
    Adapts maps to either JSON objects or JSON arrays.
    
    <h2>Maps as JSON objects</h2>
    For primitive keys or when complex map key serialization is not enabled, this
    converts Java Map Maps to JSON Objects. This requires that map keys
    can be serialized as strings; this is insufficient for some key types. For
    example, consider a map whose keys are points on a grid. The default JSON
    form encodes reasonably: ```   `Map<Point, String> original = new LinkedHashMap<>();
      original.put(new Point(5, 6), "a");
      original.put(new Point(8, 8), "b");
      System.out.println(gson.toJson(original, type));````
    The above code prints this JSON object:```   `{
        "(5,6)": "a",
        "(8,8)": "b"`
    }```
    But GSON is unable to deserialize this value because the JSON string name is
    just the Object.toString() toString() of the map key. Attempting to
    convert the above JSON to an object fails with a parse exception:
    ```com.google.gson.JsonParseException: Expecting object found: "(5,6)"
      at com.google.gson.JsonObjectDeserializationVisitor.visitFieldUsingCustomHandler
      at com.google.gson.ObjectNavigator.navigateClassFields
      ...```
    
    <h2>Maps as JSON arrays</h2>
    An alternative approach taken by this type adapter when it is required and
    complex map key serialization is enabled is to encode maps as arrays of map
    entries. Each map entry is a two element array containing a key and a value.
    This approach is more flexible because any type can be used as the map's key;
    not just strings. But it's also less portable because the receiver of such
    JSON must be aware of the map entry convention.
    
    Register this adapter when you are creating your GSON instance.
    ```   `Gson gson = new GsonBuilder()
        .registerTypeAdapter(Map.class, new MapAsArrayTypeAdapter())
        .create();````
    This will change the structure of the JSON emitted by the code above. Now we
    get an array. In this case the arrays elements are map entries:
    ```   `[
        [
          {
            "x": 5,
            "y": 6`,
          "a",
        ],
        [
          {
            "x": 8,
            "y": 8
          },
          "b"
        ]
      ]
    }```
    This format will serialize and deserialize just fine as long as this adapter
    is registered.
    """

    def __init__(self, constructorConstructor: "ConstructorConstructor", complexMapKeySerialization: bool):
        ...


    def create(self, gson: "Gson", typeToken: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        ...
