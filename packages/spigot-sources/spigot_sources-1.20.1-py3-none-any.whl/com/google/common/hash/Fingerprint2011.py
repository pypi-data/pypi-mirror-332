"""
Python module generated from Java source file com.google.common.hash.Fingerprint2011

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import VisibleForTesting
from com.google.common.hash import *
from typing import Any, Callable, Iterable, Tuple


class Fingerprint2011(AbstractNonStreamingHashFunction):
    """
    Implementation of Geoff Pike's fingerprint2011 hash function. See Hashing.fingerprint2011
    for information on the behaviour of the algorithm.
    
    On Intel Core2 2.66, on 1000 bytes, fingerprint2011 takes 0.9 microseconds compared to
    fingerprint at 4.0 microseconds and md5 at 4.5 microseconds.
    
    Note to maintainers: This implementation relies on signed arithmetic being bit-wise equivalent
    to unsigned arithmetic in all cases except:
    
    
      - comparisons (signed values can be negative)
      - division (avoided here)
      - shifting (right shift must be unsigned)

    Author(s)
    - gpike@google.com (Geoff Pike)
    """

    def hashBytes(self, input: list[int], off: int, len: int) -> "HashCode":
        ...


    def bits(self) -> int:
        ...


    def toString(self) -> str:
        ...
