"""
Python module generated from Java source file java.nio.charset.StandardCharsets

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.nio.charset import *
from typing import Any, Callable, Iterable, Tuple


class StandardCharsets:
    """
    Constant definitions for the standard Charset charsets. These
    charsets are guaranteed to be available on every implementation of the Java
    platform.

    See
    - <a href="Charset.html.standard">Standard Charsets</a>

    Since
    - 1.7
    """

    US_ASCII = sun.nio.cs.US_ASCII.INSTANCE
    """
    Seven-bit ASCII, also known as ISO646-US, also known as the
    Basic Latin block of the Unicode character set.
    """
    ISO_8859_1 = sun.nio.cs.ISO_8859_1.INSTANCE
    """
    ISO Latin Alphabet No. 1, also known as ISO-LATIN-1.
    """
    UTF_8 = sun.nio.cs.UTF_8.INSTANCE
    """
    Eight-bit UCS Transformation Format.
    """
    UTF_16BE = sun.nio.cs.UTF_16BE()
    """
    Sixteen-bit UCS Transformation Format, big-endian byte order.
    """
    UTF_16LE = sun.nio.cs.UTF_16LE()
    """
    Sixteen-bit UCS Transformation Format, little-endian byte order.
    """
    UTF_16 = sun.nio.cs.UTF_16()
    """
    Sixteen-bit UCS Transformation Format, byte order identified by an
    optional byte-order mark.
    """
