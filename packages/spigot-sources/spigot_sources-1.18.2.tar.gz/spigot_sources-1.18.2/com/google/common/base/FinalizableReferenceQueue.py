"""
Python module generated from Java source file com.google.common.base.FinalizableReferenceQueue

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtIncompatible
from com.google.common.annotations import VisibleForTesting
from com.google.common.base import *
from java.io import Closeable
from java.io import FileNotFoundException
from java.io import IOException
from java.lang.ref import PhantomReference
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.reflect import Method
from java.net import URL
from java.net import URLClassLoader
from javax.annotation import CheckForNull
from typing import Any, Callable, Iterable, Tuple


class FinalizableReferenceQueue(Closeable):
    """
    A reference queue with an associated background thread that dequeues references and invokes
    FinalizableReference.finalizeReferent() on them.
    
    Keep a strong reference to this object until all of the associated referents have been
    finalized. If this object is garbage collected earlier, the backing thread will not invoke `finalizeReferent()` on the remaining references.
    
    As an example of how this is used, imagine you have a class `MyServer` that creates a
    java.net.ServerSocket ServerSocket, and you would like to ensure that the `ServerSocket` is closed even if the `MyServer` object is garbage-collected without calling
    its `close` method. You *could* use a finalizer to accomplish this, but that has a
    number of well-known problems. Here is how you might use this class instead:
    
    ````public class MyServer implements Closeable {
      private static final FinalizableReferenceQueue frq = new FinalizableReferenceQueue();
      // You might also share this between several objects.
    
      private static final Set<Reference<?>> references = Sets.newConcurrentHashSet();
      // This ensures that the FinalizablePhantomReference itself is not garbage-collected.
    
      private final ServerSocket serverSocket;
    
      private MyServer(...) {
        ...
        this.serverSocket = new ServerSocket(...);
        ...`
    
      public static MyServer create(...) {
        MyServer myServer = new MyServer(...);
        final ServerSocket serverSocket = myServer.serverSocket;
        Reference<?> reference = new FinalizablePhantomReference<MyServer>(myServer, frq) {
          public void finalizeReferent() {
            references.remove(this):
            if (!serverSocket.isClosed()) {
              ...log a message about how nobody called close()...
              try {
                serverSocket.close();
              } catch (IOException e) {
                ...
              }
            }
          }
        };
        references.add(reference);
        return myServer;
      }
    
      public void close() {
        serverSocket.close();
      }
    }
    }```

    Author(s)
    - Bob Lee

    Since
    - 2.0
    """

    def __init__(self):
        """
        Constructs a new queue.
        """
        ...


    def close(self) -> None:
        ...
