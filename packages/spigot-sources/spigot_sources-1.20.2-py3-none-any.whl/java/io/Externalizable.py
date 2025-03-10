"""
Python module generated from Java source file java.io.Externalizable

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.io import ObjectInput
from java.io import ObjectOutput
from typing import Any, Callable, Iterable, Tuple


class Externalizable(Serializable):
    """
    Only the identity of the class of an Externalizable instance is
    written in the serialization stream and it is the responsibility
    of the class to save and restore the contents of its instances.
    
    The writeExternal and readExternal methods of the Externalizable
    interface are implemented by a class to give the class complete
    control over the format and contents of the stream for an object
    and its supertypes. These methods must explicitly
    coordinate with the supertype to save its state. These methods supersede
    customized implementations of writeObject and readObject methods.
    
    Object Serialization uses the Serializable and Externalizable
    interfaces.  Object persistence mechanisms can use them as well.  Each
    object to be stored is tested for the Externalizable interface. If
    the object supports Externalizable, the writeExternal method is called. If the
    object does not support Externalizable and does implement
    Serializable, the object is saved using
    ObjectOutputStream.  When an Externalizable object is
    reconstructed, an instance is created using the public no-arg
    constructor, then the readExternal method called.  Serializable
    objects are restored by reading them from an ObjectInputStream.
    
    An Externalizable instance can designate a substitution object via
    the writeReplace and readResolve methods documented in the Serializable
    interface.

    See
    - java.io.Serializable

    Since
    - 1.1
    """

    def writeExternal(self, out: "ObjectOutput") -> None:
        """
        The object implements the writeExternal method to save its contents
        by calling the methods of DataOutput for its primitive values or
        calling the writeObject method of ObjectOutput for objects, strings,
        and arrays.

        Arguments
        - out: the stream to write the object to

        Raises
        - IOException: Includes any I/O exceptions that may occur

        Serial Data
        - Overriding methods should use this tag to describe
                    the data layout of this Externalizable object.
                    List the sequence of element types and, if possible,
                    relate the element to a public/protected field and/or
                    method of this Externalizable class.
        """
        ...


    def readExternal(self, in: "ObjectInput") -> None:
        """
        The object implements the readExternal method to restore its
        contents by calling the methods of DataInput for primitive
        types and readObject for objects, strings and arrays.  The
        readExternal method must read the values in the same sequence
        and with the same types as were written by writeExternal.

        Arguments
        - in: the stream to read data from in order to restore the object

        Raises
        - IOException: if I/O errors occur
        - ClassNotFoundException: If the class for an object being
                   restored cannot be found.
        """
        ...
