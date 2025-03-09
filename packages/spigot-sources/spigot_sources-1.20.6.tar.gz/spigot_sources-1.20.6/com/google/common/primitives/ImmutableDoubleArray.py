"""
Python module generated from Java source file com.google.common.primitives.ImmutableDoubleArray

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import Preconditions
from com.google.common.primitives import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import Immutable
from java.io import Serializable
from java.util import AbstractList
from java.util import Arrays
from java.util import RandomAccess
from java.util import Spliterator
from java.util.function import DoubleConsumer
from java.util.stream import DoubleStream
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ImmutableDoubleArray(Serializable):
    """
    An immutable array of `double` values, with an API resembling List.
    
    Advantages compared to `double[]`:
    
    
      - All the many well-known advantages of immutability (read *Effective Java*, third
          edition, Item 17).
      - Has the value-based (not identity-based) .equals, .hashCode, and .toString behavior you expect.
      - Offers useful operations beyond just `get` and `length`, so you don't have to
          hunt through classes like Arrays and Doubles for them.
      - Supports a copy-free .subArray view, so methods that accept this type don't need to
          add overloads that accept start and end indexes.
      - Can be streamed without "breaking the chain": `foo.getBarDoubles().stream()...`.
      - Access to all collection-based utilities via .asList (though at the cost of
          allocating garbage).
    
    
    Disadvantages compared to `double[]`:
    
    
      - Memory footprint has a fixed overhead (about 24 bytes per instance).
      - *Some* construction use cases force the data to be copied (though several construction
          APIs are offered that don't).
      - Can't be passed directly to methods that expect `double[]` (though the most common
          utilities do have replacements here).
      - Dependency on `com.google.common` / Guava.
    
    
    Advantages compared to com.google.common.collect.ImmutableList ImmutableList`<Double>`:
    
    
      - Improved memory compactness and locality.
      - Can be queried without allocating garbage.
      - Access to `DoubleStream` features (like DoubleStream.sum) using `stream()` instead of the awkward `stream().mapToDouble(v -> v)`.
    
    
    Disadvantages compared to `ImmutableList<Double>`:
    
    
      - Can't be passed directly to methods that expect `Iterable`, `Collection`, or
          `List` (though the most common utilities do have replacements here, and there is a
          lazy .asList view).

    Since
    - 22.0
    """

    @staticmethod
    def of() -> "ImmutableDoubleArray":
        """
        Returns the empty array.
        """
        ...


    @staticmethod
    def of(e0: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing a single value.
        """
        ...


    @staticmethod
    def of(e0: float, e1: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: float, e1: float, e2: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: float, e1: float, e2: float, e3: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: float, e1: float, e2: float, e3: float, e4: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(e0: float, e1: float, e2: float, e3: float, e4: float, e5: float) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def of(first: float, *rest: Tuple[float, ...]) -> "ImmutableDoubleArray":
        ...


    @staticmethod
    def copyOf(values: list[float]) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def copyOf(values: Iterable["Double"]) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        """
        ...


    @staticmethod
    def copyOf(values: Iterable["Double"]) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the given values, in order.
        
        **Performance note:** this method delegates to .copyOf(Collection) if `values` is a Collection. Otherwise it creates a .builder and uses Builder.addAll(Iterable), with all the performance implications associated with that.
        """
        ...


    @staticmethod
    def copyOf(stream: "DoubleStream") -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing all the values from `stream`, in order.
        """
        ...


    @staticmethod
    def builder(initialCapacity: int) -> "Builder":
        """
        Returns a new, empty builder for ImmutableDoubleArray instances, sized to hold up to
        `initialCapacity` values without resizing. The returned builder is not thread-safe.
        
        **Performance note:** When feasible, `initialCapacity` should be the exact number
        of values that will be added, if that knowledge is readily available. It is better to guess a
        value slightly too high than slightly too low. If the value is not exact, the ImmutableDoubleArray that is built will very likely occupy more memory than strictly
        necessary; to trim memory usage, build using `builder.build().trimmed()`.
        """
        ...


    @staticmethod
    def builder() -> "Builder":
        """
        Returns a new, empty builder for ImmutableDoubleArray instances, with a default initial
        capacity. The returned builder is not thread-safe.
        
        **Performance note:** The ImmutableDoubleArray that is built will very likely
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


    def get(self, index: int) -> float:
        """
        Returns the `double` value present at the given index.

        Raises
        - IndexOutOfBoundsException: if `index` is negative, or greater than or equal to
            .length
        """
        ...


    def indexOf(self, target: float) -> int:
        """
        Returns the smallest index for which .get returns `target`, or `-1` if no
        such index exists. Values are compared as if by Double.equals. Equivalent to `asList().indexOf(target)`.
        """
        ...


    def lastIndexOf(self, target: float) -> int:
        """
        Returns the largest index for which .get returns `target`, or `-1` if no
        such index exists. Values are compared as if by Double.equals. Equivalent to `asList().lastIndexOf(target)`.
        """
        ...


    def contains(self, target: float) -> bool:
        """
        Returns `True` if `target` is present at any index in this array. Values are
        compared as if by Double.equals. Equivalent to `asList().contains(target)`.
        """
        ...


    def forEach(self, consumer: "DoubleConsumer") -> None:
        """
        Invokes `consumer` for each value contained in this array, in order.
        """
        ...


    def stream(self) -> "DoubleStream":
        """
        Returns a stream over the values in this array, in order.
        """
        ...


    def toArray(self) -> list[float]:
        """
        Returns a new, mutable copy of this array's values, as a primitive `double[]`.
        """
        ...


    def subArray(self, startIndex: int, endIndex: int) -> "ImmutableDoubleArray":
        """
        Returns a new immutable array containing the values in the specified range.
        
        **Performance note:** The returned array has the same full memory footprint as this one
        does (no actual copying is performed). To reduce memory usage, use `subArray(start,
        end).trimmed()`.
        """
        ...


    def asList(self) -> list["Double"]:
        """
        Returns an immutable *view* of this array's values as a `List`; note that `double` values are boxed into Double instances on demand, which can be very expensive.
        The returned list should be used once and discarded. For any usages beyond that, pass the
        returned list to com.google.common.collect.ImmutableList.copyOf(Collection)
        ImmutableList.copyOf and use that list instead.
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Returns `True` if `object` is an `ImmutableDoubleArray` containing the same
        values as this one, in the same order. Values are compared as if by Double.equals.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns an unspecified hash code for the contents of this immutable array.
        """
        ...


    def toString(self) -> str:
        """
        Returns a string representation of this array in the same form as Arrays.toString(double[]), for example `"[1, 2, 3]"`.
        """
        ...


    def trimmed(self) -> "ImmutableDoubleArray":
        """
        Returns an immutable array containing the same values as `this` array. This is logically
        a no-op, and in some circumstances `this` itself is returned. However, if this instance
        is a .subArray view of a larger array, this method will copy only the appropriate range
        of values, resulting in an equivalent array with a smaller memory footprint.
        """
        ...


    class Builder:
        """
        A builder for ImmutableDoubleArray instances; obtained using ImmutableDoubleArray.builder.
        """

        def add(self, value: float) -> "Builder":
            """
            Appends `value` to the end of the values the built ImmutableDoubleArray will
            contain.
            """
            ...


        def addAll(self, values: list[float]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableDoubleArray will contain.
            """
            ...


        def addAll(self, values: Iterable["Double"]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableDoubleArray will contain.
            """
            ...


        def addAll(self, values: Iterable["Double"]) -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableDoubleArray will contain.
            """
            ...


        def addAll(self, stream: "DoubleStream") -> "Builder":
            """
            Appends all values from `stream`, in order, to the end of the values the built ImmutableDoubleArray will contain.
            """
            ...


        def addAll(self, values: "ImmutableDoubleArray") -> "Builder":
            """
            Appends `values`, in order, to the end of the values the built ImmutableDoubleArray will contain.
            """
            ...


        def build(self) -> "ImmutableDoubleArray":
            """
            Returns a new immutable array. The builder can continue to be used after this call, to append
            more values and build again.
            
            **Performance note:** the returned array is backed by the same array as the builder, so
            no data is copied as part of this step, but this may occupy more memory than strictly
            necessary. To copy the data to a right-sized backing array, use `.build().trimmed()`.
            """
            ...
