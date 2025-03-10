"""
Python module generated from Java source file org.yaml.snakeyaml.external.com.google.gdata.util.common.base.PercentEscaper

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.external.com.google.gdata.util.common.base import *
from typing import Any, Callable, Iterable, Tuple


class PercentEscaper(UnicodeEscaper):
    """
    A `UnicodeEscaper` that escapes some set of Java characters using the
    URI percent encoding scheme. The set of safe characters (those which remain
    unescaped) can be specified on construction.
    
    
    For details on escaping URIs for use in web pages, see section 2.4 of <a
    href="http://www.ietf.org/rfc/rfc3986.txt">RFC 3986</a>.
    
    
    In most cases this class should not need to be used directly. If you have no
    special requirements for escaping your URIs, you should use either
    CharEscapers.uriEscaper() or CharEscapers.uriEscaper(boolean).
    
    
    When encoding a String, the following rules apply:
    
    - The alphanumeric characters "a" through "z", "A" through "Z" and "0"
    through "9" remain the same.
    - Any additionally specified safe characters remain the same.
    - If `plusForSpace` was specified, the space character " " is
    converted into a plus sign "+".
    - All other characters are converted into one or more bytes using UTF-8
    encoding and each byte is then represented by the 3-character string "%XY",
    where "XY" is the two-digit, uppercase, hexadecimal representation of the
    byte value.
    
    
    
    RFC 2396 specifies the set of unreserved characters as "-", "_", ".", "!",
    "~", "*", "'", "(" and ")". It goes on to state:
    
    
    *Unreserved characters can be escaped without changing the semantics of the
    URI, but this should not be done unless the URI is being used in a context
    that does not allow the unescaped character to appear.*
    
    
    For performance reasons the only currently supported character encoding of
    this class is UTF-8.
    
    
    **Note**: This escaper produces uppercase hexidecimal sequences. From <a
    href="http://www.ietf.org/rfc/rfc3986.txt">RFC 3986</a>:
    *"URI producers and normalizers should use uppercase hexadecimal digits for
    all percent-encodings."*
    """

    SAFECHARS_URLENCODER = "-_.*"
    """
    A string of safe characters that mimics the behavior of
    java.net.URLEncoder.
    """
    SAFEPATHCHARS_URLENCODER = "-_.!~*'()@:$&,;="
    """
    A string of characters that do not need to be encoded when used in URI
    path segments, as specified in RFC 3986. Note that some of these
    characters do need to be escaped when used in other parts of the URI.
    """
    SAFEQUERYSTRINGCHARS_URLENCODER = "-_.!~*'()@:$,;/?:"
    """
    A string of characters that do not need to be encoded when used in URI
    query strings, as specified in RFC 3986. Note that some of these
    characters do need to be escaped when used in other parts of the URI.
    """


    def __init__(self, safeChars: str, plusForSpace: bool):
        """
        Constructs a URI escaper with the specified safe characters and optional
        handling of the space character.

        Arguments
        - safeChars: a non null string specifying additional safe characters for
                   this escaper (the ranges 0..9, a..z and A..Z are always safe
                   and should not be specified here)
        - plusForSpace: True if ASCII space should be escaped to `+` rather than
                   `%20`

        Raises
        - IllegalArgumentException: if any of the parameters were invalid
        """
        ...


    def escape(self, s: str) -> str:
        ...
