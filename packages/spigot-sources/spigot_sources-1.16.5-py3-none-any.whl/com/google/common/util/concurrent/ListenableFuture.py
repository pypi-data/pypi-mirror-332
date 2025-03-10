"""
Python module generated from Java source file com.google.common.util.concurrent.ListenableFuture

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.util.concurrent import *
from java.util.concurrent import Executor
from java.util.concurrent import Future
from java.util.concurrent import RejectedExecutionException
from typing import Any, Callable, Iterable, Tuple


class ListenableFuture(Future):
    """
    A Future that accepts completion listeners. Each listener has an associated executor, and
    it is invoked using this executor once the future's computation is Future.isDone()
    complete. If the computation has already completed when the listener is added, the listener will
    execute immediately.
    
    See the Guava User Guide article on
    <a href="https://github.com/google/guava/wiki/ListenableFutureExplained">
    `ListenableFuture`</a>.
    
    <h3>Purpose</h3>
    
    The main purpose of `ListenableFuture` is to help you chain together a graph of
    asynchronous operations. You can chain them together manually with calls to methods like
    Futures.transform(ListenableFuture, Function, Executor) Futures.transform, but you will
    often find it easier to use a framework. Frameworks automate the process, often adding features
    like monitoring, debugging, and cancellation. Examples of frameworks include:
    
    
    - <a href="http://google.github.io/dagger/producers.html">Dagger Producers</a>
    
    
    The main purpose of .addListener addListener is to support this chaining. You will
    rarely use it directly, in part because it does not provide direct access to the `Future`
    result. (If you want such access, you may prefer Futures.addCallback
    Futures.addCallback.) Still, direct `addListener` calls are occasionally useful:
    
    ```   `final String name = ...;
      inFlight.add(name);
      ListenableFuture<Result> future = service.query(name);
      future.addListener(new Runnable() {
        public void run() {
          processedCount.incrementAndGet();
          inFlight.remove(name);
          lastProcessed.set(name);
          logger.info("Done with {0`", name);
        }
      }, executor);}```
    
    <h3>How to get an instance</h3>
    
    We encourage you to return `ListenableFuture` from your methods so that your users can
    take advantage of the Futures utilities built atop the class. The way that you will
    create `ListenableFuture` instances depends on how you currently create `Future`
    instances:
    
    - If you receive them from an `java.util.concurrent.ExecutorService`, convert that
        service to a ListeningExecutorService, usually by calling
        MoreExecutors.listeningDecorator(java.util.concurrent.ExecutorService)
        MoreExecutors.listeningDecorator.
    - If you manually call java.util.concurrent.FutureTask.set or a similar method, create
        a SettableFuture instead. (If your needs are more complex, you may prefer
        AbstractFuture.)
    
    
    **Test doubles**: If you need a `ListenableFuture` for your test, try a SettableFuture or one of the methods in the Futures.immediateFuture Futures.immediate*
    family. **Avoid** creating a mock or stub `Future`. Mock and stub implementations are
    fragile because they assume that only certain methods will be called and because they often
    implement subtleties of the API improperly.
    
    **Custom implementation**: Avoid implementing `ListenableFuture` from scratch. If you
    can't get by with the standard implementations, prefer to derive a new `Future` instance
    with the methods in Futures or, if necessary, to extend AbstractFuture.
    
    Occasionally, an API will return a plain `Future` and it will be impossible to change
    the return type. For this case, we provide a more expensive workaround in `JdkFutureAdapters`. However, when possible, it is more efficient and reliable to create a `ListenableFuture` directly.

    Author(s)
    - Nishant Thakkar

    Since
    - 1.0
    """

    def addListener(self, listener: "Runnable", executor: "Executor") -> None:
        """
        Registers a listener to be Executor.execute(Runnable) run on the given executor.
        The listener will run when the `Future`'s computation is Future.isDone()
        complete or, if the computation is already complete, immediately.
        
        There is no guaranteed ordering of execution of listeners, but any listener added through
        this method is guaranteed to be called once the computation is complete.
        
        Exceptions thrown by a listener will be propagated up to the executor. Any exception thrown
        during `Executor.execute` (e.g., a `RejectedExecutionException` or an exception
        thrown by MoreExecutors.directExecutor direct execution) will be caught and
        logged.
        
        Note: For fast, lightweight listeners that would be safe to execute in any thread, consider
        MoreExecutors.directExecutor. Otherwise, avoid it. Heavyweight `directExecutor`
        listeners can cause problems, and these problems can be difficult to reproduce because they
        depend on timing. For example:
        
        
        - The listener may be executed by the caller of `addListener`. That caller may be a UI
        thread or other latency-sensitive thread. This can harm UI responsiveness.
        - The listener may be executed by the thread that completes this `Future`. That thread
        may be an internal system thread such as an RPC network thread. Blocking that thread may stall
        progress of the whole system. It may even cause a deadlock.
        - The listener may delay other listeners, even listeners that are not themselves `directExecutor` listeners.
        
        
        This is the most general listener interface. For common operations performed using
        listeners, see Futures. For a simplified but general listener interface, see Futures.addCallback addCallback().
        
        Memory consistency effects: Actions in a thread prior to adding a listener <a
        href="https://docs.oracle.com/javase/specs/jls/se7/html/jls-17.html#jls-17.4.5">
        *happen-before*</a> its execution begins, perhaps in another thread.

        Arguments
        - listener: the listener to run when the computation is complete
        - executor: the executor to run the listener in

        Raises
        - RejectedExecutionException: if we tried to execute the listener immediately but the
            executor rejected it.
        """
        ...
