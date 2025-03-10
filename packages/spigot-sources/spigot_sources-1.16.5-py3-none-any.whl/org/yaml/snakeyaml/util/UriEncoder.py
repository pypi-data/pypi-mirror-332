"""
Python module generated from Java source file org.yaml.snakeyaml.util.UriEncoder

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import UnsupportedEncodingException
from java.net import URLDecoder
from java.nio.charset import CharacterCodingException
from java.nio.charset import Charset
from java.nio.charset import CharsetDecoder
from java.nio.charset import CodingErrorAction
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.external.com.google.gdata.util.common.base import Escaper
from org.yaml.snakeyaml.external.com.google.gdata.util.common.base import PercentEscaper
from org.yaml.snakeyaml.util import *
from typing import Any, Callable, Iterable, Tuple


class UriEncoder:

    @staticmethod
    def encode(uri: str) -> str:
        """
        Escape special characters with '%'

        Arguments
        - uri: URI to be escaped

        Returns
        - encoded URI
        """
        ...


    @staticmethod
    def decode(buff: "ByteBuffer") -> str:
        """
        Decode '%'-escaped characters. Decoding fails in case of invalid UTF-8

        Arguments
        - buff: data to decode

        Returns
        - decoded data

        Raises
        - CharacterCodingException: if cannot be decoded
        """
        ...


    @staticmethod
    def decode(buff: str) -> str:
        ...
