"""
Python module generated from Java source file com.google.common.base.Utf8

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from typing import Any, Callable, Iterable, Tuple


class Utf8:
    """
    Low-level, high-performance utility methods related to the Charsets.UTF_8 UTF-8
    character encoding. UTF-8 is defined in section D92 of <a
    href="http://www.unicode.org/versions/Unicode6.2.0/ch03.pdf">The Unicode Standard Core
    Specification, Chapter 3</a>.
    
    The variant of UTF-8 implemented by this class is the restricted definition of UTF-8
    introduced in Unicode 3.1. One implication of this is that it rejects <a
    href="http://www.unicode.org/versions/corrigendum1.html">"non-shortest form"</a> byte sequences,
    even though the JDK decoder may accept them.

    Author(s)
    - Clément Roux

    Since
    - 16.0
    """

    @staticmethod
    def encodedLength(sequence: "CharSequence") -> int:
        """
        Returns the number of bytes in the UTF-8-encoded form of `sequence`. For a string, this
        method is equivalent to `string.getBytes(UTF_8).length`, but is more efficient in both
        time and space.

        Raises
        - IllegalArgumentException: if `sequence` contains ill-formed UTF-16 (unpaired
            surrogates)
        """
        ...


    @staticmethod
    def isWellFormed(bytes: list[int]) -> bool:
        """
        Returns `True` if `bytes` is a *well-formed* UTF-8 byte sequence according to
        Unicode 6.0. Note that this is a stronger criterion than simply whether the bytes can be
        decoded. For example, some versions of the JDK decoder will accept "non-shortest form" byte
        sequences, but encoding never reproduces these. Such byte sequences are *not* considered
        well-formed.
        
        This method returns `True` if and only if `Arrays.equals(bytes, new
        String(bytes, UTF_8).getBytes(UTF_8))` does, but is more efficient in both time and space.
        """
        ...


    @staticmethod
    def isWellFormed(bytes: list[int], off: int, len: int) -> bool:
        """
        Returns whether the given byte array slice is a well-formed UTF-8 byte sequence, as defined by
        .isWellFormed(byte[]). Note that this can be False even when `isWellFormed(bytes)` is True.

        Arguments
        - bytes: the input buffer
        - off: the offset in the buffer of the first byte to read
        - len: the number of bytes to read from the buffer
        """
        ...
