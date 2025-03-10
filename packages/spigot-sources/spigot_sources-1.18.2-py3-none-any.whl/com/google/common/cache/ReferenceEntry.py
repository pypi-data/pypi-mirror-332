"""
Python module generated from Java source file com.google.common.cache.ReferenceEntry

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.cache import *
from com.google.common.cache.LocalCache import ValueReference
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class ReferenceEntry:
    """
    An entry in a reference map.
    
    Entries in the map can be in the following states:
    
    Valid:
    
    
      - Live: valid key/value are set
      - Loading: loading is pending
    
    
    Invalid:
    
    
      - Expired: time expired (key/value may still be set)
      - Collected: key/value was partially collected, but not yet cleaned up
      - Unset: marked as unset, awaiting cleanup or reuse
    """

    def getValueReference(self) -> "ValueReference"["K", "V"]:
        """
        Returns the value reference from this entry.
        """
        ...


    def setValueReference(self, valueReference: "ValueReference"["K", "V"]) -> None:
        """
        Sets the value reference for this entry.
        """
        ...


    def getNext(self) -> "ReferenceEntry"["K", "V"]:
        """
        Returns the next entry in the chain.
        """
        ...


    def getHash(self) -> int:
        """
        Returns the entry's hash.
        """
        ...


    def getKey(self) -> "K":
        """
        Returns the key for this entry.
        """
        ...


    def getAccessTime(self) -> int:
        """
        Returns the time that this entry was last accessed, in ns.
        """
        ...


    def setAccessTime(self, time: int) -> None:
        """
        Sets the entry access time in ns.
        """
        ...


    def getNextInAccessQueue(self) -> "ReferenceEntry"["K", "V"]:
        """
        Returns the next entry in the access queue.
        """
        ...


    def setNextInAccessQueue(self, next: "ReferenceEntry"["K", "V"]) -> None:
        """
        Sets the next entry in the access queue.
        """
        ...


    def getPreviousInAccessQueue(self) -> "ReferenceEntry"["K", "V"]:
        """
        Returns the previous entry in the access queue.
        """
        ...


    def setPreviousInAccessQueue(self, previous: "ReferenceEntry"["K", "V"]) -> None:
        """
        Sets the previous entry in the access queue.
        """
        ...


    def getWriteTime(self) -> int:
        ...


    def setWriteTime(self, time: int) -> None:
        """
        Sets the entry write time in ns.
        """
        ...


    def getNextInWriteQueue(self) -> "ReferenceEntry"["K", "V"]:
        """
        Returns the next entry in the write queue.
        """
        ...


    def setNextInWriteQueue(self, next: "ReferenceEntry"["K", "V"]) -> None:
        """
        Sets the next entry in the write queue.
        """
        ...


    def getPreviousInWriteQueue(self) -> "ReferenceEntry"["K", "V"]:
        """
        Returns the previous entry in the write queue.
        """
        ...


    def setPreviousInWriteQueue(self, previous: "ReferenceEntry"["K", "V"]) -> None:
        """
        Sets the previous entry in the write queue.
        """
        ...
