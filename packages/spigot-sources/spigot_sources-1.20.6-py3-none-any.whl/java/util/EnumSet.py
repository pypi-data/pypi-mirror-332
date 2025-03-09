"""
Python module generated from Java source file java.util.EnumSet

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from jdk.internal.access import SharedSecrets
from typing import Any, Callable, Iterable, Tuple


class EnumSet(AbstractSet, Cloneable, Serializable):
    """
    A specialized Set implementation for use with enum types.  All of
    the elements in an enum set must come from a single enum type that is
    specified, explicitly or implicitly, when the set is created.  Enum sets
    are represented internally as bit vectors.  This representation is
    extremely compact and efficient. The space and time performance of this
    class should be good enough to allow its use as a high-quality, typesafe
    alternative to traditional `int`-based "bit flags."  Even bulk
    operations (such as `containsAll` and `retainAll`) should
    run very quickly if their argument is also an enum set.
    
    The iterator returned by the `iterator` method traverses the
    elements in their *natural order* (the order in which the enum
    constants are declared).  The returned iterator is *weakly
    consistent*: it will never throw ConcurrentModificationException
    and it may or may not show the effects of any modifications to the set that
    occur while the iteration is in progress.
    
    Null elements are not permitted.  Attempts to insert a null element
    will throw NullPointerException.  Attempts to test for the
    presence of a null element or to remove one will, however, function
    properly.
    
    <P>Like most collection implementations, `EnumSet` is not
    synchronized.  If multiple threads access an enum set concurrently, and at
    least one of the threads modifies the set, it should be synchronized
    externally.  This is typically accomplished by synchronizing on some
    object that naturally encapsulates the enum set.  If no such object exists,
    the set should be "wrapped" using the Collections.synchronizedSet
    method.  This is best done at creation time, to prevent accidental
    unsynchronized access:
    
    ```
    Set&lt;MyEnum&gt; s = Collections.synchronizedSet(EnumSet.noneOf(MyEnum.class));
    ```
    
    Implementation note: All basic operations execute in constant time.
    They are likely (though not guaranteed) to be much faster than their
    HashSet counterparts.  Even bulk operations execute in
    constant time if their argument is also an enum set.
    
    This class is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.

    Author(s)
    - Josh Bloch

    See
    - EnumMap

    Since
    - 1.5
    """

    @staticmethod
    def noneOf(elementType: type["E"]) -> "EnumSet"["E"]:
        """
        Creates an empty enum set with the specified element type.
        
        Type `<E>`: The class of the elements in the set

        Arguments
        - elementType: the class object of the element type for this enum
            set

        Returns
        - An empty enum set of the specified type.

        Raises
        - NullPointerException: if `elementType` is null
        """
        ...


    @staticmethod
    def allOf(elementType: type["E"]) -> "EnumSet"["E"]:
        """
        Creates an enum set containing all of the elements in the specified
        element type.
        
        Type `<E>`: The class of the elements in the set

        Arguments
        - elementType: the class object of the element type for this enum
            set

        Returns
        - An enum set containing all the elements in the specified type.

        Raises
        - NullPointerException: if `elementType` is null
        """
        ...


    @staticmethod
    def copyOf(s: "EnumSet"["E"]) -> "EnumSet"["E"]:
        """
        Creates an enum set with the same element type as the specified enum
        set, initially containing the same elements (if any).
        
        Type `<E>`: The class of the elements in the set

        Arguments
        - s: the enum set from which to initialize this enum set

        Returns
        - A copy of the specified enum set.

        Raises
        - NullPointerException: if `s` is null
        """
        ...


    @staticmethod
    def copyOf(c: Iterable["E"]) -> "EnumSet"["E"]:
        """
        Creates an enum set initialized from the specified collection.  If
        the specified collection is an `EnumSet` instance, this static
        factory method behaves identically to .copyOf(EnumSet).
        Otherwise, the specified collection must contain at least one element
        (in order to determine the new enum set's element type).
        
        Type `<E>`: The class of the elements in the collection

        Arguments
        - c: the collection from which to initialize this enum set

        Returns
        - An enum set initialized from the given collection.

        Raises
        - IllegalArgumentException: if `c` is not an
            `EnumSet` instance and contains no elements
        - NullPointerException: if `c` is null
        """
        ...


    @staticmethod
    def complementOf(s: "EnumSet"["E"]) -> "EnumSet"["E"]:
        """
        Creates an enum set with the same element type as the specified enum
        set, initially containing all the elements of this type that are
        *not* contained in the specified set.
        
        Type `<E>`: The class of the elements in the enum set

        Arguments
        - s: the enum set from whose complement to initialize this enum set

        Returns
        - The complement of the specified set in this set

        Raises
        - NullPointerException: if `s` is null
        """
        ...


    @staticmethod
    def of(e: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified element.
        
        Overloadings of this method exist to initialize an enum set with
        one through five elements.  A sixth overloading is provided that
        uses the varargs feature.  This overloading may be used to create
        an enum set initially containing an arbitrary number of elements, but
        is likely to run slower than the overloadings that do not use varargs.
        
        Type `<E>`: The class of the specified element and of the set

        Arguments
        - e: the element that this set is to contain initially

        Returns
        - an enum set initially containing the specified element

        Raises
        - NullPointerException: if `e` is null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified elements.
        
        Overloadings of this method exist to initialize an enum set with
        one through five elements.  A sixth overloading is provided that
        uses the varargs feature.  This overloading may be used to create
        an enum set initially containing an arbitrary number of elements, but
        is likely to run slower than the overloadings that do not use varargs.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - e1: an element that this set is to contain initially
        - e2: another element that this set is to contain initially

        Returns
        - an enum set initially containing the specified elements

        Raises
        - NullPointerException: if any parameters are null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified elements.
        
        Overloadings of this method exist to initialize an enum set with
        one through five elements.  A sixth overloading is provided that
        uses the varargs feature.  This overloading may be used to create
        an enum set initially containing an arbitrary number of elements, but
        is likely to run slower than the overloadings that do not use varargs.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - e1: an element that this set is to contain initially
        - e2: another element that this set is to contain initially
        - e3: another element that this set is to contain initially

        Returns
        - an enum set initially containing the specified elements

        Raises
        - NullPointerException: if any parameters are null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified elements.
        
        Overloadings of this method exist to initialize an enum set with
        one through five elements.  A sixth overloading is provided that
        uses the varargs feature.  This overloading may be used to create
        an enum set initially containing an arbitrary number of elements, but
        is likely to run slower than the overloadings that do not use varargs.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - e1: an element that this set is to contain initially
        - e2: another element that this set is to contain initially
        - e3: another element that this set is to contain initially
        - e4: another element that this set is to contain initially

        Returns
        - an enum set initially containing the specified elements

        Raises
        - NullPointerException: if any parameters are null
        """
        ...


    @staticmethod
    def of(e1: "E", e2: "E", e3: "E", e4: "E", e5: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified elements.
        
        Overloadings of this method exist to initialize an enum set with
        one through five elements.  A sixth overloading is provided that
        uses the varargs feature.  This overloading may be used to create
        an enum set initially containing an arbitrary number of elements, but
        is likely to run slower than the overloadings that do not use varargs.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - e1: an element that this set is to contain initially
        - e2: another element that this set is to contain initially
        - e3: another element that this set is to contain initially
        - e4: another element that this set is to contain initially
        - e5: another element that this set is to contain initially

        Returns
        - an enum set initially containing the specified elements

        Raises
        - NullPointerException: if any parameters are null
        """
        ...


    @staticmethod
    def of(first: "E", *rest: Tuple["E", ...]) -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing the specified elements.
        This factory, whose parameter list uses the varargs feature, may
        be used to create an enum set initially containing an arbitrary
        number of elements, but it is likely to run slower than the overloadings
        that do not use varargs.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - first: an element that the set is to contain initially
        - rest: the remaining elements the set is to contain initially

        Returns
        - an enum set initially containing the specified elements

        Raises
        - NullPointerException: if any of the specified elements are null,
            or if `rest` is null
        """
        ...


    @staticmethod
    def range(from: "E", to: "E") -> "EnumSet"["E"]:
        """
        Creates an enum set initially containing all of the elements in the
        range defined by the two specified endpoints.  The returned set will
        contain the endpoints themselves, which may be identical but must not
        be out of order.
        
        Type `<E>`: The class of the parameter elements and of the set

        Arguments
        - from: the first element in the range
        - to: the last element in the range

        Returns
        - an enum set initially containing all of the elements in the
                range defined by the two specified endpoints

        Raises
        - NullPointerException: if `from` or `to` are null
        - IllegalArgumentException: if `from.compareTo(to) > 0`
        """
        ...


    def clone(self) -> "EnumSet"["E"]:
        """
        Returns a copy of this set.

        Returns
        - a copy of this set
        """
        ...
