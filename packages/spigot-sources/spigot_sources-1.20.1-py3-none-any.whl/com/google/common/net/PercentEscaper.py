"""
Python module generated from Java source file com.google.common.net.PercentEscaper

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import UnicodeEscaper
from com.google.common.net import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class PercentEscaper(UnicodeEscaper):
    """
    A `UnicodeEscaper` that escapes some set of Java characters using a UTF-8 based percent
    encoding scheme. The set of safe characters (those which remain unescaped) can be specified on
    construction.
    
    This class is primarily used for creating URI escapers in UrlEscapers but can be used
    directly if required. While URI escapers impose specific semantics on which characters are
    considered 'safe', this class has a minimal set of restrictions.
    
    When escaping a String, the following rules apply:
    
    
      - All specified safe characters remain unchanged.
      - If `plusForSpace` was specified, the space character " " is converted into a plus
          sign `"+"`.
      - All other characters are converted into one or more bytes using UTF-8 encoding and each
          byte is then represented by the 3-character string "%XX", where "XX" is the two-digit,
          uppercase, hexadecimal representation of the byte value.
    
    
    For performance reasons the only currently supported character encoding of this class is
    UTF-8.
    
    **Note:** This escaper produces <a
    href="https://url.spec.whatwg.org/#percent-encode">uppercase</a> hexadecimal sequences.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    def __init__(self, safeChars: str, plusForSpace: bool):
        """
        Constructs a percent escaper with the specified safe characters and optional handling of the
        space character.
        
        Not that it is allowed, but not necessarily desirable to specify `%` as a safe
        character. This has the effect of creating an escaper which has no well defined inverse but it
        can be useful when escaping additional characters.

        Arguments
        - safeChars: a non null string specifying additional safe characters for this escaper (the
            ranges 0..9, a..z and A..Z are always safe and should not be specified here)
        - plusForSpace: True if ASCII space should be escaped to `+` rather than `%20`

        Raises
        - IllegalArgumentException: if any of the parameters were invalid
        """
        ...


    def escape(self, s: str) -> str:
        ...
