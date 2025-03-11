"""
Python module generated from Java source file com.google.common.collect.BiMap

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class BiMap(Map):
    """
    A bimap (or "bidirectional map") is a map that preserves the uniqueness of its values as well as
    that of its keys. This constraint enables bimaps to support an "inverse view", which is another
    bimap containing the same entries as this bimap but with reversed keys and values.
    
    <h3>Implementations</h3>
    
    
      - ImmutableBiMap
      - HashBiMap
      - EnumBiMap
      - EnumHashBiMap
    
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/NewCollectionTypesExplained#bimap">`BiMap`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def put(self, key: "K", value: "V") -> "V":
        """
        Raises
        - IllegalArgumentException: if the given value is already bound to a different key in this
            bimap. The bimap will remain unmodified in this event. To avoid this exception, call .forcePut instead.
        """
        ...


    def forcePut(self, key: "K", value: "V") -> "V":
        """
        An alternate form of `put` that silently removes any existing entry with the value `value` before proceeding with the .put operation. If the bimap previously contained the
        provided key-value mapping, this method has no effect.
        
        Note that a successful call to this method could cause the size of the bimap to increase by
        one, stay the same, or even decrease by one.
        
        **Warning:** If an existing entry with this value is removed, the key for that entry is
        discarded and not returned.

        Arguments
        - key: the key with which the specified value is to be associated
        - value: the value to be associated with the specified key

        Returns
        - the value that was previously associated with the key, or `null` if there was no
            previous entry. (If the bimap contains null values, then `forcePut`, like `put`, returns `null` both if the key is absent and if it is present with a null
            value.)
        """
        ...


    def putAll(self, map: dict["K", "V"]) -> None:
        """
        
        
        **Warning:** the results of calling this method may vary depending on the iteration order
        of `map`.

        Raises
        - IllegalArgumentException: if an attempt to `put` any entry fails. Note that some
            map entries may have been added to the bimap before the exception was thrown.
        """
        ...


    def values(self) -> set["V"]:
        """
        
        
        Because a bimap has unique values, this method returns a Set, instead of the java.util.Collection specified in the Map interface.
        """
        ...


    def inverse(self) -> "BiMap"["V", "K"]:
        """
        Returns the inverse view of this bimap, which maps each of this bimap's values to its
        associated key. The two bimaps are backed by the same data; any changes to one will appear in
        the other.
        
        **Note:**There is no guaranteed correspondence between the iteration order of a bimap and
        that of its inverse.

        Returns
        - the inverse view of this bimap
        """
        ...
