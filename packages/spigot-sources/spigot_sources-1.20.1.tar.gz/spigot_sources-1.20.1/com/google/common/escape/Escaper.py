"""
Python module generated from Java source file com.google.common.escape.Escaper

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Function
from com.google.common.escape import *
from com.google.errorprone.annotations import DoNotMock
from typing import Any, Callable, Iterable, Tuple


class Escaper:
    """
    An object that converts literal text into a format safe for inclusion in a particular context
    (such as an XML document). Typically (but not always), the inverse process of "unescaping" the
    text is performed automatically by the relevant parser.
    
    For example, an XML escaper would convert the literal string `"Foo<Bar>"` into `"Foo&lt;Bar&gt;"` to prevent `"<Bar>"` from being confused with an XML tag. When the
    resulting XML document is parsed, the parser API will return this text as the original literal
    string `"Foo<Bar>"`.
    
    An `Escaper` instance is required to be stateless, and safe when used concurrently by
    multiple threads.
    
    Because, in general, escaping operates on the code points of a string and not on its
    individual `char` values, it is not safe to assume that `escape(s)` is equivalent to
    `escape(s.substring(0, n)) + escape(s.substring(n))` for arbitrary `n`. This is
    because of the possibility of splitting a surrogate pair. The only case in which it is safe to
    escape strings and concatenate the results is if you can rule out this possibility, either by
    splitting an existing long string into short strings adaptively around Character.isHighSurrogate surrogate Character.isLowSurrogate pairs, or by starting
    with short strings already known to be free of unpaired surrogates.
    
    The two primary implementations of this interface are CharEscaper and UnicodeEscaper. They are heavily optimized for performance and greatly simplify the task of
    implementing new escapers. It is strongly recommended that when implementing a new escaper you
    extend one of these classes. If you find that you are unable to achieve the desired behavior
    using either of these classes, please contact the Java libraries team for advice.
    
    Popular escapers are defined as constants in classes like com.google.common.html.HtmlEscapers and com.google.common.xml.XmlEscapers. To create
    your own escapers, use CharEscaperBuilder, or extend `CharEscaper` or `UnicodeEscaper`.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    def escape(self, string: str) -> str:
        """
        Returns the escaped form of a given literal string.
        
        Note that this method may treat input characters differently depending on the specific
        escaper implementation.
        
        
          - UnicodeEscaper handles <a href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a>
              correctly, including surrogate character pairs. If the input is badly formed the escaper
              should throw IllegalArgumentException.
          - CharEscaper handles Java characters independently and does not verify the input
              for well formed characters. A `CharEscaper` should not be used in situations where
              input is not guaranteed to be restricted to the Basic Multilingual Plane (BMP).

        Arguments
        - string: the literal string to be escaped

        Returns
        - the escaped form of `string`

        Raises
        - NullPointerException: if `string` is null
        - IllegalArgumentException: if `string` contains badly formed UTF-16 or cannot be
            escaped for any other reason
        """
        ...


    def asFunction(self) -> "Function"[str, str]:
        """
        Returns a Function that invokes .escape(String) on this escaper.
        """
        ...
