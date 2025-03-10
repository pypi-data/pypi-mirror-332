"""
Python module generated from Java source file org.yaml.snakeyaml.scanner.Constant

Java source file obtained from artifact snakeyaml version 1.30

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Arrays
from org.yaml.snakeyaml.scanner import *
from typing import Any, Callable, Iterable, Tuple


class Constant:

    LINEBR = Constant(LINEBR_S)
    NULL_OR_LINEBR = Constant(NULL_OR_LINEBR_S)
    NULL_BL_LINEBR = Constant(NULL_BL_LINEBR_S)
    NULL_BL_T_LINEBR = Constant(NULL_BL_T_LINEBR_S)
    NULL_BL_T = Constant(NULL_BL_T_S)
    URI_CHARS = Constant(URI_CHARS_S)
    ALPHA = Constant(ALPHA_S)


    def has(self, c: int) -> bool:
        ...


    def hasNo(self, c: int) -> bool:
        ...


    def has(self, c: int, additional: str) -> bool:
        ...


    def hasNo(self, c: int, additional: str) -> bool:
        ...
