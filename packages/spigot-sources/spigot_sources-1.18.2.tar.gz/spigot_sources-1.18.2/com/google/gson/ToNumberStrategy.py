"""
Python module generated from Java source file com.google.gson.ToNumberStrategy

Java source file obtained from artifact gson version 2.8.9

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.stream import JsonReader
from java.io import IOException
from typing import Any, Callable, Iterable, Tuple


class ToNumberStrategy:
    """
    A strategy that is used to control how numbers should be deserialized for Object and Number
    when a concrete type of the deserialized number is unknown in advance. By default, Gson uses the following
    deserialization strategies:
    
    
    - Double values are returned for JSON numbers if the deserialization type is declared as
    `Object`, see ToNumberPolicy.DOUBLE;
    - Lazily parsed number values are returned if the deserialization type is declared as `Number`,
    see ToNumberPolicy.LAZILY_PARSED_NUMBER.
    
    
    For historical reasons, Gson does not support deserialization of arbitrary-length numbers for
    `Object` and `Number` by default, potentially causing precision loss. However,
    <a href="https://tools.ietf.org/html/rfc8259#section-6">RFC 8259</a> permits this:
    
    ```
      This specification allows implementations to set limits on the range
      and precision of numbers accepted.  Since software that implements
      IEEE 754 binary64 (double precision) numbers [IEEE754] is generally
      available and widely used, good interoperability can be achieved by
      implementations that expect no more precision or range than these
      provide, in the sense that implementations will approximate JSON
      numbers within the expected precision.  A JSON number such as 1E400
      or 3.141592653589793238462643383279 may indicate potential
      interoperability problems, since it suggests that the software that
      created it expects receiving software to have greater capabilities
      for numeric magnitude and precision than is widely available.
    ```
    
    To overcome the precision loss, use for example ToNumberPolicy.LONG_OR_DOUBLE or
    ToNumberPolicy.BIG_DECIMAL.

    See
    - GsonBuilder.setNumberToNumberStrategy(ToNumberStrategy)
    """

    def readNumber(self, in: "JsonReader") -> "Number":
        """
        Reads a number from the given JSON reader. A strategy is supposed to read a single value from the
        reader, and the read value is guaranteed never to be `null`.

        Arguments
        - in: JSON reader to read a number from

        Returns
        - number read from the JSON reader.

        Raises
        - IOException: 
        """
        ...
