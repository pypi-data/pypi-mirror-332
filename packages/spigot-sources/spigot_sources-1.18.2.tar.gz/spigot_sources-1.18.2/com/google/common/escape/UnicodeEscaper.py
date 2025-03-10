"""
Python module generated from Java source file com.google.common.escape.UnicodeEscaper

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import *
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class UnicodeEscaper(Escaper):
    """
    An Escaper that converts literal text into a format safe for inclusion in a particular
    context (such as an XML document). Typically (but not always), the inverse process of
    "unescaping" the text is performed automatically by the relevant parser.
    
    For example, an XML escaper would convert the literal string `"Foo<Bar>"` into `"Foo&lt;Bar&gt;"` to prevent `"<Bar>"` from being confused with an XML tag. When the
    resulting XML document is parsed, the parser API will return this text as the original literal
    string `"Foo<Bar>"`.
    
    **Note:** This class is similar to CharEscaper but with one very important
    difference. A CharEscaper can only process Java <a
    href="http://en.wikipedia.org/wiki/UTF-16">UTF16</a> characters in isolation and may not cope
    when it encounters surrogate pairs. This class facilitates the correct escaping of all Unicode
    characters.
    
    As there are important reasons, including potential security issues, to handle Unicode
    correctly if you are considering implementing a new escaper you should favor using UnicodeEscaper
    wherever possible.
    
    A `UnicodeEscaper` instance is required to be stateless, and safe when used concurrently
    by multiple threads.
    
    Popular escapers are defined as constants in classes like com.google.common.html.HtmlEscapers and com.google.common.xml.XmlEscapers. To create
    your own escapers extend this class and implement the .escape(int) method.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    def escape(self, string: str) -> str:
        """
        Returns the escaped form of a given literal string.
        
        If you are escaping input in arbitrary successive chunks, then it is not generally safe to
        use this method. If an input string ends with an unmatched high surrogate character, then this
        method will throw IllegalArgumentException. You should ensure your input is valid <a
        href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a> before calling this method.
        
        **Note:** When implementing an escaper it is a good idea to override this method for
        efficiency by inlining the implementation of .nextEscapeIndex(CharSequence, int, int)
        directly. Doing this for com.google.common.net.PercentEscaper more than doubled the
        performance for unescaped strings (as measured by `CharEscapersBenchmark`).

        Arguments
        - string: the literal string to be escaped

        Returns
        - the escaped form of `string`

        Raises
        - NullPointerException: if `string` is null
        - IllegalArgumentException: if invalid surrogate characters are encountered
        """
        ...
