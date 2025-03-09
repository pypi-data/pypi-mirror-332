"""
Python module generated from Java source file java.net.URLDecoder

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.net import *
from java.nio.charset import Charset
from java.nio.charset import IllegalCharsetNameException
from java.nio.charset import UnsupportedCharsetException
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class URLDecoder:

    @staticmethod
    def decode(s: str) -> str:
        """
        Decodes a `x-www-form-urlencoded` string.
        The platform's default encoding is used to determine what characters
        are represented by any consecutive sequences of the form
        "*`%xy`*".

        Arguments
        - s: the `String` to decode

        Returns
        - the newly decoded `String`

        Deprecated
        - The resulting string may vary depending on the platform's
                 default encoding. Instead, use the decode(String,String) method
                 to specify the encoding.
        """
        ...


    @staticmethod
    def decode(s: str, enc: str) -> str:
        """
        Decodes an `application/x-www-form-urlencoded` string using
        a specific encoding scheme.
        
        
        This method behaves the same as decode(String s, Charset charset)
        except that it will java.nio.charset.Charset.forName look up the charset
        using the given encoding name.

        Arguments
        - s: the `String` to decode
        - enc: The name of a supported
           <a href="../lang/package-summary.html#charenc">character
           encoding</a>.

        Returns
        - the newly decoded `String`

        Raises
        - UnsupportedEncodingException: If character encoding needs to be consulted, but
                    named character encoding is not supported

        See
        - URLEncoder.encode(java.lang.String, java.lang.String)

        Since
        - 1.4

        Unknown Tags
        - This implementation will throw an java.lang.IllegalArgumentException
        when illegal strings are encountered.
        """
        ...


    @staticmethod
    def decode(s: str, charset: "Charset") -> str:
        """
        Decodes an `application/x-www-form-urlencoded` string using
        a specific java.nio.charset.Charset Charset.
        The supplied charset is used to determine
        what characters are represented by any consecutive sequences of the
        form "*`%xy`*".
        
        *<strong>Note:</strong> The <a href=
        "http://www.w3.org/TR/html40/appendix/notes.html#non-ascii-chars">
        World Wide Web Consortium Recommendation</a> states that
        UTF-8 should be used. Not doing so may introduce
        incompatibilities.*

        Arguments
        - s: the `String` to decode
        - charset: the given charset

        Returns
        - the newly decoded `String`

        Raises
        - NullPointerException: if `s` or `charset` is `null`
        - IllegalArgumentException: if the implementation encounters illegal
        characters

        See
        - URLEncoder.encode(java.lang.String, java.nio.charset.Charset)

        Since
        - 10

        Unknown Tags
        - This implementation will throw an java.lang.IllegalArgumentException
        when illegal strings are encountered.
        """
        ...
