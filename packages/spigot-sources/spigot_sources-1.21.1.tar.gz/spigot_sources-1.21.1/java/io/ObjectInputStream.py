"""
Python module generated from Java source file java.io.ObjectInputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.io.ObjectInputFilter import Config
from java.io.ObjectStreamClass import RecordSupport
from java.io.ObjectStreamClass import WeakClassKey
from java.lang.System import Logger
from java.lang.invoke import MethodHandle
from java.lang.ref import ReferenceQueue
from java.lang.reflect import Array
from java.lang.reflect import InvocationHandler
from java.lang.reflect import Modifier
from java.lang.reflect import Proxy
from java.security import AccessControlContext
from java.security import AccessController
from java.security import PrivilegedAction
from java.security import PrivilegedActionException
from java.security import PrivilegedExceptionAction
from java.util import Arrays
from java.util import Objects
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from jdk.internal.access import SharedSecrets
from jdk.internal.event import DeserializationEvent
from jdk.internal.misc import Unsafe
from sun.reflect.misc import ReflectUtil
from sun.security.action import GetBooleanAction
from sun.security.action import GetIntegerAction
from typing import Any, Callable, Iterable, Tuple


class ObjectInputStream(InputStream, ObjectInput, ObjectStreamConstants):
    """
    An ObjectInputStream deserializes primitive data and objects previously
    written using an ObjectOutputStream.
    
    <strong>Warning: Deserialization of untrusted data is inherently dangerous
    and should be avoided. Untrusted data should be carefully validated according to the
    "Serialization and Deserialization" section of the
    secure_coding_guidelines_javase Secure Coding Guidelines for Java SE.
    serialization_filter_guide Serialization Filtering describes best
    practices for defensive use of serial filters.
    </strong>
    
    The key to disabling deserialization attacks is to prevent instances of
    arbitrary classes from being deserialized, thereby preventing the direct or
    indirect execution of their methods.
    ObjectInputFilter describes how to use filters and
    ObjectInputFilter.Config describes how to configure the filter and filter factory.
    Each stream has an optional deserialization filter
    to check the classes and resource limits during deserialization.
    The JVM-wide filter factory ensures that a filter can be set on every ObjectInputStream
    and every object read from the stream can be checked.
    The .ObjectInputStream() ObjectInputStream constructors invoke the filter factory
    to select the initial filter which may be updated or replaced by .setObjectInputFilter.
    
    If an ObjectInputStream has a filter, the ObjectInputFilter can check that
    the classes, array lengths, number of references in the stream, depth, and
    number of bytes consumed from the input stream are allowed and
    if not, can terminate deserialization.
    
    ObjectOutputStream and ObjectInputStream can provide an application with
    persistent storage for graphs of objects when used with a FileOutputStream
    and FileInputStream respectively.  ObjectInputStream is used to recover
    those objects previously serialized. Other uses include passing objects
    between hosts using a socket stream or for marshaling and unmarshaling
    arguments and parameters in a remote communication system.
    
    ObjectInputStream ensures that the types of all objects in the graph
    created from the stream match the classes present in the Java Virtual
    Machine.  Classes are loaded as required using the standard mechanisms.
    
    Only objects that support the java.io.Serializable or
    java.io.Externalizable interface can be read from streams.
    
    The method `readObject` is used to read an object from the
    stream.  Java's safe casting should be used to get the desired type.  In
    Java, strings and arrays are objects and are treated as objects during
    serialization. When read they need to be cast to the expected type.
    
    Primitive data types can be read from the stream using the appropriate
    method on DataInput.
    
    The default deserialization mechanism for objects restores the contents
    of each field to the value and type it had when it was written.  Fields
    declared as transient or static are ignored by the deserialization process.
    References to other objects cause those objects to be read from the stream
    as necessary.  Graphs of objects are restored correctly using a reference
    sharing mechanism.  New objects are always allocated when deserializing,
    which prevents existing objects from being overwritten.
    
    Reading an object is analogous to running the constructors of a new
    object.  Memory is allocated for the object and initialized to zero (NULL).
    No-arg constructors are invoked for the non-serializable classes and then
    the fields of the serializable classes are restored from the stream starting
    with the serializable class closest to java.lang.object and finishing with
    the object's most specific class.
    
    For example to read from a stream as written by the example in
    ObjectOutputStream:
    
    ```
         FileInputStream fis = new FileInputStream("t.tmp");
         ObjectInputStream ois = new ObjectInputStream(fis);
    
         int i = ois.readInt();
         String today = (String) ois.readObject();
         Date date = (Date) ois.readObject();
    
         ois.close();
    ```
    
    Classes control how they are serialized by implementing either the
    java.io.Serializable or java.io.Externalizable interfaces.
    
    Implementing the Serializable interface allows object serialization to
    save and restore the entire state of the object and it allows classes to
    evolve between the time the stream is written and the time it is read.  It
    automatically traverses references between objects, saving and restoring
    entire graphs.
    
    Serializable classes that require special handling during the
    serialization and deserialization process should implement the following
    methods:
    
    ```
    private void writeObject(java.io.ObjectOutputStream stream)
        throws IOException;
    private void readObject(java.io.ObjectInputStream stream)
        throws IOException, ClassNotFoundException;
    private void readObjectNoData()
        throws ObjectStreamException;
    ```
    
    The readObject method is responsible for reading and restoring the state
    of the object for its particular class using data written to the stream by
    the corresponding writeObject method.  The method does not need to concern
    itself with the state belonging to its superclasses or subclasses.  State is
    restored by reading data from the ObjectInputStream for the individual
    fields and making assignments to the appropriate fields of the object.
    Reading primitive data types is supported by DataInput.
    
    Any attempt to read object data which exceeds the boundaries of the
    custom data written by the corresponding writeObject method will cause an
    OptionalDataException to be thrown with an eof field value of True.
    Non-object reads which exceed the end of the allotted data will reflect the
    end of data in the same way that they would indicate the end of the stream:
    bytewise reads will return -1 as the byte read or number of bytes read, and
    primitive reads will throw EOFExceptions.  If there is no corresponding
    writeObject method, then the end of default serialized data marks the end of
    the allotted data.
    
    Primitive and object read calls issued from within a readExternal method
    behave in the same manner--if the stream is already positioned at the end of
    data written by the corresponding writeExternal method, object reads will
    throw OptionalDataExceptions with eof set to True, bytewise reads will
    return -1, and primitive reads will throw EOFExceptions.  Note that this
    behavior does not hold for streams written with the old
    `ObjectStreamConstants.PROTOCOL_VERSION_1` protocol, in which the
    end of data written by writeExternal methods is not demarcated, and hence
    cannot be detected.
    
    The readObjectNoData method is responsible for initializing the state of
    the object for its particular class in the event that the serialization
    stream does not list the given class as a superclass of the object being
    deserialized.  This may occur in cases where the receiving party uses a
    different version of the deserialized instance's class than the sending
    party, and the receiver's version extends classes that are not extended by
    the sender's version.  This may also occur if the serialization stream has
    been tampered; hence, readObjectNoData is useful for initializing
    deserialized objects properly despite a "hostile" or incomplete source
    stream.
    
    Serialization does not read or assign values to the fields of any object
    that does not implement the java.io.Serializable interface.  Subclasses of
    Objects that are not serializable can be serializable. In this case the
    non-serializable class must have a no-arg constructor to allow its fields to
    be initialized.  In this case it is the responsibility of the subclass to
    save and restore the state of the non-serializable class. It is frequently
    the case that the fields of that class are accessible (public, package, or
    protected) or that there are get and set methods that can be used to restore
    the state.
    
    Any exception that occurs while deserializing an object will be caught by
    the ObjectInputStream and abort the reading process.
    
    Implementing the Externalizable interface allows the object to assume
    complete control over the contents and format of the object's serialized
    form.  The methods of the Externalizable interface, writeExternal and
    readExternal, are called to save and restore the objects state.  When
    implemented by a class they can write and read their own state using all of
    the methods of ObjectOutput and ObjectInput.  It is the responsibility of
    the objects to handle any versioning that occurs.
    
    Enum constants are deserialized differently than ordinary serializable or
    externalizable objects.  The serialized form of an enum constant consists
    solely of its name; field values of the constant are not transmitted.  To
    deserialize an enum constant, ObjectInputStream reads the constant name from
    the stream; the deserialized constant is then obtained by calling the static
    method `Enum.valueOf(Class, String)` with the enum constant's
    base type and the received constant name as arguments.  Like other
    serializable or externalizable objects, enum constants can function as the
    targets of back references appearing subsequently in the serialization
    stream.  The process by which enum constants are deserialized cannot be
    customized: any class-specific readObject, readObjectNoData, and readResolve
    methods defined by enum types are ignored during deserialization.
    Similarly, any serialPersistentFields or serialVersionUID field declarations
    are also ignored--all enum types have a fixed serialVersionUID of 0L.
    
    <a id="record-serialization"></a>
    Records are serialized differently than ordinary serializable or externalizable
    objects. During deserialization the record's canonical constructor is invoked
    to construct the record object. Certain serialization-related methods, such
    as readObject and writeObject, are ignored for serializable records. See
    <a href="/../specs/serialization/serial-arch.html#serialization-of-records">
    <cite>Java Object Serialization Specification,</cite> Section 1.13,
    "Serialization of Records"</a> for additional information.

    Author(s)
    - Roger Riggs

    See
    - <a href="/../specs/serialization/input.html">
         <cite>Java Object Serialization Specification,</cite> Section 3, "Object Input Classes"</a>

    Since
    - 1.1
    """

    def __init__(self, in: "InputStream"):
        """
        Creates an ObjectInputStream that reads from the specified InputStream.
        A serialization stream header is read from the stream and verified.
        This constructor will block until the corresponding ObjectOutputStream
        has written and flushed the header.
        
        The constructor initializes the deserialization filter to the filter returned
        by invoking the Config.getSerialFilterFactory() with `null` for the current filter
        and the Config.getSerialFilter() static JVM-wide filter for the requested filter.
        
        If a security manager is installed, this constructor will check for
        the "enableSubclassImplementation" SerializablePermission when invoked
        directly or indirectly by the constructor of a subclass which overrides
        the ObjectInputStream.readFields or ObjectInputStream.readUnshared
        methods.

        Arguments
        - in: input stream to read from

        Raises
        - StreamCorruptedException: if the stream header is incorrect
        - IOException: if an I/O error occurs while reading stream header
        - SecurityException: if untrusted subclass illegally overrides
                 security-sensitive methods
        - NullPointerException: if `in` is `null`

        See
        - ObjectOutputStream.ObjectOutputStream(OutputStream)
        """
        ...


    def readObject(self) -> "Object":
        """
        Read an object from the ObjectInputStream.  The class of the object, the
        signature of the class, and the values of the non-transient and
        non-static fields of the class and all of its supertypes are read.
        Default deserializing for a class can be overridden using the writeObject
        and readObject methods.  Objects referenced by this object are read
        transitively so that a complete equivalent graph of objects is
        reconstructed by readObject.
        
        The root object is completely restored when all of its fields and the
        objects it references are completely restored.  At this point the object
        validation callbacks are executed in order based on their registered
        priorities. The callbacks are registered by objects (in the readObject
        special methods) as they are individually restored.
        
        The deserialization filter, when not `null`, is invoked for
        each object (regular or class) read to reconstruct the root object.
        See .setObjectInputFilter(ObjectInputFilter) setObjectInputFilter for details.
        
        Exceptions are thrown for problems with the InputStream and for
        classes that should not be deserialized.  All exceptions are fatal to
        the InputStream and leave it in an indeterminate state; it is up to the
        caller to ignore or recover the stream state.

        Raises
        - ClassNotFoundException: Class of a serialized object cannot be
                 found.
        - InvalidClassException: Something is wrong with a class used by
                 deserialization.
        - StreamCorruptedException: Control information in the
                 stream is inconsistent.
        - OptionalDataException: Primitive data was found in the
                 stream instead of objects.
        - IOException: Any of the usual Input/Output related exceptions.
        """
        ...


    def readUnshared(self) -> "Object":
        """
        Reads an "unshared" object from the ObjectInputStream.  This method is
        identical to readObject, except that it prevents subsequent calls to
        readObject and readUnshared from returning additional references to the
        deserialized instance obtained via this call.  Specifically:
        
          - If readUnshared is called to deserialize a back-reference (the
              stream representation of an object which has been written
              previously to the stream), an ObjectStreamException will be
              thrown.
        
          - If readUnshared returns successfully, then any subsequent attempts
              to deserialize back-references to the stream handle deserialized
              by readUnshared will cause an ObjectStreamException to be thrown.
        
        Deserializing an object via readUnshared invalidates the stream handle
        associated with the returned object.  Note that this in itself does not
        always guarantee that the reference returned by readUnshared is unique;
        the deserialized object may define a readResolve method which returns an
        object visible to other parties, or readUnshared may return a Class
        object or enum constant obtainable elsewhere in the stream or through
        external means. If the deserialized object defines a readResolve method
        and the invocation of that method returns an array, then readUnshared
        returns a shallow clone of that array; this guarantees that the returned
        array object is unique and cannot be obtained a second time from an
        invocation of readObject or readUnshared on the ObjectInputStream,
        even if the underlying data stream has been manipulated.
        
        The deserialization filter, when not `null`, is invoked for
        each object (regular or class) read to reconstruct the root object.
        See .setObjectInputFilter(ObjectInputFilter) setObjectInputFilter for details.
        
        ObjectInputStream subclasses which override this method can only be
        constructed in security contexts possessing the
        "enableSubclassImplementation" SerializablePermission; any attempt to
        instantiate such a subclass without this permission will cause a
        SecurityException to be thrown.

        Returns
        - reference to deserialized object

        Raises
        - ClassNotFoundException: if class of an object to deserialize
                 cannot be found
        - StreamCorruptedException: if control information in the stream
                 is inconsistent
        - ObjectStreamException: if object to deserialize has already
                 appeared in stream
        - OptionalDataException: if primitive data is next in stream
        - IOException: if an I/O error occurs during deserialization

        Since
        - 1.4
        """
        ...


    def defaultReadObject(self) -> None:
        """
        Read the non-static and non-transient fields of the current class from
        this stream.  This may only be called from the readObject method of the
        class being deserialized. It will throw the NotActiveException if it is
        called otherwise.

        Raises
        - ClassNotFoundException: if the class of a serialized object
                 could not be found.
        - IOException: if an I/O error occurs.
        - NotActiveException: if the stream is not currently reading
                 objects.
        """
        ...


    def readFields(self) -> "ObjectInputStream.GetField":
        """
        Reads the persistent fields from the stream and makes them available by
        name.

        Returns
        - the `GetField` object representing the persistent
                 fields of the object being deserialized

        Raises
        - ClassNotFoundException: if the class of a serialized object
                 could not be found.
        - IOException: if an I/O error occurs.
        - NotActiveException: if the stream is not currently reading
                 objects.

        Since
        - 1.2
        """
        ...


    def registerValidation(self, obj: "ObjectInputValidation", prio: int) -> None:
        """
        Register an object to be validated before the graph is returned.  While
        similar to resolveObject these validations are called after the entire
        graph has been reconstituted.  Typically, a readObject method will
        register the object with the stream so that when all of the objects are
        restored a final set of validations can be performed.

        Arguments
        - obj: the object to receive the validation callback.
        - prio: controls the order of callbacks;zero is a good default.
                 Use higher numbers to be called back earlier, lower numbers for
                 later callbacks. Within a priority, callbacks are processed in
                 no particular order.

        Raises
        - NotActiveException: The stream is not currently reading objects
                 so it is invalid to register a callback.
        - InvalidObjectException: The validation object is null.
        """
        ...


    def read(self) -> int:
        """
        Reads a byte of data. This method will block if no input is available.

        Returns
        - the byte read, or -1 if the end of the stream is reached.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def read(self, buf: list[int], off: int, len: int) -> int:
        """
        Reads into an array of bytes.  This method will block until some input
        is available. Consider using java.io.DataInputStream.readFully to read
        exactly 'length' bytes.

        Arguments
        - buf: the buffer into which the data is read
        - off: the start offset in the destination array `buf`
        - len: the maximum number of bytes read

        Returns
        - the actual number of bytes read, -1 is returned when the end of
                 the stream is reached.

        Raises
        - NullPointerException: if `buf` is `null`.
        - IndexOutOfBoundsException: if `off` is negative,
                 `len` is negative, or `len` is greater than
                 `buf.length - off`.
        - IOException: If an I/O error has occurred.

        See
        - java.io.DataInputStream.readFully(byte[],int,int)
        """
        ...


    def available(self) -> int:
        """
        Returns the number of bytes that can be read without blocking.

        Returns
        - the number of available bytes.

        Raises
        - IOException: if there are I/O errors while reading from the
                 underlying `InputStream`
        """
        ...


    def close(self) -> None:
        """
        Closes the input stream. Must be called to release any resources
        associated with the stream.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def readBoolean(self) -> bool:
        """
        Reads in a boolean.

        Returns
        - the boolean read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readByte(self) -> int:
        """
        Reads an 8 bit byte.

        Returns
        - the 8 bit byte read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readUnsignedByte(self) -> int:
        """
        Reads an unsigned 8 bit byte.

        Returns
        - the 8 bit byte read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readChar(self) -> str:
        """
        Reads a 16 bit char.

        Returns
        - the 16 bit char read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readShort(self) -> int:
        """
        Reads a 16 bit short.

        Returns
        - the 16 bit short read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readUnsignedShort(self) -> int:
        """
        Reads an unsigned 16 bit short.

        Returns
        - the 16 bit short read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readInt(self) -> int:
        """
        Reads a 32 bit int.

        Returns
        - the 32 bit integer read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readLong(self) -> int:
        """
        Reads a 64 bit long.

        Returns
        - the read 64 bit long.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readFloat(self) -> float:
        """
        Reads a 32 bit float.

        Returns
        - the 32 bit float read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readDouble(self) -> float:
        """
        Reads a 64 bit double.

        Returns
        - the 64 bit double read.

        Raises
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readFully(self, buf: list[int]) -> None:
        """
        Reads bytes, blocking until all bytes are read.

        Arguments
        - buf: the buffer into which the data is read

        Raises
        - NullPointerException: If `buf` is `null`.
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def readFully(self, buf: list[int], off: int, len: int) -> None:
        """
        Reads bytes, blocking until all bytes are read.

        Arguments
        - buf: the buffer into which the data is read
        - off: the start offset into the data array `buf`
        - len: the maximum number of bytes to read

        Raises
        - NullPointerException: If `buf` is `null`.
        - IndexOutOfBoundsException: If `off` is negative,
                 `len` is negative, or `len` is greater than
                 `buf.length - off`.
        - EOFException: If end of file is reached.
        - IOException: If other I/O error has occurred.
        """
        ...


    def skipBytes(self, len: int) -> int:
        """
        Skips bytes.

        Arguments
        - len: the number of bytes to be skipped

        Returns
        - the actual number of bytes skipped.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def readLine(self) -> str:
        """
        Reads in a line that has been terminated by a \n, \r, \r\n or EOF.

        Returns
        - a String copy of the line.

        Raises
        - IOException: if there are I/O errors while reading from the
                 underlying `InputStream`

        Deprecated
        - This method does not properly convert bytes to characters.
                 see DataInputStream for the details and alternatives.
        """
        ...


    def readUTF(self) -> str:
        """
        Reads a String in
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        format.

        Returns
        - the String.

        Raises
        - IOException: if there are I/O errors while reading from the
                 underlying `InputStream`
        - UTFDataFormatException: if read bytes do not represent a valid
                 modified UTF-8 encoding of a string
        """
        ...


    def getObjectInputFilter(self) -> "ObjectInputFilter":
        """
        Returns the deserialization filter for this stream.
        The filter is the result of invoking the
        Config.getSerialFilterFactory() JVM-wide filter factory
        either by the .ObjectInputStream() constructor or the most recent invocation of
        .setObjectInputFilter setObjectInputFilter.

        Returns
        - the deserialization filter for the stream; may be null

        Since
        - 9
        """
        ...


    def setObjectInputFilter(self, filter: "ObjectInputFilter") -> None:
        """
        Set the deserialization filter for the stream.
        
        The deserialization filter is set to the filter returned by invoking the
        Config.getSerialFilterFactory() JVM-wide filter factory
        with the .getObjectInputFilter() current filter and the `filter` parameter.
        The current filter was set in the
        .ObjectInputStream() ObjectInputStream constructors by invoking the
        Config.getSerialFilterFactory() JVM-wide filter factory and may be `null`.
        .setObjectInputFilter(ObjectInputFilter) This method} can be called
        once and only once before reading any objects from the stream;
        for example, by calling .readObject or .readUnshared.
        
        It is not permitted to replace a `non-null` filter with a `null` filter.
        If the .getObjectInputFilter() current filter is `non-null`,
        the value returned from the filter factory must be `non-null`.
        
        The filter's ObjectInputFilter.checkInput checkInput method is called
        for each class and reference in the stream.
        The filter can check any or all of the class, the array length, the number
        of references, the depth of the graph, and the size of the input stream.
        The depth is the number of nested .readObject readObject
        calls starting with the reading of the root of the graph being deserialized
        and the current object being deserialized.
        The number of references is the cumulative number of objects and references
        to objects already read from the stream including the current object being read.
        The filter is invoked only when reading objects from the stream and not for
        primitives.
        
        If the filter returns ObjectInputFilter.Status.REJECTED Status.REJECTED,
        `null` or throws a RuntimeException,
        the active `readObject` or `readUnshared`
        throws InvalidClassException, otherwise deserialization
        continues uninterrupted.

        Arguments
        - filter: the filter, may be null

        Raises
        - SecurityException: if there is security manager and the
              `SerializablePermission("serialFilter")` is not granted
        - IllegalStateException: if an object has been read,
              if the filter factory returns `null` when the
              .getObjectInputFilter() current filter is non-null, or
              if the filter has already been set.

        Since
        - 9

        Unknown Tags
        - The filter, when not `null`, is invoked during .readObject readObject
        and .readUnshared readUnshared for each object (regular or class) in the stream.
        Strings are treated as primitives and do not invoke the filter.
        The filter is called for:
        
            - each object reference previously deserialized from the stream
            (class is `null`, arrayLength is -1),
            - each regular class (class is not `null`, arrayLength is -1),
            - each interface class explicitly referenced in the stream
                (it is not called for interfaces implemented by classes in the stream),
            - each interface of a dynamic proxy and the dynamic proxy class itself
            (class is not `null`, arrayLength is -1),
            - each array is filtered using the array type and length of the array
            (class is the array type, arrayLength is the requested length),
            - each object replaced by its class' `readResolve` method
                is filtered using the replacement object's class, if not `null`,
                and if it is an array, the arrayLength, otherwise -1,
            - and each object replaced by .resolveObject resolveObject
                is filtered using the replacement object's class, if not `null`,
                and if it is an array, the arrayLength, otherwise -1.
        
        
        When the ObjectInputFilter.checkInput checkInput method is invoked
        it is given access to the current class, the array length,
        the current number of references already read from the stream,
        the depth of nested calls to .readObject readObject or
        .readUnshared readUnshared,
        and the implementation dependent number of bytes consumed from the input stream.
        
        Each call to .readObject readObject or
        .readUnshared readUnshared increases the depth by 1
        before reading an object and decreases by 1 before returning
        normally or exceptionally.
        The depth starts at `1` and increases for each nested object and
        decrements when each nested call returns.
        The count of references in the stream starts at `1` and
        is increased before reading an object.
        """
        ...


    class GetField:
        """
        Provide access to the persistent fields read from the input stream.
        """

        def __init__(self):
            """
            Constructor for subclasses to call.
            """
            ...


        def getObjectStreamClass(self) -> "ObjectStreamClass":
            """
            Get the ObjectStreamClass that describes the fields in the stream.

            Returns
            - the descriptor class that describes the serializable fields
            """
            ...


        def defaulted(self, name: str) -> bool:
            """
            Return True if the named field is defaulted and has no value in this
            stream.

            Arguments
            - name: the name of the field

            Returns
            - True, if and only if the named field is defaulted

            Raises
            - IOException: if there are I/O errors while reading from
                    the underlying `InputStream`
            - IllegalArgumentException: if `name` does not
                    correspond to a serializable field
            """
            ...


        def get(self, name: str, val: bool) -> bool:
            """
            Get the value of the named boolean field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `boolean` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: int) -> int:
            """
            Get the value of the named byte field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `byte` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: str) -> str:
            """
            Get the value of the named char field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `char` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: int) -> int:
            """
            Get the value of the named short field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `short` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: int) -> int:
            """
            Get the value of the named int field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `int` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: int) -> int:
            """
            Get the value of the named long field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `long` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: float) -> float:
            """
            Get the value of the named float field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `float` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: float) -> float:
            """
            Get the value of the named double field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `double` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...


        def get(self, name: str, val: "Object") -> "Object":
            """
            Get the value of the named Object field from the persistent field.

            Arguments
            - name: the name of the field
            - val: the default value to use if `name` does not
                    have a value

            Returns
            - the value of the named `Object` field

            Raises
            - IOException: if there are I/O errors while reading from the
                    underlying `InputStream`
            - IllegalArgumentException: if type of `name` is
                    not serializable or if the field type is incorrect
            """
            ...
