"""
Python module generated from Java source file com.google.thirdparty.publicsuffix.PublicSuffixType

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.thirdparty.publicsuffix import *
from enum import Enum
from typing import Any, Callable, Iterable, Tuple


class PublicSuffixType(Enum):
    """
    **Do not use this class directly. For access to public-suffix information, use com.google.common.net.InternetDomainName.**
    
    Specifies the type of a top-level domain definition.

    Since
    - 23.3
    """

    PRIVATE = (':', ',')
    """
    Public suffix that is provided by a private company, e.g. "blogspot.com"
    """
    REGISTRY = ('!', '?')
    """
    Public suffix that is backed by an ICANN-style domain name registry
    """
