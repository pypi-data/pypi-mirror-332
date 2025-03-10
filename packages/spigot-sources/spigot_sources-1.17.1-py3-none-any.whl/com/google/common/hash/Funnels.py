"""
Python module generated from Java source file com.google.common.hash.Funnels

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import Preconditions
from com.google.common.hash import *
from java.io import OutputStream
from java.io import Serializable
from java.nio.charset import Charset
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Funnels:
    """
    Funnels for common types. All implementations are serializable.

    Author(s)
    - Dimitris Andreou

    Since
    - 11.0
    """

    @staticmethod
    def byteArrayFunnel() -> "Funnel"[list[int]]:
        """
        Returns a funnel that extracts the bytes from a `byte` array.
        """
        ...


    @staticmethod
    def unencodedCharsFunnel() -> "Funnel"["CharSequence"]:
        """
        Returns a funnel that extracts the characters from a `CharSequence`, a character at a
        time, without performing any encoding. If you need to use a specific encoding, use
        Funnels.stringFunnel(Charset) instead.

        Since
        - 15.0 (since 11.0 as `Funnels.stringFunnel()`.
        """
        ...


    @staticmethod
    def stringFunnel(charset: "Charset") -> "Funnel"["CharSequence"]:
        """
        Returns a funnel that encodes the characters of a `CharSequence` with the specified
        `Charset`.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def integerFunnel() -> "Funnel"["Integer"]:
        """
        Returns a funnel for integers.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def sequentialFunnel(elementFunnel: "Funnel"["E"]) -> "Funnel"[Iterable["E"]]:
        """
        Returns a funnel that processes an `Iterable` by funneling its elements in iteration
        order with the specified funnel. No separators are added between the elements.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def longFunnel() -> "Funnel"["Long"]:
        """
        Returns a funnel for longs.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def asOutputStream(sink: "PrimitiveSink") -> "OutputStream":
        """
        Wraps a `PrimitiveSink` as an OutputStream, so it is easy to Funnel.funnel
        funnel an object to a `PrimitiveSink` if there is already a way to write the contents of
        the object to an `OutputStream`.
        
        The `close` and `flush` methods of the returned `OutputStream` do nothing,
        and no method throws `IOException`.

        Since
        - 13.0
        """
        ...
