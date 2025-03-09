"""
Python module generated from Java source file java.util.EnumMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class EnumMap(AbstractMap, Serializable, Cloneable):
    """
    A specialized Map implementation for use with enum type keys.  All
    of the keys in an enum map must come from a single enum type that is
    specified, explicitly or implicitly, when the map is created.  Enum maps
    are represented internally as arrays.  This representation is extremely
    compact and efficient.
    
    Enum maps are maintained in the *natural order* of their keys
    (the order in which the enum constants are declared).  This is reflected
    in the iterators returned by the collections views (.keySet(),
    .entrySet(), and .values()).
    
    Iterators returned by the collection views are *weakly consistent*:
    they will never throw ConcurrentModificationException and they may
    or may not show the effects of any modifications to the map that occur while
    the iteration is in progress.
    
    Null keys are not permitted.  Attempts to insert a null key will
    throw NullPointerException.  Attempts to test for the
    presence of a null key or to remove one will, however, function properly.
    Null values are permitted.
    
    <P>Like most collection implementations `EnumMap` is not
    synchronized. If multiple threads access an enum map concurrently, and at
    least one of the threads modifies the map, it should be synchronized
    externally.  This is typically accomplished by synchronizing on some
    object that naturally encapsulates the enum map.  If no such object exists,
    the map should be "wrapped" using the Collections.synchronizedMap
    method.  This is best done at creation time, to prevent accidental
    unsynchronized access:
    
    ```
        Map&lt;EnumKey, V&gt; m
            = Collections.synchronizedMap(new EnumMap&lt;EnumKey, V&gt;(...));
    ```
    
    Implementation note: All basic operations execute in constant time.
    They are likely (though not guaranteed) to be faster than their
    HashMap counterparts.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.

    Author(s)
    - Josh Bloch

    See
    - EnumSet

    Since
    - 1.5
    """

    def __init__(self, keyType: type["K"]):
        """
        Creates an empty enum map with the specified key type.

        Arguments
        - keyType: the class object of the key type for this enum map

        Raises
        - NullPointerException: if `keyType` is null
        """
        ...


    def __init__(self, m: "EnumMap"["K", "V"]):
        """
        Creates an enum map with the same key type as the specified enum
        map, initially containing the same mappings (if any).

        Arguments
        - m: the enum map from which to initialize this enum map

        Raises
        - NullPointerException: if `m` is null
        """
        ...


    def __init__(self, m: dict["K", "V"]):
        """
        Creates an enum map initialized from the specified map.  If the
        specified map is an `EnumMap` instance, this constructor behaves
        identically to .EnumMap(EnumMap).  Otherwise, the specified map
        must contain at least one mapping (in order to determine the new
        enum map's key type).

        Arguments
        - m: the map from which to initialize this enum map

        Raises
        - IllegalArgumentException: if `m` is not an
            `EnumMap` instance and contains no mappings
        - NullPointerException: if `m` is null
        """
        ...


    def size(self) -> int:
        """
        Returns the number of key-value mappings in this map.

        Returns
        - the number of key-value mappings in this map
        """
        ...


    def containsValue(self, value: "Object") -> bool:
        """
        Returns `True` if this map maps one or more keys to the
        specified value.

        Arguments
        - value: the value whose presence in this map is to be tested

        Returns
        - `True` if this map maps one or more keys to this value
        """
        ...


    def containsKey(self, key: "Object") -> bool:
        """
        Returns `True` if this map contains a mapping for the specified
        key.

        Arguments
        - key: the key whose presence in this map is to be tested

        Returns
        - `True` if this map contains a mapping for the specified
                   key
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
        """
        ...


    def put(self, key: "K", value: "V") -> "V":
        """
        Associates the specified value with the specified key in this map.
        If the map previously contained a mapping for this key, the old
        value is replaced.

        Arguments
        - key: the key with which the specified value is to be associated
        - value: the value to be associated with the specified key

        Returns
        - the previous value associated with specified key, or
            `null` if there was no mapping for key.  (A `null`
            return can also indicate that the map previously associated
            `null` with the specified key.)

        Raises
        - NullPointerException: if the specified key is null
        """
        ...


    def remove(self, key: "Object") -> "V":
        """
        Removes the mapping for this key from this map if present.

        Arguments
        - key: the key whose mapping is to be removed from the map

        Returns
        - the previous value associated with specified key, or
            `null` if there was no entry for key.  (A `null`
            return can also indicate that the map previously associated
            `null` with the specified key.)
        """
        ...


    def putAll(self, m: dict["K", "V"]) -> None:
        """
        Copies all of the mappings from the specified map to this map.
        These mappings will replace any mappings that this map had for
        any of the keys currently in the specified map.

        Arguments
        - m: the mappings to be stored in this map

        Raises
        - NullPointerException: the specified map is null, or if
            one or more keys in the specified map are null
        """
        ...


    def clear(self) -> None:
        """
        Removes all mappings from this map.
        """
        ...


    def keySet(self) -> set["K"]:
        """
        Returns a Set view of the keys contained in this map.
        The returned set obeys the general contract outlined in
        Map.keySet().  The set's iterator will return the keys
        in their natural order (the order in which the enum constants
        are declared).

        Returns
        - a set view of the keys contained in this enum map
        """
        ...


    def values(self) -> Iterable["V"]:
        """
        Returns a Collection view of the values contained in this map.
        The returned collection obeys the general contract outlined in
        Map.values().  The collection's iterator will return the
        values in the order their corresponding keys appear in map,
        which is their natural order (the order in which the enum constants
        are declared).

        Returns
        - a collection view of the values contained in this map
        """
        ...


    def entrySet(self) -> set["Map.Entry"["K", "V"]]:
        """
        Returns a Set view of the mappings contained in this map.
        The returned set obeys the general contract outlined in
        Map.keySet().  The set's iterator will return the
        mappings in the order their keys appear in map, which is their
        natural order (the order in which the enum constants are declared).

        Returns
        - a set view of the mappings contained in this enum map
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this map for equality.  Returns
        `True` if the given object is also a map and the two maps
        represent the same mappings, as specified in the Map.equals(Object) contract.

        Arguments
        - o: the object to be compared for equality with this map

        Returns
        - `True` if the specified object is equal to this map
        """
        ...


    def hashCode(self) -> int:
        """
        Returns the hash code value for this map.  The hash code of a map is
        defined to be the sum of the hash codes of each entry in the map.
        """
        ...


    def clone(self) -> "EnumMap"["K", "V"]:
        """
        Returns a shallow copy of this enum map. The values themselves
        are not cloned.

        Returns
        - a shallow copy of this enum map
        """
        ...
