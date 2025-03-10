"""
Python module generated from Java source file com.google.common.hash.BloomFilterStrategies

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.hash import *
from com.google.common.math import LongMath
from com.google.common.primitives import Ints
from com.google.common.primitives import Longs
from enum import Enum
from java.math import RoundingMode
from java.util import Arrays
from java.util.concurrent.atomic import AtomicLongArray
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class BloomFilterStrategies(Enum):
    """
    Collections of strategies of generating the k * log(M) bits required for an element to be mapped
    to a BloomFilter of M bits and k hash functions. These strategies are part of the serialized form
    of the Bloom filters that use them, thus they must be preserved as is (no updates allowed, only
    introduction of new versions).
    
    Important: the order of the constants cannot change, and they cannot be deleted - we depend on
    their ordinal for BloomFilter serialization.

    Author(s)
    - Kurt Alfred Kluever
    """

    MURMUR128_MITZ_32 = 0
    """
    See "Less Hashing, Same Performance: Building a Better Bloom Filter" by Adam Kirsch and Michael
    Mitzenmacher. The paper argues that this trick doesn't significantly deteriorate the
    performance of a Bloom filter (yet only needs two 32bit hash functions).
    """
    MURMUR128_MITZ_64 = 1
    """
    This strategy uses all 128 bits of Hashing.murmur3_128 when hashing. It looks different
    than the implementation in MURMUR128_MITZ_32 because we're avoiding the multiplication in the
    loop and doing a (much simpler) += hash2. We're also changing the index to a positive number by
    AND'ing with Long.MAX_VALUE instead of flipping the bits.
    """
