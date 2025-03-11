"""
Python module generated from Java source file com.google.gson.FormattingStyle

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.stream import JsonWriter
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class FormattingStyle:
    """
    A class used to control what the serialization output looks like.
    
    It currently has the following configuration methods, but more methods might be added in the
    future:
    
    
      - .withNewline(String)
      - .withIndent(String)
      - .withSpaceAfterSeparators(boolean)

    See
    - <a href="https://en.wikipedia.org/wiki/Newline">Wikipedia Newline article</a>

    Since
    - 2.11.0
    """

    COMPACT = FormattingStyle("", "", false)
    """
    The default compact formatting style:
    
    
      - no newline
      - no indent
      - no space after `','` and `':'`
    """
    PRETTY = FormattingStyle("\n", "  ", true)
    """
    The default pretty printing formatting style:
    
    
      - `"\n"` as newline
      - two spaces as indent
      - a space between `':'` and the subsequent value
    """


    def withNewline(self, newline: str) -> "FormattingStyle":
        """
        Creates a FormattingStyle with the specified newline setting.
        
        It can be used to accommodate certain OS convention, for example hardcode `"\n"` for
        Linux and macOS, `"\r\n"` for Windows, or call java.lang.System.lineSeparator()
        to match the current OS.
        
        Only combinations of `\n` and `\r` are allowed.

        Arguments
        - newline: the string value that will be used as newline.

        Returns
        - a newly created FormattingStyle
        """
        ...


    def withIndent(self, indent: str) -> "FormattingStyle":
        """
        Creates a FormattingStyle with the specified indent string.
        
        Only combinations of spaces and tabs allowed in indent.

        Arguments
        - indent: the string value that will be used as indent.

        Returns
        - a newly created FormattingStyle
        """
        ...


    def withSpaceAfterSeparators(self, spaceAfterSeparators: bool) -> "FormattingStyle":
        """
        Creates a FormattingStyle which either uses a space after the separators `','`
        and `':'` in the JSON output, or not.
        
        This setting has no effect on the .withNewline(String) configured newline. If a
        non-empty newline is configured, it will always be added after `','` and no space is
        added after the `','` in that case.

        Arguments
        - spaceAfterSeparators: whether to output a space after `','` and `':'`.

        Returns
        - a newly created FormattingStyle
        """
        ...


    def getNewline(self) -> str:
        """
        Returns the string value that will be used as a newline.

        Returns
        - the newline value.
        """
        ...


    def getIndent(self) -> str:
        """
        Returns the string value that will be used as indent.

        Returns
        - the indent value.
        """
        ...


    def usesSpaceAfterSeparators(self) -> bool:
        """
        Returns whether a space will be used after `','` and `':'`.
        """
        ...
