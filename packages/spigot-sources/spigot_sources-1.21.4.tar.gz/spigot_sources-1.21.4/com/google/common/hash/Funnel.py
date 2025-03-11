"""
Python module generated from Java source file com.google.common.hash.Funnel

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.hash import *
from com.google.errorprone.annotations import DoNotMock
from java.io import Serializable
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Funnel(Serializable):
    """
    An object which can send data from an object of type `T` into a `PrimitiveSink`.
    Implementations for common types can be found in Funnels.
    
    Note that serialization of BloomFilter bloom filters requires the proper
    serialization of funnels. When possible, it is recommended that funnels be implemented as a
    single-element enum to maintain serialization guarantees. See Effective Java (2nd Edition), Item
    3: "Enforce the singleton property with a private constructor or an enum type". For example:
    
    ````public enum PersonFunnel implements Funnel<Person> {
      INSTANCE;
      public void funnel(Person person, PrimitiveSink into) {
        into.putUnencodedChars(person.getFirstName())
            .putUnencodedChars(person.getLastName())
            .putInt(person.getAge());`
    }
    }```

    Author(s)
    - Dimitris Andreou

    Since
    - 11.0
    """

    def funnel(self, from: "T", into: "PrimitiveSink") -> None:
        """
        Sends a stream of data from the `from` object into the sink `into`. There is no
        requirement that this data be complete enough to fully reconstitute the object later.

        Since
        - 12.0 (in Guava 11.0, `PrimitiveSink` was named `Sink`)
        """
        ...
