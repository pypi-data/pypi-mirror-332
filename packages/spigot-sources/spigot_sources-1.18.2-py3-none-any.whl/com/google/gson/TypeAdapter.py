"""
Python module generated from Java source file com.google.gson.TypeAdapter

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal.bind import JsonTreeReader
from com.google.gson.internal.bind import JsonTreeWriter
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.io import Reader
from java.io import StringReader
from java.io import StringWriter
from java.io import Writer
from typing import Any, Callable, Iterable, Tuple


class TypeAdapter:

    def write(self, out: "JsonWriter", value: "T") -> None:
        """
        Writes one JSON value (an array, object, string, number, boolean or null)
        for `value`.

        Arguments
        - value: the Java object to write. May be null.
        """
        ...


    def toJson(self, out: "Writer", value: "T") -> None:
        """
        Converts `value` to a JSON document and writes it to `out`.
        Unlike Gson's similar Gson.toJson(JsonElement, Appendable) toJson
        method, this write is strict. Create a JsonWriter.setLenient(boolean) lenient `JsonWriter` and call
        .write(com.google.gson.stream.JsonWriter, Object) for lenient
        writing.

        Arguments
        - value: the Java object to convert. May be null.

        Since
        - 2.2
        """
        ...


    def nullSafe(self) -> "TypeAdapter"["T"]:
        """
        This wrapper method is used to make a type adapter null tolerant. In general, a
        type adapter is required to handle nulls in write and read methods. Here is how this
        is typically done:
        ```   `Gson gson = new GsonBuilder().registerTypeAdapter(Foo.class,
          new TypeAdapter<Foo>() {
            public Foo read(JsonReader in) throws IOException {
              if (in.peek() == JsonToken.NULL) {
                in.nextNull();
                return null;`
              // read a Foo from in and return it
            }
            public void write(JsonWriter out, Foo src) throws IOException {
              if (src == null) {
                out.nullValue();
                return;
              }
              // write src as JSON to out
            }
          }).create();
        }```
        You can avoid this boilerplate handling of nulls by wrapping your type adapter with
        this method. Here is how we will rewrite the above example:
        ```   `Gson gson = new GsonBuilder().registerTypeAdapter(Foo.class,
          new TypeAdapter<Foo>() {
            public Foo read(JsonReader in) throws IOException {
              // read a Foo from in and return it`
            public void write(JsonWriter out, Foo src) throws IOException {
              // write src as JSON to out
            }
          }.nullSafe()).create();
        }```
        Note that we didn't need to check for nulls in our type adapter after we used nullSafe.
        """
        ...


    def toJson(self, value: "T") -> str:
        """
        Converts `value` to a JSON document. Unlike Gson's similar Gson.toJson(Object) toJson method, this write is strict. Create a JsonWriter.setLenient(boolean) lenient `JsonWriter` and call
        .write(com.google.gson.stream.JsonWriter, Object) for lenient
        writing.

        Arguments
        - value: the Java object to convert. May be null.

        Since
        - 2.2
        """
        ...


    def toJsonTree(self, value: "T") -> "JsonElement":
        """
        Converts `value` to a JSON tree.

        Arguments
        - value: the Java object to convert. May be null.

        Returns
        - the converted JSON tree. May be JsonNull.

        Since
        - 2.2
        """
        ...


    def read(self, in: "JsonReader") -> "T":
        """
        Reads one JSON value (an array, object, string, number, boolean or null)
        and converts it to a Java object. Returns the converted object.

        Returns
        - the converted Java object. May be null.
        """
        ...


    def fromJson(self, in: "Reader") -> "T":
        """
        Converts the JSON document in `in` to a Java object. Unlike Gson's
        similar Gson.fromJson(java.io.Reader, Class) fromJson method, this
        read is strict. Create a JsonReader.setLenient(boolean) lenient
        `JsonReader` and call .read(JsonReader) for lenient reading.

        Returns
        - the converted Java object. May be null.

        Since
        - 2.2
        """
        ...


    def fromJson(self, json: str) -> "T":
        """
        Converts the JSON document in `json` to a Java object. Unlike Gson's
        similar Gson.fromJson(String, Class) fromJson method, this read is
        strict. Create a JsonReader.setLenient(boolean) lenient `JsonReader` and call .read(JsonReader) for lenient reading.

        Returns
        - the converted Java object. May be null.

        Since
        - 2.2
        """
        ...


    def fromJsonTree(self, jsonTree: "JsonElement") -> "T":
        """
        Converts `jsonTree` to a Java object.

        Arguments
        - jsonTree: the Java object to convert. May be JsonNull.

        Since
        - 2.2
        """
        ...
