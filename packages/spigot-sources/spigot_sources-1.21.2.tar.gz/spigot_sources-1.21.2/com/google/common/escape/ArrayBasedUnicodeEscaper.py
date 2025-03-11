"""
Python module generated from Java source file com.google.common.escape.ArrayBasedUnicodeEscaper

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ArrayBasedUnicodeEscaper(UnicodeEscaper):
    """
    A UnicodeEscaper that uses an array to quickly look up replacement characters for a given
    code point. An additional safe range is provided that determines whether code points without
    specific replacements are to be considered safe and left unescaped or should be escaped in a
    general way.
    
    A good example of usage of this class is for HTML escaping where the replacement array
    contains information about the named HTML entities such as `&amp;` and `&quot;` while
    .escapeUnsafe is overridden to handle general escaping of the form `&.NNNNN;`.
    
    The size of the data structure used by ArrayBasedUnicodeEscaper is proportional to the
    highest valued code point that requires escaping. For example a replacement map containing the
    single character '`\``u1000`' will require approximately 16K of memory. If you need
    to create multiple escaper instances that have the same character replacement mapping consider
    using ArrayBasedEscaperMap.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    def escape(self, s: str) -> str:
        ...
