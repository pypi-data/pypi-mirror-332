"""
Python module generated from Java source file com.google.gson.Strictness

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class Strictness(Enum):
    """
    Modes that indicate how strictly a JSON JsonReader reader or JsonWriter
    writer follows the syntax laid out in the <a href="https://www.ietf.org/rfc/rfc8259.txt">RFC
    8259 JSON specification</a>.
    
    You can look at JsonReader.setStrictness(Strictness) to see how the strictness affects
    the JsonReader and you can look at JsonWriter.setStrictness(Strictness) to see
    how the strictness affects the JsonWriter.

    See
    - JsonWriter.setStrictness(Strictness)

    Since
    - 2.11.0
    """

    LENIENT = 0
    """
    Allow large deviations from the JSON specification.
    """
    LEGACY_STRICT = 1
    """
    Allow certain small deviations from the JSON specification for legacy reasons.
    """
    STRICT = 2
    """
    Strict compliance with the JSON specification.
    """
