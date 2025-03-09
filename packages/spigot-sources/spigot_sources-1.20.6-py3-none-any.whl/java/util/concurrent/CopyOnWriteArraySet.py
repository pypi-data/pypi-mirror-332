"""
Python module generated from Java source file java.util.concurrent.CopyOnWriteArraySet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import AbstractSet
from java.util import Iterator
from java.util import Objects
from java.util import Spliterator
from java.util.concurrent import *
from java.util.function import Consumer
from java.util.function import Predicate
from typing import Any, Callable, Iterable, Tuple


class CopyOnWriteArraySet(AbstractSet, Serializable):
    """
    A Set that uses an internal CopyOnWriteArrayList
    for all of its operations.  Thus, it shares the same basic properties:
    
     - It is best suited for applications in which set sizes generally
          stay small, read-only operations
          vastly outnumber mutative operations, and you need
          to prevent interference among threads during traversal.
     - It is thread-safe.
     - Mutative operations (`add`, `set`, `remove`, etc.)
         are expensive since they usually entail copying the entire underlying
         array.
     - Iterators do not support the mutative `remove` operation.
     - Traversal via iterators is fast and cannot encounter
         interference from other threads. Iterators rely on
         unchanging snapshots of the array at the time the iterators were
         constructed.
    
    
    **Sample Usage.** The following code sketch uses a
    copy-on-write set to maintain a set of Handler objects that
    perform some action upon state updates.
    
    ``` `class Handler { void handle() { ...` }
    
    class X {
      private final CopyOnWriteArraySet<Handler> handlers
        = new CopyOnWriteArraySet<>();
      public void addHandler(Handler h) { handlers.add(h); }
    
      private long internalState;
      private synchronized void changeState() { internalState = ...; }
    
      public void update() {
        changeState();
        for (Handler handler : handlers)
          handler.handle();
      }
    }}```
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this set

    Author(s)
    - Doug Lea

    See
    - CopyOnWriteArrayList

    Since
    - 1.5
    """

    def __init__(self):
        """
        Creates an empty set.
        """
        ...


    def __init__(self, c: Iterable["E"]):
        """
        Creates a set containing all of the elements of the specified
        collection.

        Arguments
        - c: the collection of elements to initially contain

        Raises
        - NullPointerException: if the specified collection is null
        """
        ...


    def size(self) -> int:
        """
        Returns the number of elements in this set.

        Returns
        - the number of elements in this set
        """
        ...


    def isEmpty(self) -> bool:
        """
        Returns `True` if this set contains no elements.

        Returns
        - `True` if this set contains no elements
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this set contains the specified element.
        More formally, returns `True` if and only if this set
        contains an element `e` such that `Objects.equals(o, e)`.

        Arguments
        - o: element whose presence in this set is to be tested

        Returns
        - `True` if this set contains the specified element
        """
        ...


    def toArray(self) -> list["Object"]:
        """
        Returns an array containing all of the elements in this set.
        If this set makes any guarantees as to what order its elements
        are returned by its iterator, this method must return the
        elements in the same order.
        
        The returned array will be "safe" in that no references to it
        are maintained by this set.  (In other words, this method must
        allocate a new array even if this set is backed by an array).
        The caller is thus free to modify the returned array.
        
        This method acts as bridge between array-based and collection-based
        APIs.

        Returns
        - an array containing all the elements in this set
        """
        ...


    def toArray(self, a: list["T"]) -> list["T"]:
        """
        Returns an array containing all of the elements in this set; the
        runtime type of the returned array is that of the specified array.
        If the set fits in the specified array, it is returned therein.
        Otherwise, a new array is allocated with the runtime type of the
        specified array and the size of this set.
        
        If this set fits in the specified array with room to spare
        (i.e., the array has more elements than this set), the element in
        the array immediately following the end of the set is set to
        `null`.  (This is useful in determining the length of this
        set *only* if the caller knows that this set does not contain
        any null elements.)
        
        If this set makes any guarantees as to what order its elements
        are returned by its iterator, this method must return the elements
        in the same order.
        
        Like the .toArray() method, this method acts as bridge between
        array-based and collection-based APIs.  Further, this method allows
        precise control over the runtime type of the output array, and may,
        under certain circumstances, be used to save allocation costs.
        
        Suppose `x` is a set known to contain only strings.
        The following code can be used to dump the set into a newly allocated
        array of `String`:
        
        ``` `String[] y = x.toArray(new String[0]);````
        
        Note that `toArray(new Object[0])` is identical in function to
        `toArray()`.

        Arguments
        - a: the array into which the elements of this set are to be
               stored, if it is big enough; otherwise, a new array of the same
               runtime type is allocated for this purpose.

        Returns
        - an array containing all the elements in this set

        Raises
        - ArrayStoreException: if the runtime type of the specified array
                is not a supertype of the runtime type of every element in this
                set
        - NullPointerException: if the specified array is null
        """
        ...


    def clear(self) -> None:
        """
        Removes all of the elements from this set.
        The set will be empty after this call returns.
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes the specified element from this set if it is present.
        More formally, removes an element `e` such that
        `Objects.equals(o, e)`, if this set contains such an element.
        Returns `True` if this set contained the element (or
        equivalently, if this set changed as a result of the call).
        (This set will not contain the element once the call returns.)

        Arguments
        - o: object to be removed from this set, if present

        Returns
        - `True` if this set contained the specified element
        """
        ...


    def add(self, e: "E") -> bool:
        """
        Adds the specified element to this set if it is not already present.
        More formally, adds the specified element `e` to this set if
        the set contains no element `e2` such that
        `Objects.equals(e, e2)`.
        If this set already contains the element, the call leaves the set
        unchanged and returns `False`.

        Arguments
        - e: element to be added to this set

        Returns
        - `True` if this set did not already contain the specified
                element
        """
        ...


    def containsAll(self, c: Iterable[Any]) -> bool:
        """
        Returns `True` if this set contains all of the elements of the
        specified collection.  If the specified collection is also a set, this
        method returns `True` if it is a *subset* of this set.

        Arguments
        - c: collection to be checked for containment in this set

        Returns
        - `True` if this set contains all of the elements of the
                specified collection

        Raises
        - NullPointerException: if the specified collection is null

        See
        - .contains(Object)
        """
        ...


    def addAll(self, c: Iterable["E"]) -> bool:
        """
        Adds all of the elements in the specified collection to this set if
        they're not already present.  If the specified collection is also a
        set, the `addAll` operation effectively modifies this set so
        that its value is the *union* of the two sets.  The behavior of
        this operation is undefined if the specified collection is modified
        while the operation is in progress.

        Arguments
        - c: collection containing elements to be added to this set

        Returns
        - `True` if this set changed as a result of the call

        Raises
        - NullPointerException: if the specified collection is null

        See
        - .add(Object)
        """
        ...


    def removeAll(self, c: Iterable[Any]) -> bool:
        """
        Removes from this set all of its elements that are contained in the
        specified collection.  If the specified collection is also a set,
        this operation effectively modifies this set so that its value is the
        *asymmetric set difference* of the two sets.

        Arguments
        - c: collection containing elements to be removed from this set

        Returns
        - `True` if this set changed as a result of the call

        Raises
        - ClassCastException: if the class of an element of this set
                is incompatible with the specified collection
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if this set contains a null element and the
                specified collection does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>),
                or if the specified collection is null

        See
        - .remove(Object)
        """
        ...


    def retainAll(self, c: Iterable[Any]) -> bool:
        """
        Retains only the elements in this set that are contained in the
        specified collection.  In other words, removes from this set all of
        its elements that are not contained in the specified collection.  If
        the specified collection is also a set, this operation effectively
        modifies this set so that its value is the *intersection* of the
        two sets.

        Arguments
        - c: collection containing elements to be retained in this set

        Returns
        - `True` if this set changed as a result of the call

        Raises
        - ClassCastException: if the class of an element of this set
                is incompatible with the specified collection
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if this set contains a null element and the
                specified collection does not permit null elements
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>),
                or if the specified collection is null

        See
        - .remove(Object)
        """
        ...


    def iterator(self) -> Iterator["E"]:
        """
        Returns an iterator over the elements contained in this set
        in the order in which these elements were added.
        
        The returned iterator provides a snapshot of the state of the set
        when the iterator was constructed. No synchronization is needed while
        traversing the iterator. The iterator does *NOT* support the
        `remove` method.

        Returns
        - an iterator over the elements in this set
        """
        ...


    def equals(self, o: "Object") -> bool:
        """
        Compares the specified object with this set for equality.
        Returns `True` if the specified object is the same object
        as this object, or if it is also a Set and the elements
        returned by an Set.iterator() iterator over the
        specified set are the same as the elements returned by an
        iterator over this set.  More formally, the two iterators are
        considered to return the same elements if they return the same
        number of elements and for every element `e1` returned by
        the iterator over the specified set, there is an element
        `e2` returned by the iterator over this set such that
        `Objects.equals(e1, e2)`.

        Arguments
        - o: object to be compared for equality with this set

        Returns
        - `True` if the specified object is equal to this set
        """
        ...


    def removeIf(self, filter: "Predicate"["E"]) -> bool:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def forEach(self, action: "Consumer"["E"]) -> None:
        """
        Raises
        - NullPointerException: 
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        """
        Returns a Spliterator over the elements in this set in the order
        in which these elements were added.
        
        The `Spliterator` reports Spliterator.IMMUTABLE,
        Spliterator.DISTINCT, Spliterator.SIZED, and
        Spliterator.SUBSIZED.
        
        The spliterator provides a snapshot of the state of the set
        when the spliterator was constructed. No synchronization is needed while
        operating on the spliterator.

        Returns
        - a `Spliterator` over the elements in this set

        Since
        - 1.8
        """
        ...
