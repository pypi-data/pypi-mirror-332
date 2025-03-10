"""
Python module generated from Java source file java.io.ObjectStreamClass

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.lang.invoke import MethodHandle
from java.lang.invoke import MethodHandles
from java.lang.invoke import MethodType
from java.lang.ref import Reference
from java.lang.ref import ReferenceQueue
from java.lang.ref import WeakReference
from java.lang.reflect import Constructor
from java.lang.reflect import Field
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Member
from java.lang.reflect import Method
from java.lang.reflect import Modifier
from java.lang.reflect import Proxy
from java.lang.reflect import RecordComponent
from java.lang.reflect import UndeclaredThrowableException
from java.security import AccessControlContext
from java.security import AccessController
from java.security import MessageDigest
from java.security import NoSuchAlgorithmException
from java.security import PermissionCollection
from java.security import Permissions
from java.security import PrivilegedAction
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.security import ProtectionDomain
from java.util import Arrays
from java.util import Collections
from java.util import Comparator
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from jdk.internal.access import JavaSecurityAccess
from jdk.internal.access import SharedSecrets
from jdk.internal.misc import Unsafe
from jdk.internal.reflect import CallerSensitive
from jdk.internal.reflect import Reflection
from jdk.internal.reflect import ReflectionFactory
from sun.reflect.misc import ReflectUtil
from typing import Any, Callable, Iterable, Tuple


class ObjectStreamClass(Serializable):
    """
    Serialization's descriptor for classes.  It contains the name and
    serialVersionUID of the class.  The ObjectStreamClass for a specific class
    loaded in this Java VM can be found/created using the lookup method.
    
    The algorithm to compute the SerialVersionUID is described in
    <a href="/../specs/serialization/class.html#stream-unique-identifiers">
       <cite>Java Object Serialization Specification,</cite> Section 4.6, "Stream Unique Identifiers"</a>.

    Author(s)
    - Roger Riggs

    See
    - <a href="/../specs/serialization/class.html">
         <cite>Java Object Serialization Specification,</cite> Section 4, "Class Descriptors"</a>

    Since
    - 1.1
    """

    NO_FIELDS = ObjectStreamField[0]
    """
    serialPersistentFields value indicating no serializable fields
    """


    @staticmethod
    def lookup(cl: type[Any]) -> "ObjectStreamClass":
        """
        Find the descriptor for a class that can be serialized.  Creates an
        ObjectStreamClass instance if one does not exist yet for class. Null is
        returned if the specified class does not implement java.io.Serializable
        or java.io.Externalizable.

        Arguments
        - cl: class for which to get the descriptor

        Returns
        - the class descriptor for the specified class
        """
        ...


    @staticmethod
    def lookupAny(cl: type[Any]) -> "ObjectStreamClass":
        """
        Returns the descriptor for any class, regardless of whether it
        implements Serializable.

        Arguments
        - cl: class for which to get the descriptor

        Returns
        - the class descriptor for the specified class

        Since
        - 1.6
        """
        ...


    def getName(self) -> str:
        """
        Returns the name of the class described by this descriptor.
        This method returns the name of the class in the format that
        is used by the Class.getName method.

        Returns
        - a string representing the name of the class
        """
        ...


    def getSerialVersionUID(self) -> int:
        """
        Return the serialVersionUID for this class.  The serialVersionUID
        defines a set of classes all with the same name that have evolved from a
        common root class and agree to be serialized and deserialized using a
        common format.  NonSerializable classes have a serialVersionUID of 0L.

        Returns
        - the SUID of the class described by this descriptor
        """
        ...


    def forClass(self) -> type[Any]:
        """
        Return the class in the local VM that this version is mapped to.  Null
        is returned if there is no corresponding local class.

        Returns
        - the `Class` instance that this descriptor represents
        """
        ...


    def getFields(self) -> list["ObjectStreamField"]:
        """
        Return an array of the fields of this serializable class.

        Returns
        - an array containing an element for each persistent field of
                 this class. Returns an array of length zero if there are no
                 fields.

        Since
        - 1.2
        """
        ...


    def getField(self, name: str) -> "ObjectStreamField":
        """
        Get the field of this class by name.

        Arguments
        - name: the name of the data field to look for

        Returns
        - The ObjectStreamField object of the named field or null if
                 there is no such named field.
        """
        ...


    def toString(self) -> str:
        """
        Return a string describing this ObjectStreamClass.
        """
        ...
