"""
Python module generated from Java source file java.util.IdentityHashMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import ObjectInputStream
from java.io import ObjectOutputStream
from java.lang.reflect import Array
from java.util import *
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Consumer
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class IdentityHashMap(AbstractMap, Map, Serializable, Cloneable):

    def __init__(self):
        """
        Constructs a new, empty identity hash map with a default expected
        maximum size (21).
        """
        ...


    def __init__(self, expectedMaxSize: int):
        """
        Constructs a new, empty map with the specified expected maximum size.
        Putting more than the expected number of key-value mappings into
        the map may cause the internal data structure to grow, which may be
        somewhat time-consuming.

        Arguments
        - expectedMaxSize: the expected maximum size of the map

        Raises
        - IllegalArgumentException: if `expectedMaxSize` is negative
        """
        ...


    def __init__(self, m: dict["K", "V"]):
        """
        Constructs a new identity hash map containing the keys-value mappings
        in the specified map.

        Arguments
        - m: the map whose mappings are to be placed into this map

        Raises
        - NullPointerException: if the specified map is null
        """
        ...


    def size(self) -> int:
        """
        Returns the number of key-value mappings in this identity hash map.

        Returns
        - the number of key-value mappings in this map
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this identity hash map contains no key-value
        mappings.

        Returns
        - `True` if this identity hash map contains no key-value
                mappings
        """
        ...


    def get(self, key: "Object") -> "V":
        """
        Returns the value to which the specified key is mapped,
        or `null` if this map contains no mapping for the key.
        
        More formally, if this map contains a mapping from a key
        `k` to a value `v` such that `(key == k)`,
        then this method returns `v`; otherwise it returns
        `null`.  (There can be at most one such mapping.)
        
        A return value of `null` does not *necessarily*
        indicate that the map contains no mapping for the key; it's also
        possible that the map explicitly maps the key to `null`.
        The .containsKey containsKey operation may be used to
        distinguish these two cases.

        See
        - .put(Object, Object)
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Tests whether the specified object reference is a key in this identity
        hash map.

        Arguments
        - key: possible key

        Returns
        - `True` if the specified object reference is a key
                 in this map

        See
        - .containsValue(Object)
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Tests whether the specified object reference is a value in this identity
        hash map.

        Arguments
        - value: value whose presence in this map is to be tested

        Returns
        - `True` if this map maps one or more keys to the
                specified object reference

        See
        - .containsKey(Object)
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        """
        Associates the specified value with the specified key in this identity
        hash map.  If the map previously contained a mapping for the key, the
        old value is replaced.

        Arguments
        - key: the key with which the specified value is to be associated
        - value: the value to be associated with the specified key

        Returns
        - the previous value associated with `key`, or
                `null` if there was no mapping for `key`.
                (A `null` return can also indicate that the map
                previously associated `null` with `key`.)

        See
        - .containsKey(Object)
        """
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        """
        Copies all of the mappings from the specified map to this map.
        These mappings will replace any mappings that this map had for
        any of the keys currently in the specified map.

        Arguments
        - m: mappings to be stored in this map

        Raises
        - NullPointerException: if the specified map is null
        """
        ...


    def remove(self, key: "Object") -> "V":
        """
        Removes the mapping for this key from this map if present.

        Arguments
        - key: key whose mapping is to be removed from the map

        Returns
        - the previous value associated with `key`, or
                `null` if there was no mapping for `key`.
                (A `null` return can also indicate that the map
                previously associated `null` with `key`.)
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the mappings from this map.
        The map will be empty after this call returns.
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this map for equality.  Returns
        `True` if the given object is also a map and the two maps
        represent identical object-reference mappings.  More formally, this
        map is equal to another map `m` if and only if
        `this.entrySet().equals(m.entrySet())`.
        
        **Owing to the reference-equality-based semantics of this map it is
        possible that the symmetry and transitivity requirements of the
        `Object.equals` contract may be violated if this map is compared
        to a normal map.  However, the `Object.equals` contract is
        guaranteed to hold among `IdentityHashMap` instances.**

        Arguments
        - o: object to be compared for equality with this map

        Returns
        - `True` if the specified object is equal to this map

        See
        - Object.equals(Object)
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this map.  The hash code of a map is
        defined to be the sum of the hash codes of each entry in the map's
        `entrySet()` view.  This ensures that `m1.equals(m2)`
        implies that `m1.hashCode()==m2.hashCode()` for any two
        `IdentityHashMap` instances `m1` and `m2`, as
        required by the general contract of Object.hashCode.
        
        **Owing to the reference-equality-based semantics of the
        `Map.Entry` instances in the set returned by this map's
        `entrySet` method, it is possible that the contractual
        requirement of `Object.hashCode` mentioned in the previous
        paragraph will be violated if one of the two objects being compared is
        an `IdentityHashMap` instance and the other is a normal map.**

        Returns
        - the hash code value for this map

        See
        - .equals(Object)
        """
        ...


    def clone(self) -> "Object":
        """
        Returns a shallow copy of this identity hash map: the keys and values
        themselves are not cloned.

        Returns
        - a shallow copy of this map
        """
        ...


    def keySet(self) -> set["K"]:
        """
        Returns an identity-based set view of the keys contained in this map.
        The set is backed by the map, so changes to the map are reflected in
        the set, and vice-versa.  If the map is modified while an iteration
        over the set is in progress, the results of the iteration are
        undefined.  The set supports element removal, which removes the
        corresponding mapping from the map, via the `Iterator.remove`,
        `Set.remove`, `removeAll`, `retainAll`, and
        `clear` methods.  It does not support the `add` or
        `addAll` methods.
        
        **While the object returned by this method implements the
        `Set` interface, it does *not* obey `Set's` general
        contract.  Like its backing map, the set returned by this method
        defines element equality as reference-equality rather than
        object-equality.  This affects the behavior of its `contains`,
        `remove`, `containsAll`, `equals`, and
        `hashCode` methods.**
        
        **The `equals` method of the returned set returns `True`
        only if the specified object is a set containing exactly the same
        object references as the returned set.  The symmetry and transitivity
        requirements of the `Object.equals` contract may be violated if
        the set returned by this method is compared to a normal set.  However,
        the `Object.equals` contract is guaranteed to hold among sets
        returned by this method.**
        
        The `hashCode` method of the returned set returns the sum of
        the *identity hashcodes* of the elements in the set, rather than
        the sum of their hashcodes.  This is mandated by the change in the
        semantics of the `equals` method, in order to enforce the
        general contract of the `Object.hashCode` method among sets
        returned by this method.

        Returns
        - an identity-based set view of the keys contained in this map

        See
        - System.identityHashCode(Object)
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a Collection view of the values contained in this map.
        The collection is backed by the map, so changes to the map are
        reflected in the collection, and vice-versa.  If the map is
        modified while an iteration over the collection is in progress,
        the results of the iteration are undefined.  The collection
        supports element removal, which removes the corresponding
        mapping from the map, via the `Iterator.remove`,
        `Collection.remove`, `removeAll`,
        `retainAll` and `clear` methods.  It does not
        support the `add` or `addAll` methods.
        
        **While the object returned by this method implements the
        `Collection` interface, it does *not* obey
        `Collection's` general contract.  Like its backing map,
        the collection returned by this method defines element equality as
        reference-equality rather than object-equality.  This affects the
        behavior of its `contains`, `remove` and
        `containsAll` methods.**
        """
        ...


    def entrySet(self) -> set["Map.Entry"["K", "V"]]:
        """
        Returns a Set view of the mappings contained in this map.
        Each element in the returned set is a reference-equality-based
        `Map.Entry`.  The set is backed by the map, so changes
        to the map are reflected in the set, and vice-versa.  If the
        map is modified while an iteration over the set is in progress,
        the results of the iteration are undefined.  The set supports
        element removal, which removes the corresponding mapping from
        the map, via the `Iterator.remove`, `Set.remove`,
        `removeAll`, `retainAll` and `clear`
        methods.  It does not support the `add` or
        `addAll` methods.
        
        Like the backing map, the `Map.Entry` objects in the set
        returned by this method define key and value equality as
        reference-equality rather than object-equality.  This affects the
        behavior of the `equals` and `hashCode` methods of these
        `Map.Entry` objects.  A reference-equality based `Map.Entry
        e` is equal to an object `o` if and only if `o` is a
        `Map.Entry` and `e.getKey()==o.getKey() &&
        e.getValue()==o.getValue()`.  To accommodate these equals
        semantics, the `hashCode` method returns
        `System.identityHashCode(e.getKey()) ^
        System.identityHashCode(e.getValue())`.
        
        **Owing to the reference-equality-based semantics of the
        `Map.Entry` instances in the set returned by this method,
        it is possible that the symmetry and transitivity requirements of
        the Object.equals(Object) contract may be violated if any of
        the entries in the set is compared to a normal map entry, or if
        the set returned by this method is compared to a set of normal map
        entries (such as would be returned by a call to this method on a normal
        map).  However, the `Object.equals` contract is guaranteed to
        hold among identity-based map entries, and among sets of such entries.
        **

        Returns
        - a set view of the identity-mappings contained in this map
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        ...
