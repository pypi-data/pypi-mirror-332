"""
Python module generated from Java source file com.google.common.escape.Escapers

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Escapers:
    """
    Static utility methods pertaining to Escaper instances.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    @staticmethod
    def nullEscaper() -> "Escaper":
        """
        Returns an Escaper that does no escaping, passing all character data through unchanged.
        """
        ...


    @staticmethod
    def builder() -> "Builder":
        """
        Returns a builder for creating simple, fast escapers. A builder instance can be reused and each
        escaper that is created will be a snapshot of the current builder state. Builders are not
        thread safe.
        
        The initial state of the builder is such that:
        
        
          - There are no replacement mappings
          - `safeMin == Character.MIN_VALUE`
          - `safeMax == Character.MAX_VALUE`
          - `unsafeReplacement == null`
        
        
        For performance reasons escapers created by this builder are not Unicode aware and will not
        validate the well-formedness of their input.
        """
        ...


    @staticmethod
    def computeReplacement(escaper: "CharEscaper", c: str) -> str:
        """
        Returns a string that would replace the given character in the specified escaper, or `null` if no replacement should be made. This method is intended for use in tests through the
        `EscaperAsserts` class; production users of CharEscaper should limit themselves
        to its public interface.

        Arguments
        - c: the character to escape if necessary

        Returns
        - the replacement string, or `null` if no escaping was needed
        """
        ...


    @staticmethod
    def computeReplacement(escaper: "UnicodeEscaper", cp: int) -> str:
        """
        Returns a string that would replace the given character in the specified escaper, or `null` if no replacement should be made. This method is intended for use in tests through the
        `EscaperAsserts` class; production users of UnicodeEscaper should limit
        themselves to its public interface.

        Arguments
        - cp: the Unicode code point to escape if necessary

        Returns
        - the replacement string, or `null` if no escaping was needed
        """
        ...


    class Builder:
        """
        A builder for simple, fast escapers.
        
        Typically an escaper needs to deal with the escaping of high valued characters or code
        points. In these cases it is necessary to extend either ArrayBasedCharEscaper or ArrayBasedUnicodeEscaper to provide the desired behavior. However this builder is suitable for
        creating escapers that replace a relative small set of characters.

    Author(s)
        - David Beaumont

        Since
        - 15.0
        """

        def setSafeRange(self, safeMin: str, safeMax: str) -> "Builder":
            """
            Sets the safe range of characters for the escaper. Characters in this range that have no
            explicit replacement are considered 'safe' and remain unescaped in the output. If `safeMax < safeMin` then the safe range is empty.

            Arguments
            - safeMin: the lowest 'safe' character
            - safeMax: the highest 'safe' character

            Returns
            - the builder instance
            """
            ...


        def setUnsafeReplacement(self, unsafeReplacement: str) -> "Builder":
            """
            Sets the replacement string for any characters outside the 'safe' range that have no explicit
            replacement. If `unsafeReplacement` is `null` then no replacement will occur, if
            it is `""` then the unsafe characters are removed from the output.

            Arguments
            - unsafeReplacement: the string to replace unsafe characters

            Returns
            - the builder instance
            """
            ...


        def addEscape(self, c: str, replacement: str) -> "Builder":
            """
            Adds a replacement string for the given input character. The specified character will be
            replaced by the given string whenever it occurs in the input, irrespective of whether it lies
            inside or outside the 'safe' range.

            Arguments
            - c: the character to be replaced
            - replacement: the string to replace the given character

            Returns
            - the builder instance

            Raises
            - NullPointerException: if `replacement` is null
            """
            ...


        def build(self) -> "Escaper":
            """
            Returns a new escaper based on the current state of the builder.
            """
            ...
