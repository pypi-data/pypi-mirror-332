"""
Python module generated from Java source file com.google.common.collect.Multimaps

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Function
from com.google.common.base import Predicate
from com.google.common.base import Predicates
from com.google.common.base import Supplier
from com.google.common.collect import *
from com.google.common.collect.Maps import EntryTransformer
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations.concurrent import LazyInit
from com.google.j2objc.annotations import Weak
from com.google.j2objc.annotations import WeakOuter
from java.io import IOException
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.io import Serializable
from java.util import AbstractCollection
from java.util import Collections
from java.util import Comparator
from java.util import Iterator
from java.util import NavigableSet
from java.util import NoSuchElementException
from java.util import SortedSet
from java.util import Spliterator
from java.util.function import BiConsumer
from java.util.function import Consumer
from java.util.stream import Collector
from java.util.stream import Stream
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Multimaps:
    """
    Provides static methods acting on or generating a `Multimap`.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/CollectionUtilitiesExplained#multimaps">`Multimaps`</a>.

    Author(s)
    - Louis Wasserman

    Since
    - 2.0
    """

    @staticmethod
    def toMultimap(keyFunction: "java.util.function.Function"["T", "K"], valueFunction: "java.util.function.Function"["T", "V"], multimapSupplier: "java.util.function.Supplier"["M"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a `Collector` accumulating entries into a `Multimap` generated from the
        specified supplier. The keys and values of the entries are the result of applying the provided
        mapping functions to the input elements, accumulated in the encounter order of the stream.
        
        Example:
        
        ````static final ListMultimap<Character, String> FIRST_LETTER_MULTIMAP =
            Stream.of("banana", "apple", "carrot", "asparagus", "cherry")
                .collect(
                    toMultimap(
                         str -> str.charAt(0),
                         str -> str.substring(1),
                         MultimapBuilder.treeKeys().arrayListValues()::build));
        
        // is equivalent to
        
        static final ListMultimap<Character, String> FIRST_LETTER_MULTIMAP;
        
        static {
            FIRST_LETTER_MULTIMAP = MultimapBuilder.treeKeys().arrayListValues().build();
            FIRST_LETTER_MULTIMAP.put('b', "anana");
            FIRST_LETTER_MULTIMAP.put('a', "pple");
            FIRST_LETTER_MULTIMAP.put('a', "sparagus");
            FIRST_LETTER_MULTIMAP.put('c', "arrot");
            FIRST_LETTER_MULTIMAP.put('c', "herry");`
        }```
        
        To collect to an ImmutableMultimap, use either ImmutableSetMultimap.toImmutableSetMultimap or ImmutableListMultimap.toImmutableListMultimap.

        Since
        - 21.0
        """
        ...


    @staticmethod
    def flatteningToMultimap(keyFunction: "java.util.function.Function"["T", "K"], valueFunction: "java.util.function.Function"["T", "Stream"["V"]], multimapSupplier: "java.util.function.Supplier"["M"]) -> "Collector"["T", Any, "M"]:
        """
        Returns a `Collector` accumulating entries into a `Multimap` generated from the
        specified supplier. Each input element is mapped to a key and a stream of values, each of which
        are put into the resulting `Multimap`, in the encounter order of the stream and the
        encounter order of the streams of values.
        
        Example:
        
        ````static final ListMultimap<Character, Character> FIRST_LETTER_MULTIMAP =
            Stream.of("banana", "apple", "carrot", "asparagus", "cherry")
                .collect(
                    flatteningToMultimap(
                         str -> str.charAt(0),
                         str -> str.substring(1).chars().mapToObj(c -> (char) c),
                         MultimapBuilder.linkedHashKeys().arrayListValues()::build));
        
        // is equivalent to
        
        static final ListMultimap<Character, Character> FIRST_LETTER_MULTIMAP;
        
        static {
            FIRST_LETTER_MULTIMAP = MultimapBuilder.linkedHashKeys().arrayListValues().build();
            FIRST_LETTER_MULTIMAP.putAll('b', Arrays.asList('a', 'n', 'a', 'n', 'a'));
            FIRST_LETTER_MULTIMAP.putAll('a', Arrays.asList('p', 'p', 'l', 'e'));
            FIRST_LETTER_MULTIMAP.putAll('c', Arrays.asList('a', 'r', 'r', 'o', 't'));
            FIRST_LETTER_MULTIMAP.putAll('a', Arrays.asList('s', 'p', 'a', 'r', 'a', 'g', 'u', 's'));
            FIRST_LETTER_MULTIMAP.putAll('c', Arrays.asList('h', 'e', 'r', 'r', 'y'));`
        }```

        Since
        - 21.0
        """
        ...


    @staticmethod
    def newMultimap(map: dict["K", Iterable["V"]], factory: "Supplier"[Iterable["V"]]) -> "Multimap"["K", "V"]:
        """
        Creates a new `Multimap` backed by `map`, whose internal value collections are
        generated by `factory`.
        
        **Warning: do not use** this method when the collections returned by `factory`
        implement either List or `Set`! Use the more specific method .newListMultimap, .newSetMultimap or .newSortedSetMultimap instead, to avoid
        very surprising behavior from Multimap.equals.
        
        The `factory`-generated and `map` classes determine the multimap iteration
        order. They also specify the behavior of the `equals`, `hashCode`, and `toString` methods for the multimap and its returned views. However, the multimap's `get`
        method returns instances of a different class than `factory.get()` does.
        
        The multimap is serializable if `map`, `factory`, the collections generated by
        `factory`, and the multimap contents are all serializable.
        
        The multimap is not threadsafe when any concurrent operations update the multimap, even if
        `map` and the instances generated by `factory` are. Concurrent read operations will
        work correctly. To allow concurrent update operations, wrap the multimap with a call to .synchronizedMultimap.
        
        Call this method only when the simpler methods ArrayListMultimap.create(), HashMultimap.create(), LinkedHashMultimap.create(), LinkedListMultimap.create(), TreeMultimap.create(), and TreeMultimap.create(Comparator, Comparator) won't suffice.
        
        Note: the multimap assumes complete ownership over of `map` and the collections
        returned by `factory`. Those objects should not be manually updated and they should not
        use soft, weak, or phantom references.

        Arguments
        - map: place to store the mapping from each key to its corresponding values
        - factory: supplier of new, empty collections that will each hold all values for a given
            key

        Raises
        - IllegalArgumentException: if `map` is not empty
        """
        ...


    @staticmethod
    def newListMultimap(map: dict["K", Iterable["V"]], factory: "Supplier"[list["V"]]) -> "ListMultimap"["K", "V"]:
        """
        Creates a new `ListMultimap` that uses the provided map and factory. It can generate a
        multimap based on arbitrary Map and List classes.
        
        The `factory`-generated and `map` classes determine the multimap iteration
        order. They also specify the behavior of the `equals`, `hashCode`, and `toString` methods for the multimap and its returned views. The multimap's `get`, `removeAll`, and `replaceValues` methods return `RandomAccess` lists if the factory
        does. However, the multimap's `get` method returns instances of a different class than
        does `factory.get()`.
        
        The multimap is serializable if `map`, `factory`, the lists generated by `factory`, and the multimap contents are all serializable.
        
        The multimap is not threadsafe when any concurrent operations update the multimap, even if
        `map` and the instances generated by `factory` are. Concurrent read operations will
        work correctly. To allow concurrent update operations, wrap the multimap with a call to .synchronizedListMultimap.
        
        Call this method only when the simpler methods ArrayListMultimap.create() and LinkedListMultimap.create() won't suffice.
        
        Note: the multimap assumes complete ownership over of `map` and the lists returned by
        `factory`. Those objects should not be manually updated, they should be empty when
        provided, and they should not use soft, weak, or phantom references.

        Arguments
        - map: place to store the mapping from each key to its corresponding values
        - factory: supplier of new, empty lists that will each hold all values for a given key

        Raises
        - IllegalArgumentException: if `map` is not empty
        """
        ...


    @staticmethod
    def newSetMultimap(map: dict["K", Iterable["V"]], factory: "Supplier"[set["V"]]) -> "SetMultimap"["K", "V"]:
        """
        Creates a new `SetMultimap` that uses the provided map and factory. It can generate a
        multimap based on arbitrary Map and Set classes.
        
        The `factory`-generated and `map` classes determine the multimap iteration
        order. They also specify the behavior of the `equals`, `hashCode`, and `toString` methods for the multimap and its returned views. However, the multimap's `get`
        method returns instances of a different class than `factory.get()` does.
        
        The multimap is serializable if `map`, `factory`, the sets generated by `factory`, and the multimap contents are all serializable.
        
        The multimap is not threadsafe when any concurrent operations update the multimap, even if
        `map` and the instances generated by `factory` are. Concurrent read operations will
        work correctly. To allow concurrent update operations, wrap the multimap with a call to .synchronizedSetMultimap.
        
        Call this method only when the simpler methods HashMultimap.create(), LinkedHashMultimap.create(), TreeMultimap.create(), and TreeMultimap.create(Comparator, Comparator) won't suffice.
        
        Note: the multimap assumes complete ownership over of `map` and the sets returned by
        `factory`. Those objects should not be manually updated and they should not use soft,
        weak, or phantom references.

        Arguments
        - map: place to store the mapping from each key to its corresponding values
        - factory: supplier of new, empty sets that will each hold all values for a given key

        Raises
        - IllegalArgumentException: if `map` is not empty
        """
        ...


    @staticmethod
    def newSortedSetMultimap(map: dict["K", Iterable["V"]], factory: "Supplier"["SortedSet"["V"]]) -> "SortedSetMultimap"["K", "V"]:
        """
        Creates a new `SortedSetMultimap` that uses the provided map and factory. It can generate
        a multimap based on arbitrary Map and SortedSet classes.
        
        The `factory`-generated and `map` classes determine the multimap iteration
        order. They also specify the behavior of the `equals`, `hashCode`, and `toString` methods for the multimap and its returned views. However, the multimap's `get`
        method returns instances of a different class than `factory.get()` does.
        
        The multimap is serializable if `map`, `factory`, the sets generated by `factory`, and the multimap contents are all serializable.
        
        The multimap is not threadsafe when any concurrent operations update the multimap, even if
        `map` and the instances generated by `factory` are. Concurrent read operations will
        work correctly. To allow concurrent update operations, wrap the multimap with a call to .synchronizedSortedSetMultimap.
        
        Call this method only when the simpler methods TreeMultimap.create() and TreeMultimap.create(Comparator, Comparator) won't suffice.
        
        Note: the multimap assumes complete ownership over of `map` and the sets returned by
        `factory`. Those objects should not be manually updated and they should not use soft,
        weak, or phantom references.

        Arguments
        - map: place to store the mapping from each key to its corresponding values
        - factory: supplier of new, empty sorted sets that will each hold all values for a given
            key

        Raises
        - IllegalArgumentException: if `map` is not empty
        """
        ...


    @staticmethod
    def invertFrom(source: "Multimap"["V", "K"], dest: "M") -> "M":
        """
        Copies each key-value mapping in `source` into `dest`, with its key and value
        reversed.
        
        If `source` is an ImmutableMultimap, consider using ImmutableMultimap.inverse instead.

        Arguments
        - source: any multimap
        - dest: the multimap to copy into; usually empty

        Returns
        - `dest`
        """
        ...


    @staticmethod
    def synchronizedMultimap(multimap: "Multimap"["K", "V"]) -> "Multimap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) multimap backed by the specified multimap. In order to
        guarantee serial access, it is critical that **all** access to the backing multimap is
        accomplished through the returned multimap.
        
        It is imperative that the user manually synchronize on the returned multimap when accessing
        any of its collection views:
        
        ````Multimap<K, V> multimap = Multimaps.synchronizedMultimap(
            HashMultimap.<K, V>create());
        ...
        Collection<V> values = multimap.get(key);  // Needn't be in synchronized block
        ...
        synchronized (multimap) {  // Synchronizing on multimap, not values!
          Iterator<V> i = values.iterator(); // Must be in synchronized block
          while (i.hasNext()) {
            foo(i.next());`
        }
        }```
        
        Failure to follow this advice may result in non-deterministic behavior.
        
        Note that the generated multimap's Multimap.removeAll and Multimap.replaceValues methods return collections that aren't synchronized.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - multimap: the multimap to be wrapped in a synchronized view

        Returns
        - a synchronized view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableMultimap(delegate: "Multimap"["K", "V"]) -> "Multimap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified multimap. Query operations on the returned
        multimap "read through" to the specified multimap, and attempts to modify the returned
        multimap, either directly or through the multimap's views, result in an `UnsupportedOperationException`.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - delegate: the multimap for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableMultimap(delegate: "ImmutableMultimap"["K", "V"]) -> "Multimap"["K", "V"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def synchronizedSetMultimap(multimap: "SetMultimap"["K", "V"]) -> "SetMultimap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) `SetMultimap` backed by the specified multimap.
        
        You must follow the warnings described in .synchronizedMultimap.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - multimap: the multimap to be wrapped

        Returns
        - a synchronized view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableSetMultimap(delegate: "SetMultimap"["K", "V"]) -> "SetMultimap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified `SetMultimap`. Query operations on the
        returned multimap "read through" to the specified multimap, and attempts to modify the returned
        multimap, either directly or through the multimap's views, result in an `UnsupportedOperationException`.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - delegate: the multimap for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableSetMultimap(delegate: "ImmutableSetMultimap"["K", "V"]) -> "SetMultimap"["K", "V"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def synchronizedSortedSetMultimap(multimap: "SortedSetMultimap"["K", "V"]) -> "SortedSetMultimap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) `SortedSetMultimap` backed by the specified
        multimap.
        
        You must follow the warnings described in .synchronizedMultimap.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - multimap: the multimap to be wrapped

        Returns
        - a synchronized view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableSortedSetMultimap(delegate: "SortedSetMultimap"["K", "V"]) -> "SortedSetMultimap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified `SortedSetMultimap`. Query operations on
        the returned multimap "read through" to the specified multimap, and attempts to modify the
        returned multimap, either directly or through the multimap's views, result in an `UnsupportedOperationException`.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - delegate: the multimap for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified multimap
        """
        ...


    @staticmethod
    def synchronizedListMultimap(multimap: "ListMultimap"["K", "V"]) -> "ListMultimap"["K", "V"]:
        """
        Returns a synchronized (thread-safe) `ListMultimap` backed by the specified multimap.
        
        You must follow the warnings described in .synchronizedMultimap.

        Arguments
        - multimap: the multimap to be wrapped

        Returns
        - a synchronized view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableListMultimap(delegate: "ListMultimap"["K", "V"]) -> "ListMultimap"["K", "V"]:
        """
        Returns an unmodifiable view of the specified `ListMultimap`. Query operations on the
        returned multimap "read through" to the specified multimap, and attempts to modify the returned
        multimap, either directly or through the multimap's views, result in an `UnsupportedOperationException`.
        
        The returned multimap will be serializable if the specified multimap is serializable.

        Arguments
        - delegate: the multimap for which an unmodifiable view is to be returned

        Returns
        - an unmodifiable view of the specified multimap
        """
        ...


    @staticmethod
    def unmodifiableListMultimap(delegate: "ImmutableListMultimap"["K", "V"]) -> "ListMultimap"["K", "V"]:
        """
        Simply returns its argument.

        Since
        - 10.0

        Deprecated
        - no need to use this
        """
        ...


    @staticmethod
    def asMap(multimap: "ListMultimap"["K", "V"]) -> dict["K", list["V"]]:
        """
        Returns ListMultimap.asMap multimap.asMap(), with its type corrected from `Map<K,
        Collection<V>>` to `Map<K, List<V>>`.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def asMap(multimap: "SetMultimap"["K", "V"]) -> dict["K", set["V"]]:
        """
        Returns SetMultimap.asMap multimap.asMap(), with its type corrected from `Map<K,
        Collection<V>>` to `Map<K, Set<V>>`.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def asMap(multimap: "SortedSetMultimap"["K", "V"]) -> dict["K", "SortedSet"["V"]]:
        """
        Returns SortedSetMultimap.asMap multimap.asMap(), with its type corrected from `Map<K, Collection<V>>` to `Map<K, SortedSet<V>>`.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def asMap(multimap: "Multimap"["K", "V"]) -> dict["K", Iterable["V"]]:
        """
        Returns Multimap.asMap multimap.asMap(). This is provided for parity with the other
        more strongly-typed `asMap()` implementations.

        Since
        - 15.0
        """
        ...


    @staticmethod
    def forMap(map: dict["K", "V"]) -> "SetMultimap"["K", "V"]:
        """
        Returns a multimap view of the specified map. The multimap is backed by the map, so changes to
        the map are reflected in the multimap, and vice versa. If the map is modified while an
        iteration over one of the multimap's collection views is in progress (except through the
        iterator's own `remove` operation, or through the `setValue` operation on a map
        entry returned by the iterator), the results of the iteration are undefined.
        
        The multimap supports mapping removal, which removes the corresponding mapping from the map.
        It does not support any operations which might add mappings, such as `put`, `putAll` or `replaceValues`.
        
        The returned multimap will be serializable if the specified map is serializable.

        Arguments
        - map: the backing map for the returned multimap view
        """
        ...


    @staticmethod
    def transformValues(fromMultimap: "Multimap"["K", "V1"], function: "Function"["V1", "V2"]) -> "Multimap"["K", "V2"]:
        """
        Returns a view of a multimap where each value is transformed by a function. All other
        properties of the multimap, such as iteration order, are left intact. For example, the code:
        
        ````Multimap<String, Integer> multimap =
            ImmutableSetMultimap.of("a", 2, "b", -3, "b", -3, "a", 4, "c", 6);
        Function<Integer, String> square = new Function<Integer, String>() {
            public String apply(Integer in) {
              return Integer.toString(in * in);`
        };
        Multimap<String, String> transformed =
            Multimaps.transformValues(multimap, square);
          System.out.println(transformed);
        }```
        
        ... prints `{a=[4, 16], b=[9, 9], c=[36]`}.
        
        Changes in the underlying multimap are reflected in this view. Conversely, this view
        supports removal operations, and these are reflected in the underlying multimap.
        
        It's acceptable for the underlying multimap to contain null keys, and even null values
        provided that the function is capable of accepting null input. The transformed multimap might
        contain null values, if the function sometimes gives a null result.
        
        The returned multimap is not thread-safe or serializable, even if the underlying multimap
        is. The `equals` and `hashCode` methods of the returned multimap are meaningless,
        since there is not a definition of `equals` or `hashCode` for general collections,
        and `get()` will return a general `Collection` as opposed to a `List` or a
        `Set`.
        
        The function is applied lazily, invoked when needed. This is necessary for the returned
        multimap to be a view, but it means that the function will be applied many times for bulk
        operations like Multimap.containsValue and `Multimap.toString()`. For this to
        perform well, `function` should be fast. To avoid lazy evaluation when the returned
        multimap doesn't need to be a view, copy the returned multimap into a new multimap of your
        choosing.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def transformValues(fromMultimap: "ListMultimap"["K", "V1"], function: "Function"["V1", "V2"]) -> "ListMultimap"["K", "V2"]:
        """
        Returns a view of a `ListMultimap` where each value is transformed by a function. All
        other properties of the multimap, such as iteration order, are left intact. For example, the
        code:
        
        ````ListMultimap<String, Integer> multimap
             = ImmutableListMultimap.of("a", 4, "a", 16, "b", 9);
        Function<Integer, Double> sqrt =
            new Function<Integer, Double>() {
              public Double apply(Integer in) {
                return Math.sqrt((int) in);`
            };
        ListMultimap<String, Double> transformed = Multimaps.transformValues(map,
            sqrt);
        System.out.println(transformed);
        }```
        
        ... prints `{a=[2.0, 4.0], b=[3.0]`}.
        
        Changes in the underlying multimap are reflected in this view. Conversely, this view
        supports removal operations, and these are reflected in the underlying multimap.
        
        It's acceptable for the underlying multimap to contain null keys, and even null values
        provided that the function is capable of accepting null input. The transformed multimap might
        contain null values, if the function sometimes gives a null result.
        
        The returned multimap is not thread-safe or serializable, even if the underlying multimap
        is.
        
        The function is applied lazily, invoked when needed. This is necessary for the returned
        multimap to be a view, but it means that the function will be applied many times for bulk
        operations like Multimap.containsValue and `Multimap.toString()`. For this to
        perform well, `function` should be fast. To avoid lazy evaluation when the returned
        multimap doesn't need to be a view, copy the returned multimap into a new multimap of your
        choosing.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def transformEntries(fromMap: "Multimap"["K", "V1"], transformer: "EntryTransformer"["K", "V1", "V2"]) -> "Multimap"["K", "V2"]:
        """
        Returns a view of a multimap whose values are derived from the original multimap's entries. In
        contrast to .transformValues, this method's entry-transformation logic may depend on
        the key as well as the value.
        
        All other properties of the transformed multimap, such as iteration order, are left intact.
        For example, the code:
        
        ````SetMultimap<String, Integer> multimap =
            ImmutableSetMultimap.of("a", 1, "a", 4, "b", -6);
        EntryTransformer<String, Integer, String> transformer =
            new EntryTransformer<String, Integer, String>() {
              public String transformEntry(String key, Integer value) {
                 return (value >= 0) ? key : "no" + key;`
            };
        Multimap<String, String> transformed =
            Multimaps.transformEntries(multimap, transformer);
        System.out.println(transformed);
        }```
        
        ... prints `{a=[a, a], b=[nob]`}.
        
        Changes in the underlying multimap are reflected in this view. Conversely, this view
        supports removal operations, and these are reflected in the underlying multimap.
        
        It's acceptable for the underlying multimap to contain null keys and null values provided
        that the transformer is capable of accepting null inputs. The transformed multimap might
        contain null values if the transformer sometimes gives a null result.
        
        The returned multimap is not thread-safe or serializable, even if the underlying multimap
        is. The `equals` and `hashCode` methods of the returned multimap are meaningless,
        since there is not a definition of `equals` or `hashCode` for general collections,
        and `get()` will return a general `Collection` as opposed to a `List` or a
        `Set`.
        
        The transformer is applied lazily, invoked when needed. This is necessary for the returned
        multimap to be a view, but it means that the transformer will be applied many times for bulk
        operations like Multimap.containsValue and Object.toString. For this to perform
        well, `transformer` should be fast. To avoid lazy evaluation when the returned multimap
        doesn't need to be a view, copy the returned multimap into a new multimap of your choosing.
        
        **Warning:** This method assumes that for any instance `k` of `EntryTransformer` key type `K`, `k.equals(k2)` implies that `k2` is also of
        type `K`. Using an `EntryTransformer` key type for which this may not hold, such as
        `ArrayList`, may risk a `ClassCastException` when calling methods on the
        transformed multimap.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def transformEntries(fromMap: "ListMultimap"["K", "V1"], transformer: "EntryTransformer"["K", "V1", "V2"]) -> "ListMultimap"["K", "V2"]:
        """
        Returns a view of a `ListMultimap` whose values are derived from the original multimap's
        entries. In contrast to .transformValues(ListMultimap, Function), this method's
        entry-transformation logic may depend on the key as well as the value.
        
        All other properties of the transformed multimap, such as iteration order, are left intact.
        For example, the code:
        
        ````Multimap<String, Integer> multimap =
            ImmutableMultimap.of("a", 1, "a", 4, "b", 6);
        EntryTransformer<String, Integer, String> transformer =
            new EntryTransformer<String, Integer, String>() {
              public String transformEntry(String key, Integer value) {
                return key + value;`
            };
        Multimap<String, String> transformed =
            Multimaps.transformEntries(multimap, transformer);
        System.out.println(transformed);
        }```
        
        ... prints `{"a"=["a1", "a4"], "b"=["b6"]`}.
        
        Changes in the underlying multimap are reflected in this view. Conversely, this view
        supports removal operations, and these are reflected in the underlying multimap.
        
        It's acceptable for the underlying multimap to contain null keys and null values provided
        that the transformer is capable of accepting null inputs. The transformed multimap might
        contain null values if the transformer sometimes gives a null result.
        
        The returned multimap is not thread-safe or serializable, even if the underlying multimap
        is.
        
        The transformer is applied lazily, invoked when needed. This is necessary for the returned
        multimap to be a view, but it means that the transformer will be applied many times for bulk
        operations like Multimap.containsValue and Object.toString. For this to perform
        well, `transformer` should be fast. To avoid lazy evaluation when the returned multimap
        doesn't need to be a view, copy the returned multimap into a new multimap of your choosing.
        
        **Warning:** This method assumes that for any instance `k` of `EntryTransformer` key type `K`, `k.equals(k2)` implies that `k2` is also of
        type `K`. Using an `EntryTransformer` key type for which this may not hold, such as
        `ArrayList`, may risk a `ClassCastException` when calling methods on the
        transformed multimap.

        Since
        - 7.0
        """
        ...


    @staticmethod
    def index(values: Iterable["V"], keyFunction: "Function"["V", "K"]) -> "ImmutableListMultimap"["K", "V"]:
        """
        Creates an index `ImmutableListMultimap` that contains the results of applying a
        specified function to each item in an `Iterable` of values. Each value will be stored as
        a value in the resulting multimap, yielding a multimap with the same size as the input
        iterable. The key used to store that value in the multimap will be the result of calling the
        function on that value. The resulting multimap is created as an immutable snapshot. In the
        returned multimap, keys appear in the order they are first encountered, and the values
        corresponding to each key appear in the same order as they are encountered.
        
        For example,
        
        ````List<String> badGuys =
            Arrays.asList("Inky", "Blinky", "Pinky", "Pinky", "Clyde");
        Function<String, Integer> stringLengthFunction = ...;
        Multimap<Integer, String> index =
            Multimaps.index(badGuys, stringLengthFunction);
        System.out.println(index);````
        
        prints
        
        ````{4=[Inky], 6=[Blinky], 5=[Pinky, Pinky, Clyde]`
        }```
        
        The returned multimap is serializable if its keys and values are all serializable.

        Arguments
        - values: the values to use when constructing the `ImmutableListMultimap`
        - keyFunction: the function used to produce the key for each value

        Returns
        - `ImmutableListMultimap` mapping the result of evaluating the function `keyFunction` on each value in the input collection to that value

        Raises
        - NullPointerException: if any element of `values` is `null`, or if `keyFunction` produces `null` for any key
        """
        ...


    @staticmethod
    def index(values: Iterator["V"], keyFunction: "Function"["V", "K"]) -> "ImmutableListMultimap"["K", "V"]:
        """
        Creates an index `ImmutableListMultimap` that contains the results of applying a
        specified function to each item in an `Iterator` of values. Each value will be stored as
        a value in the resulting multimap, yielding a multimap with the same size as the input
        iterator. The key used to store that value in the multimap will be the result of calling the
        function on that value. The resulting multimap is created as an immutable snapshot. In the
        returned multimap, keys appear in the order they are first encountered, and the values
        corresponding to each key appear in the same order as they are encountered.
        
        For example,
        
        ````List<String> badGuys =
            Arrays.asList("Inky", "Blinky", "Pinky", "Pinky", "Clyde");
        Function<String, Integer> stringLengthFunction = ...;
        Multimap<Integer, String> index =
            Multimaps.index(badGuys.iterator(), stringLengthFunction);
        System.out.println(index);````
        
        prints
        
        ````{4=[Inky], 6=[Blinky], 5=[Pinky, Pinky, Clyde]`
        }```
        
        The returned multimap is serializable if its keys and values are all serializable.

        Arguments
        - values: the values to use when constructing the `ImmutableListMultimap`
        - keyFunction: the function used to produce the key for each value

        Returns
        - `ImmutableListMultimap` mapping the result of evaluating the function `keyFunction` on each value in the input collection to that value

        Raises
        - NullPointerException: if any element of `values` is `null`, or if `keyFunction` produces `null` for any key

        Since
        - 10.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "Multimap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "Multimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` whose keys satisfy a
        predicate. The returned multimap is a live view of `unfiltered`; changes to one affect
        the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a key that doesn't
        satisfy the predicate, the multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose keys satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "SetMultimap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "SetMultimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` whose keys satisfy a
        predicate. The returned multimap is a live view of `unfiltered`; changes to one affect
        the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a key that doesn't
        satisfy the predicate, the multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose keys satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterKeys(unfiltered: "ListMultimap"["K", "V"], keyPredicate: "Predicate"["K"]) -> "ListMultimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` whose keys satisfy a
        predicate. The returned multimap is a live view of `unfiltered`; changes to one affect
        the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a key that doesn't
        satisfy the predicate, the multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose keys satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `keyPredicate` must be *consistent with equals*, as documented at
        Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterValues(unfiltered: "Multimap"["K", "V"], valuePredicate: "Predicate"["V"]) -> "Multimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` whose values satisfy a
        predicate. The returned multimap is a live view of `unfiltered`; changes to one affect
        the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a value that doesn't
        satisfy the predicate, the multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose value satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `valuePredicate` must be *consistent with equals*, as documented
        at Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterValues(unfiltered: "SetMultimap"["K", "V"], valuePredicate: "Predicate"["V"]) -> "SetMultimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` whose values satisfy a
        predicate. The returned multimap is a live view of `unfiltered`; changes to one affect
        the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a value that doesn't
        satisfy the predicate, the multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose value satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `valuePredicate` must be *consistent with equals*, as documented
        at Predicate.apply. Do not provide a predicate such as `Predicates.instanceOf(ArrayList.class)`, which is inconsistent with equals.

        Since
        - 14.0
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: "Multimap"["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> "Multimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` that satisfy a predicate. The
        returned multimap is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a key/value pair that
        doesn't satisfy the predicate, multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose keys satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals*, as documented
        at Predicate.apply.

        Since
        - 11.0
        """
        ...


    @staticmethod
    def filterEntries(unfiltered: "SetMultimap"["K", "V"], entryPredicate: "Predicate"["Entry"["K", "V"]]) -> "SetMultimap"["K", "V"]:
        """
        Returns a multimap containing the mappings in `unfiltered` that satisfy a predicate. The
        returned multimap is a live view of `unfiltered`; changes to one affect the other.
        
        The resulting multimap's views have iterators that don't support `remove()`, but all
        other methods are supported by the multimap and its views. When adding a key/value pair that
        doesn't satisfy the predicate, multimap's `put()`, `putAll()`, and `replaceValues()` methods throw an IllegalArgumentException.
        
        When methods such as `removeAll()` and `clear()` are called on the filtered
        multimap or its views, only mappings whose keys satisfy the filter will be removed from the
        underlying multimap.
        
        The returned multimap isn't threadsafe or serializable, even if `unfiltered` is.
        
        Many of the filtered multimap's methods, such as `size()`, iterate across every
        key/value mapping in the underlying multimap and determine which satisfy the filter. When a
        live view is *not* needed, it may be faster to copy the filtered multimap and use the
        copy.
        
        **Warning:** `entryPredicate` must be *consistent with equals*, as documented
        at Predicate.apply.

        Since
        - 14.0
        """
        ...
