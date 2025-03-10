"""
Python module generated from Java source file com.google.common.base.Strings

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from com.google.errorprone.annotations import InlineMe
from com.google.errorprone.annotations import InlineMeValidationDisabled
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Strings:
    """
    Static utility methods pertaining to `String` or `CharSequence` instances.

    Author(s)
    - Kevin Bourrillion

    Since
    - 3.0
    """

    @staticmethod
    def nullToEmpty(string: str) -> str:
        """
        Returns the given string if it is non-null; the empty string otherwise.

        Arguments
        - string: the string to test and possibly return

        Returns
        - `string` itself if it is non-null; `""` if it is null
        """
        ...


    @staticmethod
    def emptyToNull(string: str) -> str:
        """
        Returns the given string if it is nonempty; `null` otherwise.

        Arguments
        - string: the string to test and possibly return

        Returns
        - `string` itself if it is nonempty; `null` if it is empty or null
        """
        ...


    @staticmethod
    def isNullOrEmpty(string: str) -> bool:
        """
        Returns `True` if the given string is null or is the empty string.
        
        Consider normalizing your string references with .nullToEmpty. If you do, you can
        use String.isEmpty() instead of this method, and you won't need special null-safe forms
        of methods like String.toUpperCase either. Or, if you'd like to normalize "in the other
        direction," converting empty strings to `null`, you can use .emptyToNull.

        Arguments
        - string: a string reference to check

        Returns
        - `True` if the string is null or is the empty string
        """
        ...


    @staticmethod
    def padStart(string: str, minLength: int, padChar: str) -> str:
        """
        Returns a string, of length at least `minLength`, consisting of `string` prepended
        with as many copies of `padChar` as are necessary to reach that length. For example,
        
        
          - `padStart("7", 3, '0')` returns `"007"`
          - `padStart("2010", 3, '0')` returns `"2010"`
        
        
        See java.util.Formatter for a richer set of formatting capabilities.

        Arguments
        - string: the string which should appear at the end of the result
        - minLength: the minimum length the resulting string must have. Can be zero or negative, in
            which case the input string is always returned.
        - padChar: the character to insert at the beginning of the result until the minimum length
            is reached

        Returns
        - the padded string
        """
        ...


    @staticmethod
    def padEnd(string: str, minLength: int, padChar: str) -> str:
        """
        Returns a string, of length at least `minLength`, consisting of `string` appended
        with as many copies of `padChar` as are necessary to reach that length. For example,
        
        
          - `padEnd("4.", 5, '0')` returns `"4.000"`
          - `padEnd("2010", 3, '!')` returns `"2010"`
        
        
        See java.util.Formatter for a richer set of formatting capabilities.

        Arguments
        - string: the string which should appear at the beginning of the result
        - minLength: the minimum length the resulting string must have. Can be zero or negative, in
            which case the input string is always returned.
        - padChar: the character to append to the end of the result until the minimum length is
            reached

        Returns
        - the padded string
        """
        ...


    @staticmethod
    def repeat(string: str, count: int) -> str:
        """
        Returns a string consisting of a specific number of concatenated copies of an input string. For
        example, `repeat("hey", 3)` returns the string `"heyheyhey"`.
        
        **Java 11+ users:** use `string.repeat(count)` instead.

        Arguments
        - string: any non-null string
        - count: the number of times to repeat it; a nonnegative integer

        Returns
        - a string containing `string` repeated `count` times (the empty string if
            `count` is zero)

        Raises
        - IllegalArgumentException: if `count` is negative
        """
        ...


    @staticmethod
    def commonPrefix(a: "CharSequence", b: "CharSequence") -> str:
        """
        Returns the longest string `prefix` such that `a.toString().startsWith(prefix) &&
        b.toString().startsWith(prefix)`, taking care not to split surrogate pairs. If `a` and
        `b` have no common prefix, returns the empty string.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def commonSuffix(a: "CharSequence", b: "CharSequence") -> str:
        """
        Returns the longest string `suffix` such that `a.toString().endsWith(suffix) &&
        b.toString().endsWith(suffix)`, taking care not to split surrogate pairs. If `a` and
        `b` have no common suffix, returns the empty string.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def lenientFormat(template: str, *args: Tuple["Object", ...]) -> str:
        ...
