"""
Python module generated from Java source file java.util.Enumeration

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from typing import Any, Callable, Iterable, Tuple


class Enumeration:
    """
    An object that implements the Enumeration interface generates a
    series of elements, one at a time. Successive calls to the
    `nextElement` method return successive elements of the
    series.
    
    For example, to print all elements of a `Vector<E>` *v*:
    ```
      for (Enumeration&lt;E&gt; e = v.elements(); e.hasMoreElements();)
          System.out.println(e.nextElement());```
    
    Methods are provided to enumerate through the elements of a
    vector, the keys of a hashtable, and the values in a hashtable.
    Enumerations are also used to specify the input streams to a
    `SequenceInputStream`.

    Author(s)
    - Lee Boynton

    See
    - java.util.Vector.elements()

    Since
    - 1.0

    Unknown Tags
    - The functionality of this interface is duplicated by the Iterator
    interface.  In addition, `Iterator` adds an optional remove operation,
    and has shorter method names.  New implementations should consider using
    `Iterator` in preference to `Enumeration`. It is possible to
    adapt an `Enumeration` to an `Iterator` by using the
    .asIterator method.
    """

    def hasMoreElements(self) -> bool:
        """
        Tests if this enumeration contains more elements.

        Returns
        - `True` if and only if this enumeration object
                  contains at least one more element to provide;
                 `False` otherwise.
        """
        ...


    def nextElement(self) -> "E":
        """
        Returns the next element of this enumeration if this enumeration
        object has at least one more element to provide.

        Returns
        - the next element of this enumeration.

        Raises
        - NoSuchElementException: if no more elements exist.
        """
        ...


    def asIterator(self) -> Iterator["E"]:
        """
        Returns an Iterator that traverses the remaining elements
        covered by this enumeration. Traversal is undefined if any methods
        are called on this enumeration after the call to `asIterator`.

        Returns
        - an Iterator representing the remaining elements of this Enumeration

        Since
        - 9

        Unknown Tags
        - This method is intended to help adapt code that produces
        `Enumeration` instances to code that consumes `Iterator`
        instances. For example, the java.util.jar.JarFile.entries()
        JarFile.entries() method returns an `Enumeration<JarEntry>`.
        This can be turned into an `Iterator`, and then the
        `forEachRemaining()` method can be used:
        
        ````JarFile jarFile = ... ;
            jarFile.entries().asIterator().forEachRemaining(entry -> { ...`);
        }```
        
        (Note that there is also a java.util.jar.JarFile.stream()
        JarFile.stream() method that returns a `Stream` of entries,
        which may be more convenient in some cases.)
        - The default implementation returns an `Iterator` whose
        Iterator.hasNext hasNext method calls this Enumeration's
        `hasMoreElements` method, whose Iterator.next next
        method calls this Enumeration's `nextElement` method, and
        whose Iterator.remove remove method throws
        `UnsupportedOperationException`.
        """
        ...
