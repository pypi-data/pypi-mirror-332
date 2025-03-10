"""
Python module generated from Java source file org.yaml.snakeyaml.external.com.google.gdata.util.common.base.UnicodeEscaper

Java source file obtained from artifact snakeyaml version 2.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from org.yaml.snakeyaml.external.com.google.gdata.util.common.base import *
from typing import Any, Callable, Iterable, Tuple


class UnicodeEscaper(Escaper):
    """
    An Escaper that converts literal text into a format safe for inclusion in a particular
    context (such as an XML document). Typically (but not always), the inverse process of
    "unescaping" the text is performed automatically by the relevant parser.
    
    
    For example, an XML escaper would convert the literal string `"Foo<Bar>"` into
    `"Foo&lt;Bar&gt;"` to prevent `"<Bar>"` from being confused with an XML tag. When the
    resulting XML document is parsed, the parser API will return this text as the original literal
    string `"Foo<Bar>"`.
    
    
    **Note:** This class is similar to CharEscaper but with one very important difference.
    A CharEscaper can only process Java <a href="http://en.wikipedia.org/wiki/UTF-16">UTF16</a>
    characters in isolation and may not cope when it encounters surrogate pairs. This class
    facilitates the correct escaping of all Unicode characters.
    
    
    As there are important reasons, including potential security issues, to handle Unicode correctly
    if you are considering implementing a new escaper you should favor using UnicodeEscaper wherever
    possible.
    
    
    A `UnicodeEscaper` instance is required to be stateless, and safe when used concurrently by
    multiple threads.
    
    
    Several popular escapers are defined as constants in the class CharEscapers. To create
    your own escapers extend this class and implement the .escape(int) method.
    """

    def escape(self, string: str) -> str:
        """
        Returns the escaped form of a given literal string.
        
        
        If you are escaping input in arbitrary successive chunks, then it is not generally safe to use
        this method. If an input string ends with an unmatched high surrogate character, then this
        method will throw IllegalArgumentException. You should either ensure your input is
        valid <a href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a> before calling this method or
        use an escaped Appendable (as returned by .escape(Appendable)) which can cope
        with arbitrarily split input.
        
        
        **Note:** When implementing an escaper it is a good idea to override this method for
        efficiency by inlining the implementation of .nextEscapeIndex(CharSequence, int, int)
        directly. Doing this for PercentEscaper more than doubled the performance for unescaped
        strings (as measured by CharEscapersBenchmark).

        Arguments
        - string: the literal string to be escaped

        Returns
        - the escaped form of `string`

        Raises
        - NullPointerException: if `string` is null
        - IllegalArgumentException: if invalid surrogate characters are encountered
        """
        ...


    def escape(self, out: "Appendable") -> "Appendable":
        """
        Returns an `Appendable` instance which automatically escapes all text appended to it
        before passing the resulting text to an underlying `Appendable`.
        
        
        Unlike .escape(String) it is permitted to append arbitrarily split input to this
        Appendable, including input that is split over a surrogate pair. In this case the pending high
        surrogate character will not be processed until the corresponding low surrogate is appended.
        This means that a trailing high surrogate character at the end of the input cannot be detected
        and will be silently ignored. This is unavoidable since the Appendable interface has no
        `close()` method, and it is impossible to determine when the last characters have been
        appended.
        
        
        The methods of the returned object will propagate any exceptions thrown by the underlying
        `Appendable`.
        
        
        For well formed <a href="http://en.wikipedia.org/wiki/UTF-16">UTF-16</a> the escaping behavior
        is identical to that of .escape(String) and the following code is equivalent to (but
        much slower than) `escaper.escape(string)`:
        
        ```
        {
          &#064;code
          StringBuilder sb = new StringBuilder();
          escaper.escape(sb).append(string);
          return sb.toString();
        }
        ```

        Arguments
        - out: the underlying `Appendable` to append escaped output to

        Returns
        - an `Appendable` which passes text to `out` after escaping it

        Raises
        - NullPointerException: if `out` is null
        - IllegalArgumentException: if invalid surrogate characters are encountered
        """
        ...
