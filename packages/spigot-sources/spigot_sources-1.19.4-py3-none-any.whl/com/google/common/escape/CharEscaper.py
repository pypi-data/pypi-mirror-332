"""
Python module generated from Java source file com.google.common.escape.CharEscaper

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class CharEscaper(Escaper):
    """
    An object that converts literal text into a format safe for inclusion in a particular context
    (such as an XML document). Typically (but not always), the inverse process of "unescaping" the
    text is performed automatically by the relevant parser.
    
    For example, an XML escaper would convert the literal string `"Foo<Bar>"` into `"Foo&lt;Bar&gt;"` to prevent `"<Bar>"` from being confused with an XML tag. When the
    resulting XML document is parsed, the parser API will return this text as the original literal
    string `"Foo<Bar>"`.
    
    A `CharEscaper` instance is required to be stateless, and safe when used concurrently by
    multiple threads.
    
    Popular escapers are defined as constants in classes like com.google.common.html.HtmlEscapers and com.google.common.xml.XmlEscapers. To create
    your own escapers extend this class and implement the .escape(char) method.

    Author(s)
    - Sven Mawson

    Since
    - 15.0
    """

    def escape(self, string: str) -> str:
        """
        Returns the escaped form of a given literal string.

        Arguments
        - string: the literal string to be escaped

        Returns
        - the escaped form of `string`

        Raises
        - NullPointerException: if `string` is null
        """
        ...
