"""
Python module generated from Java source file com.google.common.collect.Multimap

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import CompatibleWith
from java.util.function import BiConsumer
from javax.annotation import Nullable
from typing import Any, Callable, Iterable, Tuple


class Multimap:
    """
    A collection that maps keys to values, similar to Map, but in which
    each key may be associated with *multiple* values. You can visualize the
    contents of a multimap either as a map from keys to *nonempty*
    collections of values:
    
    
    - a → 1, 2
    - b → 3
    
    
    ... or as a single "flattened" collection of key-value pairs:
    
    
    - a → 1
    - a → 2
    - b → 3
    
    
    **Important:** although the first interpretation resembles how most
    multimaps are *implemented*, the design of the `Multimap` API is
    based on the *second* form. So, using the multimap shown above as an
    example, the .size is `3`, not `2`, and the .values collection is `[1, 2, 3]`, not `[[1, 2], [3]]`. For
    those times when the first style is more useful, use the multimap's .asMap view (or create a `Map<K, Collection<V>>` in the first place).
    
    <h3>Example</h3>
    
    The following code: ```   `ListMultimap<String, String> multimap = ArrayListMultimap.create();
      for (President pres : US_PRESIDENTS_IN_ORDER) {
        multimap.put(pres.firstName(), pres.lastName());`
      for (String firstName : multimap.keySet()) {
        List<String> lastNames = multimap.get(firstName);
        out.println(firstName + ": " + lastNames);
      }}```
    
    ... produces output such as: ```   `Zachary: [Taylor]
      John: [Adams, Adams, Tyler, Kennedy]  // Remember, Quincy!
      George: [Washington, Bush, Bush]
      Grover: [Cleveland, Cleveland]        // Two, non-consecutive terms, rep'ing NJ!
      ...````
    
    <h3>Views</h3>
    
    Much of the power of the multimap API comes from the *view
    collections* it provides. These always reflect the latest state of the
    multimap itself. When they support modification, the changes are
    *write-through* (they automatically update the backing multimap). These
    view collections are:
    
    
    - .asMap, mentioned above
    - .keys, .keySet, .values, .entries, which
        are similar to the corresponding view collections of Map
    - and, notably, even the collection returned by .get get(key) is an
        active view of the values corresponding to `key`
    
    
    The collections returned by the .replaceValues replaceValues and
    .removeAll removeAll methods, which contain values that have just
    been removed from the multimap, are naturally *not* views.
    
    <h3>Subinterfaces</h3>
    
    Instead of using the `Multimap` interface directly, prefer the
    subinterfaces ListMultimap and SetMultimap. These take their
    names from the fact that the collections they return from `get` behave
    like (and, of course, implement) List and Set, respectively.
    
    For example, the "presidents" code snippet above used a `ListMultimap`; if it had used a `SetMultimap` instead, two presidents
    would have vanished, and last names might or might not appear in
    chronological order.
    
    **Warning:** instances of type `Multimap` may not implement
    Object.equals in the way you expect.  Multimaps containing the same
    key-value pairs, even in the same order, may or may not be equal and may or
    may not have the same `hashCode`. The recommended subinterfaces
    provide much stronger guarantees.
    
    <h3>Comparison to a map of collections</h3>
    
    Multimaps are commonly used in places where a `Map<K,
    Collection<V>>` would otherwise have appeared. The differences include:
    
    
    - There is no need to populate an empty collection before adding an entry
        with .put put.
    - `get` never returns `null`, only an empty collection.
    - A key is contained in the multimap if and only if it maps to at least
        one value. Any operation that causes a key to have zero associated
        values has the effect of *removing* that key from the multimap.
    - The total entry count is available as .size.
    - Many complex operations become easier; for example, `Collections.min(multimap.values())` finds the smallest value across all
        keys.
    
    
    <h3>Implementations</h3>
    
    As always, prefer the immutable implementations, ImmutableListMultimap and ImmutableSetMultimap. General-purpose
    mutable implementations are listed above under "All Known Implementing
    Classes". You can also create a *custom* multimap, backed by any `Map` and Collection types, using the Multimaps.newMultimap
    Multimaps.newMultimap family of methods. Finally, another popular way to
    obtain a multimap is using Multimaps.index Multimaps.index. See
    the Multimaps class for these and other static utilities related
    to multimaps.
    
    <h3>Other Notes</h3>
    
    As with `Map`, the behavior of a `Multimap` is not specified
    if key objects already present in the multimap change in a manner that
    affects `equals` comparisons.  Use caution if mutable objects are used
    as keys in a `Multimap`.
    
    All methods that modify the multimap are optional. The view collections
    returned by the multimap may or may not be modifiable. Any modification
    method that is not supported will throw UnsupportedOperationException.
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#multimap">
    `Multimap`</a>.

    Author(s)
    - Jared Levy

    Since
    - 2.0
    """

    def size(self) -> int:
        """
        Returns the number of key-value pairs in this multimap.
        
        **Note:** this method does not return the number of *distinct
        keys* in the multimap, which is given by `keySet().size()` or
        `asMap().size()`. See the opening section of the Multimap
        class documentation for clarification.
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this multimap contains no key-value pairs.
        Equivalent to `size() == 0`, but can in some cases be more efficient.
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Returns `True` if this multimap contains at least one key-value pair
        with the key `key`.
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if this multimap contains at least one key-value pair
        with the value `value`.
        """
        ...


    def containsEntry(self, key: "Object", value: "Object") -> bool:
        """
        Returns `True` if this multimap contains at least one key-value pair
        with the key `key` and the value `value`.
        """
        ...


    def put(self, key: "K", value: "V") -> bool:
        """
        Stores a key-value pair in this multimap.
        
        Some multimap implementations allow duplicate key-value pairs, in which
        case `put` always adds a new key-value pair and increases the
        multimap size by 1. Other implementations prohibit duplicates, and storing
        a key-value pair that's already in the multimap has no effect.

        Returns
        - `True` if the method increased the size of the multimap, or
            `False` if the multimap already contained the key-value pair and
            doesn't allow duplicates
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Removes a single key-value pair with the key `key` and the value
        `value` from this multimap, if such exists. If multiple key-value
        pairs in the multimap fit this description, which one is removed is
        unspecified.

        Returns
        - `True` if the multimap changed
        """
        ...


    def putAll(self, key: "K", values: Iterable["V"]) -> bool:
        """
        Stores a key-value pair in this multimap for each of `values`, all
        using the same key, `key`. Equivalent to (but expected to be more
        efficient than): ```   `for (V value : values) {
            put(key, value);`}```
        
        In particular, this is a no-op if `values` is empty.

        Returns
        - `True` if the multimap changed
        """
        ...


    def putAll(self, multimap: "Multimap"["K", "V"]) -> bool:
        """
        Stores all key-value pairs of `multimap` in this multimap, in the
        order returned by `multimap.entries()`.

        Returns
        - `True` if the multimap changed
        """
        ...


    def replaceValues(self, key: "K", values: Iterable["V"]) -> Iterable["V"]:
        """
        Stores a collection of values with the same key, replacing any existing
        values for that key.
        
        If `values` is empty, this is equivalent to
        .removeAll(Object) removeAll(key).

        Returns
        - the collection of replaced values, or an empty collection if no
            values were previously associated with the key. The collection
            *may* be modifiable, but updating it will have no effect on the
            multimap.
        """
        ...


    def removeAll(self, key: "Object") -> Iterable["V"]:
        """
        Removes all values associated with the key `key`.
        
        Once this method returns, `key` will not be mapped to any values,
        so it will not appear in .keySet(), .asMap(), or any other
        views.

        Returns
        - the values that were removed (possibly empty). The returned
            collection *may* be modifiable, but updating it will have no
            effect on the multimap.
        """
        ...


    def clear(self) -> None:
        """
        Removes all key-value pairs from the multimap, leaving it .isEmpty empty.
        """
        ...


    def get(self, key: "K") -> Iterable["V"]:
        """
        Returns a view collection of the values associated with `key` in this
        multimap, if any. Note that when `containsKey(key)` is False, this
        returns an empty collection, not `null`.
        
        Changes to the returned collection will update the underlying multimap,
        and vice versa.
        """
        ...


    def keySet(self) -> set["K"]:
        """
        Returns a view collection of all *distinct* keys contained in this
        multimap. Note that the key set contains a key if and only if this multimap
        maps that key to at least one value.
        
        Changes to the returned set will update the underlying multimap, and
        vice versa. However, *adding* to the returned set is not possible.
        """
        ...


    def keys(self) -> "Multiset"["K"]:
        """
        Returns a view collection containing the key from each key-value pair in
        this multimap, *without* collapsing duplicates. This collection has
        the same size as this multimap, and `keys().count(k) ==
        get(k).size()` for all `k`.
        
        Changes to the returned multiset will update the underlying multimap,
        and vice versa. However, *adding* to the returned collection is not
        possible.
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a view collection containing the *value* from each key-value
        pair contained in this multimap, without collapsing duplicates (so `values().size() == size()`).
        
        Changes to the returned collection will update the underlying multimap,
        and vice versa. However, *adding* to the returned collection is not
        possible.
        """
        ...


    def entries(self) -> Iterable["Map.Entry"["K", "V"]]:
        """
        Returns a view collection of all key-value pairs contained in this
        multimap, as Map.Entry instances.
        
        Changes to the returned collection or the entries it contains will
        update the underlying multimap, and vice versa. However, *adding* to
        the returned collection is not possible.
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        """
        Performs the given action for all key-value pairs contained in this multimap. If an ordering is
        specified by the `Multimap` implementation, actions will be performed in the order of
        iteration of .entries(). Exceptions thrown by the action are relayed to the caller.
        
        To loop over all keys and their associated value collections, write
        `Multimaps.asMap(multimap).forEach((key, valueCollection) -> action())`.

        Since
        - 21.0
        """
        ...


    def asMap(self) -> dict["K", Iterable["V"]]:
        """
        Returns a view of this multimap as a `Map` from each distinct key
        to the nonempty collection of that key's associated values. Note that
        `this.asMap().get(k)` is equivalent to `this.get(k)` only when
        `k` is a key contained in the multimap; otherwise it returns `null` as opposed to an empty collection.
        
        Changes to the returned map or the collections that serve as its values
        will update the underlying multimap, and vice versa. The map does not
        support `put` or `putAll`, nor do its entries support Map.Entry.setValue setValue.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Compares the specified object with this multimap for equality. Two
        multimaps are equal when their map views, as returned by .asMap,
        are also equal.
        
        In general, two multimaps with identical key-value mappings may or may
        not be equal, depending on the implementation. For example, two
        SetMultimap instances with the same key-value mappings are equal,
        but equality of two ListMultimap instances depends on the ordering
        of the values for each key.
        
        A non-empty SetMultimap cannot be equal to a non-empty
        ListMultimap, since their .asMap views contain unequal
        collections as values. However, any two empty multimaps are equal, because
        they both have empty .asMap views.
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code for this multimap.
        
        The hash code of a multimap is defined as the hash code of the map view,
        as returned by Multimap.asMap.
        
        In general, two multimaps with identical key-value mappings may or may
        not have the same hash codes, depending on the implementation. For
        example, two SetMultimap instances with the same key-value
        mappings will have the same `hashCode`, but the `hashCode`
        of ListMultimap instances depends on the ordering of the values
        for each key.
        """
        ...
