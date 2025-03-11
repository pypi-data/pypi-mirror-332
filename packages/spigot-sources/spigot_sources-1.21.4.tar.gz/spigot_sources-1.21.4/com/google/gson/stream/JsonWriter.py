"""
Python module generated from Java source file com.google.gson.stream.JsonWriter

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.gson import FormattingStyle
from com.google.gson import Gson
from com.google.gson import GsonBuilder
from com.google.gson import Strictness
from com.google.gson.stream import *
from java.io import Closeable
from java.io import Flushable
from java.io import IOException
from java.io import Writer
from java.math import BigDecimal
from java.math import BigInteger
from java.util import Arrays
from java.util import Objects
from java.util.concurrent.atomic import AtomicInteger
from java.util.concurrent.atomic import AtomicLong
from java.util.regex import Pattern
from typing import Any, Callable, Iterable, Tuple


class JsonWriter(Closeable, Flushable):
    """
    Writes a JSON (<a href="https://www.ietf.org/rfc/rfc8259.txt">RFC 8259</a>) encoded value to a
    stream, one token at a time. The stream includes both literal values (strings, numbers, booleans
    and nulls) as well as the begin and end delimiters of objects and arrays.
    
    <h2>Encoding JSON</h2>
    
    To encode your data as JSON, create a new `JsonWriter`. Call methods on the writer as you
    walk the structure's contents, nesting arrays and objects as necessary:
    
    
      - To write <strong>arrays</strong>, first call .beginArray(). Write each of the
          array's elements with the appropriate .value methods or by nesting other arrays and
          objects. Finally close the array using .endArray().
      - To write <strong>objects</strong>, first call .beginObject(). Write each of the
          object's properties by alternating calls to .name with the property's value. Write
          property values with the appropriate .value method or by nesting other objects or
          arrays. Finally close the object using .endObject().
    
    
    <h2>Configuration</h2>
    
    The behavior of this writer can be customized with the following methods:
    
    
      - .setFormattingStyle(FormattingStyle), the default is FormattingStyle.COMPACT
      - .setHtmlSafe(boolean), by default HTML characters are not escaped in the JSON
          output
      - .setStrictness(Strictness), the default is Strictness.LEGACY_STRICT
      - .setSerializeNulls(boolean), by default `null` is serialized
    
    
    The default configuration of `JsonWriter` instances used internally by the Gson
    class differs, and can be adjusted with the various GsonBuilder methods.
    
    <h2>Example</h2>
    
    Suppose we'd like to encode a stream of messages such as the following:
    
    ````[
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
    ]
    }```
    
    This code encodes the above structure:
    
    ````public void writeJsonStream(OutputStream out, List<Message> messages) throws IOException {
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
    }
    }```
    
    Each `JsonWriter` may be used to write a single JSON stream. Instances of this class are
    not thread safe. Calls that would result in a malformed JSON string will fail with an IllegalStateException.

    Author(s)
    - Jesse Wilson

    Since
    - 1.6
    """

    def __init__(self, out: "Writer"):
        """
        Creates a new instance that writes a JSON-encoded stream to `out`. For best performance,
        ensure Writer is buffered; wrapping in java.io.BufferedWriter BufferedWriter if
        necessary.
        """
        ...


    def setIndent(self, indent: str) -> None:
        """
        Sets the indentation string to be repeated for each level of indentation in the encoded
        document. If `indent.isEmpty()` the encoded document will be compact. Otherwise the
        encoded document will be more human-readable.
        
        This is a convenience method which overwrites any previously .setFormattingStyle(FormattingStyle) set formatting style with either FormattingStyle.COMPACT if the given indent string is empty, or FormattingStyle.PRETTY
        with the given indent if not empty.

        Arguments
        - indent: a string containing only whitespace.
        """
        ...


    def setFormattingStyle(self, formattingStyle: "FormattingStyle") -> None:
        """
        Sets the formatting style to be used in the encoded document.
        
        The formatting style specifies for example the indentation string to be repeated for each
        level of indentation, or the newline style, to accommodate various OS styles.

        Arguments
        - formattingStyle: the formatting style to use, must not be `null`.

        Since
        - 2.11.0
        """
        ...


    def getFormattingStyle(self) -> "FormattingStyle":
        """
        Returns the pretty printing style used by this writer.

        Returns
        - the `FormattingStyle` that will be used.

        Since
        - 2.11.0
        """
        ...


    def setLenient(self, lenient: bool) -> None:
        """
        Sets the strictness of this writer.

        Arguments
        - lenient: whether this writer should be lenient. If True, the strictness is set to Strictness.LENIENT. If False, the strictness is set to Strictness.LEGACY_STRICT.

        See
        - .setStrictness(Strictness)

        Deprecated
        - Please use .setStrictness(Strictness) instead. `JsonWriter.setLenient(True)` should be replaced by `JsonWriter.setStrictness(Strictness.LENIENT)` and `JsonWriter.setLenient(False)`
            should be replaced by `JsonWriter.setStrictness(Strictness.LEGACY_STRICT)`.
            However, if you used `setLenient(False)` before, you might prefer Strictness.STRICT now instead.
        """
        ...


    def isLenient(self) -> bool:
        """
        Returns True if the Strictness of this writer is equal to Strictness.LENIENT.

        See
        - .getStrictness()
        """
        ...


    def setStrictness(self, strictness: "Strictness") -> None:
        """
        Configures how strict this writer is with regard to the syntax rules specified in <a
        href="https://www.ietf.org/rfc/rfc8259.txt">RFC 8259</a>. By default, Strictness.LEGACY_STRICT is used.
        
        <dl>
          <dt>Strictness.STRICT &amp; Strictness.LEGACY_STRICT
          <dd>The behavior of these is currently identical. In these strictness modes, the writer only
              writes JSON in accordance with RFC 8259.
          <dt>Strictness.LENIENT
          <dd>This mode relaxes the behavior of the writer to allow the writing of Double.isNaN() NaNs and Double.isInfinite() infinities. It also allows writing
              multiple top level values.
        </dl>

        Arguments
        - strictness: the new strictness of this writer. May not be `null`.

        See
        - .getStrictness()

        Since
        - 2.11.0
        """
        ...


    def getStrictness(self) -> "Strictness":
        """
        Returns the Strictness strictness of this writer.

        See
        - .setStrictness(Strictness)

        Since
        - 2.11.0
        """
        ...


    def setHtmlSafe(self, htmlSafe: bool) -> None:
        """
        Configures this writer to emit JSON that's safe for direct inclusion in HTML and XML documents.
        This escapes the HTML characters `<`, `>`, `&`, `=` and `'`
        before writing them to the stream. Without this setting, your XML/HTML encoder should replace
        these characters with the corresponding escape sequences.
        """
        ...


    def isHtmlSafe(self) -> bool:
        """
        Returns True if this writer writes JSON that's safe for inclusion in HTML and XML documents.
        """
        ...


    def setSerializeNulls(self, serializeNulls: bool) -> None:
        """
        Sets whether object members are serialized when their value is null. This has no impact on
        array elements. The default is True.
        """
        ...


    def getSerializeNulls(self) -> bool:
        """
        Returns True if object members are serialized when their value is null. This has no impact on
        array elements. The default is True.
        """
        ...


    def beginArray(self) -> "JsonWriter":
        """
        Begins encoding a new array. Each call to this method must be paired with a call to .endArray.

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
        Begins encoding a new object. Each call to this method must be paired with a call to .endObject.

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
        - name: the name of the forthcoming value. May not be `null`.

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

        Since
        - 2.7
        """
        ...


    def value(self, value: float) -> "JsonWriter":
        """
        Encodes `value`.

        Arguments
        - value: a finite value, or if .setStrictness(Strictness) lenient, also Float.isNaN() NaN or Float.isInfinite() infinity.

        Returns
        - this writer.

        Raises
        - IllegalArgumentException: if the value is NaN or Infinity and this writer is not .setStrictness(Strictness) lenient.

        Since
        - 2.9.1
        """
        ...


    def value(self, value: float) -> "JsonWriter":
        """
        Encodes `value`.

        Arguments
        - value: a finite value, or if .setStrictness(Strictness) lenient, also Double.isNaN() NaN or Double.isInfinite() infinity.

        Returns
        - this writer.

        Raises
        - IllegalArgumentException: if the value is NaN or Infinity and this writer is not .setStrictness(Strictness) lenient.
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
        Encodes `value`. The value is written by directly writing the Number.toString()
        result to JSON. Implementations must make sure that the result represents a valid JSON number.

        Arguments
        - value: a finite value, or if .setStrictness(Strictness) lenient, also Double.isNaN() NaN or Double.isInfinite() infinity.

        Returns
        - this writer.

        Raises
        - IllegalArgumentException: if the value is NaN or Infinity and this writer is not .setStrictness(Strictness) lenient; or if the `toString()` result is not a valid
            JSON number.
        """
        ...


    def nullValue(self) -> "JsonWriter":
        """
        Encodes `null`.

        Returns
        - this writer.
        """
        ...


    def jsonValue(self, value: str) -> "JsonWriter":
        """
        Writes `value` directly to the writer without quoting or escaping. This might not be
        supported by all implementations, if not supported an `UnsupportedOperationException` is
        thrown.

        Arguments
        - value: the literal string value, or null to encode a null literal.

        Returns
        - this writer.

        Raises
        - UnsupportedOperationException: if this writer does not support writing raw JSON values.

        Since
        - 2.4
        """
        ...


    def flush(self) -> None:
        """
        Ensures all buffered data is written to the underlying Writer and flushes that writer.
        """
        ...


    def close(self) -> None:
        """
        Flushes and closes this writer and the underlying Writer.

        Raises
        - IOException: if the JSON document is incomplete.
        """
        ...
