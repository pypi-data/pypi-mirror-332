"""
Python module generated from Java source file com.google.common.annotations.GwtIncompatible

Java source file obtained from artifact guava version 31.0.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import *
from typing import Any, Callable, Iterable, Tuple


class GwtIncompatible:
    """
    The presence of this annotation on an API indicates that the method may *not* be used with
    the <a href="http://www.gwtproject.org/">Google Web Toolkit</a> (GWT).
    
    This annotation behaves identically to <a href=
    "http://www.gwtproject.org/javadoc/latest/com/google/gwt/core/shared/GwtIncompatible.html">the
    `@GwtIncompatible` annotation in GWT itself</a>.

    Author(s)
    - Charles Fry
    """

    def value(self) -> str:
        """
        Describes why the annotated element is incompatible with GWT. Since this is generally due to a
        dependence on a type/method which GWT doesn't support, it is sufficient to simply reference the
        unsupported type/method. E.g. "Class.isInstance".
        
        As of Guava 20.0, this value is optional. We encourage authors who wish to describe why an
        API is `@GwtIncompatible` to instead leave an implementation comment.
        """
        return ""
