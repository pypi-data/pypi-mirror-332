"""
Python module generated from Java source file com.google.common.hash.Hasher

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.hash import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from java.nio.charset import Charset
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Hasher(PrimitiveSink):
    """
    A PrimitiveSink that can compute a hash code after reading the input. Each hasher should
    translate all multibyte values (.putInt(int), .putLong(long), etc) to bytes in
    little-endian order.
    
    **Warning:** The result of calling any methods after calling .hash is undefined.
    
    **Warning:** Using a specific character encoding when hashing a CharSequence with
    .putString(CharSequence, Charset) is generally only useful for cross-language
    compatibility (otherwise prefer .putUnencodedChars). However, the character encodings
    must be identical across languages. Also beware that Charset definitions may occasionally
    change between Java releases.
    
    **Warning:** Chunks of data that are put into the Hasher are not delimited. The
    resulting HashCode is dependent only on the bytes inserted, and the order in which they
    were inserted, not how those bytes were chunked into discrete put() operations. For example, the
    following three expressions all generate colliding hash codes:
    
    ````newHasher().putByte(b1).putByte(b2).putByte(b3).hash()
    newHasher().putByte(b1).putBytes(new byte[] { b2, b3`).hash()
    newHasher().putBytes(new byte[] { b1, b2, b3 }).hash()
    }```
    
    If you wish to avoid this, you should either prepend or append the size of each chunk. Keep in
    mind that when dealing with char sequences, the encoded form of two concatenated char sequences
    is not equivalent to the concatenation of their encoded form. Therefore, .putString(CharSequence, Charset) should only be used consistently with *complete*
    sequences and not broken into chunks.

    Author(s)
    - Kevin Bourrillion

    Since
    - 11.0
    """

    def putByte(self, b: int) -> "Hasher":
        ...


    def putBytes(self, bytes: list[int]) -> "Hasher":
        ...


    def putBytes(self, bytes: list[int], off: int, len: int) -> "Hasher":
        ...


    def putBytes(self, bytes: "ByteBuffer") -> "Hasher":
        ...


    def putShort(self, s: int) -> "Hasher":
        ...


    def putInt(self, i: int) -> "Hasher":
        ...


    def putLong(self, l: int) -> "Hasher":
        ...


    def putFloat(self, f: float) -> "Hasher":
        """
        Equivalent to `putInt(Float.floatToRawIntBits(f))`.
        """
        ...


    def putDouble(self, d: float) -> "Hasher":
        """
        Equivalent to `putLong(Double.doubleToRawLongBits(d))`.
        """
        ...


    def putBoolean(self, b: bool) -> "Hasher":
        """
        Equivalent to `putByte(b ? (byte) 1 : (byte) 0)`.
        """
        ...


    def putChar(self, c: str) -> "Hasher":
        ...


    def putUnencodedChars(self, charSequence: "CharSequence") -> "Hasher":
        """
        Equivalent to processing each `char` value in the `CharSequence`, in order. In
        other words, no character encoding is performed; the low byte and high byte of each `char` are hashed directly (in that order). The input must not be updated while this method is
        in progress.
        
        **Warning:** This method will produce different output than most other languages do when
        running the same hash function on the equivalent input. For cross-language compatibility, use
        .putString, usually with a charset of UTF-8. For other use cases, use `putUnencodedChars`.

        Since
        - 15.0 (since 11.0 as putString(CharSequence)).
        """
        ...


    def putString(self, charSequence: "CharSequence", charset: "Charset") -> "Hasher":
        """
        Equivalent to `putBytes(charSequence.toString().getBytes(charset))`.
        
        **Warning:** This method, which reencodes the input before hashing it, is useful only for
        cross-language compatibility. For other use cases, prefer .putUnencodedChars, which is
        faster, produces the same output across Java releases, and hashes every `char` in the
        input, even if some are invalid.
        """
        ...


    def putObject(self, instance: "T", funnel: "Funnel"["T"]) -> "Hasher":
        """
        A simple convenience for `funnel.funnel(object, this)`.
        """
        ...


    def hash(self) -> "HashCode":
        """
        Computes a hash code based on the data that have been provided to this hasher. The result is
        unspecified if this method is called more than once on the same instance.
        """
        ...


    def hashCode(self) -> int:
        """
        Deprecated
        - This returns Object.hashCode(); you almost certainly mean to call `hash().asInt()`.
        """
        ...
