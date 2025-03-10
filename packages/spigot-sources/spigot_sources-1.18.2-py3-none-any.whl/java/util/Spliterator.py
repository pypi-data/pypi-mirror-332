"""
Python module generated from Java source file java.util.Spliterator

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


class Spliterator:
    """
    An object for traversing and partitioning elements of a source.  The source
    of elements covered by a Spliterator could be, for example, an array, a
    Collection, an IO channel, or a generator function.
    
    A Spliterator may traverse elements individually (.tryAdvance tryAdvance()) or sequentially in bulk
    (.forEachRemaining forEachRemaining()).
    
    A Spliterator may also partition off some of its elements (using
    .trySplit) as another Spliterator, to be used in
    possibly-parallel operations.  Operations using a Spliterator that
    cannot split, or does so in a highly imbalanced or inefficient
    manner, are unlikely to benefit from parallelism.  Traversal
    and splitting exhaust elements; each Spliterator is useful for only a single
    bulk computation.
    
    A Spliterator also reports a set of .characteristics() of its
    structure, source, and elements from among .ORDERED,
    .DISTINCT, .SORTED, .SIZED, .NONNULL,
    .IMMUTABLE, .CONCURRENT, and .SUBSIZED. These may
    be employed by Spliterator clients to control, specialize or simplify
    computation.  For example, a Spliterator for a Collection would
    report `SIZED`, a Spliterator for a Set would report
    `DISTINCT`, and a Spliterator for a SortedSet would also
    report `SORTED`.  Characteristics are reported as a simple unioned bit
    set.
    
    Some characteristics additionally constrain method behavior; for example if
    `ORDERED`, traversal methods must conform to their documented ordering.
    New characteristics may be defined in the future, so implementors should not
    assign meanings to unlisted values.
    
    <a id="binding">A Spliterator that does not report `IMMUTABLE` or
    `CONCURRENT` is expected to have a documented policy concerning:
    when the spliterator *binds* to the element source; and detection of
    structural interference of the element source detected after binding.</a>  A
    *late-binding* Spliterator binds to the source of elements at the
    point of first traversal, first split, or first query for estimated size,
    rather than at the time the Spliterator is created.  A Spliterator that is
    not *late-binding* binds to the source of elements at the point of
    construction or first invocation of any method.  Modifications made to the
    source prior to binding are reflected when the Spliterator is traversed.
    After binding a Spliterator should, on a best-effort basis, throw
    ConcurrentModificationException if structural interference is
    detected.  Spliterators that do this are called *fail-fast*.  The
    bulk traversal method (.forEachRemaining forEachRemaining()) of a
    Spliterator may optimize traversal and check for structural interference
    after all elements have been traversed, rather than checking per-element and
    failing immediately.
    
    Spliterators can provide an estimate of the number of remaining elements
    via the .estimateSize method.  Ideally, as reflected in characteristic
    .SIZED, this value corresponds exactly to the number of elements
    that would be encountered in a successful traversal.  However, even when not
    exactly known, an estimated value may still be useful to operations
    being performed on the source, such as helping to determine whether it is
    preferable to split further or traverse the remaining elements sequentially.
    
    Despite their obvious utility in parallel algorithms, spliterators are not
    expected to be thread-safe; instead, implementations of parallel algorithms
    using spliterators should ensure that the spliterator is only used by one
    thread at a time.  This is generally easy to attain via *serial
    thread-confinement*, which often is a natural consequence of typical
    parallel algorithms that work by recursive decomposition.  A thread calling
    .trySplit() may hand over the returned Spliterator to another thread,
    which in turn may traverse or further split that Spliterator.  The behaviour
    of splitting and traversal is undefined if two or more threads operate
    concurrently on the same spliterator.  If the original thread hands a
    spliterator off to another thread for processing, it is best if that handoff
    occurs before any elements are consumed with .tryAdvance(Consumer)
    tryAdvance(), as certain guarantees (such as the accuracy of
    .estimateSize() for `SIZED` spliterators) are only valid before
    traversal has begun.
    
    Primitive subtype specializations of `Spliterator` are provided for
    OfInt int, OfLong long, and OfDouble double values.
    The subtype default implementations of
    Spliterator.tryAdvance(java.util.function.Consumer)
    and Spliterator.forEachRemaining(java.util.function.Consumer) box
    primitive values to instances of their corresponding wrapper class.  Such
    boxing may undermine any performance advantages gained by using the primitive
    specializations.  To avoid boxing, the corresponding primitive-based methods
    should be used.  For example,
    Spliterator.OfInt.tryAdvance(java.util.function.IntConsumer)
    and Spliterator.OfInt.forEachRemaining(java.util.function.IntConsumer)
    should be used in preference to
    Spliterator.OfInt.tryAdvance(java.util.function.Consumer) and
    Spliterator.OfInt.forEachRemaining(java.util.function.Consumer).
    Traversal of primitive values using boxing-based methods
    .tryAdvance tryAdvance() and
    .forEachRemaining(java.util.function.Consumer) forEachRemaining()
    does not affect the order in which the values, transformed to boxed values,
    are encountered.
    
    Type `<T>`: the type of elements returned by this Spliterator

    See
    - Collection

    Since
    - 1.8

    Unknown Tags
    - Spliterators, like `Iterator`s, are for traversing the elements of
    a source.  The `Spliterator` API was designed to support efficient
    parallel traversal in addition to sequential traversal, by supporting
    decomposition as well as single-element iteration.  In addition, the
    protocol for accessing elements via a Spliterator is designed to impose
    smaller per-element overhead than `Iterator`, and to avoid the inherent
    race involved in having separate methods for `hasNext()` and
    `next()`.
    
    For mutable sources, arbitrary and non-deterministic behavior may occur if
    the source is structurally interfered with (elements added, replaced, or
    removed) between the time that the Spliterator binds to its data source and
    the end of traversal.  For example, such interference will produce arbitrary,
    non-deterministic results when using the `java.util.stream` framework.
    
    Structural interference of a source can be managed in the following ways
    (in approximate order of decreasing desirability):
    
    - The source cannot be structurally interfered with.
    For example, an instance of
    java.util.concurrent.CopyOnWriteArrayList is an immutable source.
    A Spliterator created from the source reports a characteristic of
    `IMMUTABLE`.
    - The source manages concurrent modifications.
    For example, a key set of a java.util.concurrent.ConcurrentHashMap
    is a concurrent source.  A Spliterator created from the source reports a
    characteristic of `CONCURRENT`.
    - The mutable source provides a late-binding and fail-fast Spliterator.
    Late binding narrows the window during which interference can affect
    the calculation; fail-fast detects, on a best-effort basis, that structural
    interference has occurred after traversal has commenced and throws
    ConcurrentModificationException.  For example, ArrayList,
    and many other non-concurrent `Collection` classes in the JDK, provide
    a late-binding, fail-fast spliterator.
    - The mutable source provides a non-late-binding but fail-fast Spliterator.
    The source increases the likelihood of throwing
    `ConcurrentModificationException` since the window of potential
    interference is larger.
    - The mutable source provides a late-binding and non-fail-fast Spliterator.
    The source risks arbitrary, non-deterministic behavior after traversal
    has commenced since interference is not detected.
    
    - The mutable source provides a non-late-binding and non-fail-fast
    Spliterator.
    The source increases the risk of arbitrary, non-deterministic behavior
    since non-detected interference may occur after construction.
    
    
    
    **Example.** Here is a class (not a very useful one, except
    for illustration) that maintains an array in which the actual data
    are held in even locations, and unrelated tag data are held in odd
    locations. Its Spliterator ignores the tags.
    
    ``` `class TaggedArray<T> {
      private final Object[] elements; // immutable after construction
      TaggedArray(T[] data, Object[] tags) {
        int size = data.length;
        if (tags.length != size) throw new IllegalArgumentException();
        this.elements = new Object[2 * size];
        for (int i = 0, j = 0; i < size; ++i) {
          elements[j++] = data[i];
          elements[j++] = tags[i];`
      }
    
      public Spliterator<T> spliterator() {
        return new TaggedArraySpliterator<>(elements, 0, elements.length);
      }
    
      static class TaggedArraySpliterator<T> implements Spliterator<T> {
        private final Object[] array;
        private int origin; // current index, advanced on split or traversal
        private final int fence; // one past the greatest index
    
        TaggedArraySpliterator(Object[] array, int origin, int fence) {
          this.array = array; this.origin = origin; this.fence = fence;
        }
    
        public void forEachRemaining(Consumer<? super T> action) {
          for (; origin < fence; origin += 2)
            action.accept((T) array[origin]);
        }
    
        public boolean tryAdvance(Consumer<? super T> action) {
          if (origin < fence) {
            action.accept((T) array[origin]);
            origin += 2;
            return True;
          }
          else // cannot advance
            return False;
        }
    
        public Spliterator<T> trySplit() {
          int lo = origin; // divide range in half
          int mid = ((lo + fence) >>> 1) & ~1; // force midpoint to be even
          if (lo < mid) { // split out left half
            origin = mid; // reset this Spliterator's origin
            return new TaggedArraySpliterator<>(array, lo, mid);
          }
          else       // too small to split
            return null;
        }
    
        public long estimateSize() {
          return (long)((fence - origin) / 2);
        }
    
        public int characteristics() {
          return ORDERED | SIZED | IMMUTABLE | SUBSIZED;
        }
      }
    }}```
    
    As an example how a parallel computation framework, such as the
    `java.util.stream` package, would use Spliterator in a parallel
    computation, here is one way to implement an associated parallel forEach,
    that illustrates the primary usage idiom of splitting off subtasks until
    the estimated amount of work is small enough to perform
    sequentially. Here we assume that the order of processing across
    subtasks doesn't matter; different (forked) tasks may further split
    and process elements concurrently in undetermined order.  This
    example uses a java.util.concurrent.CountedCompleter;
    similar usages apply to other parallel task constructions.
    
    ````static <T> void parEach(TaggedArray<T> a, Consumer<T> action) {
      Spliterator<T> s = a.spliterator();
      long targetBatchSize = s.estimateSize() / (ForkJoinPool.getCommonPoolParallelism() * 8);
      new ParEach(null, s, action, targetBatchSize).invoke();`
    
    static class ParEach<T> extends CountedCompleter<Void> {
      final Spliterator<T> spliterator;
      final Consumer<T> action;
      final long targetBatchSize;
    
      ParEach(ParEach<T> parent, Spliterator<T> spliterator,
              Consumer<T> action, long targetBatchSize) {
        super(parent);
        this.spliterator = spliterator; this.action = action;
        this.targetBatchSize = targetBatchSize;
      }
    
      public void compute() {
        Spliterator<T> sub;
        while (spliterator.estimateSize() > targetBatchSize &&
               (sub = spliterator.trySplit()) != null) {
          addToPendingCount(1);
          new ParEach<>(this, sub, action, targetBatchSize).fork();
        }
        spliterator.forEachRemaining(action);
        propagateCompletion();
      }
    }}```
    - If the boolean system property org.openjdk.java.util.stream.tripwire
    is set to `True` then diagnostic warnings are reported if boxing of
    primitive values occur when operating on primitive subtype specializations.
    """

    ORDERED = 0x00000010
    """
    Characteristic value signifying that an encounter order is defined for
    elements. If so, this Spliterator guarantees that method
    .trySplit splits a strict prefix of elements, that method
    .tryAdvance steps by one element in prefix order, and that
    .forEachRemaining performs actions in encounter order.
    
    A Collection has an encounter order if the corresponding
    Collection.iterator documents an order. If so, the encounter
    order is the same as the documented order. Otherwise, a collection does
    not have an encounter order.

    Unknown Tags
    - Encounter order is guaranteed to be ascending index order for
    any List. But no order is guaranteed for hash-based collections
    such as HashSet. Clients of a Spliterator that reports
    `ORDERED` are expected to preserve ordering constraints in
    non-commutative parallel computations.
    """
    DISTINCT = 0x00000001
    """
    Characteristic value signifying that, for each pair of
    encountered elements `x, y`, `!x.equals(y)`. This
    applies for example, to a Spliterator based on a Set.
    """
    SORTED = 0x00000004
    """
    Characteristic value signifying that encounter order follows a defined
    sort order. If so, method .getComparator() returns the associated
    Comparator, or `null` if all elements are Comparable and
    are sorted by their natural ordering.
    
    A Spliterator that reports `SORTED` must also report
    `ORDERED`.

    Unknown Tags
    - The spliterators for `Collection` classes in the JDK that
    implement NavigableSet or SortedSet report `SORTED`.
    """
    SIZED = 0x00000040
    """
    Characteristic value signifying that the value returned from
    `estimateSize()` prior to traversal or splitting represents a
    finite size that, in the absence of structural source modification,
    represents an exact count of the number of elements that would be
    encountered by a complete traversal.

    Unknown Tags
    - Most Spliterators for Collections, that cover all elements of a
    `Collection` report this characteristic. Sub-spliterators, such as
    those for HashSet, that cover a sub-set of elements and
    approximate their reported size do not.
    """
    NONNULL = 0x00000100
    """
    Characteristic value signifying that the source guarantees that
    encountered elements will not be `null`. (This applies,
    for example, to most concurrent collections, queues, and maps.)
    """
    IMMUTABLE = 0x00000400
    """
    Characteristic value signifying that the element source cannot be
    structurally modified; that is, elements cannot be added, replaced, or
    removed, so such changes cannot occur during traversal. A Spliterator
    that does not report `IMMUTABLE` or `CONCURRENT` is expected
    to have a documented policy (for example throwing
    ConcurrentModificationException) concerning structural
    interference detected during traversal.
    """
    CONCURRENT = 0x00001000
    """
    Characteristic value signifying that the element source may be safely
    concurrently modified (allowing additions, replacements, and/or removals)
    by multiple threads without external synchronization. If so, the
    Spliterator is expected to have a documented policy concerning the impact
    of modifications during traversal.
    
    A top-level Spliterator should not report both `CONCURRENT` and
    `SIZED`, since the finite size, if known, may change if the source
    is concurrently modified during traversal. Such a Spliterator is
    inconsistent and no guarantees can be made about any computation using
    that Spliterator. Sub-spliterators may report `SIZED` if the
    sub-split size is known and additions or removals to the source are not
    reflected when traversing.
    
    A top-level Spliterator should not report both `CONCURRENT` and
    `IMMUTABLE`, since they are mutually exclusive. Such a Spliterator
    is inconsistent and no guarantees can be made about any computation using
    that Spliterator. Sub-spliterators may report `IMMUTABLE` if
    additions or removals to the source are not reflected when traversing.

    Unknown Tags
    - Most concurrent collections maintain a consistency policy
    guaranteeing accuracy with respect to elements present at the point of
    Spliterator construction, but possibly not reflecting subsequent
    additions or removals.
    """
    SUBSIZED = 0x00004000
    """
    Characteristic value signifying that all Spliterators resulting from
    `trySplit()` will be both .SIZED and .SUBSIZED.
    (This means that all child Spliterators, whether direct or indirect, will
    be `SIZED`.)
    
    A Spliterator that does not report `SIZED` as required by
    `SUBSIZED` is inconsistent and no guarantees can be made about any
    computation using that Spliterator.

    Unknown Tags
    - Some spliterators, such as the top-level spliterator for an
    approximately balanced binary tree, will report `SIZED` but not
    `SUBSIZED`, since it is common to know the size of the entire tree
    but not the exact sizes of subtrees.
    """


    def tryAdvance(self, action: "Consumer"["T"]) -> bool:
        """
        If a remaining element exists, performs the given action on it,
        returning `True`; else returns `False`.  If this
        Spliterator is .ORDERED the action is performed on the
        next element in encounter order.  Exceptions thrown by the
        action are relayed to the caller.
        
        Subsequent behavior of a spliterator is unspecified if the action throws
        an exception.

        Arguments
        - action: The action

        Returns
        - `False` if no remaining elements existed
        upon entry to this method, else `True`.

        Raises
        - NullPointerException: if the specified action is null
        """
        ...


    def forEachRemaining(self, action: "Consumer"["T"]) -> None:
        """
        Performs the given action for each remaining element, sequentially in
        the current thread, until all elements have been processed or the action
        throws an exception.  If this Spliterator is .ORDERED, actions
        are performed in encounter order.  Exceptions thrown by the action
        are relayed to the caller.
        
        Subsequent behavior of a spliterator is unspecified if the action throws
        an exception.

        Arguments
        - action: The action

        Raises
        - NullPointerException: if the specified action is null

        Unknown Tags
        - The default implementation repeatedly invokes .tryAdvance until
        it returns `False`.  It should be overridden whenever possible.
        """
        ...


    def trySplit(self) -> "Spliterator"["T"]:
        """
        If this spliterator can be partitioned, returns a Spliterator
        covering elements, that will, upon return from this method, not
        be covered by this Spliterator.
        
        If this Spliterator is .ORDERED, the returned Spliterator
        must cover a strict prefix of the elements.
        
        Unless this Spliterator covers an infinite number of elements,
        repeated calls to `trySplit()` must eventually return `null`.
        Upon non-null return:
        
        - the value reported for `estimateSize()` before splitting,
        must, after splitting, be greater than or equal to `estimateSize()`
        for this and the returned Spliterator; and
        - if this Spliterator is `SUBSIZED`, then `estimateSize()`
        for this spliterator before splitting must be equal to the sum of
        `estimateSize()` for this and the returned Spliterator after
        splitting.
        
        
        This method may return `null` for any reason,
        including emptiness, inability to split after traversal has
        commenced, data structure constraints, and efficiency
        considerations.

        Returns
        - a `Spliterator` covering some portion of the
        elements, or `null` if this spliterator cannot be split

        Unknown Tags
        - An ideal `trySplit` method efficiently (without
        traversal) divides its elements exactly in half, allowing
        balanced parallel computation.  Many departures from this ideal
        remain highly effective; for example, only approximately
        splitting an approximately balanced tree, or for a tree in
        which leaf nodes may contain either one or two elements,
        failing to further split these nodes.  However, large
        deviations in balance and/or overly inefficient `trySplit` mechanics typically result in poor parallel
        performance.
        """
        ...


    def estimateSize(self) -> int:
        """
        Returns an estimate of the number of elements that would be
        encountered by a .forEachRemaining traversal, or returns Long.MAX_VALUE if infinite, unknown, or too expensive to compute.
        
        If this Spliterator is .SIZED and has not yet been partially
        traversed or split, or this Spliterator is .SUBSIZED and has
        not yet been partially traversed, this estimate must be an accurate
        count of elements that would be encountered by a complete traversal.
        Otherwise, this estimate may be arbitrarily inaccurate, but must decrease
        as specified across invocations of .trySplit.

        Returns
        - the estimated size, or `Long.MAX_VALUE` if infinite,
                unknown, or too expensive to compute.

        Unknown Tags
        - Even an inexact estimate is often useful and inexpensive to compute.
        For example, a sub-spliterator of an approximately balanced binary tree
        may return a value that estimates the number of elements to be half of
        that of its parent; if the root Spliterator does not maintain an
        accurate count, it could estimate size to be the power of two
        corresponding to its maximum depth.
        """
        ...


    def getExactSizeIfKnown(self) -> int:
        """
        Convenience method that returns .estimateSize() if this
        Spliterator is .SIZED, else `-1`.

        Returns
        - the exact size, if known, else `-1`.

        Unknown Tags
        - The default implementation returns the result of `estimateSize()`
        if the Spliterator reports a characteristic of `SIZED`, and
        `-1` otherwise.
        """
        ...


    def characteristics(self) -> int:
        """
        Returns a set of characteristics of this Spliterator and its
        elements. The result is represented as ORed values from .ORDERED, .DISTINCT, .SORTED, .SIZED,
        .NONNULL, .IMMUTABLE, .CONCURRENT,
        .SUBSIZED.  Repeated calls to `characteristics()` on
        a given spliterator, prior to or in-between calls to `trySplit`,
        should always return the same result.
        
        If a Spliterator reports an inconsistent set of
        characteristics (either those returned from a single invocation
        or across multiple invocations), no guarantees can be made
        about any computation using this Spliterator.

        Returns
        - a representation of characteristics

        Unknown Tags
        - The characteristics of a given spliterator before splitting
        may differ from the characteristics after splitting.  For specific
        examples see the characteristic values .SIZED, .SUBSIZED
        and .CONCURRENT.
        """
        ...


    def hasCharacteristics(self, characteristics: int) -> bool:
        """
        Returns `True` if this Spliterator's .characteristics contain all of the given characteristics.

        Arguments
        - characteristics: the characteristics to check for

        Returns
        - `True` if all the specified characteristics are present,
        else `False`

        Unknown Tags
        - The default implementation returns True if the corresponding bits
        of the given characteristics are set.
        """
        ...


    def getComparator(self) -> "Comparator"["T"]:
        """
        If this Spliterator's source is .SORTED by a Comparator,
        returns that `Comparator`. If the source is `SORTED` in
        Comparable natural order, returns `null`.  Otherwise,
        if the source is not `SORTED`, throws IllegalStateException.

        Returns
        - a Comparator, or `null` if the elements are sorted in the
        natural order.

        Raises
        - IllegalStateException: if the spliterator does not report
                a characteristic of `SORTED`.

        Unknown Tags
        - The default implementation always throws IllegalStateException.
        """
        ...


    class OfPrimitive(Spliterator):
        """
        A Spliterator specialized for primitive values.
        
        Type `<T>`: the type of elements returned by this Spliterator.  The
        type must be a wrapper type for a primitive type, such as `Integer`
        for the primitive `int` type.

        Arguments
        - <T_CONS>: the type of primitive consumer.  The type must be a
        primitive specialization of java.util.function.Consumer for
        `T`, such as java.util.function.IntConsumer for
        `Integer`.
        - <T_SPLITR>: the type of primitive Spliterator.  The type must be
        a primitive specialization of Spliterator for `T`, such as
        Spliterator.OfInt for `Integer`.

        See
        - Spliterator.OfDouble

        Since
        - 1.8
        """

        def trySplit(self) -> "T_SPLITR":
            ...


        def tryAdvance(self, action: "T_CONS") -> bool:
            """
            If a remaining element exists, performs the given action on it,
            returning `True`; else returns `False`.  If this
            Spliterator is .ORDERED the action is performed on the
            next element in encounter order.  Exceptions thrown by the
            action are relayed to the caller.
            
            Subsequent behavior of a spliterator is unspecified if the action throws
            an exception.

            Arguments
            - action: The action

            Returns
            - `False` if no remaining elements existed
            upon entry to this method, else `True`.

            Raises
            - NullPointerException: if the specified action is null
            """
            ...


        def forEachRemaining(self, action: "T_CONS") -> None:
            """
            Performs the given action for each remaining element, sequentially in
            the current thread, until all elements have been processed or the
            action throws an exception.  If this Spliterator is .ORDERED,
            actions are performed in encounter order.  Exceptions thrown by the
            action are relayed to the caller.
            
            Subsequent behavior of a spliterator is unspecified if the action throws
            an exception.

            Arguments
            - action: The action

            Raises
            - NullPointerException: if the specified action is null

            Unknown Tags
            - The default implementation repeatedly invokes .tryAdvance
            until it returns `False`.  It should be overridden whenever
            possible.
            """
            ...


    class OfInt(OfPrimitive):
        """
        A Spliterator specialized for `int` values.

        Since
        - 1.8
        """

        def trySplit(self) -> "OfInt":
            ...


        def tryAdvance(self, action: "IntConsumer") -> bool:
            ...


        def forEachRemaining(self, action: "IntConsumer") -> None:
            ...


        def tryAdvance(self, action: "Consumer"["Integer"]) -> bool:
            """
            Unknown Tags
            - If the action is an instance of `IntConsumer` then it is cast
            to `IntConsumer` and passed to
            .tryAdvance(java.util.function.IntConsumer); otherwise
            the action is adapted to an instance of `IntConsumer`, by
            boxing the argument of `IntConsumer`, and then passed to
            .tryAdvance(java.util.function.IntConsumer).
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Integer"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `IntConsumer` then it is cast
            to `IntConsumer` and passed to
            .forEachRemaining(java.util.function.IntConsumer); otherwise
            the action is adapted to an instance of `IntConsumer`, by
            boxing the argument of `IntConsumer`, and then passed to
            .forEachRemaining(java.util.function.IntConsumer).
            """
            ...


    class OfLong(OfPrimitive):
        """
        A Spliterator specialized for `long` values.

        Since
        - 1.8
        """

        def trySplit(self) -> "OfLong":
            ...


        def tryAdvance(self, action: "LongConsumer") -> bool:
            ...


        def forEachRemaining(self, action: "LongConsumer") -> None:
            ...


        def tryAdvance(self, action: "Consumer"["Long"]) -> bool:
            """
            Unknown Tags
            - If the action is an instance of `LongConsumer` then it is cast
            to `LongConsumer` and passed to
            .tryAdvance(java.util.function.LongConsumer); otherwise
            the action is adapted to an instance of `LongConsumer`, by
            boxing the argument of `LongConsumer`, and then passed to
            .tryAdvance(java.util.function.LongConsumer).
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Long"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `LongConsumer` then it is cast
            to `LongConsumer` and passed to
            .forEachRemaining(java.util.function.LongConsumer); otherwise
            the action is adapted to an instance of `LongConsumer`, by
            boxing the argument of `LongConsumer`, and then passed to
            .forEachRemaining(java.util.function.LongConsumer).
            """
            ...


    class OfDouble(OfPrimitive):
        """
        A Spliterator specialized for `double` values.

        Since
        - 1.8
        """

        def trySplit(self) -> "OfDouble":
            ...


        def tryAdvance(self, action: "DoubleConsumer") -> bool:
            ...


        def forEachRemaining(self, action: "DoubleConsumer") -> None:
            ...


        def tryAdvance(self, action: "Consumer"["Double"]) -> bool:
            """
            Unknown Tags
            - If the action is an instance of `DoubleConsumer` then it is
            cast to `DoubleConsumer` and passed to
            .tryAdvance(java.util.function.DoubleConsumer); otherwise
            the action is adapted to an instance of `DoubleConsumer`, by
            boxing the argument of `DoubleConsumer`, and then passed to
            .tryAdvance(java.util.function.DoubleConsumer).
            """
            ...


        def forEachRemaining(self, action: "Consumer"["Double"]) -> None:
            """
            Unknown Tags
            - If the action is an instance of `DoubleConsumer` then it is
            cast to `DoubleConsumer` and passed to
            .forEachRemaining(java.util.function.DoubleConsumer);
            otherwise the action is adapted to an instance of
            `DoubleConsumer`, by boxing the argument of
            `DoubleConsumer`, and then passed to
            .forEachRemaining(java.util.function.DoubleConsumer).
            """
            ...
