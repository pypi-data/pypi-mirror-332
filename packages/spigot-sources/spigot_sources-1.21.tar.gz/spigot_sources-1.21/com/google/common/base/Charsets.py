"""
Python module generated from Java source file com.google.common.base.Charsets

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import *
from java.nio.charset import Charset
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

    US_ASCII = Charset.forName("US-ASCII")
    """
    US-ASCII: seven-bit ASCII, the Basic Latin block of the Unicode character set (ISO646-US).
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.US_ASCII instead.
    """
    ISO_8859_1 = Charset.forName("ISO-8859-1")
    """
    ISO-8859-1: ISO Latin Alphabet Number 1 (ISO-LATIN-1).
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.ISO_8859_1 instead.
    """
    UTF_8 = Charset.forName("UTF-8")
    """
    UTF-8: eight-bit UCS Transformation Format.
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.UTF_8 instead.
    """
    UTF_16BE = Charset.forName("UTF-16BE")
    """
    UTF-16BE: sixteen-bit UCS Transformation Format, big-endian byte order.
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.UTF_16BE instead.
    """
    UTF_16LE = Charset.forName("UTF-16LE")
    """
    UTF-16LE: sixteen-bit UCS Transformation Format, little-endian byte order.
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.UTF_16LE instead.
    """
    UTF_16 = Charset.forName("UTF-16")
    """
    UTF-16: sixteen-bit UCS Transformation Format, byte order identified by an optional byte-order
    mark.
    
    **Note for Java 7 and later:** this constant should be treated as deprecated; use java.nio.charset.StandardCharsets.UTF_16 instead.
    """
