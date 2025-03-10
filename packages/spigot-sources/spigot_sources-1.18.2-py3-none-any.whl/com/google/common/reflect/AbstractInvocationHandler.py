"""
Python module generated from Java source file com.google.common.reflect.AbstractInvocationHandler

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.reflect import *
from java.lang.reflect import InvocationHandler
from java.lang.reflect import Method
from java.lang.reflect import Proxy
from java.util import Arrays
from javax.annotation import CheckForNull
from org.checkerframework.checker.nullness.qual import Nullable
from typing import Any, Callable, Iterable, Tuple


class AbstractInvocationHandler(InvocationHandler):
    """
    Abstract implementation of InvocationHandler that handles Object.equals, Object.hashCode and Object.toString. For example:
    
    ```
    class Unsupported extends AbstractInvocationHandler {
      protected Object handleInvocation(Object proxy, Method method, Object[] args) {
        throw new UnsupportedOperationException();
      }
    }
    
    CharSequence unsupported = Reflection.newProxy(CharSequence.class, new Unsupported());
    ```

    Author(s)
    - Ben Yu

    Since
    - 12.0
    """

    def invoke(self, proxy: "Object", method: "Method", args: list["Object"]) -> "Object":
        """
        
        
        
          - `proxy.hashCode()` delegates to AbstractInvocationHandler.hashCode
          - `proxy.toString()` delegates to AbstractInvocationHandler.toString
          - `proxy.equals(argument)` returns True if:
              
                - `proxy` and `argument` are of the same type
                - and AbstractInvocationHandler.equals returns True for the InvocationHandler of `argument`
              
          - other method calls are dispatched to .handleInvocation.
        """
        ...


    def equals(self, obj: "Object") -> bool:
        """
        By default delegates to Object.equals so instances are only equal if they are
        identical. `proxy.equals(argument)` returns True if:
        
        
          - `proxy` and `argument` are of the same type
          - and this method returns True for the InvocationHandler of `argument`
        
        
        Subclasses can override this method to provide custom equality.
        """
        ...


    def hashCode(self) -> int:
        """
        By default delegates to Object.hashCode. The dynamic proxies' `hashCode()` will
        delegate to this method. Subclasses can override this method to provide custom equality.
        """
        ...


    def toString(self) -> str:
        """
        By default delegates to Object.toString. The dynamic proxies' `toString()` will
        delegate to this method. Subclasses can override this method to provide custom string
        representation for the proxies.
        """
        ...
