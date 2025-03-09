"""
Python module generated from Java source file com.google.common.util.concurrent.ListenerCallQueue

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import J2ktIncompatible
from com.google.common.base import Preconditions
from com.google.common.collect import Queues
from com.google.common.util.concurrent import *
from com.google.errorprone.annotations.concurrent import GuardedBy
from java.util import Collections
from java.util import Queue
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class ListenerCallQueue:
    """
    A list of listeners for implementing a concurrency friendly observable object.
    
    Listeners are registered once via .addListener and then may be invoked by .enqueue enqueueing and then .dispatch dispatching events.
    
    The API of this class is designed to make it easy to achieve the following properties
    
    
      - Multiple events for the same listener are never dispatched concurrently.
      - Events for the different listeners are dispatched concurrently.
      - All events for a given listener dispatch on the provided .executor.
      - It is easy for the user to ensure that listeners are never invoked while holding locks.
    
    
    The last point is subtle. Often the observable object will be managing its own internal state
    using a lock, however it is dangerous to dispatch listeners while holding a lock because they
    might run on the `directExecutor()` or be otherwise re-entrant (call back into your
    object). So it is important to not call .dispatch while holding any locks. This is why
    .enqueue and .dispatch are 2 different methods. It is expected that the decision
    to run a particular event is made during the state change, but the decision to actually invoke
    the listeners can be delayed slightly so that locks can be dropped. Also, because .dispatch is expected to be called concurrently, it is idempotent.
    """

    def addListener(self, listener: "L", executor: "Executor") -> None:
        """
        Adds a listener that will be called using the given executor when events are later .enqueue enqueued and .dispatch dispatched.
        """
        ...


    def enqueue(self, event: "Event"["L"]) -> None:
        """
        Enqueues an event to be run on currently known listeners.
        
        The `toString` method of the Event itself will be used to describe the event in the
        case of an error.

        Arguments
        - event: the callback to execute on .dispatch
        """
        ...


    def enqueue(self, event: "Event"["L"], label: str) -> None:
        """
        Enqueues an event to be run on currently known listeners, with a label.

        Arguments
        - event: the callback to execute on .dispatch
        - label: a description of the event to use in the case of an error
        """
        ...


    def dispatch(self) -> None:
        """
        Dispatches all events enqueued prior to this call, serially and in order, for every listener.
        
        Note: this method is idempotent and safe to call from any thread
        """
        ...
