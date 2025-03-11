"""
Python module generated from Java source file org.yaml.snakeyaml.internal.Logger

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from org.yaml.snakeyaml.internal import *
from typing import Any, Callable, Iterable, Tuple


class Logger:

    @staticmethod
    def getLogger(name: str) -> "Logger":
        ...


    def isLoggable(self, level: "Level") -> bool:
        ...


    def warn(self, msg: str) -> None:
        ...


    class Level(Enum):

        WARNING = (java.util.logging.Level.FINE)
