"""
Python module generated from Java source file java.util.PrimitiveIterator

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import *
from java.util.function import Consumer
from java.util.function import DoubleConsumer
from java.util.function import IntConsumer
from java.util.function import LongConsumer
from typing import Any, Callable, Iterable, Tuple


class PrimitiveIterator(Iterator):
    """
    A base type for primitive specializations of `Iterator`.  Specialized
    subtypes are provided for OfInt int, OfLong long, and
    OfDouble double values.
    
    The specialized subtype default implementations of Iterator.next
    and Iterator.forEachRemaining(java.util.function.Consumer) box
    primitive values to instances of their corresponding wrapper class.  Such
    boxing may offset any advantages gained when using the primitive
    specializations.  To avoid boxing, the corresponding primitive-based methods
    should be used.  For example, PrimitiveIterator.OfInt.nextInt() and
    PrimitiveIterator.OfInt.forEachRemaining(java.util.function.IntConsumer)
    should be used in preference to PrimitiveIterator.OfInt.next() and
    PrimitiveIterator.OfInt.forEachRemaining(java.util.function.Consumer).
    
    Iteration of primitive values using boxing-based methods
    Iterator.next next() and
    Iterator.forEachRemaining(java.util.function.Consumer) forEachRemaining(),
    does not affect the order in which the values, transformed to boxed values,
    are encountered.
    
    Type `<T>`: the type of elements returned by this PrimitiveIterator.  The
           type must be a wrapper type for a primitive type, such as
           `Integer` for the primitive `int` type.

    Arguments
    - <T_CONS>: the type of primitive consumer.  The type must be a
           primitive specialization of java.util.function.Consumer for
           `T`, such as java.util.function.IntConsumer for
           `Integer`.

    Since
    - 1.8

    Unknown Tags
    - If the boolean system property `org.openjdk.java.util.stream.tripwire`
    is set to `True` then diagnostic warnings are reported if boxing of
    primitive values occur when operating on primitive subtype specializations.
    """

    def forEachRemaining(self, action: "T_CONS") -> None:
        """
        Performs the given action for each remaining element until all elements
        have been processed or the action throws an exception.  Actions are
        performed in the order of iteration, if that order is specified.
        Exceptions thrown by the action are relayed to the caller.
        
        The behavior of an iterator is unspecified if the action modifies the
        source of elements in any way (even by calling the .remove remove
        method or other mutator methods of `Iterator` subtypes),
        unless an overriding class has specified a concurrent modification policy.
        
        Subsequent behavior of an iterator is unspecified if the action throws an
        exception.

        Arguments
        - action: The action to be performed for each element

        Raises
        - NullPointerException: if the specified action is null
        """
        ...


    class OfInt(PrimitiveIterator):
        """
        An Iterator specialized for `int` values.

        Since
        - 1.8
        """

        def nextInt(self) -> int:
            """
            Returns the next `int` element in the iteration.

            Returns
            - the next `int` element in the iteration

            Raises
            - NoSuchElementException: if the iteration has no more elements
            """
            ...


        def forEachRemaining(self, action: "IntConsumer") -> None:
            """
            Unknown Tags
            - The default implementation behaves as if:
            ````while (hasNext())
                    action.accept(nextInt());````
            """
            ...


        def next(self) -> "Integer":
            """
            Unknown Tags
            - The default implementation boxes the result of calling
            .nextInt(), and returns that boxed result.
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Integer"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `IntConsumer` then it is cast
            to `IntConsumer` and passed to .forEachRemaining;
            otherwise the action is adapted to an instance of
            `IntConsumer`, by boxing the argument of `IntConsumer`,
            and then passed to .forEachRemaining.
            """
            ...


    class OfLong(PrimitiveIterator):
        """
        An Iterator specialized for `long` values.

        Since
        - 1.8
        """

        def nextLong(self) -> int:
            """
            Returns the next `long` element in the iteration.

            Returns
            - the next `long` element in the iteration

            Raises
            - NoSuchElementException: if the iteration has no more elements
            """
            ...


        def forEachRemaining(self, action: "LongConsumer") -> None:
            """
            Unknown Tags
            - The default implementation behaves as if:
            ````while (hasNext())
                    action.accept(nextLong());````
            """
            ...


        def next(self) -> "Long":
            """
            Unknown Tags
            - The default implementation boxes the result of calling
            .nextLong(), and returns that boxed result.
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Long"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `LongConsumer` then it is cast
            to `LongConsumer` and passed to .forEachRemaining;
            otherwise the action is adapted to an instance of
            `LongConsumer`, by boxing the argument of `LongConsumer`,
            and then passed to .forEachRemaining.
            """
            ...


    class OfDouble(PrimitiveIterator):
        """
        An Iterator specialized for `double` values.

        Since
        - 1.8
        """

        def nextDouble(self) -> float:
            """
            Returns the next `double` element in the iteration.

            Returns
            - the next `double` element in the iteration

            Raises
            - NoSuchElementException: if the iteration has no more elements
            """
            ...


        def forEachRemaining(self, action: "DoubleConsumer") -> None:
            """
            Unknown Tags
            - The default implementation behaves as if:
            ````while (hasNext())
                    action.accept(nextDouble());````
            """
            ...


        def next(self) -> "Double":
            """
            Unknown Tags
            - The default implementation boxes the result of calling
            .nextDouble(), and returns that boxed result.
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Double"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `DoubleConsumer` then it is
            cast to `DoubleConsumer` and passed to
            .forEachRemaining; otherwise the action is adapted to
            an instance of `DoubleConsumer`, by boxing the argument of
            `DoubleConsumer`, and then passed to
            .forEachRemaining.
            """
            ...
