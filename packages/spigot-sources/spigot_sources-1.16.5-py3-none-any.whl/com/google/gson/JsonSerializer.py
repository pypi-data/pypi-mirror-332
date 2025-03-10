"""
Python module generated from Java source file com.google.gson.JsonSerializer

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class JsonSerializer:
    """
    Interface representing a custom serializer for Json. You should write a custom serializer, if
    you are not happy with the default serialization done by Gson. You will also need to register
    this serializer through com.google.gson.GsonBuilder.registerTypeAdapter(Type, Object).
    
    Let us look at example where defining a serializer will be useful. The `Id` class
    defined below has two fields: `clazz` and `value`.
    
    ```
    public class Id&lt;T&gt; {
      private final Class&lt;T&gt; clazz;
      private final long value;
    
      public Id(Class&lt;T&gt; clazz, long value) {
        this.clazz = clazz;
        this.value = value;
      }
    
      public long getValue() {
        return value;
      }
    }
    ```
    
    The default serialization of `Id(com.foo.MyObject.class, 20L)` will be
    `{"clazz":com.foo.MyObject,"value":20}`. Suppose, you just want the output to be
    the value instead, which is `20` in this case. You can achieve that by writing a custom
    serializer:
    
    ```
    class IdSerializer implements JsonSerializer&lt;Id&gt;() {
      public JsonElement serialize(Id id, Type typeOfId, JsonSerializationContext context) {
        return new JsonPrimitive(id.getValue());
      }
    }
    ```
    
    You will also need to register `IdSerializer` with Gson as follows:
    ```
    Gson gson = new GsonBuilder().registerTypeAdapter(Id.class, new IdSerializer()).create();
    ```
    
    New applications should prefer TypeAdapter, whose streaming API
    is more efficient than this interface's tree API.
    
    Type `<T>`: type for which the serializer is being registered. It is possible that a serializer
           may be asked to serialize a specific generic type of the T.

    Author(s)
    - Joel Leitch
    """

    def serialize(self, src: "T", typeOfSrc: "Type", context: "JsonSerializationContext") -> "JsonElement":
        """
        Gson invokes this call-back method during serialization when it encounters a field of the
        specified type.
        
        In the implementation of this call-back method, you should consider invoking
        JsonSerializationContext.serialize(Object, Type) method to create JsonElements for any
        non-trivial field of the `src` object. However, you should never invoke it on the
        `src` object itself since that will cause an infinite loop (Gson will call your
        call-back method again).

        Arguments
        - src: the object that needs to be converted to Json.
        - typeOfSrc: the actual type (fully genericized version) of the source object.

        Returns
        - a JsonElement corresponding to the specified object.
        """
        ...
