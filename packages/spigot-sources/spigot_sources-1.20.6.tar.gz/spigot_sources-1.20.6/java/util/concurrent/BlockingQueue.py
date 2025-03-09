"""
Python module generated from Java source file java.util.concurrent.BlockingQueue

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Queue
from java.util.concurrent import *
from typing import Any, Callable, Iterable, Tuple


class BlockingQueue(Queue):
    """
    A Queue that additionally supports operations that wait for
    the queue to become non-empty when retrieving an element, and wait
    for space to become available in the queue when storing an element.
    
    `BlockingQueue` methods come in four forms, with different ways
    of handling operations that cannot be satisfied immediately, but may be
    satisfied at some point in the future:
    one throws an exception, the second returns a special value (either
    `null` or `False`, depending on the operation), the third
    blocks the current thread indefinitely until the operation can succeed,
    and the fourth blocks for only a given maximum time limit before giving
    up.  These methods are summarized in the following table:
    
    <table class="plain">
    <caption>Summary of BlockingQueue methods</caption>
     <tr>
       <td></td>
       <th scope="col" style="font-weight:normal; font-style:italic">Throws exception</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Special value</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Blocks</th>
       <th scope="col" style="font-weight:normal; font-style:italic">Times out</th>
     </tr>
     <tr>
       <th scope="row" style="text-align:left">Insert</th>
       <td>.add(Object) add(e)</td>
       <td>.offer(Object) offer(e)</td>
       <td>.put(Object) put(e)</td>
       <td>.offer(Object, long, TimeUnit) offer(e, time, unit)</td>
     </tr>
     <tr>
       <th scope="row" style="text-align:left">Remove</th>
       <td>.remove() remove()</td>
       <td>.poll() poll()</td>
       <td>.take() take()</td>
       <td>.poll(long, TimeUnit) poll(time, unit)</td>
     </tr>
     <tr>
       <th scope="row" style="text-align:left">Examine</th>
       <td>.element() element()</td>
       <td>.peek() peek()</td>
       <td style="font-style: italic">not applicable</td>
       <td style="font-style: italic">not applicable</td>
     </tr>
    </table>
    
    A `BlockingQueue` does not accept `null` elements.
    Implementations throw `NullPointerException` on attempts
    to `add`, `put` or `offer` a `null`.  A
    `null` is used as a sentinel value to indicate failure of
    `poll` operations.
    
    A `BlockingQueue` may be capacity bounded. At any given
    time it may have a `remainingCapacity` beyond which no
    additional elements can be `put` without blocking.
    A `BlockingQueue` without any intrinsic capacity constraints always
    reports a remaining capacity of `Integer.MAX_VALUE`.
    
    `BlockingQueue` implementations are designed to be used
    primarily for producer-consumer queues, but additionally support
    the Collection interface.  So, for example, it is
    possible to remove an arbitrary element from a queue using
    `remove(x)`. However, such operations are in general
    *not* performed very efficiently, and are intended for only
    occasional use, such as when a queued message is cancelled.
    
    `BlockingQueue` implementations are thread-safe.  All
    queuing methods achieve their effects atomically using internal
    locks or other forms of concurrency control. However, the
    *bulk* Collection operations `addAll`,
    `containsAll`, `retainAll` and `removeAll` are
    *not* necessarily performed atomically unless specified
    otherwise in an implementation. So it is possible, for example, for
    `addAll(c)` to fail (throwing an exception) after adding
    only some of the elements in `c`.
    
    A `BlockingQueue` does *not* intrinsically support
    any kind of &quot;close&quot; or &quot;shutdown&quot; operation to
    indicate that no more items will be added.  The needs and usage of
    such features tend to be implementation-dependent. For example, a
    common tactic is for producers to insert special
    *end-of-stream* or *poison* objects, that are
    interpreted accordingly when taken by consumers.
    
    
    Usage example, based on a typical producer-consumer scenario.
    Note that a `BlockingQueue` can safely be used with multiple
    producers and multiple consumers.
    ``` `class Producer implements Runnable {
      private final BlockingQueue queue;
      Producer(BlockingQueue q) { queue = q;`
      public void run() {
        try {
          while (True) { queue.put(produce()); }
        } catch (InterruptedException ex) { ... handle ...}
      }
      Object produce() { ... }
    }
    
    class Consumer implements Runnable {
      private final BlockingQueue queue;
      Consumer(BlockingQueue q) { queue = q; }
      public void run() {
        try {
          while (True) { consume(queue.take()); }
        } catch (InterruptedException ex) { ... handle ...}
      }
      void consume(Object x) { ... }
    }
    
    class Setup {
      void main() {
        BlockingQueue q = new SomeQueueImplementation();
        Producer p = new Producer(q);
        Consumer c1 = new Consumer(q);
        Consumer c2 = new Consumer(q);
        new Thread(p).start();
        new Thread(c1).start();
        new Thread(c2).start();
      }
    }}```
    
    Memory consistency effects: As with other concurrent
    collections, actions in a thread prior to placing an object into a
    `BlockingQueue`
    <a href="package-summary.html#MemoryVisibility">*happen-before*</a>
    actions subsequent to the access or removal of that element from
    the `BlockingQueue` in another thread.
    
    This interface is a member of the
    <a href="/java.base/java/util/package-summary.html#CollectionsFramework">
    Java Collections Framework</a>.
    
    Type `<E>`: the type of elements held in this queue

    Author(s)
    - Doug Lea

    Since
    - 1.5
    """

    def add(self, e: "E") -> bool:
        """
        Inserts the specified element into this queue if it is possible to do
        so immediately without violating capacity restrictions, returning
        `True` upon success and throwing an
        `IllegalStateException` if no space is currently available.
        When using a capacity-restricted queue, it is generally preferable to
        use .offer(Object) offer.

        Arguments
        - e: the element to add

        Returns
        - `True` (as specified by Collection.add)

        Raises
        - IllegalStateException: if the element cannot be added at this
                time due to capacity restrictions
        - ClassCastException: if the class of the specified element
                prevents it from being added to this queue
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this queue
        """
        ...


    def offer(self, e: "E") -> bool:
        """
        Inserts the specified element into this queue if it is possible to do
        so immediately without violating capacity restrictions, returning
        `True` upon success and `False` if no space is currently
        available.  When using a capacity-restricted queue, this method is
        generally preferable to .add, which can fail to insert an
        element only by throwing an exception.

        Arguments
        - e: the element to add

        Returns
        - `True` if the element was added to this queue, else
                `False`

        Raises
        - ClassCastException: if the class of the specified element
                prevents it from being added to this queue
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this queue
        """
        ...


    def put(self, e: "E") -> None:
        """
        Inserts the specified element into this queue, waiting if necessary
        for space to become available.

        Arguments
        - e: the element to add

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this queue
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this queue
        """
        ...


    def offer(self, e: "E", timeout: int, unit: "TimeUnit") -> bool:
        """
        Inserts the specified element into this queue, waiting up to the
        specified wait time if necessary for space to become available.

        Arguments
        - e: the element to add
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - `True` if successful, or `False` if
                the specified waiting time elapses before space is available

        Raises
        - InterruptedException: if interrupted while waiting
        - ClassCastException: if the class of the specified element
                prevents it from being added to this queue
        - NullPointerException: if the specified element is null
        - IllegalArgumentException: if some property of the specified
                element prevents it from being added to this queue
        """
        ...


    def take(self) -> "E":
        """
        Retrieves and removes the head of this queue, waiting if necessary
        until an element becomes available.

        Returns
        - the head of this queue

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def poll(self, timeout: int, unit: "TimeUnit") -> "E":
        """
        Retrieves and removes the head of this queue, waiting up to the
        specified wait time if necessary for an element to become available.

        Arguments
        - timeout: how long to wait before giving up, in units of
               `unit`
        - unit: a `TimeUnit` determining how to interpret the
               `timeout` parameter

        Returns
        - the head of this queue, or `null` if the
                specified waiting time elapses before an element is available

        Raises
        - InterruptedException: if interrupted while waiting
        """
        ...


    def remainingCapacity(self) -> int:
        """
        Returns the number of additional elements that this queue can ideally
        (in the absence of memory or resource constraints) accept without
        blocking, or `Integer.MAX_VALUE` if there is no intrinsic
        limit.
        
        Note that you *cannot* always tell if an attempt to insert
        an element will succeed by inspecting `remainingCapacity`
        because it may be the case that another thread is about to
        insert or remove an element.

        Returns
        - the remaining capacity
        """
        ...


    def remove(self, o: "Object") -> bool:
        """
        Removes a single instance of the specified element from this queue,
        if it is present.  More formally, removes an element `e` such
        that `o.equals(e)`, if this queue contains one or more such
        elements.
        Returns `True` if this queue contained the specified element
        (or equivalently, if this queue changed as a result of the call).

        Arguments
        - o: element to be removed from this queue, if present

        Returns
        - `True` if this queue changed as a result of the call

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this queue
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def contains(self, o: "Object") -> bool:
        """
        Returns `True` if this queue contains the specified element.
        More formally, returns `True` if and only if this queue contains
        at least one element `e` such that `o.equals(e)`.

        Arguments
        - o: object to be checked for containment in this queue

        Returns
        - `True` if this queue contains the specified element

        Raises
        - ClassCastException: if the class of the specified element
                is incompatible with this queue
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        - NullPointerException: if the specified element is null
        (<a href="/java.base/java/util/Collection.html#optional-restrictions">optional</a>)
        """
        ...


    def drainTo(self, c: Iterable["E"]) -> int:
        """
        Removes all available elements from this queue and adds them
        to the given collection.  This operation may be more
        efficient than repeatedly polling this queue.  A failure
        encountered while attempting to add elements to
        collection `c` may result in elements being in neither,
        either or both collections when the associated exception is
        thrown.  Attempts to drain a queue to itself result in
        `IllegalArgumentException`. Further, the behavior of
        this operation is undefined if the specified collection is
        modified while the operation is in progress.

        Arguments
        - c: the collection to transfer elements into

        Returns
        - the number of elements transferred

        Raises
        - UnsupportedOperationException: if addition of elements
                is not supported by the specified collection
        - ClassCastException: if the class of an element of this queue
                prevents it from being added to the specified collection
        - NullPointerException: if the specified collection is null
        - IllegalArgumentException: if the specified collection is this
                queue, or some property of an element of this queue prevents
                it from being added to the specified collection
        """
        ...


    def drainTo(self, c: Iterable["E"], maxElements: int) -> int:
        """
        Removes at most the given number of available elements from
        this queue and adds them to the given collection.  A failure
        encountered while attempting to add elements to
        collection `c` may result in elements being in neither,
        either or both collections when the associated exception is
        thrown.  Attempts to drain a queue to itself result in
        `IllegalArgumentException`. Further, the behavior of
        this operation is undefined if the specified collection is
        modified while the operation is in progress.

        Arguments
        - c: the collection to transfer elements into
        - maxElements: the maximum number of elements to transfer

        Returns
        - the number of elements transferred

        Raises
        - UnsupportedOperationException: if addition of elements
                is not supported by the specified collection
        - ClassCastException: if the class of an element of this queue
                prevents it from being added to the specified collection
        - NullPointerException: if the specified collection is null
        - IllegalArgumentException: if the specified collection is this
                queue, or some property of an element of this queue prevents
                it from being added to the specified collection
        """
        ...
