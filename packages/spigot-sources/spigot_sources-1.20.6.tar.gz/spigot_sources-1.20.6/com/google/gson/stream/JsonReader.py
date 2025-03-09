"""
Python module generated from Java source file com.google.gson.stream.JsonReader

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson.internal import JsonReaderInternalAccess
from com.google.gson.internal.bind import JsonTreeReader
from com.google.gson.stream import *
from java.io import Closeable
from java.io import EOFException
from java.io import IOException
from java.io import Reader
from java.util import Arrays
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class JsonReader(Closeable):
    """
    Reads a JSON (<a href="http://www.ietf.org/rfc/rfc7159.txt">RFC 7159</a>)
    encoded value as a stream of tokens. This stream includes both literal
    values (strings, numbers, booleans, and nulls) as well as the begin and
    end delimiters of objects and arrays. The tokens are traversed in
    depth-first order, the same order that they appear in the JSON document.
    Within JSON objects, name/value pairs are represented by a single token.
    
    <h2>Parsing JSON</h2>
    To create a recursive descent parser for your own JSON streams, first create
    an entry point method that creates a `JsonReader`.
    
    Next, create handler methods for each structure in your JSON text. You'll
    need a method for each object type and for each array type.
    
      - Within <strong>array handling</strong> methods, first call .beginArray to consume the array's opening bracket. Then create a
          while loop that accumulates values, terminating when .hasNext
          is False. Finally, read the array's closing bracket by calling .endArray.
      - Within <strong>object handling</strong> methods, first call .beginObject to consume the object's opening brace. Then create a
          while loop that assigns values to local variables based on their name.
          This loop should terminate when .hasNext is False. Finally,
          read the object's closing brace by calling .endObject.
    
    When a nested object or array is encountered, delegate to the
    corresponding handler method.
    
    When an unknown name is encountered, strict parsers should fail with an
    exception. Lenient parsers should call .skipValue() to recursively
    skip the value's nested tokens, which may otherwise conflict.
    
    If a value may be null, you should first check using .peek().
    Null literals can be consumed using either .nextNull() or .skipValue().
    
    <h2>Example</h2>
    Suppose we'd like to parse a stream of messages such as the following: ``` `[
      {
        "id": 912345678901,
        "text": "How do I read a JSON stream in Java?",
        "geo": null,
        "user": {
          "name": "json_newb",
          "followers_count": 41`
      },
      {
        "id": 912345678902,
        "text": "@json_newb just use JsonReader!",
        "geo": [50.454722, -104.606667],
        "user": {
          "name": "jesse",
          "followers_count": 2
        }
      }
    ]}```
    This code implements the parser for the above structure: ```   `public List<Message> readJsonStream(InputStream in) throws IOException {
        JsonReader reader = new JsonReader(new InputStreamReader(in, "UTF-8"));
        try {
          return readMessagesArray(reader);` finally {
          reader.close();
        }
      }
    
      public List<Message> readMessagesArray(JsonReader reader) throws IOException {
        List<Message> messages = new ArrayList<>();
    
        reader.beginArray();
        while (reader.hasNext()) {
          messages.add(readMessage(reader));
        }
        reader.endArray();
        return messages;
      }
    
      public Message readMessage(JsonReader reader) throws IOException {
        long id = -1;
        String text = null;
        User user = null;
        List<Double> geo = null;
    
        reader.beginObject();
        while (reader.hasNext()) {
          String name = reader.nextName();
          if (name.equals("id")) {
            id = reader.nextLong();
          } else if (name.equals("text")) {
            text = reader.nextString();
          } else if (name.equals("geo") && reader.peek() != JsonToken.NULL) {
            geo = readDoublesArray(reader);
          } else if (name.equals("user")) {
            user = readUser(reader);
          } else {
            reader.skipValue();
          }
        }
        reader.endObject();
        return new Message(id, text, user, geo);
      }
    
      public List<Double> readDoublesArray(JsonReader reader) throws IOException {
        List<Double> doubles = new ArrayList<>();
    
        reader.beginArray();
        while (reader.hasNext()) {
          doubles.add(reader.nextDouble());
        }
        reader.endArray();
        return doubles;
      }
    
      public User readUser(JsonReader reader) throws IOException {
        String username = null;
        int followersCount = -1;
    
        reader.beginObject();
        while (reader.hasNext()) {
          String name = reader.nextName();
          if (name.equals("name")) {
            username = reader.nextString();
          } else if (name.equals("followers_count")) {
            followersCount = reader.nextInt();
          } else {
            reader.skipValue();
          }
        }
        reader.endObject();
        return new User(username, followersCount);
      }}```
    
    <h2>Number Handling</h2>
    This reader permits numeric values to be read as strings and string values to
    be read as numbers. For example, both elements of the JSON array `[1, "1"]` may be read using either .nextInt or .nextString.
    This behavior is intended to prevent lossy numeric conversions: double is
    JavaScript's only numeric type and very large values like `9007199254740993` cannot be represented exactly on that platform. To minimize
    precision loss, extremely large values should be written and read as strings
    in JSON.
    
    <h2 id="nonexecuteprefix">Non-Execute Prefix</h2>
    Web servers that serve private data using JSON may be vulnerable to <a
    href="http://en.wikipedia.org/wiki/JSON#Cross-site_request_forgery">Cross-site
    request forgery</a> attacks. In such an attack, a malicious site gains access
    to a private JSON file by executing it with an HTML `<script>` tag.
    
    Prefixing JSON files with `")]}'\n"` makes them non-executable
    by `<script>` tags, disarming the attack. Since the prefix is malformed
    JSON, strict parsing fails when it is encountered. This class permits the
    non-execute prefix when .setLenient(boolean) lenient parsing is
    enabled.
    
    Each `JsonReader` may be used to read a single JSON stream. Instances
    of this class are not thread safe.

    Author(s)
    - Jesse Wilson

    Since
    - 1.6
    """

    def __init__(self, in: "Reader"):
        """
        Creates a new instance that reads a JSON-encoded stream from `in`.
        """
        ...


    def setLenient(self, lenient: bool) -> None:
        """
        Configure this parser to be liberal in what it accepts. By default,
        this parser is strict and only accepts JSON as specified by <a
        href="http://www.ietf.org/rfc/rfc4627.txt">RFC 4627</a>. Setting the
        parser to lenient causes it to ignore the following syntax errors:
        
        
          - Streams that start with the <a href="#nonexecuteprefix">non-execute
              prefix</a>, `")]}'\n"`.
          - Streams that include multiple top-level values. With strict parsing,
              each stream must contain exactly one top-level value.
          - Numbers may be Double.isNaN() NaNs or Double.isInfinite() infinities.
          - End of line comments starting with `//` or `.` and
              ending with a newline character.
          - C-style comments starting with `/*` and ending with
              `*``/`. Such comments may not be nested.
          - Names that are unquoted or `'single quoted'`.
          - Strings that are unquoted or `'single quoted'`.
          - Array elements separated by `;` instead of `,`.
          - Unnecessary array separators. These are interpreted as if null
              was the omitted value.
          - Names and values separated by `=` or `=>` instead of
              `:`.
          - Name/value pairs separated by `;` instead of `,`.
        
        
        Note: Even in strict mode there are slight derivations from the JSON
        specification:
        
          - JsonReader allows the literals `True`, `False` and `null`
              to have any capitalization, for example `fAlSe`
          - JsonReader supports the escape sequence `\'`, representing a `'`
          - JsonReader supports the escape sequence `\*LF*` (with `LF`
              being the Unicode character U+000A), resulting in a `LF` within the
              read JSON string
          - JsonReader allows unescaped control characters (U+0000 through U+001F)
        """
        ...


    def isLenient(self) -> bool:
        """
        Returns True if this parser is liberal in what it accepts.
        """
        ...


    def beginArray(self) -> None:
        """
        Consumes the next token from the JSON stream and asserts that it is the
        beginning of a new array.
        """
        ...


    def endArray(self) -> None:
        """
        Consumes the next token from the JSON stream and asserts that it is the
        end of the current array.
        """
        ...


    def beginObject(self) -> None:
        """
        Consumes the next token from the JSON stream and asserts that it is the
        beginning of a new object.
        """
        ...


    def endObject(self) -> None:
        """
        Consumes the next token from the JSON stream and asserts that it is the
        end of the current object.
        """
        ...


    def hasNext(self) -> bool:
        """
        Returns True if the current array or object has another element.
        """
        ...


    def peek(self) -> "JsonToken":
        """
        Returns the type of the next token without consuming it.
        """
        ...


    def nextName(self) -> str:
        """
        Returns the next token, a JsonToken.NAME property name, and consumes it.

        Raises
        - IOException: if the next token in the stream is not a property
            name.
        """
        ...


    def nextString(self) -> str:
        """
        Returns the JsonToken.STRING string value of the next token,
        consuming it. If the next token is a number, this method will return its
        string form.

        Raises
        - IllegalStateException: if the next token is not a string or if
            this reader is closed.
        """
        ...


    def nextBoolean(self) -> bool:
        """
        Returns the JsonToken.BOOLEAN boolean value of the next token,
        consuming it.

        Raises
        - IllegalStateException: if the next token is not a boolean or if
            this reader is closed.
        """
        ...


    def nextNull(self) -> None:
        """
        Consumes the next token from the JSON stream and asserts that it is a
        literal null.

        Raises
        - IllegalStateException: if the next token is not null or if this
            reader is closed.
        """
        ...


    def nextDouble(self) -> float:
        """
        Returns the JsonToken.NUMBER double value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as a double using Double.parseDouble(String).

        Raises
        - IllegalStateException: if the next token is not a literal value.
        - NumberFormatException: if the next literal value cannot be parsed
            as a double.
        - MalformedJsonException: if the next literal value is NaN or Infinity
            and this reader is not .setLenient(boolean) lenient.
        """
        ...


    def nextLong(self) -> int:
        """
        Returns the JsonToken.NUMBER long value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as a long. If the next token's numeric value cannot be exactly
        represented by a Java `long`, this method throws.

        Raises
        - IllegalStateException: if the next token is not a literal value.
        - NumberFormatException: if the next literal value cannot be parsed
            as a number, or exactly represented as a long.
        """
        ...


    def nextInt(self) -> int:
        """
        Returns the JsonToken.NUMBER int value of the next token,
        consuming it. If the next token is a string, this method will attempt to
        parse it as an int. If the next token's numeric value cannot be exactly
        represented by a Java `int`, this method throws.

        Raises
        - IllegalStateException: if the next token is not a literal value.
        - NumberFormatException: if the next literal value cannot be parsed
            as a number, or exactly represented as an int.
        """
        ...


    def close(self) -> None:
        """
        Closes this JSON reader and the underlying Reader.
        """
        ...


    def skipValue(self) -> None:
        """
        Skips the next value recursively. This method is intended for use when
        the JSON token stream contains unrecognized or unhandled values.
        
        The behavior depends on the type of the next JSON token:
        
          - Start of a JSON array or object: It and all of its nested values are skipped.
          - Primitive value (for example a JSON number): The primitive value is skipped.
          - Property name: Only the name but not the value of the property is skipped.
          `skipValue()` has to be called again to skip the property value as well.
          - End of a JSON array or object: Only this end token is skipped.
          - End of JSON document: Skipping has no effect, the next token continues to be the
          end of the document.
        """
        ...


    def toString(self) -> str:
        ...


    def getPreviousPath(self) -> str:
        """
        Returns a <a href="https://goessner.net/articles/JsonPath/">JSONPath</a>
        in *dot-notation* to the previous (or current) location in the JSON document:
        
          - For JSON arrays the path points to the index of the previous element.
          If no element has been consumed yet it uses the index 0 (even if there are no elements).
          - For JSON objects the path points to the last property, or to the current
          property if its name has already been consumed.
        
        
        This method can be useful to add additional context to exception messages
        *after* a value has been consumed.
        """
        ...


    def getPath(self) -> str:
        """
        Returns a <a href="https://goessner.net/articles/JsonPath/">JSONPath</a>
        in *dot-notation* to the next (or current) location in the JSON document:
        
          - For JSON arrays the path points to the index of the next element (even
          if there are no further elements).
          - For JSON objects the path points to the last property, or to the current
          property if its name has already been consumed.
        
        
        This method can be useful to add additional context to exception messages
        *before* a value is consumed, for example when the .peek() peeked
        token is unexpected.
        """
        ...
