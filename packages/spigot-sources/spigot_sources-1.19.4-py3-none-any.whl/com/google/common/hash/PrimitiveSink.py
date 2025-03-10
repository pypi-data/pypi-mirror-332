"""
Python module generated from Java source file com.google.common.hash.PrimitiveSink

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.nio.charset import Charset
from typing import Any, Callable, Iterable, Tuple


class PrimitiveSink:
    """
    An object which can receive a stream of primitive values.

    Author(s)
    - Kevin Bourrillion

    Since
    - 12.0 (in 11.0 as `Sink`)
    """

    def putByte(self, b: int) -> "PrimitiveSink":
        """
        Puts a byte into this sink.

        Arguments
        - b: a byte

        Returns
        - this instance
        """
        ...


    def putBytes(self, bytes: list[int]) -> "PrimitiveSink":
        """
        Puts an array of bytes into this sink.

        Arguments
        - bytes: a byte array

        Returns
        - this instance
        """
        ...


    def putBytes(self, bytes: list[int], off: int, len: int) -> "PrimitiveSink":
        """
        Puts a chunk of an array of bytes into this sink. `bytes[off]` is the first byte written,
        `bytes[off + len - 1]` is the last.

        Arguments
        - bytes: a byte array
        - off: the start offset in the array
        - len: the number of bytes to write

        Returns
        - this instance

        Raises
        - IndexOutOfBoundsException: if `off < 0` or `off + len > bytes.length` or
            `len < 0`
        """
        ...


    def putBytes(self, bytes: "ByteBuffer") -> "PrimitiveSink":
        """
        Puts the remaining bytes of a byte buffer into this sink. `bytes.position()` is the first
        byte written, `bytes.limit() - 1` is the last. The position of the buffer will be equal
        to the limit when this method returns.

        Arguments
        - bytes: a byte buffer

        Returns
        - this instance

        Since
        - 23.0
        """
        ...


    def putShort(self, s: int) -> "PrimitiveSink":
        """
        Puts a short into this sink.
        """
        ...


    def putInt(self, i: int) -> "PrimitiveSink":
        """
        Puts an int into this sink.
        """
        ...


    def putLong(self, l: int) -> "PrimitiveSink":
        """
        Puts a long into this sink.
        """
        ...


    def putFloat(self, f: float) -> "PrimitiveSink":
        """
        Puts a float into this sink.
        """
        ...


    def putDouble(self, d: float) -> "PrimitiveSink":
        """
        Puts a double into this sink.
        """
        ...


    def putBoolean(self, b: bool) -> "PrimitiveSink":
        """
        Puts a boolean into this sink.
        """
        ...


    def putChar(self, c: str) -> "PrimitiveSink":
        """
        Puts a character into this sink.
        """
        ...


    def putUnencodedChars(self, charSequence: "CharSequence") -> "PrimitiveSink":
        """
        Puts each 16-bit code unit from the CharSequence into this sink.
        
        **Warning:** This method will produce different output than most other languages do when
        running on the equivalent input. For cross-language compatibility, use .putString,
        usually with a charset of UTF-8. For other use cases, use `putUnencodedChars`.

        Since
        - 15.0 (since 11.0 as putString(CharSequence))
        """
        ...


    def putString(self, charSequence: "CharSequence", charset: "Charset") -> "PrimitiveSink":
        """
        Puts a string into this sink using the given charset.
        
        **Warning:** This method, which reencodes the input before processing it, is useful only
        for cross-language compatibility. For other use cases, prefer .putUnencodedChars, which
        is faster, produces the same output across Java releases, and processes every `char` in
        the input, even if some are invalid.
        """
        ...
