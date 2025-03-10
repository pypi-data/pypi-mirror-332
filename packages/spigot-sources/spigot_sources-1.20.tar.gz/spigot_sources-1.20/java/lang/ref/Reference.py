"""
Python module generated from Java source file java.lang.ref.Reference

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.lang.ref import *
from jdk.internal.access import JavaLangRefAccess
from jdk.internal.access import SharedSecrets
from jdk.internal.ref import Cleaner
from jdk.internal.vm.annotation import ForceInline
from jdk.internal.vm.annotation import IntrinsicCandidate
from typing import Any, Callable, Iterable, Tuple


class Reference:

    def get(self) -> "T":
        """
        Returns this reference object's referent.  If this reference object has
        been cleared, either by the program or by the garbage collector, then
        this method returns `null`.

        Returns
        - The object to which this reference refers, or
                  `null` if this reference object has been cleared

        See
        - .refersTo

        Unknown Tags
        - This method returns a strong reference to the referent. This may cause
        the garbage collector to treat it as strongly reachable until some later
        collection cycle.  The .refersTo(Object) refersTo method can be
        used to avoid such strengthening when testing whether some object is
        the referent of a reference object; that is, use `ref.refersTo(obj)`
        rather than `ref.get() == obj`.
        """
        ...


    def refersTo(self, obj: "T") -> bool:
        """
        Tests if the referent of this reference object is `obj`.
        Using a `null` `obj` returns `True` if the
        reference object has been cleared.

        Arguments
        - obj: the object to compare with this reference object's referent

        Returns
        - `True` if `obj` is the referent of this reference object

        Since
        - 16
        """
        ...


    def clear(self) -> None:
        """
        Clears this reference object.  Invoking this method will not cause this
        object to be enqueued.
        
         This method is invoked only by Java code; when the garbage collector
        clears references it does so directly, without invoking this method.
        """
        ...


    def isEnqueued(self) -> bool:
        """
        Tests if this reference object is in its associated queue, if any.
        This method returns `True` only if all of the following conditions
        are met:
        
        - this reference object was registered with a queue when it was created; and
        - the garbage collector has added this reference object to the queue
            or .enqueue() is called; and
        - this reference object is not yet removed from the queue.
        
        Otherwise, this method returns `False`.
        This method may return `False` if this reference object has been cleared
        but not enqueued due to the race condition.

        Returns
        - `True` if and only if this reference object is
                  in its associated queue (if any).

        Deprecated
        - This method was originally specified to test if a reference object has
        been cleared and enqueued but was never implemented to do this test.
        This method could be misused due to the inherent race condition
        or without an associated `ReferenceQueue`.
        An application relying on this method to release critical resources
        could cause serious performance issue.
        An application should use ReferenceQueue to reliably determine
        what reference objects that have been enqueued or
        .refersTo(Object) refersTo(null) to determine if this reference
        object has been cleared.
        """
        ...


    def enqueue(self) -> bool:
        """
        Clears this reference object and adds it to the queue with which
        it is registered, if any.
        
         This method is invoked only by Java code; when the garbage collector
        enqueues references it does so directly, without invoking this method.

        Returns
        - `True` if this reference object was successfully
                  enqueued; `False` if it was already enqueued or if
                  it was not registered with a queue when it was created
        """
        ...


    @staticmethod
    def reachabilityFence(ref: "Object") -> None:
        """
        Ensures that the object referenced by the given reference remains
        <a href="package-summary.html#reachability">*strongly reachable*</a>,
        regardless of any prior actions of the program that might otherwise cause
        the object to become unreachable; thus, the referenced object is not
        reclaimable by garbage collection at least until after the invocation of
        this method.  Invocation of this method does not itself initiate garbage
        collection or finalization.
        
         This method establishes an ordering for
        <a href="package-summary.html#reachability">*strong reachability*</a>
        with respect to garbage collection.  It controls relations that are
        otherwise only implicit in a program -- the reachability conditions
        triggering garbage collection.  This method is designed for use in
        uncommon situations of premature finalization where using
        `synchronized` blocks or methods, or using other synchronization
        facilities are not possible or do not provide the desired control.  This
        method is applicable only when reclamation may have visible effects,
        which is possible for objects with finalizers (See Section 12.6
        of <cite>The Java Language Specification</cite>) that
        are implemented in ways that rely on ordering control for
        correctness.

        Arguments
        - ref: the reference. If `null`, this method has no effect.

        Since
        - 9

        Unknown Tags
        - Finalization may occur whenever the virtual machine detects that no
        reference to an object will ever be stored in the heap: The garbage
        collector may reclaim an object even if the fields of that object are
        still in use, so long as the object has otherwise become unreachable.
        This may have surprising and undesirable effects in cases such as the
        following example in which the bookkeeping associated with a class is
        managed through array indices.  Here, method `action` uses a
        `reachabilityFence` to ensure that the `Resource` object is
        not reclaimed before bookkeeping on an associated
        `ExternalResource` has been performed; in particular here, to
        ensure that the array slot holding the `ExternalResource` is not
        nulled out in method Object.finalize, which may otherwise run
        concurrently.
        
        ``` `class Resource {
          private static ExternalResource[] externalResourceArray = ...
        
          int myIndex;
          Resource(...) {
            myIndex = ...
            externalResourceArray[myIndex] = ...;
            ...`
          protected void finalize() {
            externalResourceArray[myIndex] = null;
            ...
          }
          public void action() {
            try {
              // ...
              int i = myIndex;
              Resource.update(externalResourceArray[i]);
            } finally {
              Reference.reachabilityFence(this);
            }
          }
          private static void update(ExternalResource ext) {
            ext.status = ...;
          }
        }}```
        
        Here, the invocation of `reachabilityFence` is nonintuitively
        placed *after* the call to `update`, to ensure that the
        array slot is not nulled out by Object.finalize before the
        update, even if the call to `action` was the last use of this
        object.  This might be the case if, for example a usage in a user program
        had the form `new Resource().action();` which retains no other
        reference to this `Resource`.  While probably overkill here,
        `reachabilityFence` is placed in a `finally` block to ensure
        that it is invoked across all paths in the method.  In a method with more
        complex control paths, you might need further precautions to ensure that
        `reachabilityFence` is encountered along all of them.
        
         It is sometimes possible to better encapsulate use of
        `reachabilityFence`.  Continuing the above example, if it were
        acceptable for the call to method `update` to proceed even if the
        finalizer had already executed (nulling out slot), then you could
        localize use of `reachabilityFence`:
        
        ``` `public void action2() {
          // ...
          Resource.update(getExternalResource());`
        private ExternalResource getExternalResource() {
          ExternalResource ext = externalResourceArray[myIndex];
          Reference.reachabilityFence(this);
          return ext;
        }}```
        
         Method `reachabilityFence` is not required in constructions
        that themselves ensure reachability.  For example, because objects that
        are locked cannot, in general, be reclaimed, it would suffice if all
        accesses of the object, in all methods of class `Resource`
        (including `finalize`) were enclosed in `synchronized (this)`
        blocks.  (Further, such blocks must not include infinite loops, or
        themselves be unreachable, which fall into the corner case exceptions to
        the "in general" disclaimer.)  However, method `reachabilityFence`
        remains a better option in cases where this approach is not as efficient,
        desirable, or possible; for example because it would encounter deadlock.
        - 12.6 Finalization of Class Instances
        """
        ...
