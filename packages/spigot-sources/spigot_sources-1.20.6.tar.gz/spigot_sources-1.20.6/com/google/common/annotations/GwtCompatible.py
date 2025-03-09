"""
Python module generated from Java source file com.google.common.annotations.GwtCompatible

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import *
from typing import Any, Callable, Iterable, Tuple


class GwtCompatible:
    """
    The presence of this annotation on a type indicates that the type may be used with the <a
    href="http://code.google.com/webtoolkit/">Google Web Toolkit</a> (GWT). When applied to a method,
    the return type of the method is GWT compatible. It's useful to indicate that an instance created
    by factory methods has a GWT serializable type. In the following example,
    
    ```
    @GwtCompatible
    class Lists {
      ...
      @GwtCompatible(serializable = True)
      static <E> List<E> newArrayList(E... elements) {
        ...
      }
    }
    ```
    
    The return value of `Lists.newArrayList(E[])` has GWT serializable type. It is also
    useful in specifying contracts of interface methods. In the following example,
    
    ```
    @GwtCompatible
    interface ListFactory {
      ...
      @GwtCompatible(serializable = True)
      <E> List<E> newArrayList(E... elements);
    }
    ```
    
    The `newArrayList(E[])` method of all implementations of `ListFactory` is expected
    to return a value with a GWT serializable type.
    
    Note that a `GwtCompatible` type may have some GwtIncompatible methods.

    Author(s)
    - Hayward Chan
    """

    def serializable(self) -> bool:
        """
        When `True`, the annotated type or the type of the method return value is GWT
        serializable.

        See
        - <a href=
            "http://code.google.com/webtoolkit/doc/latest/DevGuideServerCommunication.html.DevGuideSerializableTypes">
            Documentation about GWT serialization</a>
        """
        return False


    def emulated(self) -> bool:
        """
        When `True`, the annotated type is emulated in GWT. The emulated source (also known as
        super-source) is different from the implementation used by the JVM.

        See
        - <a href=
            "http://code.google.com/webtoolkit/doc/latest/DevGuideOrganizingProjects.html.DevGuideModules">
            Documentation about GWT emulated source</a>
        """
        return False
