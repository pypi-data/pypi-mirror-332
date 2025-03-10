"""
Python module generated from Java source file com.google.gson.stream.JsonWriter

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.stream import *
from java.io import Closeable
from java.io import Flushable
from java.io import IOException
from java.io import Writer
from java.util import Arrays
from typing import Any, Callable, Iterable, Tuple


class JsonWriter(Closeable, Flushable):
    """
    Writes a JSON (<a href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>)
    encoded value to a stream, one token at a time. The stream includes both
    literal values (strings, numbers, booleans and nulls) as well as the begin
    and end delimiters of objects and arrays.
    
    <h3>Encoding JSON</h3>
    To encode your data as JSON, create a new `JsonWriter`. Each JSON
    document must contain one top-level array or object. Call methods on the
    writer as you walk the structure's contents, nesting arrays and objects as
    necessary:
    
      - To write <strong>arrays</strong>, first call .beginArray().
          Write each of the array's elements with the appropriate .value
          methods or by nesting other arrays and objects. Finally close the array
          using .endArray().
      - To write <strong>objects</strong>, first call .beginObject().
          Write each of the object's properties by alternating calls to
          .name with the property's value. Write property values with the
          appropriate .value method or by nesting other objects or arrays.
          Finally close the object using .endObject().
    
    
    <h3>Example</h3>
    Suppose we'd like to encode a stream of messages such as the following: ``` `[
      {
        "id": 912345678901,
        "text": "How do I stream JSON in Java?",
        "geo": null,
        "user": {
          "name": "json_newb",
          "followers_count": 41`
      },
      {
        "id": 912345678902,
        "text": "@json_newb just use JsonWriter!",
        "geo": [50.454722, -104.606667],
        "user": {
          "name": "jesse",
          "followers_count": 2
        }
      }
    ]}```
    This code encodes the above structure: ```   `public void writeJsonStream(OutputStream out, List<Message> messages) throws IOException {
        JsonWriter writer = new JsonWriter(new OutputStreamWriter(out, "UTF-8"));
        writer.setIndent("    ");
        writeMessagesArray(writer, messages);
        writer.close();`
    
      public void writeMessagesArray(JsonWriter writer, List<Message> messages) throws IOException {
        writer.beginArray();
        for (Message message : messages) {
          writeMessage(writer, message);
        }
        writer.endArray();
      }
    
      public void writeMessage(JsonWriter writer, Message message) throws IOException {
        writer.beginObject();
        writer.name("id").value(message.getId());
        writer.name("text").value(message.getText());
        if (message.getGeo() != null) {
          writer.name("geo");
          writeDoublesArray(writer, message.getGeo());
        } else {
          writer.name("geo").nullValue();
        }
        writer.name("user");
        writeUser(writer, message.getUser());
        writer.endObject();
      }
    
      public void writeUser(JsonWriter writer, User user) throws IOException {
        writer.beginObject();
        writer.name("name").value(user.getName());
        writer.name("followers_count").value(user.getFollowersCount());
        writer.endObject();
      }
    
      public void writeDoublesArray(JsonWriter writer, List<Double> doubles) throws IOException {
        writer.beginArray();
        for (Double value : doubles) {
          writer.value(value);
        }
        writer.endArray();
      }}```
    
    Each `JsonWriter` may be used to write a single JSON stream.
    Instances of this class are not thread safe. Calls that would result in a
    malformed JSON string will fail with an IllegalStateException.

    Author(s)
    - Jesse Wilson

    Since
    - 1.6
    """

    def __init__(self, out: "Writer"):
        """
        Creates a new instance that writes a JSON-encoded stream to `out`.
        For best performance, ensure Writer is buffered; wrapping in
        java.io.BufferedWriter BufferedWriter if necessary.
        """
        ...


    def setIndent(self, indent: str) -> None:
        """
        Sets the indentation string to be repeated for each level of indentation
        in the encoded document. If `indent.isEmpty()` the encoded document
        will be compact. Otherwise the encoded document will be more
        human-readable.

        Arguments
        - indent: a string containing only whitespace.
        """
        ...


    def setLenient(self, lenient: bool) -> None:
        """
        Configure this writer to relax its syntax rules. By default, this writer
        only emits well-formed JSON as specified by <a
        href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>. Setting the writer
        to lenient permits the following:
        
          - Top-level values of any type. With strict writing, the top-level
              value must be an object or an array.
          - Numbers may be Double.isNaN() NaNs or Double.isInfinite() infinities.
        """
        ...


    def isLenient(self) -> bool:
        """
        Returns True if this writer has relaxed syntax rules.
        """
        ...


    def setHtmlSafe(self, htmlSafe: bool) -> None:
        """
        Configure this writer to emit JSON that's safe for direct inclusion in HTML
        and XML documents. This escapes the HTML characters `<`, `>`,
        `&` and `=` before writing them to the stream. Without this
        setting, your XML/HTML encoder should replace these characters with the
        corresponding escape sequences.
        """
        ...


    def isHtmlSafe(self) -> bool:
        """
        Returns True if this writer writes JSON that's safe for inclusion in HTML
        and XML documents.
        """
        ...


    def setSerializeNulls(self, serializeNulls: bool) -> None:
        """
        Sets whether object members are serialized when their value is null.
        This has no impact on array elements. The default is True.
        """
        ...


    def getSerializeNulls(self) -> bool:
        """
        Returns True if object members are serialized when their value is null.
        This has no impact on array elements. The default is True.
        """
        ...


    def beginArray(self) -> "JsonWriter":
        """
        Begins encoding a new array. Each call to this method must be paired with
        a call to .endArray.

        Returns
        - this writer.
        """
        ...


    def endArray(self) -> "JsonWriter":
        """
        Ends encoding the current array.

        Returns
        - this writer.
        """
        ...


    def beginObject(self) -> "JsonWriter":
        """
        Begins encoding a new object. Each call to this method must be paired
        with a call to .endObject.

        Returns
        - this writer.
        """
        ...


    def endObject(self) -> "JsonWriter":
        """
        Ends encoding the current object.

        Returns
        - this writer.
        """
        ...


    def name(self, name: str) -> "JsonWriter":
        """
        Encodes the property name.

        Arguments
        - name: the name of the forthcoming value. May not be null.

        Returns
        - this writer.
        """
        ...


    def value(self, value: str) -> "JsonWriter":
        """
        Encodes `value`.

        Arguments
        - value: the literal string value, or null to encode a null literal.

        Returns
        - this writer.
        """
        ...


    def jsonValue(self, value: str) -> "JsonWriter":
        """
        Writes `value` directly to the writer without quoting or
        escaping.

        Arguments
        - value: the literal string value, or null to encode a null literal.

        Returns
        - this writer.
        """
        ...


    def nullValue(self) -> "JsonWriter":
        """
        Encodes `null`.

        Returns
        - this writer.
        """
        ...


    def value(self, value: bool) -> "JsonWriter":
        """
        Encodes `value`.

        Returns
        - this writer.
        """
        ...


    def value(self, value: "Boolean") -> "JsonWriter":
        """
        Encodes `value`.

        Returns
        - this writer.
        """
        ...


    def value(self, value: float) -> "JsonWriter":
        """
        Encodes `value`.

        Arguments
        - value: a finite value. May not be Double.isNaN() NaNs or
            Double.isInfinite() infinities.

        Returns
        - this writer.
        """
        ...


    def value(self, value: int) -> "JsonWriter":
        """
        Encodes `value`.

        Returns
        - this writer.
        """
        ...


    def value(self, value: "Number") -> "JsonWriter":
        """
        Encodes `value`.

        Arguments
        - value: a finite value. May not be Double.isNaN() NaNs or
            Double.isInfinite() infinities.

        Returns
        - this writer.
        """
        ...


    def flush(self) -> None:
        """
        Ensures all buffered data is written to the underlying Writer
        and flushes that writer.
        """
        ...


    def close(self) -> None:
        """
        Flushes and closes this writer and the underlying Writer.

        Raises
        - IOException: if the JSON document is incomplete.
        """
        ...
