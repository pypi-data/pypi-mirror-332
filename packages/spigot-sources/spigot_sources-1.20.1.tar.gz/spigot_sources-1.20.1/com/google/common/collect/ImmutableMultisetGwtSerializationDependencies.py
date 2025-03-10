"""
Python module generated from Java source file com.google.common.collect.ImmutableMultisetGwtSerializationDependencies

Java source file obtained from artifact guava version 31.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.collect import *
from typing import Any, Callable, Iterable, Tuple


class ImmutableMultisetGwtSerializationDependencies(ImmutableCollection):
    """
    A dummy superclass to support GWT serialization of the element type of an ImmutableMultiset. The GWT supersource for this class contains a field of type `E`.
    
    For details about this hack, see `GwtSerializationDependencies`, which takes the same
    approach but with a subclass rather than a superclass.
    
    TODO(cpovirk): Consider applying this subclass approach to our other types.
    
    For `ImmutableMultiset` in particular, I ran into a problem with the `GwtSerializationDependencies` approach: When autogenerating a serializer for the new class, GWT
    tries to refer to our dummy serializer for the superclass,
    ImmutableMultiset_CustomFieldSerializer. But that type has no methods (since it's never actually
    used). We could probably fix the problem by adding dummy methods to that class, but that is
    starting to sound harder than taking the superclass approach, which I've been coming to like,
    anyway, since it doesn't require us to declare dummy methods (though occasionally constructors)
    and make types non-final.
    """


