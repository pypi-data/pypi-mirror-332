"""
Python module generated from Java source file java.nio.file.LinkOption

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.nio.file import *
from typing import Any, Callable, Iterable, Tuple


class LinkOption(Enum):

    NOFOLLOW_LINKS = 0
    """
    Do not follow symbolic links.

    See
    - SecureDirectoryStream.newByteChannel
    """
