"""
Python module generated from Java source file org.yaml.snakeyaml.external.biz.base64Coder.Base64Coder

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.external.biz.base64Coder import *
from typing import Any, Callable, Iterable, Tuple


class Base64Coder:
    """
    A Base64 encoder/decoder.
    
    
    This class is used to encode and decode data in Base64 format as described in RFC 1521.
    
    
    Project home page: <a href="http://www.source-code.biz/base64coder/java/">www.
    source-code.biz/base64coder/java</a>
    Author: Christian d'Heureuse, Inventec Informatik AG, Zurich, Switzerland
    Multi-licensed: EPL / LGPL / GPL / AL / BSD.
    """

    @staticmethod
    def encodeString(s: str) -> str:
        """
        Encodes a string into Base64 format. No blanks or line breaks are inserted.

        Arguments
        - s: A String to be encoded.

        Returns
        - A String containing the Base64 encoded data.
        """
        ...


    @staticmethod
    def encodeLines(in: list[int]) -> str:
        """
        Encodes a byte array into Base 64 format and breaks the output into lines of 76 characters.
        This method is compatible with `sun.misc.BASE64Encoder.encodeBuffer(byte[])`.

        Arguments
        - in: An array containing the data bytes to be encoded.

        Returns
        - A String containing the Base64 encoded data, broken into lines.
        """
        ...


    @staticmethod
    def encodeLines(in: list[int], iOff: int, iLen: int, lineLen: int, lineSeparator: str) -> str:
        """
        Encodes a byte array into Base 64 format and breaks the output into lines.

        Arguments
        - in: An array containing the data bytes to be encoded.
        - iOff: Offset of the first byte in `in` to be processed.
        - iLen: Number of bytes to be processed in `in`, starting at `iOff`.
        - lineLen: Line length for the output data. Should be a multiple of 4.
        - lineSeparator: The line separator to be used to separate the output lines.

        Returns
        - A String containing the Base64 encoded data, broken into lines.
        """
        ...


    @staticmethod
    def encode(in: list[int]) -> list[str]:
        """
        Encodes a byte array into Base64 format. No blanks or line breaks are inserted in the output.

        Arguments
        - in: An array containing the data bytes to be encoded.

        Returns
        - A character array containing the Base64 encoded data.
        """
        ...


    @staticmethod
    def encode(in: list[int], iLen: int) -> list[str]:
        """
        Encodes a byte array into Base64 format. No blanks or line breaks are inserted in the output.

        Arguments
        - in: An array containing the data bytes to be encoded.
        - iLen: Number of bytes to process in `in`.

        Returns
        - A character array containing the Base64 encoded data.
        """
        ...


    @staticmethod
    def encode(in: list[int], iOff: int, iLen: int) -> list[str]:
        """
        Encodes a byte array into Base64 format. No blanks or line breaks are inserted in the output.

        Arguments
        - in: An array containing the data bytes to be encoded.
        - iOff: Offset of the first byte in `in` to be processed.
        - iLen: Number of bytes to process in `in`, starting at `iOff`.

        Returns
        - A character array containing the Base64 encoded data.
        """
        ...


    @staticmethod
    def decodeString(s: str) -> str:
        """
        Decodes a string from Base64 format. No blanks or line breaks are allowed within the Base64
        encoded input data.

        Arguments
        - s: A Base64 String to be decoded.

        Returns
        - A String containing the decoded data.

        Raises
        - IllegalArgumentException: If the input is not valid Base64 encoded data.
        """
        ...


    @staticmethod
    def decodeLines(s: str) -> list[int]:
        """
        Decodes a byte array from Base64 format and ignores line separators, tabs and blanks. CR, LF,
        Tab and Space characters are ignored in the input data. This method is compatible with
        `sun.misc.BASE64Decoder.decodeBuffer(String)`.

        Arguments
        - s: A Base64 String to be decoded.

        Returns
        - An array containing the decoded data bytes.

        Raises
        - IllegalArgumentException: If the input is not valid Base64 encoded data.
        """
        ...


    @staticmethod
    def decode(s: str) -> list[int]:
        """
        Decodes a byte array from Base64 format. No blanks or line breaks are allowed within the Base64
        encoded input data.

        Arguments
        - s: A Base64 String to be decoded.

        Returns
        - An array containing the decoded data bytes.

        Raises
        - IllegalArgumentException: If the input is not valid Base64 encoded data.
        """
        ...


    @staticmethod
    def decode(in: list[str]) -> list[int]:
        """
        Decodes a byte array from Base64 format. No blanks or line breaks are allowed within the Base64
        encoded input data.

        Arguments
        - in: A character array containing the Base64 encoded data.

        Returns
        - An array containing the decoded data bytes.

        Raises
        - IllegalArgumentException: If the input is not valid Base64 encoded data.
        """
        ...


    @staticmethod
    def decode(in: list[str], iOff: int, iLen: int) -> list[int]:
        """
        Decodes a byte array from Base64 format. No blanks or line breaks are allowed within the Base64
        encoded input data.

        Arguments
        - in: A character array containing the Base64 encoded data.
        - iOff: Offset of the first character in `in` to be processed.
        - iLen: Number of characters to process in `in`, starting at `iOff`.

        Returns
        - An array containing the decoded data bytes.

        Raises
        - IllegalArgumentException: If the input is not valid Base64 encoded data.
        """
        ...
