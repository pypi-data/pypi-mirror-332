"""
Python module generated from Java source file org.bukkit.util.StringUtil

Java source file obtained from artifact spigot-api version 1.21-R0.1-20240807.214924-87

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.base import Preconditions
from org.bukkit.util import *
from typing import Any, Callable, Iterable, Tuple


class StringUtil:

    @staticmethod
    def copyPartialMatches(token: str, originals: Iterable[str], collection: "T") -> "T":
        """
        Copies all elements from the iterable collection of originals to the
        collection provided.
        
        Type `<T>`: the collection of strings

        Arguments
        - token: String to search for
        - originals: An iterable collection of strings to filter.
        - collection: The collection to add matches to

        Returns
        - the collection provided that would have the elements copied
            into

        Raises
        - UnsupportedOperationException: if the collection is immutable
            and originals contains a string which starts with the specified
            search string.
        - IllegalArgumentException: if any parameter is is null
        - IllegalArgumentException: if originals contains a null element.
            **Note: the collection may be modified before this is thrown**
        """
        ...


    @staticmethod
    def startsWithIgnoreCase(string: str, prefix: str) -> bool:
        """
        This method uses a region to check case-insensitive equality. This
        means the internal array does not need to be copied like a
        toLowerCase() call would.

        Arguments
        - string: String to check
        - prefix: Prefix of string to compare

        Returns
        - True if provided string starts with, ignoring case, the prefix
            provided

        Raises
        - NullPointerException: if prefix is null
        - IllegalArgumentException: if string is null
        """
        ...
