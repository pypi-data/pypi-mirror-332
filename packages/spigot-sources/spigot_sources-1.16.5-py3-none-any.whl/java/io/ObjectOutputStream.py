"""
Python module generated from Java source file java.io.ObjectOutputStream

Java source file obtained from artifact jdk version jdk

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import *
from java.io.ObjectStreamClass import WeakClassKey
from java.lang.ref import ReferenceQueue
from java.security import AccessController
from java.security import PrivilegedAction
from java.util import Arrays
from java.util import StringJoiner
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from sun.reflect.misc import ReflectUtil
from typing import Any, Callable, Iterable, Tuple


class ObjectOutputStream(OutputStream, ObjectOutput, ObjectStreamConstants):
    """
    An ObjectOutputStream writes primitive data types and graphs of Java objects
    to an OutputStream.  The objects can be read (reconstituted) using an
    ObjectInputStream.  Persistent storage of objects can be accomplished by
    using a file for the stream.  If the stream is a network socket stream, the
    objects can be reconstituted on another host or in another process.
    
    Only objects that support the java.io.Serializable interface can be
    written to streams.  The class of each serializable object is encoded
    including the class name and signature of the class, the values of the
    object's fields and arrays, and the closure of any other objects referenced
    from the initial objects.
    
    The method writeObject is used to write an object to the stream.  Any
    object, including Strings and arrays, is written with writeObject. Multiple
    objects or primitives can be written to the stream.  The objects must be
    read back from the corresponding ObjectInputstream with the same types and
    in the same order as they were written.
    
    Primitive data types can also be written to the stream using the
    appropriate methods from DataOutput. Strings can also be written using the
    writeUTF method.
    
    The default serialization mechanism for an object writes the class of the
    object, the class signature, and the values of all non-transient and
    non-static fields.  References to other objects (except in transient or
    static fields) cause those objects to be written also. Multiple references
    to a single object are encoded using a reference sharing mechanism so that
    graphs of objects can be restored to the same shape as when the original was
    written.
    
    For example to write an object that can be read by the example in
    ObjectInputStream:
    
    ```
         FileOutputStream fos = new FileOutputStream("t.tmp");
         ObjectOutputStream oos = new ObjectOutputStream(fos);
    
         oos.writeInt(12345);
         oos.writeObject("Today");
         oos.writeObject(new Date());
    
         oos.close();
    ```
    
    Classes that require special handling during the serialization and
    deserialization process must implement special methods with these exact
    signatures:
    
    ```
    private void readObject(java.io.ObjectInputStream stream)
        throws IOException, ClassNotFoundException;
    private void writeObject(java.io.ObjectOutputStream stream)
        throws IOException
    private void readObjectNoData()
        throws ObjectStreamException;
    ```
    
    The writeObject method is responsible for writing the state of the object
    for its particular class so that the corresponding readObject method can
    restore it.  The method does not need to concern itself with the state
    belonging to the object's superclasses or subclasses.  State is saved by
    writing the individual fields to the ObjectOutputStream using the
    writeObject method or by using the methods for primitive data types
    supported by DataOutput.
    
    Serialization does not write out the fields of any object that does not
    implement the java.io.Serializable interface.  Subclasses of Objects that
    are not serializable can be serializable. In this case the non-serializable
    class must have a no-arg constructor to allow its fields to be initialized.
    In this case it is the responsibility of the subclass to save and restore
    the state of the non-serializable class. It is frequently the case that the
    fields of that class are accessible (public, package, or protected) or that
    there are get and set methods that can be used to restore the state.
    
    Serialization of an object can be prevented by implementing writeObject
    and readObject methods that throw the NotSerializableException.  The
    exception will be caught by the ObjectOutputStream and abort the
    serialization process.
    
    Implementing the Externalizable interface allows the object to assume
    complete control over the contents and format of the object's serialized
    form.  The methods of the Externalizable interface, writeExternal and
    readExternal, are called to save and restore the objects state.  When
    implemented by a class they can write and read their own state using all of
    the methods of ObjectOutput and ObjectInput.  It is the responsibility of
    the objects to handle any versioning that occurs.
    
    Enum constants are serialized differently than ordinary serializable or
    externalizable objects.  The serialized form of an enum constant consists
    solely of its name; field values of the constant are not transmitted.  To
    serialize an enum constant, ObjectOutputStream writes the string returned by
    the constant's name method.  Like other serializable or externalizable
    objects, enum constants can function as the targets of back references
    appearing subsequently in the serialization stream.  The process by which
    enum constants are serialized cannot be customized; any class-specific
    writeObject and writeReplace methods defined by enum types are ignored
    during serialization.  Similarly, any serialPersistentFields or
    serialVersionUID field declarations are also ignored--all enum types have a
    fixed serialVersionUID of 0L.
    
    Primitive data, excluding serializable fields and externalizable data, is
    written to the ObjectOutputStream in block-data records. A block data record
    is composed of a header and data. The block data header consists of a marker
    and the number of bytes to follow the header.  Consecutive primitive data
    writes are merged into one block-data record.  The blocking factor used for
    a block-data record will be 1024 bytes.  Each block-data record will be
    filled up to 1024 bytes, or be written whenever there is a termination of
    block-data mode.  Calls to the ObjectOutputStream methods writeObject,
    defaultWriteObject and writeFields initially terminate any existing
    block-data record.
    
    Records are serialized differently than ordinary serializable or externalizable
    objects, see <a href="ObjectInputStream.html#record-serialization">record serialization</a>.

    Author(s)
    - Roger Riggs

    See
    - <a href="/../specs/serialization/output.html">
         <cite>Java Object Serialization Specification,</cite> Section 2, "Object Output Classes"</a>

    Since
    - 1.1
    """

    def __init__(self, out: "OutputStream"):
        """
        Creates an ObjectOutputStream that writes to the specified OutputStream.
        This constructor writes the serialization stream header to the
        underlying stream; callers may wish to flush the stream immediately to
        ensure that constructors for receiving ObjectInputStreams will not block
        when reading the header.
        
        If a security manager is installed, this constructor will check for
        the "enableSubclassImplementation" SerializablePermission when invoked
        directly or indirectly by the constructor of a subclass which overrides
        the ObjectOutputStream.putFields or ObjectOutputStream.writeUnshared
        methods.

        Arguments
        - out: output stream to write to

        Raises
        - IOException: if an I/O error occurs while writing stream header
        - SecurityException: if untrusted subclass illegally overrides
                 security-sensitive methods
        - NullPointerException: if `out` is `null`

        See
        - ObjectInputStream.ObjectInputStream(InputStream)

        Since
        - 1.4
        """
        ...


    def useProtocolVersion(self, version: int) -> None:
        """
        Specify stream protocol version to use when writing the stream.
        
        This routine provides a hook to enable the current version of
        Serialization to write in a format that is backwards compatible to a
        previous version of the stream format.
        
        Every effort will be made to avoid introducing additional
        backwards incompatibilities; however, sometimes there is no
        other alternative.

        Arguments
        - version: use ProtocolVersion from java.io.ObjectStreamConstants.

        Raises
        - IllegalStateException: if called after any objects
                 have been serialized.
        - IllegalArgumentException: if invalid version is passed in.
        - IOException: if I/O errors occur

        See
        - java.io.ObjectStreamConstants.PROTOCOL_VERSION_2

        Since
        - 1.2
        """
        ...


    def writeObject(self, obj: "Object") -> None:
        """
        Write the specified object to the ObjectOutputStream.  The class of the
        object, the signature of the class, and the values of the non-transient
        and non-static fields of the class and all of its supertypes are
        written.  Default serialization for a class can be overridden using the
        writeObject and the readObject methods.  Objects referenced by this
        object are written transitively so that a complete equivalent graph of
        objects can be reconstructed by an ObjectInputStream.
        
        Exceptions are thrown for problems with the OutputStream and for
        classes that should not be serialized.  All exceptions are fatal to the
        OutputStream, which is left in an indeterminate state, and it is up to
        the caller to ignore or recover the stream state.

        Raises
        - InvalidClassException: Something is wrong with a class used by
                 serialization.
        - NotSerializableException: Some object to be serialized does not
                 implement the java.io.Serializable interface.
        - IOException: Any exception thrown by the underlying
                 OutputStream.
        """
        ...


    def writeUnshared(self, obj: "Object") -> None:
        """
        Writes an "unshared" object to the ObjectOutputStream.  This method is
        identical to writeObject, except that it always writes the given object
        as a new, unique object in the stream (as opposed to a back-reference
        pointing to a previously serialized instance).  Specifically:
        
          - An object written via writeUnshared is always serialized in the
              same manner as a newly appearing object (an object that has not
              been written to the stream yet), regardless of whether or not the
              object has been written previously.
        
          - If writeObject is used to write an object that has been previously
              written with writeUnshared, the previous writeUnshared operation
              is treated as if it were a write of a separate object.  In other
              words, ObjectOutputStream will never generate back-references to
              object data written by calls to writeUnshared.
        
        While writing an object via writeUnshared does not in itself guarantee a
        unique reference to the object when it is deserialized, it allows a
        single object to be defined multiple times in a stream, so that multiple
        calls to readUnshared by the receiver will not conflict.  Note that the
        rules described above only apply to the base-level object written with
        writeUnshared, and not to any transitively referenced sub-objects in the
        object graph to be serialized.
        
        ObjectOutputStream subclasses which override this method can only be
        constructed in security contexts possessing the
        "enableSubclassImplementation" SerializablePermission; any attempt to
        instantiate such a subclass without this permission will cause a
        SecurityException to be thrown.

        Arguments
        - obj: object to write to stream

        Raises
        - NotSerializableException: if an object in the graph to be
                 serialized does not implement the Serializable interface
        - InvalidClassException: if a problem exists with the class of an
                 object to be serialized
        - IOException: if an I/O error occurs during serialization

        Since
        - 1.4
        """
        ...


    def defaultWriteObject(self) -> None:
        """
        Write the non-static and non-transient fields of the current class to
        this stream.  This may only be called from the writeObject method of the
        class being serialized. It will throw the NotActiveException if it is
        called otherwise.

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 `OutputStream`
        """
        ...


    def putFields(self) -> "ObjectOutputStream.PutField":
        """
        Retrieve the object used to buffer persistent fields to be written to
        the stream.  The fields will be written to the stream when writeFields
        method is called.

        Returns
        - an instance of the class Putfield that holds the serializable
                 fields

        Raises
        - IOException: if I/O errors occur

        Since
        - 1.2
        """
        ...


    def writeFields(self) -> None:
        """
        Write the buffered fields to the stream.

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        - NotActiveException: Called when a classes writeObject method was
                 not called to write the state of the object.

        Since
        - 1.2
        """
        ...


    def reset(self) -> None:
        """
        Reset will disregard the state of any objects already written to the
        stream.  The state is reset to be the same as a new ObjectOutputStream.
        The current point in the stream is marked as reset so the corresponding
        ObjectInputStream will be reset at the same point.  Objects previously
        written to the stream will not be referred to as already being in the
        stream.  They will be written to the stream again.

        Raises
        - IOException: if reset() is invoked while serializing an object.
        """
        ...


    def write(self, val: int) -> None:
        """
        Writes a byte. This method will block until the byte is actually
        written.

        Arguments
        - val: the byte to be written to the stream

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def write(self, buf: list[int]) -> None:
        """
        Writes an array of bytes. This method will block until the bytes are
        actually written.

        Arguments
        - buf: the data to be written

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def write(self, buf: list[int], off: int, len: int) -> None:
        """
        Writes a sub array of bytes.

        Arguments
        - buf: the data to be written
        - off: the start offset in the data
        - len: the number of bytes that are written

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def flush(self) -> None:
        """
        Flushes the stream. This will write any buffered output bytes and flush
        through to the underlying stream.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def close(self) -> None:
        """
        Closes the stream. This method must be called to release any resources
        associated with the stream.

        Raises
        - IOException: If an I/O error has occurred.
        """
        ...


    def writeBoolean(self, val: bool) -> None:
        """
        Writes a boolean.

        Arguments
        - val: the boolean to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeByte(self, val: int) -> None:
        """
        Writes an 8 bit byte.

        Arguments
        - val: the byte value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeShort(self, val: int) -> None:
        """
        Writes a 16 bit short.

        Arguments
        - val: the short value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeChar(self, val: int) -> None:
        """
        Writes a 16 bit char.

        Arguments
        - val: the char value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeInt(self, val: int) -> None:
        """
        Writes a 32 bit int.

        Arguments
        - val: the integer value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeLong(self, val: int) -> None:
        """
        Writes a 64 bit long.

        Arguments
        - val: the long value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeFloat(self, val: float) -> None:
        """
        Writes a 32 bit float.

        Arguments
        - val: the float value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeDouble(self, val: float) -> None:
        """
        Writes a 64 bit double.

        Arguments
        - val: the double value to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeBytes(self, str: str) -> None:
        """
        Writes a String as a sequence of bytes.

        Arguments
        - str: the String of bytes to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeChars(self, str: str) -> None:
        """
        Writes a String as a sequence of chars.

        Arguments
        - str: the String of chars to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    def writeUTF(self, str: str) -> None:
        """
        Primitive data write of this String in
        <a href="DataInput.html#modified-utf-8">modified UTF-8</a>
        format.  Note that there is a
        significant difference between writing a String into the stream as
        primitive data or as an Object. A String instance written by writeObject
        is written into the stream as a String initially. Future writeObject()
        calls write references to the string into the stream.

        Arguments
        - str: the String to be written

        Raises
        - IOException: if I/O errors occur while writing to the underlying
                 stream
        """
        ...


    class PutField:
        """
        Provide programmatic access to the persistent fields to be written
        to ObjectOutput.

        Since
        - 1.2
        """

        def __init__(self):
            """
            Constructor for subclasses to call.
            """
            ...


        def put(self, name: str, val: bool) -> None:
            """
            Put the value of the named boolean field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `boolean`
            """
            ...


        def put(self, name: str, val: int) -> None:
            """
            Put the value of the named byte field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `byte`
            """
            ...


        def put(self, name: str, val: str) -> None:
            """
            Put the value of the named char field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `char`
            """
            ...


        def put(self, name: str, val: int) -> None:
            """
            Put the value of the named short field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `short`
            """
            ...


        def put(self, name: str, val: int) -> None:
            """
            Put the value of the named int field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `int`
            """
            ...


        def put(self, name: str, val: int) -> None:
            """
            Put the value of the named long field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `long`
            """
            ...


        def put(self, name: str, val: float) -> None:
            """
            Put the value of the named float field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `float`
            """
            ...


        def put(self, name: str, val: float) -> None:
            """
            Put the value of the named double field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not
            `double`
            """
            ...


        def put(self, name: str, val: "Object") -> None:
            """
            Put the value of the named Object field into the persistent field.

            Arguments
            - name: the name of the serializable field
            - val: the value to assign to the field
                    (which may be `null`)

            Raises
            - IllegalArgumentException: if `name` does not
            match the name of a serializable field for the class whose fields
            are being written, or if the type of the named field is not a
            reference type
            """
            ...


        def write(self, out: "ObjectOutput") -> None:
            """
            Write the data and fields to the specified ObjectOutput stream,
            which must be the same stream that produced this
            `PutField` object.

            Arguments
            - out: the stream to write the data and fields to

            Raises
            - IOException: if I/O errors occur while writing to the
                    underlying stream
            - IllegalArgumentException: if the specified stream is not
                    the same stream that produced this `PutField`
                    object

            Deprecated
            - This method does not write the values contained by this
                    `PutField` object in a proper format, and may
                    result in corruption of the serialization stream.  The
                    correct way to write `PutField` data is by
                    calling the java.io.ObjectOutputStream.writeFields()
                    method.
            """
            ...
