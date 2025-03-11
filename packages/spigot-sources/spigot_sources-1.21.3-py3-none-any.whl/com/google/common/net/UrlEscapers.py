"""
Python module generated from Java source file com.google.common.net.UrlEscapers

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import Escaper
from com.google.common.net import *
from typing import Any, Callable, Iterable, Tuple


class UrlEscapers:
    """
    `Escaper` instances suitable for strings to be included in particular sections of URLs.
    
    If the resulting URLs are inserted into an HTML or XML document, they will require additional
    escaping with com.google.common.html.HtmlEscapers or com.google.common.xml.XmlEscapers.

    Author(s)
    - Chris Povirk

    Since
    - 15.0
    """

    @staticmethod
    def urlFormParameterEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes strings so they can be safely included in <a
        href="https://goo.gl/MplK6I">URL form parameter names and values</a>. Escaping is performed
        with the UTF-8 character encoding. The caller is responsible for <a
        href="https://goo.gl/9EfkM1">replacing any unpaired carriage return or line feed characters
        with a CR+LF pair</a> on any non-file inputs before escaping them with this escaper.
        
        When escaping a String, the following rules apply:
        
        
          - The alphanumeric characters "a" through "z", "A" through "Z" and "0" through "9" remain
              the same.
          - The special characters ".", "-", "*", and "_" remain the same.
          - The space character " " is converted into a plus sign "+".
          - All other characters are converted into one or more bytes using UTF-8 encoding and each
              byte is then represented by the 3-character string "%XY", where "XY" is the two-digit,
              uppercase, hexadecimal representation of the byte value.
        
        
        This escaper is suitable for escaping parameter names and values even when <a
        href="https://goo.gl/utn6M">using the non-standard semicolon</a>, rather than the ampersand, as
        a parameter delimiter. Nevertheless, we recommend using the ampersand unless you must
        interoperate with systems that require semicolons.
        
        **Note:** Unlike other escapers, URL escapers produce <a
        href="https://url.spec.whatwg.org/#percent-encode">uppercase</a> hexadecimal sequences.
        """
        ...


    @staticmethod
    def urlPathSegmentEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes strings so they can be safely included in <a
        href="https://goo.gl/m2MIf0">URL path segments</a>. The returned escaper escapes all non-ASCII
        characters, even though <a href="https://goo.gl/e7E0In">many of these are accepted in modern
        URLs</a>. (<a href="https://goo.gl/jfVxXW">If the escaper were to leave these characters
        unescaped, they would be escaped by the consumer at parse time, anyway.</a>) Additionally, the
        escaper escapes the slash character ("/"). While slashes are acceptable in URL paths, they are
        considered by the specification to be separators between "path segments." This implies that, if
        you wish for your path to contain slashes, you must escape each segment separately and then
        join them.
        
        When escaping a String, the following rules apply:
        
        
          - The alphanumeric characters "a" through "z", "A" through "Z" and "0" through "9" remain
              the same.
          - The unreserved characters ".", "-", "~", and "_" remain the same.
          - The general delimiters "@" and ":" remain the same.
          - The subdelimiters "!", "$", "&amp;", "'", "(", ")", "*", "+", ",", ";", and "=" remain
              the same.
          - The space character " " is converted into %20.
          - All other characters are converted into one or more bytes using UTF-8 encoding and each
              byte is then represented by the 3-character string "%XY", where "XY" is the two-digit,
              uppercase, hexadecimal representation of the byte value.
        
        
        **Note:** Unlike other escapers, URL escapers produce <a
        href="https://url.spec.whatwg.org/#percent-encode">uppercase</a> hexadecimal sequences.
        """
        ...


    @staticmethod
    def urlFragmentEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes strings so they can be safely included in a <a
        href="https://goo.gl/xXEq4p">URL fragment</a>. The returned escaper escapes all non-ASCII
        characters, even though <a href="https://goo.gl/e7E0In">many of these are accepted in modern
        URLs</a>.
        
        When escaping a String, the following rules apply:
        
        
          - The alphanumeric characters "a" through "z", "A" through "Z" and "0" through "9" remain
              the same.
          - The unreserved characters ".", "-", "~", and "_" remain the same.
          - The general delimiters "@" and ":" remain the same.
          - The subdelimiters "!", "$", "&amp;", "'", "(", ")", "*", "+", ",", ";", and "=" remain
              the same.
          - The space character " " is converted into %20.
          - Fragments allow unescaped "/" and "?", so they remain the same.
          - All other characters are converted into one or more bytes using UTF-8 encoding and each
              byte is then represented by the 3-character string "%XY", where "XY" is the two-digit,
              uppercase, hexadecimal representation of the byte value.
        
        
        **Note:** Unlike other escapers, URL escapers produce <a
        href="https://url.spec.whatwg.org/#percent-encode">uppercase</a> hexadecimal sequences.
        """
        ...
