"""
Python module generated from Java source file java.net.URLEncoder

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import CharArrayWriter
from java.io import UnsupportedEncodingException
from java.net import *
from java.nio.charset import Charset
from java.nio.charset import IllegalCharsetNameException
from java.nio.charset import UnsupportedCharsetException
from java.util import BitSet
from java.util import Objects
from sun.security.action import GetPropertyAction
from typing import Any, Callable, Iterable, Tuple


class URLEncoder:
    """
    Utility class for HTML form encoding. This class contains static methods
    for converting a String to the <CODE>application/x-www-form-urlencoded</CODE> MIME
    format. For more information about HTML form encoding, consult the HTML
    <A HREF="http://www.w3.org/TR/html4/">specification</A>.
    
    
    When encoding a String, the following rules apply:
    
    
    - The alphanumeric characters &quot;`a`&quot; through
        &quot;`z`&quot;, &quot;`A`&quot; through
        &quot;`Z`&quot; and &quot;`0`&quot;
        through &quot;`9`&quot; remain the same.
    - The special characters &quot;`.`&quot;,
        &quot;`-`&quot;, &quot;`*`&quot;, and
        &quot;`_`&quot; remain the same.
    - The space character &quot; &nbsp; &quot; is
        converted into a plus sign &quot;`+`&quot;.
    - All other characters are unsafe and are first converted into
        one or more bytes using some encoding scheme. Then each byte is
        represented by the 3-character string
        &quot;*`%xy`*&quot;, where *xy* is the
        two-digit hexadecimal representation of the byte.
        The recommended encoding scheme to use is UTF-8. However,
        for compatibility reasons, if an encoding is not specified,
        then the default encoding of the platform is used.
    
    
    
    For example using UTF-8 as the encoding scheme the string &quot;The
    string &#252;@foo-bar&quot; would get converted to
    &quot;The+string+%C3%BC%40foo-bar&quot; because in UTF-8 the character
    &#252; is encoded as two bytes C3 (hex) and BC (hex), and the
    character @ is encoded as one byte 40 (hex).

    Author(s)
    - Herb Jellinek

    Since
    - 1.0
    """

    @staticmethod
    def encode(s: str) -> str:
        """
        Translates a string into `x-www-form-urlencoded`
        format. This method uses the platform's default encoding
        as the encoding scheme to obtain the bytes for unsafe characters.

        Arguments
        - s: `String` to be translated.

        Returns
        - the translated `String`.

        Deprecated
        - The resulting string may vary depending on the platform's
                    default encoding. Instead, use the encode(String,String)
                    method to specify the encoding.
        """
        ...


    @staticmethod
    def encode(s: str, enc: str) -> str:
        """
        Translates a string into `application/x-www-form-urlencoded`
        format using a specific encoding scheme.
        
        This method behaves the same as .encode(String s, Charset charset)
        except that it will java.nio.charset.Charset.forName look up the charset
        using the given encoding name.

        Arguments
        - s: `String` to be translated.
        - enc: The name of a supported
           <a href="../lang/package-summary.html#charenc">character
           encoding</a>.

        Returns
        - the translated `String`.

        Raises
        - UnsupportedEncodingException: If the named encoding is not supported

        See
        - URLDecoder.decode(java.lang.String, java.lang.String)

        Since
        - 1.4
        """
        ...


    @staticmethod
    def encode(s: str, charset: "Charset") -> str:
        """
        Translates a string into `application/x-www-form-urlencoded`
        format using a specific java.nio.charset.Charset Charset.
        This method uses the supplied charset to obtain the bytes for unsafe
        characters.
        
        *<strong>Note:</strong> The <a href=
        "http://www.w3.org/TR/html40/appendix/notes.html#non-ascii-chars">
        World Wide Web Consortium Recommendation</a> states that
        UTF-8 should be used. Not doing so may introduce incompatibilities.*

        Arguments
        - s: `String` to be translated.
        - charset: the given charset

        Returns
        - the translated `String`.

        Raises
        - NullPointerException: if `s` or `charset` is `null`.

        See
        - URLDecoder.decode(java.lang.String, java.nio.charset.Charset)

        Since
        - 10
        """
        ...
