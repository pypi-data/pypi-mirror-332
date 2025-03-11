"""
Python module generated from Java source file com.google.common.base.Predicate

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.base import *
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class Predicate(Predicate):
    """
    Legacy version of java.util.function.Predicate java.util.function.Predicate. Determines a
    True or False value for a given input.
    
    As this interface extends `java.util.function.Predicate`, an instance of this type may
    be used as a `Predicate` directly. To use a `java.util.function.Predicate` where a
    `com.google.common.base.Predicate` is expected, use the method reference `predicate::test`.
    
    This interface is now a legacy type. Use `java.util.function.Predicate` (or the
    appropriate primitive specialization such as `IntPredicate`) instead whenever possible.
    Otherwise, at least reduce *explicit* dependencies on this type by using lambda expressions
    or method references instead of classes, leaving your code easier to migrate in the future.
    
    The Predicates class provides common predicates and related utilities.
    
    See the Guava User Guide article on <a
    href="https://github.com/google/guava/wiki/FunctionalExplained">the use of `Predicate`</a>.

    Author(s)
    - Kevin Bourrillion

    Since
    - 2.0
    """

    def apply(self, input: "T") -> bool:
        """
        Returns the result of applying this predicate to `input` (Java 8+ users, see notes in the
        class documentation above). This method is *generally expected*, but not absolutely
        required, to have the following properties:
        
        
          - Its execution does not cause any observable side effects.
          - The computation is *consistent with equals*; that is, Objects.equal
              Objects.equal`(a, b)` implies that `predicate.apply(a) ==
              predicate.apply(b))`.

        Raises
        - NullPointerException: if `input` is null and this predicate does not accept null
            arguments
        """
        ...


    def equals(self, object: "Object") -> bool:
        """
        Indicates whether another object is equal to this predicate.
        
        Most implementations will have no reason to override the behavior of Object.equals.
        However, an implementation may also choose to return `True` whenever `object` is a
        Predicate that it considers *interchangeable* with this one. "Interchangeable"
        *typically* means that `this.apply(t) == that.apply(t)` for all `t` of type
        `T`). Note that a `False` result from this method does not imply that the
        predicates are known *not* to be interchangeable.
        """
        ...


    def test(self, input: "T") -> bool:
        ...
