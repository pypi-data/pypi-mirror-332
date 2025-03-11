"""
Python module generated from Java source file com.google.common.base.Charsets

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from java.nio.charset import Charset
from java.nio.charset import StandardCharsets
from typing import Any, Callable, Iterable, Tuple


class Charsets:
    """
    Contains constant definitions for the six standard Charset instances, which are
    guaranteed to be supported by all Java platform implementations.
    
    Assuming you're free to choose, note that **.UTF_8 is widely preferred**.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/StringsExplained#charsets">`Charsets`</a>.

    Author(s)
    - Mike Bostock

    Since
    - 1.0
    """

    US_ASCII = StandardCharsets.US_ASCII
    """
    US-ASCII: seven-bit ASCII, the Basic Latin block of the Unicode character set (ISO646-US).
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.US_ASCII instead.
    """
    ISO_8859_1 = StandardCharsets.ISO_8859_1
    """
    ISO-8859-1: ISO Latin Alphabet Number 1 (ISO-LATIN-1).
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.ISO_8859_1 instead.
    """
    UTF_8 = StandardCharsets.UTF_8
    """
    UTF-8: eight-bit UCS Transformation Format.
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.UTF_8 instead.
    """
    UTF_16BE = StandardCharsets.UTF_16BE
    """
    UTF-16BE: sixteen-bit UCS Transformation Format, big-endian byte order.
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.UTF_16BE instead.
    """
    UTF_16LE = StandardCharsets.UTF_16LE
    """
    UTF-16LE: sixteen-bit UCS Transformation Format, little-endian byte order.
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.UTF_16LE instead.
    """
    UTF_16 = StandardCharsets.UTF_16
    """
    UTF-16: sixteen-bit UCS Transformation Format, byte order identified by an optional byte-order
    mark.
    
    **Note:** this constant is now unnecessary and should be treated as deprecated; use
    StandardCharsets.UTF_16 instead.
    """
