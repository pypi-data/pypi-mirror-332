"""
Python module generated from Java source file com.google.gson.JsonStreamParser

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import Streams
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import MalformedJsonException
from java.io import EOFException
from java.io import IOException
from java.io import Reader
from java.io import StringReader
from java.util import Iterator
from java.util import NoSuchElementException
from typing import Any, Callable, Iterable, Tuple


class JsonStreamParser(Iterator):
    """
    A streaming parser that allows reading of multiple JsonElements from the specified reader
    asynchronously. The JSON data is parsed in lenient mode, see also
    JsonReader.setLenient(boolean).
    
    This class is conditionally thread-safe (see Item 70, Effective Java second edition). To
    properly use this class across multiple threads, you will need to add some external
    synchronization. For example:
    
    ```
    JsonStreamParser parser = new JsonStreamParser("['first'] {'second':10} 'third'");
    JsonElement element;
    synchronized (parser) {  // synchronize on an object shared by threads
      if (parser.hasNext()) {
        element = parser.next();
      }
    }
    ```

    Author(s)
    - Joel Leitch

    Since
    - 1.4
    """

    def __init__(self, json: str):
        """
        Arguments
        - json: The string containing JSON elements concatenated to each other.

        Since
        - 1.4
        """
        ...


    def __init__(self, reader: "Reader"):
        """
        Arguments
        - reader: The data stream containing JSON elements concatenated to each other.

        Since
        - 1.4
        """
        ...


    def next(self) -> "JsonElement":
        """
        Returns the next available JsonElement on the reader. Throws a
        NoSuchElementException if no element is available.

        Returns
        - the next available `JsonElement` on the reader.

        Raises
        - JsonSyntaxException: if the incoming stream is malformed JSON.
        - NoSuchElementException: if no `JsonElement` is available.

        Since
        - 1.4
        """
        ...


    def hasNext(self) -> bool:
        """
        Returns True if a JsonElement is available on the input for consumption

        Returns
        - True if a JsonElement is available on the input, False otherwise

        Raises
        - JsonSyntaxException: if the incoming stream is malformed JSON.

        Since
        - 1.4
        """
        ...


    def remove(self) -> None:
        """
        This optional Iterator method is not relevant for stream parsing and hence is not
        implemented.

        Since
        - 1.4
        """
        ...
