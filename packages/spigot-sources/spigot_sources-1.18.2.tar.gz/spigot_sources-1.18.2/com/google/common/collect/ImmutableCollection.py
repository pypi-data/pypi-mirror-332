"""
Python module generated from Java source file com.google.common.collect.ImmutableCollection

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from com.google.errorprone.annotations import CanIgnoreReturnValue
from com.google.errorprone.annotations import DoNotCall
from com.google.errorprone.annotations import DoNotMock
from java.io import Serializable
from java.util import AbstractCollection
from java.util import Collections
from java.util import Iterator
from java.util import Spliterator
from java.util.function import Predicate
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class ImmutableCollection(AbstractCollection, Serializable):
    """
    A Collection whose contents will never change, and which offers a few additional
    guarantees detailed below.
    
    **Warning:** avoid *direct* usage of ImmutableCollection as a type (just as
    with Collection itself). Prefer subtypes such as ImmutableSet or ImmutableList, which have well-defined .equals semantics, thus avoiding a common source
    of bugs and confusion.
    
    <h3>About *all* `Immutable-` collections</h3>
    
    The remainder of this documentation applies to every public `Immutable-` type in this
    package, whether it is a subtype of `ImmutableCollection` or not.
    
    <h4>Guarantees</h4>
    
    Each makes the following guarantees:
    
    
      - **Shallow immutability.** Elements can never be added, removed or replaced in this
          collection. This is a stronger guarantee than that of Collections.unmodifiableCollection, whose contents change whenever the wrapped collection
          is modified.
      - **Null-hostility.** This collection will never contain a null element.
      - **Deterministic iteration.** The iteration order is always well-defined, depending on
          how the collection was created. Typically this is insertion order unless an explicit
          ordering is otherwise specified (e.g. ImmutableSortedSet.naturalOrder). See the
          appropriate factory method for details. View collections such as ImmutableMultiset.elementSet iterate in the same order as the parent, except as noted.
      - **Thread safety.** It is safe to access this collection concurrently from multiple
          threads.
      - **Integrity.** This type cannot be subclassed outside this package (which would allow
          these guarantees to be violated).
    
    
    <h4>"Interfaces", not implementations</h4>
    
    These are classes instead of interfaces to prevent external subtyping, but should be thought
    of as interfaces in every important sense. Each public class such as ImmutableSet is a
    *type* offering meaningful behavioral guarantees. This is substantially different from the
    case of (say) HashSet, which is an *implementation*, with semantics that were
    largely defined by its supertype.
    
    For field types and method return types, you should generally use the immutable type (such as
    ImmutableList) instead of the general collection interface type (such as List).
    This communicates to your callers all of the semantic guarantees listed above, which is almost
    always very useful information.
    
    On the other hand, a *parameter* type of ImmutableList is generally a nuisance to
    callers. Instead, accept Iterable and have your method or constructor body pass it to the
    appropriate `copyOf` method itself.
    
    Expressing the immutability guarantee directly in the type that user code references is a
    powerful advantage. Although Java offers certain immutable collection factory methods, such as
    Collections.singleton(Object) and <a
    href="https://docs.oracle.com/javase/9/docs/api/java/util/Set.html#immutable">`Set.of`</a>,
    we recommend using *these* classes instead for this reason (as well as for consistency).
    
    <h4>Creation</h4>
    
    Except for logically "abstract" types like `ImmutableCollection` itself, each `Immutable` type provides the static operations you need to obtain instances of that type. These
    usually include:
    
    
      - Static methods named `of`, accepting an explicit list of elements or entries.
      - Static methods named `copyOf` (or `copyOfSorted`), accepting an existing
          collection whose contents should be copied.
      - A static nested `Builder` class which can be used to populate a new immutable
          instance.
    
    
    <h4>Warnings</h4>
    
    
      - **Warning:** as with any collection, it is almost always a bad idea to modify an element
          (in a way that affects its Object.equals behavior) while it is contained in a
          collection. Undefined behavior and bugs will result. It's generally best to avoid using
          mutable objects as elements at all, as many users may expect your "immutable" object to be
          *deeply* immutable.
    
    
    <h4>Performance notes</h4>
    
    
      - Implementations can be generally assumed to prioritize memory efficiency, then speed of
          access, and lastly speed of creation.
      - The `copyOf` methods will sometimes recognize that the actual copy operation is
          unnecessary; for example, `copyOf(copyOf(anArrayList))` should copy the data only
          once. This reduces the expense of habitually making defensive copies at API boundaries.
          However, the precise conditions for skipping the copy operation are undefined.
      - **Warning:** a view collection such as ImmutableMap.keySet or ImmutableList.subList may retain a reference to the entire data set, preventing it from
          being garbage collected. If some of the data is no longer reachable through other means,
          this constitutes a memory leak. Pass the view collection to the appropriate `copyOf`
          method to obtain a correctly-sized copy.
      - The performance of using the associated `Builder` class can be assumed to be no
          worse, and possibly better, than creating a mutable collection and copying it.
      - Implementations generally do not cache hash codes. If your element or key type has a slow
          `hashCode` implementation, it should cache it itself.
    
    
    <h4>Example usage</h4>
    
    ````class Foo {
      private static final ImmutableSet<String> RESERVED_CODES =
          ImmutableSet.of("AZ", "CQ", "ZX");
    
      private final ImmutableSet<String> codes;
    
      public Foo(Iterable<String> codes) {
        this.codes = ImmutableSet.copyOf(codes);
        checkArgument(Collections.disjoint(this.codes, RESERVED_CODES));`
    }
    }```
    
    <h3>See also</h3>
    
    See the Guava User Guide article on <a href=
    "https://github.com/google/guava/wiki/ImmutableCollectionsExplained"> immutable collections</a>.

    Since
    - 2.0
    """

    def iterator(self) -> "UnmodifiableIterator"["E"]:
        """
        Returns an unmodifiable iterator across the elements in this collection.
        """
        ...


    def spliterator(self) -> "Spliterator"["E"]:
        ...


    def toArray(self) -> list["Object"]:
        ...


    def toArray(self, other: list["T"]) -> list["T"]:
        ...


    def contains(self, object: "Object") -> bool:
        ...


    def add(self, e: "E") -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def remove(self, object: "Object") -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def addAll(self, newElements: Iterable["E"]) -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def removeAll(self, oldElements: Iterable[Any]) -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def removeIf(self, filter: "Predicate"["E"]) -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def retainAll(self, elementsToKeep: Iterable[Any]) -> bool:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def clear(self) -> None:
        """
        Guaranteed to throw an exception and leave the collection unmodified.

        Raises
        - UnsupportedOperationException: always

        Deprecated
        - Unsupported operation.
        """
        ...


    def asList(self) -> "ImmutableList"["E"]:
        """
        Returns an `ImmutableList` containing the same elements, in the same order, as this
        collection.
        
        **Performance note:** in most cases this method can return quickly without actually
        copying anything. The exact circumstances under which the copy is performed are undefined and
        subject to change.

        Since
        - 2.0
        """
        ...


    class Builder:
        """
        Abstract base class for builders of ImmutableCollection types.

        Since
        - 10.0
        """

        def add(self, element: "E") -> "Builder"["E"]:
            """
            Adds `element` to the `ImmutableCollection` being built.
            
            Note that each builder class covariantly returns its own type from this method.

            Arguments
            - element: the element to add

            Returns
            - this `Builder` instance

            Raises
            - NullPointerException: if `element` is null
            """
            ...


        def add(self, *elements: Tuple["E", ...]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableCollection` being built.
            
            Note that each builder class overrides this method in order to covariantly return its own
            type.

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` instance

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterable["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableCollection` being built.
            
            Note that each builder class overrides this method in order to covariantly return its own
            type.

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` instance

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def addAll(self, elements: Iterator["E"]) -> "Builder"["E"]:
            """
            Adds each element of `elements` to the `ImmutableCollection` being built.
            
            Note that each builder class overrides this method in order to covariantly return its own
            type.

            Arguments
            - elements: the elements to add

            Returns
            - this `Builder` instance

            Raises
            - NullPointerException: if `elements` is null or contains a null element
            """
            ...


        def build(self) -> "ImmutableCollection"["E"]:
            """
            Returns a newly-created `ImmutableCollection` of the appropriate type, containing the
            elements provided to this builder.
            
            Note that each builder class covariantly returns the appropriate type of `ImmutableCollection` from this method.
            """
            ...
