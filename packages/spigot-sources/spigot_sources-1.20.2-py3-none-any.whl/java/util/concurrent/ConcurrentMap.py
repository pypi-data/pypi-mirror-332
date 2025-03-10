"""
Python module generated from Java source file java.util.concurrent.ConcurrentMap

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Objects
from java.util.concurrent import *
from java.util.function import BiConsumer
from java.util.function import BiFunction
from java.util.function import Function
from typing import Any, Callable, Iterable, Tuple


class ConcurrentMap(Map):
    """
    A Map providing thread safety and atomicity guarantees.
    
    To maintain the specified guarantees, default implementations of
    methods including .putIfAbsent inherited from Map
    must be overridden by implementations of this interface. Similarly,
    implementations of the collections returned by methods .keySet, .values, and .entrySet must override
    methods such as `removeIf` when necessary to
    preserve atomicity guarantees.
    
    Memory consistency effects: As with other concurrent
    collections, actions in a thread prior to placing an object into a
    `ConcurrentMap` as a key or value
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions subsequent to the access or removal of that object from
    the `ConcurrentMap` in another thread.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<K>`: the type of keys maintained by this map
    
    Type `<V>`: the type of mapped values

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def getOrDefault(self, key: "Object", defaultValue: "V") -> "V":
        """
        Raises
        - ClassCastException: 
        - NullPointerException: 

        Since
        - 1.8

        Unknown Tags
        - This implementation assumes that the ConcurrentMap cannot
        contain null values and `get()` returning null unambiguously means
        the key is absent. Implementations which support null values
        <strong>must</strong> override this default implementation.
        """
        ...


    def forEach(self, action: "BiConsumer"["K", "V"]) -> None:
        """
        Raises
        - NullPointerException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to, for this
        `map`:
        ``` `for (Map.Entry<K,V> entry : map.entrySet()) {
          action.accept(entry.getKey(), entry.getValue());`}```
        - The default implementation assumes that
        `IllegalStateException` thrown by `getKey()` or
        `getValue()` indicates that the entry has been removed and cannot
        be processed. Operation continues for subsequent entries.
        """
        ...


    def putIfAbsent(self, key: "K", value: "V") -> "V":
        """
        If the specified key is not already associated
        with a value, associates it with the given value.
        This is equivalent to, for this `map`:
        ``` `if (!map.containsKey(key))
          return map.put(key, value);
        else
          return map.get(key);````
        
        except that the action is performed atomically.

        Arguments
        - key: key with which the specified value is to be associated
        - value: value to be associated with the specified key

        Returns
        - the previous value associated with the specified key, or
                `null` if there was no mapping for the key.
                (A `null` return can also indicate that the map
                previously associated `null` with the key,
                if the implementation supports null values.)

        Raises
        - UnsupportedOperationException: if the `put` operation
                is not supported by this map
        - ClassCastException: if the class of the specified key or value
                prevents it from being stored in this map
        - NullPointerException: if the specified key or value is null,
                and this map does not permit null keys or values
        - IllegalArgumentException: if some property of the specified key
                or value prevents it from being stored in this map

        Unknown Tags
        - This implementation intentionally re-abstracts the
        inappropriate default provided in `Map`.
        """
        ...


    def remove(self, key: "Object", value: "Object") -> bool:
        """
        Removes the entry for a key only if currently mapped to a given value.
        This is equivalent to, for this `map`:
        ``` `if (map.containsKey(key)
            && Objects.equals(map.get(key), value)) {
          map.remove(key);
          return True;` else {
          return False;
        }}```
        
        except that the action is performed atomically.

        Arguments
        - key: key with which the specified value is associated
        - value: value expected to be associated with the specified key

        Returns
        - `True` if the value was removed

        Raises
        - UnsupportedOperationException: if the `remove` operation
                is not supported by this map
        - ClassCastException: if the key or value is of an inappropriate
                type for this map
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified key or value is null,
                and this map does not permit null keys or values
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)

        Unknown Tags
        - This implementation intentionally re-abstracts the
        inappropriate default provided in `Map`.
        """
        ...


    def replace(self, key: "K", oldValue: "V", newValue: "V") -> bool:
        """
        Replaces the entry for a key only if currently mapped to a given value.
        This is equivalent to, for this `map`:
        ``` `if (map.containsKey(key)
            && Objects.equals(map.get(key), oldValue)) {
          map.put(key, newValue);
          return True;` else {
          return False;
        }}```
        
        except that the action is performed atomically.

        Arguments
        - key: key with which the specified value is associated
        - oldValue: value expected to be associated with the specified key
        - newValue: value to be associated with the specified key

        Returns
        - `True` if the value was replaced

        Raises
        - UnsupportedOperationException: if the `put` operation
                is not supported by this map
        - ClassCastException: if the class of a specified key or value
                prevents it from being stored in this map
        - NullPointerException: if a specified key or value is null,
                and this map does not permit null keys or values
        - IllegalArgumentException: if some property of a specified key
                or value prevents it from being stored in this map

        Unknown Tags
        - This implementation intentionally re-abstracts the
        inappropriate default provided in `Map`.
        """
        ...


    def replace(self, key: "K", value: "V") -> "V":
        """
        Replaces the entry for a key only if currently mapped to some value.
        This is equivalent to, for this `map`:
        ``` `if (map.containsKey(key))
          return map.put(key, value);
        else
          return null;````
        
        except that the action is performed atomically.

        Arguments
        - key: key with which the specified value is associated
        - value: value to be associated with the specified key

        Returns
        - the previous value associated with the specified key, or
                `null` if there was no mapping for the key.
                (A `null` return can also indicate that the map
                previously associated `null` with the key,
                if the implementation supports null values.)

        Raises
        - UnsupportedOperationException: if the `put` operation
                is not supported by this map
        - ClassCastException: if the class of the specified key or value
                prevents it from being stored in this map
        - NullPointerException: if the specified key or value is null,
                and this map does not permit null keys or values
        - IllegalArgumentException: if some property of the specified key
                or value prevents it from being stored in this map

        Unknown Tags
        - This implementation intentionally re-abstracts the
        inappropriate default provided in `Map`.
        """
        ...


    def replaceAll(self, function: "BiFunction"["K", "V", "V"]) -> None:
        """
        Raises
        - UnsupportedOperationException: 
        - NullPointerException: 
        - ClassCastException: 
        - IllegalArgumentException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to, for this `map`:
        ``` `for (Map.Entry<K,V> entry : map.entrySet()) {
          K k;
          V v;
          do {
            k = entry.getKey();
            v = entry.getValue();` while (!map.replace(k, v, function.apply(k, v)));
        }}```
        
        The default implementation may retry these steps when multiple
        threads attempt updates including potentially calling the function
        repeatedly for a given key.
        
        This implementation assumes that the ConcurrentMap cannot contain null
        values and `get()` returning null unambiguously means the key is
        absent. Implementations which support null values <strong>must</strong>
        override this default implementation.
        """
        ...


    def computeIfAbsent(self, key: "K", mappingFunction: "Function"["K", "V"]) -> "V":
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to the following steps for this
        `map`:
        
        ``` `V oldValue, newValue;
        return ((oldValue = map.get(key)) == null
                && (newValue = mappingFunction.apply(key)) != null
                && (oldValue = map.putIfAbsent(key, newValue)) == null)
          ? newValue
          : oldValue;````
        
        This implementation assumes that the ConcurrentMap cannot contain null
        values and `get()` returning null unambiguously means the key is
        absent. Implementations which support null values <strong>must</strong>
        override this default implementation.
        """
        ...


    def computeIfPresent(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to performing the following
        steps for this `map`:
        
        ``` `for (V oldValue; (oldValue = map.get(key)) != null; ) {
          V newValue = remappingFunction.apply(key, oldValue);
          if ((newValue == null)
              ? map.remove(key, oldValue)
              : map.replace(key, oldValue, newValue))
            return newValue;`
        return null;}```
        When multiple threads attempt updates, map operations and the
        remapping function may be called multiple times.
        
        This implementation assumes that the ConcurrentMap cannot contain null
        values and `get()` returning null unambiguously means the key is
        absent. Implementations which support null values <strong>must</strong>
        override this default implementation.
        """
        ...


    def compute(self, key: "K", remappingFunction: "BiFunction"["K", "V", "V"]) -> "V":
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to performing the following
        steps for this `map`:
        
        ``` `for (;;) {
          V oldValue = map.get(key);
          V newValue = remappingFunction.apply(key, oldValue);
          if (newValue != null) {
            if ((oldValue != null)
              ? map.replace(key, oldValue, newValue)
              : map.putIfAbsent(key, newValue) == null)
              return newValue;` else if (oldValue == null || map.remove(key, oldValue)) {
            return null;
          }
        }}```
        When multiple threads attempt updates, map operations and the
        remapping function may be called multiple times.
        
        This implementation assumes that the ConcurrentMap cannot contain null
        values and `get()` returning null unambiguously means the key is
        absent. Implementations which support null values <strong>must</strong>
        override this default implementation.
        """
        ...


    def merge(self, key: "K", value: "V", remappingFunction: "BiFunction"["V", "V", "V"]) -> "V":
        """
        Raises
        - UnsupportedOperationException: 
        - ClassCastException: 
        - NullPointerException: 
        - IllegalArgumentException: 

        Since
        - 1.8

        Unknown Tags
        - The default implementation is equivalent to performing the following
        steps for this `map`:
        
        ``` `for (;;) {
          V oldValue = map.get(key);
          if (oldValue != null) {
            V newValue = remappingFunction.apply(oldValue, value);
            if (newValue != null) {
              if (map.replace(key, oldValue, newValue))
                return newValue;` else if (map.remove(key, oldValue)) {
              return null;
            }
          } else if (map.putIfAbsent(key, value) == null) {
            return value;
          }
        }}```
        When multiple threads attempt updates, map operations and the
        remapping function may be called multiple times.
        
        This implementation assumes that the ConcurrentMap cannot contain null
        values and `get()` returning null unambiguously means the key is
        absent. Implementations which support null values <strong>must</strong>
        override this default implementation.
        """
        ...
