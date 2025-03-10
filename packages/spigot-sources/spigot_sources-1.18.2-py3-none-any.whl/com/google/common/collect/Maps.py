"""
Python module generated from Java source file com.google.common.collect.Maps

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.base import Converter
from com.google.common.base import Equivalence
from com.google.common.base import Function
from com.google.common.base import Objects
from com.google.common.base import Preconditions
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.collect import *
from com.google.common.collect.MapDifference import ValueDifference
from com.google.common.primitives import Ints
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.j2objc.annotations import RetainedWith
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.io import Serializable
from java.util import AbstractCollection
from java.util import Collections
from java.util import Comparator
from java.util import EnumMap
from java.util import Enumeration
from java.util import IdentityHashMap
from java.util import Iterator
from java.util import NavigableMap
from java.util import NavigableSet
from java.util import Properties
from java.util import SortedMap
from java.util import SortedSet
from java.util import Spliterator
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import BinaryOperator
from java.util.function import Consumer
from java.util.stream import Collector
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Maps:
    """
    Static utility methods pertaining to Map instances (including instances of SortedMap, BiMap, etc.). Also see this class's counterparts Lists, Sets
    and Queues.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#maps"> `Maps`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    @staticmethod
    def immutableEnumMap(map: dict["K", "V"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map instance containing the given entries. Internally, the returned map
        will be backed by an EnumMap.
        
        The iteration order of the returned map follows the enum's iteration order, not the order in
        which the elements appear in the given map.

        Arguments
        - map: the map to make an immutable copy of

        Returns
        - an immutable map containing those entries

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toImmutableEnumMap(keyFunction: "java.util.function.Function"["T", "K"], valueFunction: "java.util.function.Function"["T", "V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableMap` whose keys
        and values are the result of applying the provided mapping functions to the input elements. The
        resulting implementation is specialized for enum key types. The returned map and its views will
        iterate over keys in their enum definition order, not encounter order.
        
        If the mapped keys contain duplicates, an `IllegalArgumentException` is thrown when
        the collection operation is performed. (This differs from the `Collector` returned by
        java.util.stream.Collectors.toMap(java.util.function.Function,
        java.util.function.Function) Collectors.toMap(Function, Function), which throws an `IllegalStateException`.)

        Since
        - 21.0
        """
        ...


    @staticmethod
    def toImmutableEnumMap(keyFunction: "java.util.function.Function"["T", "K"], valueFunction: "java.util.function.Function"["T", "V"], mergeFunction: "BinaryOperator"["V"]) -> "Collector"["T", Any, "ImmutableMap"["K", "V"]]:
        """
        Returns a Collector that accumulates elements into an `ImmutableMap` whose keys
        and values are the result of applying the provided mapping functions to the input elements. The
        resulting implementation is specialized for enum key types. The returned map and its views will
        iterate over keys in their enum definition order, not encounter order.
        
        If the mapped keys contain duplicates, the values are merged using the specified merging
        function.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def newHashMap() -> dict["K", "V"]:
        """
        Creates a *mutable*, empty `HashMap` instance.
        
        **Note:** if mutability is not required, use ImmutableMap.of() instead.
        
        **Note:** if `K` is an `enum` type, use .newEnumMap instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `HashMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `HashMap`
        """
        ...


    @staticmethod
    def newHashMap(map: dict["K", "V"]) -> dict["K", "V"]:
        """
        Creates a *mutable* `HashMap` instance with the same mappings as the specified map.
        
        **Note:** if mutability is not required, use ImmutableMap.copyOf(Map) instead.
        
        **Note:** if `K` is an Enum type, use .newEnumMap instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `HashMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Arguments
        - map: the mappings to be placed in the new map

        Returns
        - a new `HashMap` initialized with the mappings from `map`
        """
        ...


    @staticmethod
    def newHashMapWithExpectedSize(expectedSize: int) -> dict["K", "V"]:
        """
        Creates a `HashMap` instance, with a high enough "initial capacity" that it *should*
        hold `expectedSize` elements without growth. This behavior cannot be broadly guaranteed,
        but it is observed to be True for OpenJDK 1.7. It also can't be guaranteed that the method
        isn't inadvertently *oversizing* the returned map.

        Arguments
        - expectedSize: the number of entries you expect to add to the returned map

        Returns
        - a new, empty `HashMap` with enough capacity to hold `expectedSize` entries
            without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative
        """
        ...


    @staticmethod
    def newLinkedHashMap() -> dict["K", "V"]:
        """
        Creates a *mutable*, empty, insertion-ordered `LinkedHashMap` instance.
        
        **Note:** if mutability is not required, use ImmutableMap.of() instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `LinkedHashMap` constructor directly, taking advantage of
        the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `LinkedHashMap`
        """
        ...


    @staticmethod
    def newLinkedHashMap(map: dict["K", "V"]) -> dict["K", "V"]:
        """
        Creates a *mutable*, insertion-ordered `LinkedHashMap` instance with the same
        mappings as the specified map.
        
        **Note:** if mutability is not required, use ImmutableMap.copyOf(Map) instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `LinkedHashMap` constructor directly, taking advantage of
        the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Arguments
        - map: the mappings to be placed in the new map

        Returns
        - a new, `LinkedHashMap` initialized with the mappings from `map`
        """
        ...


    @staticmethod
    def newLinkedHashMapWithExpectedSize(expectedSize: int) -> dict["K", "V"]:
        """
        Creates a `LinkedHashMap` instance, with a high enough "initial capacity" that it
        *should* hold `expectedSize` elements without growth. This behavior cannot be
        broadly guaranteed, but it is observed to be True for OpenJDK 1.7. It also can't be guaranteed
        that the method isn't inadvertently *oversizing* the returned map.

        Arguments
        - expectedSize: the number of entries you expect to add to the returned map

        Returns
        - a new, empty `LinkedHashMap` with enough capacity to hold `expectedSize`
            entries without resizing

        Raises
        - IllegalArgumentException: if `expectedSize` is negative

        Since
        - 19.0
        """
        ...


    @staticmethod
    def newConcurrentMap() -> "ConcurrentMap"["K", "V"]:
        """
        Creates a new empty ConcurrentHashMap instance.

        Since
        - 3.0
        """
        ...


    @staticmethod
    def newTreeMap() -> dict["K", "V"]:
        """
        Creates a *mutable*, empty `TreeMap` instance using the natural ordering of its
        elements.
        
        **Note:** if mutability is not required, use ImmutableSortedMap.of() instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `TreeMap`
        """
        ...


    @staticmethod
    def newTreeMap(map: "SortedMap"["K", "V"]) -> dict["K", "V"]:
        """
        Creates a *mutable* `TreeMap` instance with the same mappings as the specified map
        and using the same ordering as the specified map.
        
        **Note:** if mutability is not required, use ImmutableSortedMap.copyOfSorted(SortedMap) instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Arguments
        - map: the sorted map whose mappings are to be placed in the new map and whose comparator
            is to be used to sort the new map

        Returns
        - a new `TreeMap` initialized with the mappings from `map` and using the
            comparator of `map`
        """
        ...


    @staticmethod
    def newTreeMap(comparator: "Comparator"["C"]) -> dict["K", "V"]:
        """
        Creates a *mutable*, empty `TreeMap` instance using the given comparator.
        
        **Note:** if mutability is not required, use `ImmutableSortedMap.orderedBy(comparator).build()` instead.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `TreeMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Arguments
        - comparator: the comparator to sort the keys with

        Returns
        - a new, empty `TreeMap`
        """
        ...


    @staticmethod
    def newEnumMap(type: type["K"]) -> "EnumMap"["K", "V"]:
        """
        Creates an `EnumMap` instance.

        Arguments
        - type: the key type for this map

        Returns
        - a new, empty `EnumMap`
        """
        ...


    @staticmethod
    def newEnumMap(map: dict["K", "V"]) -> "EnumMap"["K", "V"]:
        """
        Creates an `EnumMap` with the same mappings as the specified map.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `EnumMap` constructor directly, taking advantage of the new
        <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Arguments
        - map: the map from which to initialize this `EnumMap`

        Returns
        - a new `EnumMap` initialized with the mappings from `map`

        Raises
        - IllegalArgumentException: if `m` is not an `EnumMap` instance and contains
            no mappings
        """
        ...


    @staticmethod
    def newIdentityHashMap() -> "IdentityHashMap"["K", "V"]:
        """
        Creates an `IdentityHashMap` instance.
        
        **Note for Java 7 and later:** this method is now unnecessary and should be treated as
        deprecated. Instead, use the `IdentityHashMap` constructor directly, taking advantage of
        the new <a href="http://goo.gl/iz2Wi">"diamond" syntax</a>.

        Returns
        - a new, empty `IdentityHashMap`
        """
        ...


    @staticmethod
    def difference(left: dict["K", "V"], right: dict["K", "V"]) -> "MapDifference"["K", "V"]:
        """
        Computes the difference between two maps. This difference is an immutable snapshot of the state
        of the maps at the time this method is called. It will never change, even if the maps change at
        a later time.
        
        Since this method uses `HashMap` instances internally, the keys of the supplied maps
        must be well-behaved with respect to Object.equals and Object.hashCode.
        
        **Note:**If you only need to know whether two maps have the same mappings, call `left.equals(right)` instead of this method.

        Arguments
        - left: the map to treat as the "left" map for purposes of comparison
        - right: the map to treat as the "right" map for purposes of comparison

        Returns
        - the difference between the two maps
        """
        ...


    @staticmethod
    def difference(left: dict["K", "V"], right: dict["K", "V"], valueEquivalence: "Equivalence"["V"]) -> "MapDifference"["K", "V"]:
        ...


    @staticmethod
    def difference(left: "SortedMap"["K", "V"], right: dict["K", "V"]) -> "SortedMapDifference"["K", "V"]:
        """
        Computes the difference between two sorted maps, using the comparator of the left map, or
        `Ordering.natural()` if the left map uses the natural ordering of its elements. This
        difference is an immutable snapshot of the state of the maps at the time this method is called.
        It will never change, even if the maps change at a later time.
        
        Since this method uses `TreeMap` instances internally, the keys of the right map must
        all compare as distinct according to the comparator of the left map.
        
        **Note:**If you only need to know whether two sorted maps have the same mappings, call
        `left.equals(right)` instead of this method.

        Arguments
        - left: the map to treat as the "left" map for purposes of comparison
        - right: the map to treat as the "right" map for purposes of comparison

        Returns
        - the difference between the two maps

        Since
        - 11.0
        """
        ...


    @staticmethod
    def asMap(set: set["K"], function: "Function"["K", "V"]) -> dict["K", "V"]:
        """
        Returns a live Map view whose keys are the contents of `set` and whose values are
        computed on demand using `function`. To get an immutable *copy* instead, use .toMap(Iterable, Function).
        
        Specifically, for each `k` in the backing set, the returned map has an entry mapping
        `k` to `function.apply(k)`. The `keySet`, `values`, and `entrySet` views of the returned map iterate in the same order as the backing set.
        
        Modifications to the backing set are read through to the returned map. The returned map
        supports removal operations if the backing set does. Removal operations write through to the
        backing set. The returned map does not support put operations.
        
        **Warning:** If the function rejects `null`, caution is required to make sure the
        set does not contain `null`, because the view cannot stop `null` from being added
        to the set.
        
        **Warning:** This method assumes that for any instance `k` of key type `K`,
        `k.equals(k2)` implies that `k2` is also of type `K`. Using a key type for
        which this may not hold, such as `ArrayList`, may risk a `ClassCastException` when
        calling methods on the resulting map view.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asMap(set: "SortedSet"["K"], function: "Function"["K", "V"]) -> "SortedMap"["K", "V"]:
        """
        Returns a view of the sorted set as a map, mapping keys from the set according to the specified
        function.
        
        Specifically, for each `k` in the backing set, the returned map has an entry mapping
        `k` to `function.apply(k)`. The `keySet`, `values`, and `entrySet` views of the returned map iterate in the same order as the backing set.
        
        Modifications to the backing set are read through to the returned map. The returned map
        supports removal operations if the backing set does. Removal operations write through to the
        backing set. The returned map does not support put operations.
        
        **Warning:** If the function rejects `null`, caution is required to make sure the
        set does not contain `null`, because the view cannot stop `null` from being added
        to the set.
        
        **Warning:** This method assumes that for any instance `k` of key type `K`,
        `k.equals(k2)` implies that `k2` is also of type `K`. Using a key type for
        which this may not hold, such as `ArrayList`, may risk a `ClassCastException` when
        calling methods on the resulting map view.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def asMap(set: "NavigableSet"["K"], function: "Function"["K", "V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a view of the navigable set as a map, mapping keys from the set according to the
        specified function.
        
        Specifically, for each `k` in the backing set, the returned map has an entry mapping
        `k` to `function.apply(k)`. The `keySet`, `values`, and `entrySet` views of the returned map iterate in the same order as the backing set.
        
        Modifications to the backing set are read through to the returned map. The returned map
        supports removal operations if the backing set does. Removal operations write through to the
        backing set. The returned map does not support put operations.
        
        **Warning:** If the function rejects `null`, caution is required to make sure the
        set does not contain `null`, because the view cannot stop `null` from being added
        to the set.
        
        **Warning:** This method assumes that for any instance `k` of key type `K`,
        `k.equals(k2)` implies that `k2` is also of type `K`. Using a key type for
        which this may not hold, such as `ArrayList`, may risk a `ClassCastException` when
        calling methods on the resulting map view.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toMap(keys: Iterable["K"], valueFunction: "Function"["K", "V"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map whose keys are the distinct elements of `keys` and whose value
        for each key was computed by `valueFunction`. The map's iteration order is the order of
        the first appearance of each key in `keys`.
        
        When there are multiple instances of a key in `keys`, it is unspecified whether `valueFunction` will be applied to more than one instance of that key and, if it is, which
        result will be mapped to that key in the returned map.
        
        If `keys` is a Set, a live view can be obtained instead of a copy using Maps.asMap(Set, Function).

        Raises
        - NullPointerException: if any element of `keys` is `null`, or if `valueFunction` produces `null` for any key

        Since
        - 14.0
        """
        ...


    @staticmethod
    def toMap(keys: Iterator["K"], valueFunction: "Function"["K", "V"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns an immutable map whose keys are the distinct elements of `keys` and whose value
        for each key was computed by `valueFunction`. The map's iteration order is the order of
        the first appearance of each key in `keys`.
        
        When there are multiple instances of a key in `keys`, it is unspecified whether `valueFunction` will be applied to more than one instance of that key and, if it is, which
        result will be mapped to that key in the returned map.

        Raises
        - NullPointerException: if any element of `keys` is `null`, or if `valueFunction` produces `null` for any key

        Since
        - 14.0
        """
        ...


    @staticmethod
    def uniqueIndex(values: Iterable["V"], keyFunction: "Function"["V", "K"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns a map with the given `values`, indexed by keys derived from those values. In
        other words, each input value produces an entry in the map whose key is the result of applying
        `keyFunction` to that value. These entries appear in the same order as the input values.
        Example usage:
        
        ````Color red = new Color("red", 255, 0, 0);
        ...
        ImmutableSet<Color> allColors = ImmutableSet.of(red, green, blue);
        
        Map<String, Color> colorForName =
            uniqueIndex(allColors, toStringFunction());
        assertThat(colorForName).containsEntry("red", red);````
        
        If your index may associate multiple values with each key, use Multimaps.index(Iterable, Function) Multimaps.index.

        Arguments
        - values: the values to use when constructing the `Map`
        - keyFunction: the function used to produce the key for each value

        Returns
        - a map mapping the result of evaluating the function `keyFunction` on each value
            in the input collection to that value

        Raises
        - IllegalArgumentException: if `keyFunction` produces the same key for more than one
            value in the input collection
        - NullPointerException: if any element of `values` is `null`, or if `keyFunction` produces `null` for any value
        """
        ...


    @staticmethod
    def uniqueIndex(values: Iterator["V"], keyFunction: "Function"["V", "K"]) -> "ImmutableMap"["K", "V"]:
        """
        Returns a map with the given `values`, indexed by keys derived from those values. In
        other words, each input value produces an entry in the map whose key is the result of applying
        `keyFunction` to that value. These entries appear in the same order as the input values.
        Example usage:
        
        ````Color red = new Color("red", 255, 0, 0);
        ...
        Iterator<Color> allColors = ImmutableSet.of(red, green, blue).iterator();
        
        Map<String, Color> colorForName =
            uniqueIndex(allColors, toStringFunction());
        assertThat(colorForName).containsEntry("red", red);````
        
        If your index may associate multiple values with each key, use Multimaps.index(Iterator, Function) Multimaps.index.

        Arguments
        - values: the values to use when constructing the `Map`
        - keyFunction: the function used to produce the key for each value

        Returns
        - a map mapping the result of evaluating the function `keyFunction` on each value
            in the input collection to that value

        Raises
        - IllegalArgumentException: if `keyFunction` produces the same key for more than one
            value in the input collection
        - NullPointerException: if any element of `values` is `null`, or if `keyFunction` produces `null` for any value

        Since
        - 10.0
        """
        ...


    @staticmethod
    def fromProperties(properties: "Properties") -> "ImmutableMap"[str, str]:
        """
        Creates an `ImmutableMap<String, String>` from a `Properties` instance. Properties
        normally derive from `Map<Object, Object>`, but they typically contain strings, which is
        awkward. This method lets you get a plain-old-`Map` out of a `Properties`.

        Arguments
        - properties: a `Properties` object to be converted

        Returns
        - an immutable map containing all the entries in `properties`

        Raises
        - ClassCastException: if any key in `properties` is not a `String`
        - NullPointerException: if any key or value in `properties` is null
        """
        ...


    @staticmethod
    def immutableEntry(key: "K", value: "V") -> "Entry"["K", "V"]:
        """
        Returns an immutable map entry with the specified key and value. The Entry.setValue
        operation throws an UnsupportedOperationException.
        
        The returned entry is serializable.
        
        **Java 9 users:** consider using `java.util.Map.entry(key, value)` if the key and
        value are non-null and the entry does not need to be serializable.

        Arguments
        - key: the key to be associated with the returned entry
        - value: the value to be associated with the returned entry
        """
        ...


    @staticmethod
    def asConverter(bimap: "BiMap"["A", "B"]) -> "Converter"["A", "B"]:
        """
        Returns a Converter that converts values using BiMap.get bimap.get(), and whose
        inverse view converts values using BiMap.inverse bimap.inverse()`.get()`.
        
        To use a plain Map as a Function, see com.google.common.base.Functions.forMap(Map) or com.google.common.base.Functions.forMap(Map, Object).

        Since
        - 16.0
        """
        ...


    @staticmethod
    def synchronizedBiMap(bimap: "BiMap"["K", "V"]) -> "BiMap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) bimap backed by the specified bimap. In order to guarantee
        serial access, it is critical that **all** access to the backing bimap is accomplished
        through the returned bimap.
        
        It is imperative that the user manually synchronize on the returned map when accessing any
        of its collection views:
        
        ````BiMap<Long, String> map = Maps.synchronizedBiMap(
            HashBiMap.<Long, String>create());
        ...
        Set<Long> set = map.keySet();  // Needn't be in synchronized block
        ...
        synchronized (map) {  // Synchronizing on map, not set!
          Iterator<Long> it = set.iterator(); // Must be in synchronized block
          while (it.hasNext()) {
            foo(it.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned bimap will be serializable if the specified bimap is serializable.

        Arguments
        - bimap: the bimap to be wrapped in a synchronized view

        Returns
        - a synchronized view of the specified bimap
        """
        ...


    @staticmethod
    def unmodifiableBiMap(bimap: "BiMap"["K", "V"]) -> "BiMap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified bimap. This method allows modules to provide
        users with "read-only" access to internal bimaps. Query operations on the returned bimap "read
        through" to the specified bimap, and attempts to modify the returned map, whether direct or via
        its collection views, result in an `UnsupportedOperationException`.
        
        The returned bimap will be serializable if the specified bimap is serializable.

        Arguments
        - bimap: the bimap for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified bimap
        """
        ...


    @staticmethod
    def transformValues(fromMap: dict["K", "V1"], function: "Function"["V1", "V2"]) -> dict["K", "V2"]:
        """
        Returns a view of a map where each value is transformed by a function. All other properties of
        the map, such as iteration order, are left intact. For example, the code:
        
        ````Map<String, Integer> map = ImmutableMap.of("a", 4, "b", 9);
        Function<Integer, Double> sqrt =
            new Function<Integer, Double>() {
              public Double apply(Integer in) {
                return Math.sqrt((int) in);`
            };
        Map<String, Double> transformed = Maps.transformValues(map, sqrt);
        System.out.println(transformed);
        }```
        
        ... prints `{a=2.0, b=3.0`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys, and even null values provided
        that the function is capable of accepting null input. The transformed map might contain null
        values, if the function sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The function is applied lazily, invoked when needed. This is necessary for the returned map
        to be a view, but it means that the function will be applied many times for bulk operations
        like Map.containsValue and `Map.toString()`. For this to perform well, `function` should be fast. To avoid lazy evaluation when the returned map doesn't need to be a
        view, copy the returned map into a new map of your choosing.
        """
        ...


    @staticmethod
    def transformValues(fromMap: "SortedMap"["K", "V1"], function: "Function"["V1", "V2"]) -> "SortedMap"["K", "V2"]:
        """
        Returns a view of a sorted map where each value is transformed by a function. All other
        properties of the map, such as iteration order, are left intact. For example, the code:
        
        ````SortedMap<String, Integer> map = ImmutableSortedMap.of("a", 4, "b", 9);
        Function<Integer, Double> sqrt =
            new Function<Integer, Double>() {
              public Double apply(Integer in) {
                return Math.sqrt((int) in);`
            };
        SortedMap<String, Double> transformed =
             Maps.transformValues(map, sqrt);
        System.out.println(transformed);
        }```
        
        ... prints `{a=2.0, b=3.0`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys, and even null values provided
        that the function is capable of accepting null input. The transformed map might contain null
        values, if the function sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The function is applied lazily, invoked when needed. This is necessary for the returned map
        to be a view, but it means that the function will be applied many times for bulk operations
        like Map.containsValue and `Map.toString()`. For this to perform well, `function` should be fast. To avoid lazy evaluation when the returned map doesn't need to be a
        view, copy the returned map into a new map of your choosing.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def transformValues(fromMap: "NavigableMap"["K", "V1"], function: "Function"["V1", "V2"]) -> "NavigableMap"["K", "V2"]:
        """
        Returns a view of a navigable map where each value is transformed by a function. All other
        properties of the map, such as iteration order, are left intact. For example, the code:
        
        ````NavigableMap<String, Integer> map = Maps.newTreeMap();
        map.put("a", 4);
        map.put("b", 9);
        Function<Integer, Double> sqrt =
            new Function<Integer, Double>() {
              public Double apply(Integer in) {
                return Math.sqrt((int) in);`
            };
        NavigableMap<String, Double> transformed =
             Maps.transformNavigableValues(map, sqrt);
        System.out.println(transformed);
        }```
        
        ... prints `{a=2.0, b=3.0`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys, and even null values provided
        that the function is capable of accepting null input. The transformed map might contain null
        values, if the function sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The function is applied lazily, invoked when needed. This is necessary for the returned map
        to be a view, but it means that the function will be applied many times for bulk operations
        like Map.containsValue and `Map.toString()`. For this to perform well, `function` should be fast. To avoid lazy evaluation when the returned map doesn't need to be a
        view, copy the returned map into a new map of your choosing.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def transformEntries(fromMap: dict["K", "V1"], transformer: "EntryTransformer"["K", "V1", "V2"]) -> dict["K", "V2"]:
        """
        Returns a view of a map whose values are derived from the original map's entries. In contrast
        to .transformValues, this method's entry-transformation logic may depend on the key as
        well as the value.
        
        All other properties of the transformed map, such as iteration order, are left intact. For
        example, the code:
        
        ````Map<String, Boolean> options =
            ImmutableMap.of("verbose", True, "sort", False);
        EntryTransformer<String, Boolean, String> flagPrefixer =
            new EntryTransformer<String, Boolean, String>() {
              public String transformEntry(String key, Boolean value) {
                return value ? key : "no" + key;`
            };
        Map<String, String> transformed =
            Maps.transformEntries(options, flagPrefixer);
        System.out.println(transformed);
        }```
        
        ... prints `{verbose=verbose, sort=nosort`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys and null values provided that
        the transformer is capable of accepting null inputs. The transformed map might contain null
        values if the transformer sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The transformer is applied lazily, invoked when needed. This is necessary for the returned
        map to be a view, but it means that the transformer will be applied many times for bulk
        operations like Map.containsValue and Object.toString. For this to perform
        well, `transformer` should be fast. To avoid lazy evaluation when the returned map
        doesn't need to be a view, copy the returned map into a new map of your choosing.
        
        **Warning:** This method assumes that for any instance `k` of `EntryTransformer` key type `K`, `k.equals(k2)` implies that `k2` is also of
        type `K`. Using an `EntryTransformer` key type for which this may not hold, such as
        `ArrayList`, may risk a `ClassCastException` when calling methods on the
        transformed map.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def transformEntries(fromMap: "SortedMap"["K", "V1"], transformer: "EntryTransformer"["K", "V1", "V2"]) -> "SortedMap"["K", "V2"]:
        """
        Returns a view of a sorted map whose values are derived from the original sorted map's entries.
        In contrast to .transformValues, this method's entry-transformation logic may depend on
        the key as well as the value.
        
        All other properties of the transformed map, such as iteration order, are left intact. For
        example, the code:
        
        ````Map<String, Boolean> options =
            ImmutableSortedMap.of("verbose", True, "sort", False);
        EntryTransformer<String, Boolean, String> flagPrefixer =
            new EntryTransformer<String, Boolean, String>() {
              public String transformEntry(String key, Boolean value) {
                return value ? key : "yes" + key;`
            };
        SortedMap<String, String> transformed =
            Maps.transformEntries(options, flagPrefixer);
        System.out.println(transformed);
        }```
        
        ... prints `{sort=yessort, verbose=verbose`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys and null values provided that
        the transformer is capable of accepting null inputs. The transformed map might contain null
        values if the transformer sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The transformer is applied lazily, invoked when needed. This is necessary for the returned
        map to be a view, but it means that the transformer will be applied many times for bulk
        operations like Map.containsValue and Object.toString. For this to perform
        well, `transformer` should be fast. To avoid lazy evaluation when the returned map
        doesn't need to be a view, copy the returned map into a new map of your choosing.
        
        **Warning:** This method assumes that for any instance `k` of `EntryTransformer` key type `K`, `k.equals(k2)` implies that `k2` is also of
        type `K`. Using an `EntryTransformer` key type for which this may not hold, such as
        `ArrayList`, may risk a `ClassCastException` when calling methods on the
        transformed map.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def transformEntries(fromMap: "NavigableMap"["K", "V1"], transformer: "EntryTransformer"["K", "V1", "V2"]) -> "NavigableMap"["K", "V2"]:
        """
        Returns a view of a navigable map whose values are derived from the original navigable map's
        entries. In contrast to .transformValues, this method's entry-transformation logic may
        depend on the key as well as the value.
        
        All other properties of the transformed map, such as iteration order, are left intact. For
        example, the code:
        
        ````NavigableMap<String, Boolean> options = Maps.newTreeMap();
        options.put("verbose", False);
        options.put("sort", True);
        EntryTransformer<String, Boolean, String> flagPrefixer =
            new EntryTransformer<String, Boolean, String>() {
              public String transformEntry(String key, Boolean value) {
                return value ? key : ("yes" + key);`
            };
        NavigableMap<String, String> transformed =
            LabsMaps.transformNavigableEntries(options, flagPrefixer);
        System.out.println(transformed);
        }```
        
        ... prints `{sort=yessort, verbose=verbose`}.
        
        Changes in the underlying map are reflected in this view. Conversely, this view supports
        removal operations, and these are reflected in the underlying map.
        
        It's acceptable for the underlying map to contain null keys and null values provided that
        the transformer is capable of accepting null inputs. The transformed map might contain null
        values if the transformer sometimes gives a null result.
        
        The returned map is not thread-safe or serializable, even if the underlying map is.
        
        The transformer is applied lazily, invoked when needed. This is necessary for the returned
        map to be a view, but it means that the transformer will be applied many times for bulk
        operations like Map.containsValue and Object.toString. For this to perform
        well, `transformer` should be fast. To avoid lazy evaluation when the returned map
        doesn't need to be a view, copy the returned map into a new map of your choosing.
        
        **Warning:** This method assumes that for any instance `k` of `EntryTransformer` key type `K`, `k.equals(k2)` implies that `k2` is also of
        type `K`. Using an `EntryTransformer` key type for which this may not hold, such as
        `ArrayList`, may risk a `ClassCastException` when calling methods on the
        transformed map.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: dict["K", "V"], keyPredicate: "Predicate"["K"]) -> dict["K", "V"]:
        """
        Returns a map containing the mappings in `unfiltered` whose keys satisfy a predicate. The
        returned map is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key that doesn't satisfy the predicate, the map's `put()` and
        `putAll()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose keys satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "SortedMap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "SortedMap"["K", "V"]:
        """
        Returns a sorted map containing the mappings in `unfiltered` whose keys satisfy a
        predicate. The returned map is a live view of `unfiltered`; changes to one affect the
        other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key that doesn't satisfy the predicate, the map's `put()` and
        `putAll()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose keys satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "NavigableMap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a navigable map containing the mappings in `unfiltered` whose keys satisfy a
        predicate. The returned map is a live view of `unfiltered`; changes to one affect the
        other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key that doesn't satisfy the predicate, the map's `put()` and
        `putAll()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose keys satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "BiMap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "BiMap"["K", "V"]:
        """
        Returns a bimap containing the mappings in `unfiltered` whose keys satisfy a predicate.
        The returned bimap is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting bimap's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the bimap
        and its views. When given a key that doesn't satisfy the predicate, the bimap's `put()`,
        `forcePut()` and `putAll()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        bimap or its views, only mappings that satisfy the filter will be removed from the underlying
        bimap.
        
        The returned bimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered bimap's methods, such as `size()`, iterate across every key in
        the underlying bimap and determine which satisfy the filter. When a live view is *not*
        needed, it may be faster to copy the filtered bimap and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals *, as documented
        at Predicate.apply.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterValues(unfiltered: dict["K", "V"], valuePredicate: "Predicate"["V"]) -> dict["K", "V"]:
        """
        Returns a map containing the mappings in `unfiltered` whose values satisfy a predicate.
        The returned map is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a value that doesn't satisfy the predicate, the map's `put()`,
        `putAll()`, and Entry.setValue methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose values satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `valuePredicate` must be *consistent with equals*, as documented
        at Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.
        """
        ...


    @staticmethod
    def filterValues(unfiltered: "SortedMap"["K", "V"], valuePredicate: "Predicate"["V"]) -> "SortedMap"["K", "V"]:
        """
        Returns a sorted map containing the mappings in `unfiltered` whose values satisfy a
        predicate. The returned map is a live view of `unfiltered`; changes to one affect the
        other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a value that doesn't satisfy the predicate, the map's `put()`,
        `putAll()`, and Entry.setValue methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose values satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `valuePredicate` must be *consistent with equals*, as documented
        at Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterValues(unfiltered: "NavigableMap"["K", "V"], valuePredicate: "Predicate"["V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a navigable map containing the mappings in `unfiltered` whose values satisfy a
        predicate. The returned map is a live view of `unfiltered`; changes to one affect the
        other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a value that doesn't satisfy the predicate, the map's `put()`,
        `putAll()`, and Entry.setValue methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings whose values satisfy the filter will be removed from the underlying
        map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `valuePredicate` must be *consistent with equals*, as documented
        at Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterValues(unfiltered: "BiMap"["K", "V"], valuePredicate: "Predicate"["V"]) -> "BiMap"["K", "V"]:
        """
        Returns a bimap containing the mappings in `unfiltered` whose values satisfy a predicate.
        The returned bimap is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting bimap's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the bimap
        and its views. When given a value that doesn't satisfy the predicate, the bimap's `put()`, `forcePut()` and `putAll()` methods throw an IllegalArgumentException. Similarly, the map's entries have a Entry.setValue method
        that throws an IllegalArgumentException when the provided value doesn't satisfy the
        predicate.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        bimap or its views, only mappings that satisfy the filter will be removed from the underlying
        bimap.
        
        The returned bimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered bimap's methods, such as `size()`, iterate across every value in
        the underlying bimap and determine which satisfy the filter. When a live view is *not*
        needed, it may be faster to copy the filtered bimap and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals *, as documented
        at Predicate.apply.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: dict["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> dict["K", "V"]:
        """
        Returns a map containing the mappings in `unfiltered` that satisfy a predicate. The
        returned map is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key/value pair that doesn't satisfy the predicate, the map's `put()` and `putAll()` methods throw an IllegalArgumentException. Similarly, the
        map's entries have a Entry.setValue method that throws an IllegalArgumentException when the existing key and the provided value don't satisfy the
        predicate.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings that satisfy the filter will be removed from the underlying map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals*, as documented
        at Predicate.apply.
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: "SortedMap"["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> "SortedMap"["K", "V"]:
        """
        Returns a sorted map containing the mappings in `unfiltered` that satisfy a predicate.
        The returned map is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key/value pair that doesn't satisfy the predicate, the map's `put()` and `putAll()` methods throw an IllegalArgumentException. Similarly, the
        map's entries have a Entry.setValue method that throws an IllegalArgumentException when the existing key and the provided value don't satisfy the
        predicate.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings that satisfy the filter will be removed from the underlying map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals*, as documented
        at Predicate.apply.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: "NavigableMap"["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> "NavigableMap"["K", "V"]:
        """
        Returns a sorted map containing the mappings in `unfiltered` that satisfy a predicate.
        The returned map is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting map's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the map
        and its views. When given a key/value pair that doesn't satisfy the predicate, the map's `put()` and `putAll()` methods throw an IllegalArgumentException. Similarly, the
        map's entries have a Entry.setValue method that throws an IllegalArgumentException when the existing key and the provided value don't satisfy the
        predicate.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered map
        or its views, only mappings that satisfy the filter will be removed from the underlying map.
        
        The returned map isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered map's methods, such as `size()`, iterate across every key/value
        mapping in the underlying map and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered map and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals*, as documented
        at Predicate.apply.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: "BiMap"["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> "BiMap"["K", "V"]:
        """
        Returns a bimap containing the mappings in `unfiltered` that satisfy a predicate. The
        returned bimap is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting bimap's `keySet()`, `entrySet()`, and `values()` views have
        iterators that don't support `remove()`, but all other methods are supported by the bimap
        and its views. When given a key/value pair that doesn't satisfy the predicate, the bimap's
        `put()`, `forcePut()` and `putAll()` methods throw an IllegalArgumentException. Similarly, the map's entries have an Entry.setValue method
        that throws an IllegalArgumentException when the existing key and the provided value
        don't satisfy the predicate.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        bimap or its views, only mappings that satisfy the filter will be removed from the underlying
        bimap.
        
        The returned bimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered bimap's methods, such as `size()`, iterate across every key/value
        mapping in the underlying bimap and determine which satisfy the filter. When a live view is
        *not* needed, it may be faster to copy the filtered bimap and use the copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals *, as documented
        at Predicate.apply.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def unmodifiableNavigableMap(map: "NavigableMap"["K", "V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified navigable map. Query operations on the returned
        map read through to the specified map, and attempts to modify the returned map, whether direct
        or via its views, result in an `UnsupportedOperationException`.
        
        The returned navigable map will be serializable if the specified navigable map is
        serializable.
        
        This method's signature will not permit you to convert a `NavigableMap<? extends K,
        V>` to a `NavigableMap<K, V>`. If it permitted this, the returned map's `comparator()` method might return a `Comparator<? extends K>`, which works only on a
        particular subtype of `K`, but promise that it's a `Comparator<? super K>`, which
        must work on any type of `K`.

        Arguments
        - map: the navigable map for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified navigable map

        Since
        - 12.0
        """
        ...


    @staticmethod
    def synchronizedNavigableMap(navigableMap: "NavigableMap"["K", "V"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) navigable map backed by the specified navigable map. In
        order to guarantee serial access, it is critical that **all** access to the backing
        navigable map is accomplished through the returned navigable map (or its views).
        
        It is imperative that the user manually synchronize on the returned navigable map when
        iterating over any of its collection views, or the collections views of any of its `descendingMap`, `subMap`, `headMap` or `tailMap` views.
        
        ````NavigableMap<K, V> map = synchronizedNavigableMap(new TreeMap<K, V>());
        
        // Needn't be in synchronized block
        NavigableSet<K> set = map.navigableKeySet();
        
        synchronized (map) { // Synchronizing on map, not set!
          Iterator<K> it = set.iterator(); // Must be in synchronized block
          while (it.hasNext()) {
            foo(it.next());`
        }
        }```
        
        or:
        
        ````NavigableMap<K, V> map = synchronizedNavigableMap(new TreeMap<K, V>());
        NavigableMap<K, V> map2 = map.subMap(foo, False, bar, True);
        
        // Needn't be in synchronized block
        NavigableSet<K> set2 = map2.descendingKeySet();
        
        synchronized (map) { // Synchronizing on map, not map2 or set2!
          Iterator<K> it = set2.iterator(); // Must be in synchronized block
          while (it.hasNext()) {
            foo(it.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        The returned navigable map will be serializable if the specified navigable map is
        serializable.

        Arguments
        - navigableMap: the navigable map to be "wrapped" in a synchronized navigable map.

        Returns
        - a synchronized view of the specified navigable map.

        Since
        - 13.0
        """
        ...


    @staticmethod
    def subMap(map: "NavigableMap"["K", "V"], range: "Range"["K"]) -> "NavigableMap"["K", "V"]:
        """
        Returns a view of the portion of `map` whose keys are contained by `range`.
        
        This method delegates to the appropriate methods of NavigableMap (namely NavigableMap.subMap(Object, boolean, Object, boolean) subMap(), NavigableMap.tailMap(Object, boolean) tailMap(), and NavigableMap.headMap(Object,
        boolean) headMap()) to actually construct the view. Consult these methods for a full
        description of the returned view's behavior.
        
        **Warning:** `Range`s always represent a range of values using the values' natural
        ordering. `NavigableMap` on the other hand can specify a custom ordering via a Comparator, which can violate the natural ordering. Using this method (or in general using
        `Range`) with unnaturally-ordered maps can lead to unexpected and undefined behavior.

        Since
        - 20.0
        """
        ...


    class EntryTransformer:
        """
        A transformation of the value of a key-value pair, using both key and value as inputs. To apply
        the transformation to a map, use Maps.transformEntries(Map, EntryTransformer).
        
        Type `<K>`: the key type of the input and output entries

        Arguments
        - <V1>: the value type of the input entry
        - <V2>: the value type of the output entry

        Since
        - 7.0
        """

        def transformEntry(self, key: "K", value: "V1") -> "V2":
            """
            Determines an output value based on a key-value pair. This method is *generally
            expected*, but not absolutely required, to have the following properties:
            
            
              - Its execution does not cause any observable side effects.
              - The computation is *consistent with equals*; that is, Objects.equal
                  Objects.equal`(k1, k2) &&` Objects.equal`(v1, v2)` implies that
                  `Objects.equal(transformer.transform(k1, v1), transformer.transform(k2, v2))`.

            Raises
            - NullPointerException: if the key or value is null and this transformer does not accept
                null arguments
            """
            ...
