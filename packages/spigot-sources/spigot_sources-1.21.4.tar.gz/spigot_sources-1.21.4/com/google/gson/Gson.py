"""
Python module generated from Java source file com.google.gson.Gson

Java source file obtained from artifact gson version 2.11.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.annotations import JsonAdapter
from com.google.gson.internal import ConstructorConstructor
from com.google.gson.internal import Excluder
from com.google.gson.internal import GsonBuildConfig
from com.google.gson.internal import LazilyParsedNumber
from com.google.gson.internal import Primitives
from com.google.gson.internal import Streams
from com.google.gson.internal.bind import ArrayTypeAdapter
from com.google.gson.internal.bind import CollectionTypeAdapterFactory
from com.google.gson.internal.bind import DefaultDateTypeAdapter
from com.google.gson.internal.bind import JsonAdapterAnnotationTypeAdapterFactory
from com.google.gson.internal.bind import JsonTreeReader
from com.google.gson.internal.bind import JsonTreeWriter
from com.google.gson.internal.bind import MapTypeAdapterFactory
from com.google.gson.internal.bind import NumberTypeAdapter
from com.google.gson.internal.bind import ObjectTypeAdapter
from com.google.gson.internal.bind import ReflectiveTypeAdapterFactory
from com.google.gson.internal.bind import SerializationDelegatingTypeAdapter
from com.google.gson.internal.bind import TypeAdapters
from com.google.gson.internal.sql import SqlTypesSupport
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from com.google.gson.stream import MalformedJsonException
from java.io import EOFException
from java.io import IOException
from java.io import Reader
from java.io import StringReader
from java.io import StringWriter
from java.io import Writer
from java.lang.reflect import Type
from java.math import BigDecimal
from java.math import BigInteger
from java.text import DateFormat
from java.util import Collections
from java.util import Objects
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.concurrent.atomic import AtomicLong
from java.util.concurrent.atomic import AtomicLongArray
from typing import Any, Callable, Iterable, Tuple


class Gson:
    """
    This is the main class for using Gson. Gson is typically used by first constructing a Gson
    instance and then invoking .toJson(Object) or .fromJson(String, Class) methods on
    it. Gson instances are Thread-safe so you can reuse them freely across multiple threads.
    
    You can create a Gson instance by invoking `new Gson()` if the default configuration is
    all you need. You can also use GsonBuilder to build a Gson instance with various
    configuration options such as versioning support, pretty printing, custom newline, custom indent,
    custom JsonSerializers, JsonDeserializers, and InstanceCreators.
    
    Here is an example of how Gson is used for a simple Class:
    
    ```
    Gson gson = new Gson(); // Or use new GsonBuilder().create();
    MyType target = new MyType();
    String json = gson.toJson(target); // serializes target to JSON
    MyType target2 = gson.fromJson(json, MyType.class); // deserializes json into target2
    ```
    
    If the type of the object that you are converting is a `ParameterizedType` (i.e. has at
    least one type argument, for example `List<MyType>`) then for deserialization you must use
    a `fromJson` method with Type or TypeToken parameter to specify the
    parameterized type. For serialization specifying a `Type` or `TypeToken` is optional,
    otherwise Gson will use the runtime type of the object. TypeToken is a class provided by
    Gson which helps creating parameterized types. Here is an example showing how this can be done:
    
    ```
    TypeToken&lt;List&lt;MyType&gt;&gt; listType = new TypeToken&lt;List&lt;MyType&gt;&gt;() {};
    List&lt;MyType&gt; target = new LinkedList&lt;MyType&gt;();
    target.add(new MyType(1, "abc"));
    
    Gson gson = new Gson();
    // For serialization you normally do not have to specify the type, Gson will use
    // the runtime type of the objects, however you can also specify it explicitly
    String json = gson.toJson(target, listType.getType());
    
    // But for deserialization you have to specify the type
    List&lt;MyType&gt; target2 = gson.fromJson(json, listType);
    ```
    
    See the <a href="https://github.com/google/gson/blob/main/UserGuide.md">Gson User Guide</a>
    for a more complete set of examples.
    
    <h2 id="default-lenient">JSON Strictness handling</h2>
    
    For legacy reasons most of the `Gson` methods allow JSON data which does not comply with
    the JSON specification when no explicit Strictness strictness is set (the default).
    To specify the strictness of a `Gson` instance, you should set it through GsonBuilder.setStrictness(Strictness).
    
    For older Gson versions, which don't have the strictness mode API, the following workarounds
    can be used:
    
    <h3>Serialization</h3>
    
    <ol>
      - Use .getAdapter(Class) to obtain the adapter for the type to be serialized
      - When using an existing `JsonWriter`, manually apply the writer settings of this
          `Gson` instance listed by .newJsonWriter(Writer).
          Otherwise, when not using an existing `JsonWriter`, use .newJsonWriter(Writer) to construct one.
      - Call TypeAdapter.write(JsonWriter, Object)
    </ol>
    
    <h3>Deserialization</h3>
    
    <ol>
      - Use .getAdapter(Class) to obtain the adapter for the type to be deserialized
      - When using an existing `JsonReader`, manually apply the reader settings of this
          `Gson` instance listed by .newJsonReader(Reader).
          Otherwise, when not using an existing `JsonReader`, use .newJsonReader(Reader) to construct one.
      - Call TypeAdapter.read(JsonReader)
      - Call JsonReader.peek() and verify that the result is JsonToken.END_DOCUMENT
          to make sure there is no trailing data
    </ol>
    
    Note that the `JsonReader` created this way is only 'legacy strict', it mostly adheres to
    the JSON specification but allows small deviations. See JsonReader.setStrictness(Strictness) for details.

    Author(s)
    - Jesse Wilson

    See
    - TypeToken
    """

    def __init__(self):
        """
        Constructs a Gson object with default configuration. The default configuration has the
        following settings:
        
        
          - The JSON generated by `toJson` methods is in compact representation. This means
              that all the unneeded white-space is removed. You can change this behavior with GsonBuilder.setPrettyPrinting().
          - When the JSON generated contains more than one line, the kind of newline and indent to
              use can be configured with GsonBuilder.setFormattingStyle(FormattingStyle).
          - The generated JSON omits all the fields that are null. Note that nulls in arrays are kept
              as is since an array is an ordered list. Moreover, if a field is not null, but its
              generated JSON is empty, the field is kept. You can configure Gson to serialize null
              values by setting GsonBuilder.serializeNulls().
          - Gson provides default serialization and deserialization for Enums, Map, java.net.URL, java.net.URI, java.util.Locale, java.util.Date,
              java.math.BigDecimal, and java.math.BigInteger classes. If you would
              prefer to change the default representation, you can do so by registering a type adapter
              through GsonBuilder.registerTypeAdapter(Type, Object).
          - The default Date format is same as java.text.DateFormat.DEFAULT. This format
              ignores the millisecond portion of the date during serialization. You can change this by
              invoking GsonBuilder.setDateFormat(int, int) or GsonBuilder.setDateFormat(String).
          - By default, Gson ignores the com.google.gson.annotations.Expose annotation. You
              can enable Gson to serialize/deserialize only those fields marked with this annotation
              through GsonBuilder.excludeFieldsWithoutExposeAnnotation().
          - By default, Gson ignores the com.google.gson.annotations.Since annotation. You
              can enable Gson to use this annotation through GsonBuilder.setVersion(double).
          - The default field naming policy for the output JSON is same as in Java. So, a Java class
              field `versionNumber` will be output as `"versionNumber"` in JSON. The same
              rules are applied for mapping incoming JSON to the Java classes. You can change this
              policy through GsonBuilder.setFieldNamingPolicy(FieldNamingPolicy).
          - By default, Gson excludes `transient` or `static` fields from consideration
              for serialization and deserialization. You can change this behavior through GsonBuilder.excludeFieldsWithModifiers(int...).
          - No explicit strictness is set. You can change this by calling GsonBuilder.setStrictness(Strictness).
        """
        ...


    def newBuilder(self) -> "GsonBuilder":
        """
        Returns a new GsonBuilder containing all custom factories and configuration used by the current
        instance.

        Returns
        - a GsonBuilder instance.

        Since
        - 2.8.3
        """
        ...


    def excluder(self) -> "Excluder":
        """
        Deprecated
        - This method by accident exposes an internal Gson class; it might be removed in a
            future version.
        """
        ...


    def fieldNamingStrategy(self) -> "FieldNamingStrategy":
        """
        Returns the field naming strategy used by this Gson instance.

        See
        - GsonBuilder.setFieldNamingStrategy(FieldNamingStrategy)
        """
        ...


    def serializeNulls(self) -> bool:
        """
        Returns whether this Gson instance is serializing JSON object properties with `null`
        values, or just omits them.

        See
        - GsonBuilder.serializeNulls()
        """
        ...


    def htmlSafe(self) -> bool:
        """
        Returns whether this Gson instance produces JSON output which is HTML-safe, that means all HTML
        characters are escaped.

        See
        - GsonBuilder.disableHtmlEscaping()
        """
        ...


    def getAdapter(self, type: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        """
        Returns the type adapter for `type`.
        
        When calling this method concurrently from multiple threads and requesting an adapter for
        the same type this method may return different `TypeAdapter` instances. However, that
        should normally not be an issue because `TypeAdapter` implementations are supposed to be
        stateless.

        Raises
        - IllegalArgumentException: if this Gson instance cannot serialize and deserialize `type`.
        """
        ...


    def getAdapter(self, type: type["T"]) -> "TypeAdapter"["T"]:
        """
        Returns the type adapter for `type`.

        Raises
        - IllegalArgumentException: if this Gson instance cannot serialize and deserialize `type`.
        """
        ...


    def getDelegateAdapter(self, skipPast: "TypeAdapterFactory", type: "TypeToken"["T"]) -> "TypeAdapter"["T"]:
        """
        This method is used to get an alternate type adapter for the specified type. This is used to
        access a type adapter that is overridden by a TypeAdapterFactory that you may have
        registered. This feature is typically used when you want to register a type adapter that does a
        little bit of work but then delegates further processing to the Gson default type adapter. Here
        is an example:
        
        Let's say we want to write a type adapter that counts the number of objects being read from
        or written to JSON. We can achieve this by writing a type adapter factory that uses the `getDelegateAdapter` method:
        
        ````class StatsTypeAdapterFactory implements TypeAdapterFactory {
          public int numReads = 0;
          public int numWrites = 0;
          public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
            final TypeAdapter<T> delegate = gson.getDelegateAdapter(this, type);
            return new TypeAdapter<T>() {
              public void write(JsonWriter out, T value) throws IOException {
                ++numWrites;
                delegate.write(out, value);`
              public T read(JsonReader in) throws IOException {
                ++numReads;
                return delegate.read(in);
              }
            };
          }
        }
        }```
        
        This factory can now be used like this:
        
        ````StatsTypeAdapterFactory stats = new StatsTypeAdapterFactory();
        Gson gson = new GsonBuilder().registerTypeAdapterFactory(stats).create();
        // Call gson.toJson() and fromJson methods on objects
        System.out.println("Num JSON reads: " + stats.numReads);
        System.out.println("Num JSON writes: " + stats.numWrites);````
        
        Note that this call will skip all factories registered before `skipPast`. In case of
        multiple TypeAdapterFactories registered it is up to the caller of this function to ensure that
        the order of registration does not prevent this method from reaching a factory they would
        expect to reply from this call. Note that since you can not override the type adapter factories
        for some types, see GsonBuilder.registerTypeAdapter(Type, Object), our stats factory
        will not count the number of instances of those types that will be read or written.
        
        If `skipPast` is a factory which has neither been registered on the GsonBuilder nor specified with the JsonAdapter @JsonAdapter annotation on a class,
        then this method behaves as if .getAdapter(TypeToken) had been called. This also means
        that for fields with `@JsonAdapter` annotation this method behaves normally like `getAdapter` (except for corner cases where a custom InstanceCreator is used to create
        an instance of the factory).

        Arguments
        - skipPast: The type adapter factory that needs to be skipped while searching for a
            matching type adapter. In most cases, you should just pass *this* (the type adapter
            factory from where `getDelegateAdapter` method is being invoked).
        - type: Type for which the delegate adapter is being searched for.

        Since
        - 2.2
        """
        ...


    def toJsonTree(self, src: "Object") -> "JsonElement":
        """
        This method serializes the specified object into its equivalent representation as a tree of
        JsonElements. This method should be used when the specified object is not a generic
        type. This method uses Class.getClass() to get the type for the specified object, but
        the `getClass()` loses the generic type information because of the Type Erasure feature
        of Java. Note that this method works fine if any of the object fields are of generic type, just
        the object itself should not be of a generic type. If the object is of generic type, use .toJsonTree(Object, Type) instead.

        Arguments
        - src: the object for which JSON representation is to be created

        Returns
        - JSON representation of `src`.

        See
        - .toJsonTree(Object, Type)

        Since
        - 1.4
        """
        ...


    def toJsonTree(self, src: "Object", typeOfSrc: "Type") -> "JsonElement":
        """
        This method serializes the specified object, including those of generic types, into its
        equivalent representation as a tree of JsonElements. This method must be used if the
        specified object is a generic type. For non-generic objects, use .toJsonTree(Object)
        instead.

        Arguments
        - src: the object for which JSON representation is to be created
        - typeOfSrc: The specific genericized type of src. You can obtain this type by using the
            com.google.gson.reflect.TypeToken class. For example, to get the type for `Collection<Foo>`, you should use:
            ```
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        ```

        Returns
        - JSON representation of `src`.

        See
        - .toJsonTree(Object)

        Since
        - 1.4
        """
        ...


    def toJson(self, src: "Object") -> str:
        """
        This method serializes the specified object into its equivalent JSON representation. This
        method should be used when the specified object is not a generic type. This method uses Class.getClass() to get the type for the specified object, but the `getClass()` loses
        the generic type information because of the Type Erasure feature of Java. Note that this method
        works fine if any of the object fields are of generic type, just the object itself should not
        be of a generic type. If the object is of generic type, use .toJson(Object, Type)
        instead. If you want to write out the object to a Writer, use .toJson(Object,
        Appendable) instead.

        Arguments
        - src: the object for which JSON representation is to be created

        Returns
        - JSON representation of `src`.

        See
        - .toJson(Object, Type)
        """
        ...


    def toJson(self, src: "Object", typeOfSrc: "Type") -> str:
        """
        This method serializes the specified object, including those of generic types, into its
        equivalent JSON representation. This method must be used if the specified object is a generic
        type. For non-generic objects, use .toJson(Object) instead. If you want to write out
        the object to a Appendable, use .toJson(Object, Type, Appendable) instead.

        Arguments
        - src: the object for which JSON representation is to be created
        - typeOfSrc: The specific genericized type of src. You can obtain this type by using the
            com.google.gson.reflect.TypeToken class. For example, to get the type for `Collection<Foo>`, you should use:
            ```
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        ```

        Returns
        - JSON representation of `src`.

        See
        - .toJson(Object)
        """
        ...


    def toJson(self, src: "Object", writer: "Appendable") -> None:
        """
        This method serializes the specified object into its equivalent JSON representation and writes
        it to the writer. This method should be used when the specified object is not a generic type.
        This method uses Class.getClass() to get the type for the specified object, but the
        `getClass()` loses the generic type information because of the Type Erasure feature of
        Java. Note that this method works fine if any of the object fields are of generic type, just
        the object itself should not be of a generic type. If the object is of generic type, use .toJson(Object, Type, Appendable) instead.

        Arguments
        - src: the object for which JSON representation is to be created
        - writer: Writer to which the JSON representation needs to be written

        Raises
        - JsonIOException: if there was a problem writing to the writer

        See
        - .toJson(Object, Type, Appendable)

        Since
        - 1.2
        """
        ...


    def toJson(self, src: "Object", typeOfSrc: "Type", writer: "Appendable") -> None:
        """
        This method serializes the specified object, including those of generic types, into its
        equivalent JSON representation and writes it to the writer. This method must be used if the
        specified object is a generic type. For non-generic objects, use .toJson(Object,
        Appendable) instead.

        Arguments
        - src: the object for which JSON representation is to be created
        - typeOfSrc: The specific genericized type of src. You can obtain this type by using the
            com.google.gson.reflect.TypeToken class. For example, to get the type for `Collection<Foo>`, you should use:
            ```
        Type typeOfSrc = new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}.getType();
        ```
        - writer: Writer to which the JSON representation of src needs to be written

        Raises
        - JsonIOException: if there was a problem writing to the writer

        See
        - .toJson(Object, Appendable)

        Since
        - 1.2
        """
        ...


    def toJson(self, src: "Object", typeOfSrc: "Type", writer: "JsonWriter") -> None:
        """
        Writes the JSON representation of `src` of type `typeOfSrc` to `writer`.
        
        If the `Gson` instance has an GsonBuilder.setStrictness(Strictness)
        explicit strictness setting, this setting will be used for writing the JSON regardless of the
        JsonWriter.getStrictness() strictness of the provided JsonWriter. For
        legacy reasons, if the `Gson` instance has no explicit strictness setting and the writer
        does not have the strictness Strictness.STRICT, the JSON will be written in Strictness.LENIENT mode.
        Note that in all cases the old strictness setting of the writer will be restored when this
        method returns.
        
        The 'HTML-safe' and 'serialize `null`' settings of this `Gson` instance
        (configured by the GsonBuilder) are applied, and the original settings of the writer
        are restored once this method returns.

        Arguments
        - src: the object for which JSON representation is to be created
        - typeOfSrc: the type of the object to be written
        - writer: Writer to which the JSON representation of src needs to be written

        Raises
        - JsonIOException: if there was a problem writing to the writer
        """
        ...


    def toJson(self, jsonElement: "JsonElement") -> str:
        """
        Converts a tree of JsonElements into its equivalent JSON representation.

        Arguments
        - jsonElement: root of a tree of JsonElements

        Returns
        - JSON String representation of the tree.

        Since
        - 1.4
        """
        ...


    def toJson(self, jsonElement: "JsonElement", writer: "Appendable") -> None:
        """
        Writes out the equivalent JSON for a tree of JsonElements.

        Arguments
        - jsonElement: root of a tree of JsonElements
        - writer: Writer to which the JSON representation needs to be written

        Raises
        - JsonIOException: if there was a problem writing to the writer

        Since
        - 1.4
        """
        ...


    def toJson(self, jsonElement: "JsonElement", writer: "JsonWriter") -> None:
        """
        Writes the JSON for `jsonElement` to `writer`.
        
        If the `Gson` instance has an GsonBuilder.setStrictness(Strictness)
        explicit strictness setting, this setting will be used for writing the JSON regardless of the
        JsonWriter.getStrictness() strictness of the provided JsonWriter. For
        legacy reasons, if the `Gson` instance has no explicit strictness setting and the writer
        does not have the strictness Strictness.STRICT, the JSON will be written in Strictness.LENIENT mode.
        Note that in all cases the old strictness setting of the writer will be restored when this
        method returns.
        
        The 'HTML-safe' and 'serialize `null`' settings of this `Gson` instance
        (configured by the GsonBuilder) are applied, and the original settings of the writer
        are restored once this method returns.

        Arguments
        - jsonElement: the JSON element to be written
        - writer: the JSON writer to which the provided element will be written

        Raises
        - JsonIOException: if there was a problem writing to the writer
        """
        ...


    def newJsonWriter(self, writer: "Writer") -> "JsonWriter":
        """
        Returns a new JSON writer configured for the settings on this Gson instance.
        
        The following settings are considered:
        
        
          - GsonBuilder.disableHtmlEscaping()
          - GsonBuilder.generateNonExecutableJson()
          - GsonBuilder.serializeNulls()
          - GsonBuilder.setStrictness(Strictness). If no GsonBuilder.setStrictness(Strictness) explicit strictness has been set the created
              writer will have a strictness of Strictness.LEGACY_STRICT. Otherwise, the
              strictness of the `Gson` instance will be used for the created writer.
          - GsonBuilder.setPrettyPrinting()
          - GsonBuilder.setFormattingStyle(FormattingStyle)
        """
        ...


    def newJsonReader(self, reader: "Reader") -> "JsonReader":
        """
        Returns a new JSON reader configured for the settings on this Gson instance.
        
        The following settings are considered:
        
        
          - GsonBuilder.setStrictness(Strictness). If no GsonBuilder.setStrictness(Strictness) explicit strictness has been set the created
              reader will have a strictness of Strictness.LEGACY_STRICT. Otherwise, the
              strictness of the `Gson` instance will be used for the created reader.
        """
        ...


    def fromJson(self, json: str, classOfT: type["T"]) -> "T":
        """
        This method deserializes the specified JSON into an object of the specified class. It is not
        suitable to use if the specified class is a generic type since it will not have the generic
        type information because of the Type Erasure feature of Java. Therefore, this method should not
        be used if the desired type is a generic type. Note that this method works fine if any of the
        fields of the specified object are generics, just the object itself should not be a generic
        type. For the cases when the object is of generic type, invoke .fromJson(String,
        TypeToken). If you have the JSON in a Reader instead of a String, use .fromJson(Reader, Class) instead.
        
        An exception is thrown if the JSON string has multiple top-level JSON elements, or if there
        is trailing data. Use .fromJson(JsonReader, Type) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the string from which the object is to be deserialized
        - classOfT: the class of T

        Returns
        - an object of type T from the string. Returns `null` if `json` is `null` or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of type
            classOfT

        See
        - .fromJson(String, TypeToken)
        """
        ...


    def fromJson(self, json: str, typeOfT: "Type") -> "T":
        """
        This method deserializes the specified JSON into an object of the specified type. This method
        is useful if the specified object is a generic type. For non-generic objects, use .fromJson(String, Class) instead. If you have the JSON in a Reader instead of a
        String, use .fromJson(Reader, Type) instead.
        
        Since `Type` is not parameterized by T, this method is not type-safe and should be
        used carefully. If you are creating the `Type` from a TypeToken, prefer using
        .fromJson(String, TypeToken) instead since its return type is based on the `TypeToken` and is therefore more type-safe.
        
        An exception is thrown if the JSON string has multiple top-level JSON elements, or if there
        is trailing data. Use .fromJson(JsonReader, Type) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the string from which the object is to be deserialized
        - typeOfT: The specific genericized type of src

        Returns
        - an object of type T from the string. Returns `null` if `json` is `null` or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(String, TypeToken)
        """
        ...


    def fromJson(self, json: str, typeOfT: "TypeToken"["T"]) -> "T":
        """
        This method deserializes the specified JSON into an object of the specified type. This method
        is useful if the specified object is a generic type. For non-generic objects, use .fromJson(String, Class) instead. If you have the JSON in a Reader instead of a
        String, use .fromJson(Reader, TypeToken) instead.
        
        An exception is thrown if the JSON string has multiple top-level JSON elements, or if there
        is trailing data. Use .fromJson(JsonReader, TypeToken) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the string from which the object is to be deserialized
        - typeOfT: The specific genericized type of src. You should create an anonymous subclass of
            `TypeToken` with the specific generic type arguments. For example, to get the type
            for `Collection<Foo>`, you should use:
            ```
        new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}
        ```

        Returns
        - an object of type T from the string. Returns `null` if `json` is `null` or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of the type
            typeOfT

        See
        - .fromJson(String, Class)

        Since
        - 2.10
        """
        ...


    def fromJson(self, json: "Reader", classOfT: type["T"]) -> "T":
        """
        This method deserializes the JSON read from the specified reader into an object of the
        specified class. It is not suitable to use if the specified class is a generic type since it
        will not have the generic type information because of the Type Erasure feature of Java.
        Therefore, this method should not be used if the desired type is a generic type. Note that this
        method works fine if any of the fields of the specified object are generics, just the object
        itself should not be a generic type. For the cases when the object is of generic type, invoke
        .fromJson(Reader, TypeToken). If you have the JSON in a String form instead of a Reader, use .fromJson(String, Class) instead.
        
        An exception is thrown if the JSON data has multiple top-level JSON elements, or if there is
        trailing data. Use .fromJson(JsonReader, Type) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the reader producing the JSON from which the object is to be deserialized.
        - classOfT: the class of T

        Returns
        - an object of type T from the Reader. Returns `null` if `json` is at EOF.

        Raises
        - JsonIOException: if there was a problem reading from the Reader
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(Reader, TypeToken)

        Since
        - 1.2
        """
        ...


    def fromJson(self, json: "Reader", typeOfT: "Type") -> "T":
        """
        This method deserializes the JSON read from the specified reader into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use .fromJson(Reader, Class) instead. If you have the JSON in a
        String form instead of a Reader, use .fromJson(String, Type) instead.
        
        Since `Type` is not parameterized by T, this method is not type-safe and should be
        used carefully. If you are creating the `Type` from a TypeToken, prefer using
        .fromJson(Reader, TypeToken) instead since its return type is based on the `TypeToken` and is therefore more type-safe.
        
        An exception is thrown if the JSON data has multiple top-level JSON elements, or if there is
        trailing data. Use .fromJson(JsonReader, Type) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the reader producing JSON from which the object is to be deserialized
        - typeOfT: The specific genericized type of src

        Returns
        - an object of type T from the Reader. Returns `null` if `json` is at EOF.

        Raises
        - JsonIOException: if there was a problem reading from the Reader
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(Reader, TypeToken)

        Since
        - 1.2
        """
        ...


    def fromJson(self, json: "Reader", typeOfT: "TypeToken"["T"]) -> "T":
        """
        This method deserializes the JSON read from the specified reader into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use .fromJson(Reader, Class) instead. If you have the JSON in a
        String form instead of a Reader, use .fromJson(String, TypeToken) instead.
        
        An exception is thrown if the JSON data has multiple top-level JSON elements, or if there is
        trailing data. Use .fromJson(JsonReader, TypeToken) if this behavior is not desired.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the reader producing JSON from which the object is to be deserialized
        - typeOfT: The specific genericized type of src. You should create an anonymous subclass of
            `TypeToken` with the specific generic type arguments. For example, to get the type
            for `Collection<Foo>`, you should use:
            ```
        new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}
        ```

        Returns
        - an object of type T from the Reader. Returns `null` if `json` is at EOF.

        Raises
        - JsonIOException: if there was a problem reading from the Reader
        - JsonSyntaxException: if json is not a valid representation for an object of type of
            typeOfT

        See
        - .fromJson(Reader, Class)

        Since
        - 2.10
        """
        ...


    def fromJson(self, reader: "JsonReader", typeOfT: "Type") -> "T":
        """
        Reads the next JSON value from `reader` and converts it to an object of type `typeOfT`. Returns `null`, if the `reader` is at EOF.
        
        Since `Type` is not parameterized by T, this method is not type-safe and should be
        used carefully. If you are creating the `Type` from a TypeToken, prefer using
        .fromJson(JsonReader, TypeToken) instead since its return type is based on the `TypeToken` and is therefore more type-safe. If the provided type is a `Class` the `TypeToken` can be created with TypeToken.get(Class).
        
        Unlike the other `fromJson` methods, no exception is thrown if the JSON data has
        multiple top-level JSON elements, or if there is trailing data.
        
        If the `Gson` instance has an GsonBuilder.setStrictness(Strictness)
        explicit strictness setting, this setting will be used for reading the JSON regardless of the
        JsonReader.getStrictness() strictness of the provided JsonReader. For
        legacy reasons, if the `Gson` instance has no explicit strictness setting and the reader
        does not have the strictness Strictness.STRICT, the JSON will be written in Strictness.LENIENT mode.
        Note that in all cases the old strictness setting of the reader will be restored when this
        method returns.
        
        Type `<T>`: the type of the desired object

        Arguments
        - reader: the reader whose next JSON value should be deserialized
        - typeOfT: The specific genericized type of src

        Returns
        - an object of type T from the JsonReader. Returns `null` if `reader` is at
            EOF.

        Raises
        - JsonIOException: if there was a problem reading from the JsonReader
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(JsonReader, TypeToken)
        """
        ...


    def fromJson(self, reader: "JsonReader", typeOfT: "TypeToken"["T"]) -> "T":
        """
        Reads the next JSON value from `reader` and converts it to an object of type `typeOfT`. Returns `null`, if the `reader` is at EOF. This method is useful if the
        specified object is a generic type. For non-generic objects, .fromJson(JsonReader,
        Type) can be called, or TypeToken.get(Class) can be used to create the type token.
        
        Unlike the other `fromJson` methods, no exception is thrown if the JSON data has
        multiple top-level JSON elements, or if there is trailing data.
        
        If the `Gson` instance has an GsonBuilder.setStrictness(Strictness)
        explicit strictness setting, this setting will be used for reading the JSON regardless of the
        JsonReader.getStrictness() strictness of the provided JsonReader. For
        legacy reasons, if the `Gson` instance has no explicit strictness setting and the reader
        does not have the strictness Strictness.STRICT, the JSON will be written in Strictness.LENIENT mode.
        Note that in all cases the old strictness setting of the reader will be restored when this
        method returns.
        
        Type `<T>`: the type of the desired object

        Arguments
        - reader: the reader whose next JSON value should be deserialized
        - typeOfT: The specific genericized type of src. You should create an anonymous subclass of
            `TypeToken` with the specific generic type arguments. For example, to get the type
            for `Collection<Foo>`, you should use:
            ```
        new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}
        ```

        Returns
        - an object of type T from the JsonReader. Returns `null` if `reader` is at
            EOF.

        Raises
        - JsonIOException: if there was a problem reading from the JsonReader
        - JsonSyntaxException: if json is not a valid representation for an object of the type
            typeOfT

        See
        - .fromJson(JsonReader, Type)

        Since
        - 2.10
        """
        ...


    def fromJson(self, json: "JsonElement", classOfT: type["T"]) -> "T":
        """
        This method deserializes the JSON read from the specified parse tree into an object of the
        specified type. It is not suitable to use if the specified class is a generic type since it
        will not have the generic type information because of the Type Erasure feature of Java.
        Therefore, this method should not be used if the desired type is a generic type. Note that this
        method works fine if any of the fields of the specified object are generics, just the object
        itself should not be a generic type. For the cases when the object is of generic type, invoke
        .fromJson(JsonElement, TypeToken).
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the root of the parse tree of JsonElements from which the object is to be
            deserialized
        - classOfT: The class of T

        Returns
        - an object of type T from the JSON. Returns `null` if `json` is `null`
            or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of type
            classOfT

        See
        - .fromJson(JsonElement, TypeToken)

        Since
        - 1.3
        """
        ...


    def fromJson(self, json: "JsonElement", typeOfT: "Type") -> "T":
        """
        This method deserializes the JSON read from the specified parse tree into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use .fromJson(JsonElement, Class) instead.
        
        Since `Type` is not parameterized by T, this method is not type-safe and should be
        used carefully. If you are creating the `Type` from a TypeToken, prefer using
        .fromJson(JsonElement, TypeToken) instead since its return type is based on the `TypeToken` and is therefore more type-safe.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the root of the parse tree of JsonElements from which the object is to be
            deserialized
        - typeOfT: The specific genericized type of src

        Returns
        - an object of type T from the JSON. Returns `null` if `json` is `null`
            or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(JsonElement, TypeToken)

        Since
        - 1.3
        """
        ...


    def fromJson(self, json: "JsonElement", typeOfT: "TypeToken"["T"]) -> "T":
        """
        This method deserializes the JSON read from the specified parse tree into an object of the
        specified type. This method is useful if the specified object is a generic type. For
        non-generic objects, use .fromJson(JsonElement, Class) instead.
        
        Type `<T>`: the type of the desired object

        Arguments
        - json: the root of the parse tree of JsonElements from which the object is to be
            deserialized
        - typeOfT: The specific genericized type of src. You should create an anonymous subclass of
            `TypeToken` with the specific generic type arguments. For example, to get the type
            for `Collection<Foo>`, you should use:
            ```
        new TypeToken&lt;Collection&lt;Foo&gt;&gt;(){}
        ```

        Returns
        - an object of type T from the JSON. Returns `null` if `json` is `null`
            or if `json` is empty.

        Raises
        - JsonSyntaxException: if json is not a valid representation for an object of type typeOfT

        See
        - .fromJson(JsonElement, Class)

        Since
        - 2.10
        """
        ...


    def toString(self) -> str:
        ...
