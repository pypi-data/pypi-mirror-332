"""
Python module generated from Java source file org.yaml.snakeyaml.reader.UnicodeReader

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.io import InputStreamReader
from java.io import PushbackInputStream
from java.io import Reader
from java.nio.charset import Charset
from java.nio.charset import CharsetDecoder
from java.nio.charset import CodingErrorAction
from org.yaml.snakeyaml.reader import *
from typing import Any, Callable, Iterable, Tuple


class UnicodeReader(Reader):
    """
    Generic unicode textreader, which will use BOM mark to identify the encoding
    to be used. If BOM is not found then use a given default or system encoding.
    """

    def __init__(self, in: "InputStream"):
        """
        Arguments
        - in: InputStream to be read
        """
        ...


    def getEncoding(self) -> str:
        """
        Get stream encoding or NULL if stream is uninitialized. Call init() or
        read() method to initialize it.

        Returns
        - the name of the character encoding being used by this stream.
        """
        ...


    def close(self) -> None:
        ...


    def read(self, cbuf: list[str], off: int, len: int) -> int:
        ...
