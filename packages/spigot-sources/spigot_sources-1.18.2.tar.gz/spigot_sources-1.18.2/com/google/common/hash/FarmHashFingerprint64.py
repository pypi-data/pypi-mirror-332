"""
Python module generated from Java source file com.google.common.hash.FarmHashFingerprint64

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import VisibleForTesting
from com.google.common.hash import *
from typing import Any, Callable, Iterable, Tuple


class FarmHashFingerprint64(AbstractNonStreamingHashFunction):
    """
    Implementation of FarmHash Fingerprint64, an open-source fingerprinting algorithm for strings.
    
    Its speed is comparable to CityHash64, and its quality of hashing is at least as good.
    
    Note to maintainers: This implementation relies on signed arithmetic being bit-wise equivalent
    to unsigned arithmetic in all cases except:
    
    
      - comparisons (signed values can be negative)
      - division (avoided here)
      - shifting (right shift must be unsigned)

    Author(s)
    - Geoff Pike
    """

    def hashBytes(self, input: list[int], off: int, len: int) -> "HashCode":
        ...


    def bits(self) -> int:
        ...


    def toString(self) -> str:
        ...
