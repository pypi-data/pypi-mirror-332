"""
Python module generated from Java source file org.yaml.snakeyaml.parser.Production

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.parser import *
from typing import Any, Callable, Iterable, Tuple


class Production:
    """
    Helper for ParserImpl. A grammar rule to apply given the symbols on top of its stack and
    the next input token

    See
    - <a href="http://en.wikipedia.org/wiki/LL_parser">LL parser</a>
    """

    def produce(self) -> "Event":
        ...
