"""
Python module generated from Java source file com.google.common.io.BaseEncoding

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Ascii
from com.google.common.base import Objects
from com.google.common.io import *
from com.google.errorprone.annotations.concurrent import LazyInit
from java.io import IOException
from java.io import InputStream
from java.io import OutputStream
from java.io import Reader
from java.io import Writer
from java.util import Arrays
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class BaseEncoding:
    """
    A binary encoding scheme for reversibly translating between byte sequences and printable ASCII
    strings. This class includes several constants for encoding schemes specified by <a
    href="http://tools.ietf.org/html/rfc4648">RFC 4648</a>. For example, the expression:
    
    ````BaseEncoding.base32().encode("foo".getBytes(Charsets.US_ASCII))````
    
    returns the string `"MZXW6==="`, and
    
    ````byte[] decoded = BaseEncoding.base32().decode("MZXW6===");````
    
    ...returns the ASCII bytes of the string `"foo"`.
    
    By default, `BaseEncoding`'s behavior is relatively strict and in accordance with RFC
    4648. Decoding rejects characters in the wrong case, though padding is optional. To modify
    encoding and decoding behavior, use configuration methods to obtain a new encoding with modified
    behavior:
    
    ````BaseEncoding.base16().lowerCase().decode("deadbeef");````
    
    Warning: BaseEncoding instances are immutable. Invoking a configuration method has no effect
    on the receiving instance; you must store and use the new encoding instance it returns, instead.
    
    ````// Do NOT do this
    BaseEncoding hex = BaseEncoding.base16();
    hex.lowerCase(); // does nothing!
    return hex.decode("deadbeef"); // throws an IllegalArgumentException````
    
    It is guaranteed that `encoding.decode(encoding.encode(x))` is always equal to `x`, but the reverse does not necessarily hold.
    
    <table>
    <caption>Encodings</caption>
    <tr>
    <th>Encoding
    <th>Alphabet
    <th>`char:byte` ratio
    <th>Default padding
    <th>Comments
    <tr>
    <td>.base16()
    <td>0-9 A-F
    <td>2.00
    <td>N/A
    <td>Traditional hexadecimal. Defaults to upper case.
    <tr>
    <td>.base32()
    <td>A-Z 2-7
    <td>1.60
    <td>=
    <td>Human-readable; no possibility of mixing up 0/O or 1/I. Defaults to upper case.
    <tr>
    <td>.base32Hex()
    <td>0-9 A-V
    <td>1.60
    <td>=
    <td>"Numerical" base 32; extended from the traditional hex alphabet. Defaults to upper case.
    <tr>
    <td>.base64()
    <td>A-Z a-z 0-9 + /
    <td>1.33
    <td>=
    <td>
    <tr>
    <td>.base64Url()
    <td>A-Z a-z 0-9 - _
    <td>1.33
    <td>=
    <td>Safe to use as filenames, or to pass in URLs without escaping
    </table>
    
    All instances of this class are immutable, so they may be stored safely as static constants.

    Author(s)
    - Louis Wasserman

    Since
    - 14.0
    """

    def encode(self, bytes: list[int]) -> str:
        """
        Encodes the specified byte array, and returns the encoded `String`.
        """
        ...


    def encode(self, bytes: list[int], off: int, len: int) -> str:
        """
        Encodes the specified range of the specified byte array, and returns the encoded `String`.
        """
        ...


    def encodingStream(self, writer: "Writer") -> "OutputStream":
        """
        Returns an `OutputStream` that encodes bytes using this encoding into the specified
        `Writer`. When the returned `OutputStream` is closed, so is the backing `Writer`.
        """
        ...


    def encodingSink(self, encodedSink: "CharSink") -> "ByteSink":
        """
        Returns a `ByteSink` that writes base-encoded bytes to the specified `CharSink`.
        """
        ...


    def canDecode(self, chars: "CharSequence") -> bool:
        """
        Determines whether the specified character sequence is a valid encoded string according to this
        encoding.

        Since
        - 20.0
        """
        ...


    def decode(self, chars: "CharSequence") -> list[int]:
        """
        Decodes the specified character sequence, and returns the resulting `byte[]`. This is the
        inverse operation to .encode(byte[]).

        Raises
        - IllegalArgumentException: if the input is not a valid encoded string according to this
            encoding.
        """
        ...


    def decodingStream(self, reader: "Reader") -> "InputStream":
        """
        Returns an `InputStream` that decodes base-encoded input from the specified `Reader`. The returned stream throws a DecodingException upon decoding-specific errors.
        """
        ...


    def decodingSource(self, encodedSource: "CharSource") -> "ByteSource":
        """
        Returns a `ByteSource` that reads base-encoded bytes from the specified `CharSource`.
        """
        ...


    def omitPadding(self) -> "BaseEncoding":
        """
        Returns an encoding that behaves equivalently to this encoding, but omits any padding
        characters as specified by <a href="http://tools.ietf.org/html/rfc4648#section-3.2">RFC 4648
        section 3.2</a>, Padding of Encoded Data.
        """
        ...


    def withPadChar(self, padChar: str) -> "BaseEncoding":
        """
        Returns an encoding that behaves equivalently to this encoding, but uses an alternate character
        for padding.

        Raises
        - IllegalArgumentException: if this padding character is already used in the alphabet or a
            separator
        """
        ...


    def withSeparator(self, separator: str, n: int) -> "BaseEncoding":
        """
        Returns an encoding that behaves equivalently to this encoding, but adds a separator string
        after every `n` characters. Any occurrences of any characters that occur in the separator
        are skipped over in decoding.

        Raises
        - IllegalArgumentException: if any alphabet or padding characters appear in the separator
            string, or if `n <= 0`
        - UnsupportedOperationException: if this encoding already uses a separator
        """
        ...


    def upperCase(self) -> "BaseEncoding":
        """
        Returns an encoding that behaves equivalently to this encoding, but encodes and decodes with
        uppercase letters. Padding and separator characters remain in their original case.

        Raises
        - IllegalStateException: if the alphabet used by this encoding contains mixed upper- and
            lower-case characters
        """
        ...


    def lowerCase(self) -> "BaseEncoding":
        """
        Returns an encoding that behaves equivalently to this encoding, but encodes and decodes with
        lowercase letters. Padding and separator characters remain in their original case.

        Raises
        - IllegalStateException: if the alphabet used by this encoding contains mixed upper- and
            lower-case characters
        """
        ...


    @staticmethod
    def base64() -> "BaseEncoding":
        """
        The "base64" base encoding specified by <a
        href="http://tools.ietf.org/html/rfc4648#section-4">RFC 4648 section 4</a>, Base 64 Encoding.
        (This is the same as the base 64 encoding from <a
        href="http://tools.ietf.org/html/rfc3548#section-3">RFC 3548</a>.)
        
        The character `'='` is used for padding, but can be .omitPadding()
        omitted or .withPadChar(char) replaced.
        
        No line feeds are added by default, as per <a
        href="http://tools.ietf.org/html/rfc4648#section-3.1">RFC 4648 section 3.1</a>, Line Feeds in
        Encoded Data. Line feeds may be added using .withSeparator(String, int).
        """
        ...


    @staticmethod
    def base64Url() -> "BaseEncoding":
        """
        The "base64url" encoding specified by <a
        href="http://tools.ietf.org/html/rfc4648#section-5">RFC 4648 section 5</a>, Base 64 Encoding
        with URL and Filename Safe Alphabet, also sometimes referred to as the "web safe Base64." (This
        is the same as the base 64 encoding with URL and filename safe alphabet from <a
        href="http://tools.ietf.org/html/rfc3548#section-4">RFC 3548</a>.)
        
        The character `'='` is used for padding, but can be .omitPadding()
        omitted or .withPadChar(char) replaced.
        
        No line feeds are added by default, as per <a
        href="http://tools.ietf.org/html/rfc4648#section-3.1">RFC 4648 section 3.1</a>, Line Feeds in
        Encoded Data. Line feeds may be added using .withSeparator(String, int).
        """
        ...


    @staticmethod
    def base32() -> "BaseEncoding":
        """
        The "base32" encoding specified by <a href="http://tools.ietf.org/html/rfc4648#section-6">RFC
        4648 section 6</a>, Base 32 Encoding. (This is the same as the base 32 encoding from <a
        href="http://tools.ietf.org/html/rfc3548#section-5">RFC 3548</a>.)
        
        The character `'='` is used for padding, but can be .omitPadding()
        omitted or .withPadChar(char) replaced.
        
        No line feeds are added by default, as per <a
        href="http://tools.ietf.org/html/rfc4648#section-3.1">RFC 4648 section 3.1</a>, Line Feeds in
        Encoded Data. Line feeds may be added using .withSeparator(String, int).
        """
        ...


    @staticmethod
    def base32Hex() -> "BaseEncoding":
        """
        The "base32hex" encoding specified by <a
        href="http://tools.ietf.org/html/rfc4648#section-7">RFC 4648 section 7</a>, Base 32 Encoding
        with Extended Hex Alphabet. There is no corresponding encoding in RFC 3548.
        
        The character `'='` is used for padding, but can be .omitPadding()
        omitted or .withPadChar(char) replaced.
        
        No line feeds are added by default, as per <a
        href="http://tools.ietf.org/html/rfc4648#section-3.1">RFC 4648 section 3.1</a>, Line Feeds in
        Encoded Data. Line feeds may be added using .withSeparator(String, int).
        """
        ...


    @staticmethod
    def base16() -> "BaseEncoding":
        """
        The "base16" encoding specified by <a href="http://tools.ietf.org/html/rfc4648#section-8">RFC
        4648 section 8</a>, Base 16 Encoding. (This is the same as the base 16 encoding from <a
        href="http://tools.ietf.org/html/rfc3548#section-6">RFC 3548</a>.) This is commonly known as
        "hexadecimal" format.
        
        No padding is necessary in base 16, so .withPadChar(char) and .omitPadding()
        have no effect.
        
        No line feeds are added by default, as per <a
        href="http://tools.ietf.org/html/rfc4648#section-3.1">RFC 4648 section 3.1</a>, Line Feeds in
        Encoded Data. Line feeds may be added using .withSeparator(String, int).
        """
        ...


    class DecodingException(IOException):
        """
        Exception indicating invalid base-encoded input encountered while decoding.

    Author(s)
        - Louis Wasserman

        Since
        - 15.0
        """


