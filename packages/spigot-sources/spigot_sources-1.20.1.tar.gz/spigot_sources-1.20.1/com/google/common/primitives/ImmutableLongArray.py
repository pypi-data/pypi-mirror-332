"""
Python module generated from Java source file com.google.common.primitives.ImmutableLongArray

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.primitives import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CheckReturnValue
from com.google.errorprone.annotations import Immutable
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import RandomAccess
from java.util import Spliterator
from java.util.function import LongConsumer
from java.util.stream import LongStream
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableLongArray(Serializable):
    """
    An immutable array of `long` values, with an API resembling List.
    
    Advantages compared to `long[]`:
    
    
      - All the many well-known advantages of immutability (read *Effective Java*, third
          edition, Item 17).
      - Has the value-based (not identity-based) .equals, .hashCode, and .toString behavior you expect.
      - Offers useful operations beyond just `get` and `length`, so you don't have to
          hunt through classes like Arrays and Longs for them.
      - Supports a copy-free .subArray view, so methods that accept this type don't need to
          add overloads that accept start and end indexes.
      - Can be streamed without "breaking the chain": `foo.getBarLongs().stream()...`.
      - Access to all collection-based utilities via .asList (though at the cost of
          allocating garbage).
    
    
    Disadvantages compared to `long[]`:
    
    
      - Memory footprint has a fixed overhead (about 24 bytes per instance).
      - *Some* construction use cases force the data to be copied (though several construction
          APIs are offered that don't).
      - Can't be passed directly to methods that expect `long[]` (though the most common
          utilities do have replacements here).
      - Dependency on `com.google.common` / Guava.
    
    
    Advantages compared to com.google.common.collect.ImmutableList ImmutableList`<Long>`:
    
    
      - Improved memory compactness and locality.
      - Can be queried without allocating garbage.
      - Access to `LongStream` features (like LongStream.sum) using `stream()`
          instead of the awkward `stream().mapToLong(v -> v)`.
    
    
    Disadvantages compared to `ImmutableList<Long>`:
    
    
      - Can't be passed directly to methods that expect `Iterable`, `Collection`, or
          `List` (though the most common utilities do have replacements here, and there is a
          lazy .asList view).

    Since
    - 22.0
    """

    @staticmethod
    def of() -> "ImmutableLongArray":
        """
        Returns the empty array.
        """
        ...


    @staticmethod
    def of(e0: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing a single value.
        """
        ...


    @staticmethod
    def of(e0: int, e1: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: int, e1: int, e2: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: int, e1: int, e2: int, e3: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: int, e1: int, e2: int, e3: int, e4: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: int, e1: int, e2: int, e3: int, e4: int, e5: int) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(first: int, *rest: Tuple[int, ...]) -> "ImmutableLongArray":
        ...


    @staticmethod
    def copyOf(values: list[int]) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def copyOf(values: Iterable["Long"]) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def copyOf(values: Iterable["Long"]) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the given values, in order.
        
        **Performance note:** this method delegates to .copyOf(Collection) if `values` is a Collection. Otherwise it creates a .builder and uses Builder.addAll(Iterable), with all the performance implications associated with that.
        """
        ...


    @staticmethod
    def copyOf(stream: "LongStream") -> "ImmutableLongArray":
        """
        Returns an immutable array containing all the values from `stream`, in order.
        """
        ...


    @staticmethod
    def builder(initialCapacity: int) -> "Builder":
        """
        Returns a new, empty builder for ImmutableLongArray instances, sized to hold up to
        `initialCapacity` values without resizing. The returned builder is not thread-safe.
        
        **Performance note:** When feasible, `initialCapacity` should be the exact number
        of values that will be added, if that knowledge is readily available. It is better to guess a
        value slightly too high than slightly too low. If the value is not exact, the ImmutableLongArray that is built will very likely occupy more memory than strictly necessary;
        to trim memory usage, build using `builder.build().trimmed()`.
        """
        ...


    @staticmethod
    def builder() -> "Builder":
        """
        Returns a new, empty builder for ImmutableLongArray instances, with a default initial
        capacity. The returned builder is not thread-safe.
        
        **Performance note:** The ImmutableLongArray that is built will very likely
        occupy more memory than necessary; to trim memory usage, build using `builder.build().trimmed()`.
        """
        ...


    def length(self) -> int:
        """
        Returns the number of values in this array.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if there are no values in this array (.length is zero).
        """
        ...


    def get(self, index: int) -> int:
        """
        Returns the `long` value present at the given index.

        Raises
        - IndexOutOfBoundsException: if `index` is negative, or greater than or equal to
            .length
        """
        ...


    def indexOf(self, target: int) -> int:
        """
        Returns the smallest index for which .get returns `target`, or `-1` if no
        such index exists. Equivalent to `asList().indexOf(target)`.
        """
        ...


    def lastIndexOf(self, target: int) -> int:
        """
        Returns the largest index for which .get returns `target`, or `-1` if no
        such index exists. Equivalent to `asList().lastIndexOf(target)`.
        """
        ...


    def contains(self, target: int) -> bool:
        """
        Returns `True` if `target` is present at any index in this array. Equivalent to
        `asList().contains(target)`.
        """
        ...


    def forEach(self, consumer: "LongConsumer") -> None:
        """
        Invokes `consumer` for each value contained in this array, in order.
        """
        ...


    def stream(self) -> "LongStream":
        """
        Returns a stream over the values in this array, in order.
        """
        ...


    def toArray(self) -> list[int]:
        """
        Returns a new, mutable copy of this array's values, as a primitive `long[]`.
        """
        ...


    def subArray(self, startIndex: int, endIndex: int) -> "ImmutableLongArray":
        """
        Returns a new immutable array containing the values in the specified range.
        
        **Performance note:** The returned array has the same full memory footprint as this one
        does (no actual copying is performed). To reduce memory usage, use `subArray(start,
        end).trimmed()`.
        """
        ...


    def asList(self) -> list["Long"]:
        """
        Returns an immutable *view* of this array's values as a `List`; note that `long` values are boxed into Long instances on demand, which can be very expensive. The
        returned list should be used once and discarded. For any usages beyond that, pass the returned
        list to com.google.common.collect.ImmutableList.copyOf(Collection) ImmutableList.copyOf
        and use that list instead.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` if `object` is an `ImmutableLongArray` containing the same
        values as this one, in the same order.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns an unspecified hash code for the contents of this immutable array.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this array in the same form as Arrays.toString(long[]), for example `"[1, 2, 3]"`.
        """
        ...


    def trimmed(self) -> "ImmutableLongArray":
        """
        Returns an immutable array containing the same values as `this` array. This is logically
        a no-op, and in some circumstances `this` itself is returned. However, if this instance
        is a .subArray view of a larger array, this method will copy only the appropriate range
        of values, resulting in an equivalent array with a smaller memory footprint.
        """
        ...


    class Builder:
        """
        A builder for ImmutableLongArray instances; obtained using ImmutableLongArray.builder.
        """

        def add(self, value: int) -> "Builder":
            """
            Appends `value` to the end of the values the built ImmutableLongArray will
            contain.
            """
            ...


        def addAll(self, values: list[int]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableLongArray will contain.
            """
            ...


        def addAll(self, values: Iterable["Long"]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableLongArray will contain.
            """
            ...


        def addAll(self, values: Iterable["Long"]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableLongArray will contain.
            """
            ...


        def addAll(self, stream: "LongStream") -> "Builder":
            """
            Appends all values from `stream`, in order, to the end of the values the built ImmutableLongArray will contain.
            """
            ...


        def addAll(self, values: "ImmutableLongArray") -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableLongArray will contain.
            """
            ...


        def build(self) -> "ImmutableLongArray":
            """
            Returns a new immutable array. The builder can continue to be used after this call, to append
            more values and build again.
            
            **Performance note:** the returned array is backed by the same array as the builder, so
            no data is copied as part of this step, but this may occupy more memory than strictly
            necessary. To copy the data to a right-sized backing array, use `.build().trimmed()`.
            """
            ...
