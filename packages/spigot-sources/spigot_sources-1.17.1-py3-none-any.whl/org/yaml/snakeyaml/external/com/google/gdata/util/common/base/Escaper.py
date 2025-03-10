"""
Python module generated from Java source file org.yaml.snakeyaml.external.com.google.gdata.util.common.base.Escaper

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.external.com.google.gdata.util.common.base import *
from typing import Any, Callable, Iterable, Tuple


class Escaper:
    """
    An object that converts literal text into a format safe for inclusion in a
    particular context (such as an XML document). Typically (but not always), the
    inverse process of "unescaping" the text is performed automatically by the
    relevant parser.
    
    
    For example, an XML escaper would convert the literal string
    `"Foo<Bar>"` into `"Foo&lt;Bar&gt;"` to prevent `"<Bar>"`
    from being confused with an XML tag. When the resulting XML document is
    parsed, the parser API will return this text as the original literal string
    `"Foo<Bar>"`.
    
    
    An `Escaper` instance is required to be stateless, and safe when used
    concurrently by multiple threads.
    
    
    Several popular escapers are defined as constants in the class
    CharEscapers. To create your own escapers, use
    CharEscaperBuilder, or extend CharEscaper or
    `UnicodeEscaper`.
    """

    def escape(self, string: str) -> str:
        """
        Returns the escaped form of a given literal string.
        
        
        Note that this method may treat input characters differently depending on
        the specific escaper implementation.
        
        - UnicodeEscaper handles <a
        href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a> correctly,
        including surrogate character pairs. If the input is badly formed the
        escaper should throw IllegalArgumentException.
        - CharEscaper handles Java characters independently and does
        not verify the input for well formed characters. A CharEscaper should not
        be used in situations where input is not guaranteed to be restricted to
        the Basic Multilingual Plane (BMP).

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


    def escape(self, out: "Appendable") -> "Appendable":
        """
        Returns an `Appendable` instance which automatically escapes all
        text appended to it before passing the resulting text to an underlying
        `Appendable`.
        
        
        Note that this method may treat input characters differently depending on
        the specific escaper implementation.
        
        - UnicodeEscaper handles <a
        href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a> correctly,
        including surrogate character pairs. If the input is badly formed the
        escaper should throw IllegalArgumentException.
        - CharEscaper handles Java characters independently and does
        not verify the input for well formed characters. A CharEscaper should not
        be used in situations where input is not guaranteed to be restricted to
        the Basic Multilingual Plane (BMP).

        Arguments
        - out: the underlying `Appendable` to append escaped output to

        Returns
        - an `Appendable` which passes text to `out` after
                escaping it.
        """
        ...
