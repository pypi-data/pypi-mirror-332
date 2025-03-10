"""
Python module generated from Java source file com.google.common.eventbus.EventBus

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.base import MoreObjects
from com.google.common.eventbus import *
from com.google.common.util.concurrent import MoreExecutors
from java.lang.reflect import Method
from java.util import Iterator
from java.util import Locale
from java.util.concurrent import Executor
from typing import Any, Callable, Iterable, Tuple


class EventBus:
    """
    Dispatches events to listeners, and provides ways for listeners to register themselves.
    
    The EventBus allows publish-subscribe-style communication between components without requiring
    the components to explicitly register with one another (and thus be aware of each other). It is
    designed exclusively to replace traditional Java in-process event distribution using explicit
    registration. It is *not* a general-purpose publish-subscribe system, nor is it intended
    for interprocess communication.
    
    <h2>Receiving Events</h2>
    
    To receive events, an object should:
    <ol>
    - Expose a public method, known as the *event subscriber*, which accepts a single argument
        of the type of event desired;
    - Mark it with a Subscribe annotation;
    - Pass itself to an EventBus instance's .register(Object) method.
    </ol>
    
    <h2>Posting Events</h2>
    
    To post an event, simply provide the event object to the .post(Object) method. The
    EventBus instance will determine the type of event and route it to all registered listeners.
    
    Events are routed based on their type &mdash; an event will be delivered to any subscriber for
    any type to which the event is *assignable.* This includes implemented interfaces, all
    superclasses, and all interfaces implemented by superclasses.
    
    When `post` is called, all registered subscribers for an event are run in sequence, so
    subscribers should be reasonably quick. If an event may trigger an extended process (such as a
    database load), spawn a thread or queue it for later. (For a convenient way to do this, use an
    AsyncEventBus.)
    
    <h2>Subscriber Methods</h2>
    
    Event subscriber methods must accept only one argument: the event.
    
    Subscribers should not, in general, throw. If they do, the EventBus will catch and log the
    exception. This is rarely the right solution for error handling and should not be relied upon; it
    is intended solely to help find problems during development.
    
    The EventBus guarantees that it will not call a subscriber method from multiple threads
    simultaneously, unless the method explicitly allows it by bearing the
    AllowConcurrentEvents annotation. If this annotation is not present, subscriber methods
    need not worry about being reentrant, unless also called from outside the EventBus.
    
    <h2>Dead Events</h2>
    
    If an event is posted, but no registered subscribers can accept it, it is considered "dead."
    To give the system a second chance to handle dead events, they are wrapped in an instance of
    DeadEvent and reposted.
    
    If a subscriber for a supertype of all events (such as Object) is registered, no event will
    ever be considered dead, and no DeadEvents will be generated. Accordingly, while DeadEvent
    extends Object, a subscriber registered to receive any Object will never receive a
    DeadEvent.
    
    This class is safe for concurrent use.
    
    See the Guava User Guide article on
    <a href="https://github.com/google/guava/wiki/EventBusExplained">`EventBus`</a>.

    Author(s)
    - Cliff Biffle

    Since
    - 10.0
    """

    def __init__(self):
        """
        Creates a new EventBus named "default".
        """
        ...


    def __init__(self, identifier: str):
        """
        Creates a new EventBus with the given `identifier`.

        Arguments
        - identifier: a brief name for this bus, for logging purposes. Should be a valid Java
            identifier.
        """
        ...


    def __init__(self, exceptionHandler: "SubscriberExceptionHandler"):
        """
        Creates a new EventBus with the given SubscriberExceptionHandler.

        Arguments
        - exceptionHandler: Handler for subscriber exceptions.

        Since
        - 16.0
        """
        ...


    def identifier(self) -> str:
        """
        Returns the identifier for this event bus.

        Since
        - 19.0
        """
        ...


    def register(self, object: "Object") -> None:
        """
        Registers all subscriber methods on `object` to receive events.

        Arguments
        - object: object whose subscriber methods should be registered.
        """
        ...


    def unregister(self, object: "Object") -> None:
        """
        Unregisters all subscriber methods on a registered `object`.

        Arguments
        - object: object whose subscriber methods should be unregistered.

        Raises
        - IllegalArgumentException: if the object was not previously registered.
        """
        ...


    def post(self, event: "Object") -> None:
        """
        Posts an event to all registered subscribers. This method will return successfully after the
        event has been posted to all subscribers, and regardless of any exceptions thrown by
        subscribers.
        
        If no subscribers have been subscribed for `event`'s class, and `event` is not
        already a DeadEvent, it will be wrapped in a DeadEvent and reposted.

        Arguments
        - event: event to post.
        """
        ...


    def toString(self) -> str:
        ...
