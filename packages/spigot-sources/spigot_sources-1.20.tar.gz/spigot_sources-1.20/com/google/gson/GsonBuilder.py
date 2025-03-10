"""
Python module generated from Java source file com.google.gson.GsonBuilder

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.annotations import Since
from com.google.gson.annotations import Until
from com.google.gson.internal import $Gson$Preconditions
from com.google.gson.internal import Excluder
from com.google.gson.internal.bind import DefaultDateTypeAdapter
from com.google.gson.internal.bind import TreeTypeAdapter
from com.google.gson.internal.bind import TypeAdapters
from com.google.gson.internal.sql import SqlTypesSupport
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonWriter
from java.lang.reflect import Type
from java.text import DateFormat
from java.util import Collections
from java.util import Date
from java.util import Objects
from typing import Any, Callable, Iterable, Tuple


class GsonBuilder:
    """
    Use this builder to construct a Gson instance when you need to set configuration
    options other than the default. For Gson with default configuration, it is simpler to
    use `new Gson()`. `GsonBuilder` is best used by creating it, and then invoking its
    various configuration methods, and finally calling create.
    
    The following is an example shows how to use the `GsonBuilder` to construct a Gson
    instance:
    
    ```
    Gson gson = new GsonBuilder()
        .registerTypeAdapter(Id.class, new IdTypeAdapter())
        .enableComplexMapKeySerialization()
        .serializeNulls()
        .setDateFormat(DateFormat.LONG)
        .setFieldNamingPolicy(FieldNamingPolicy.UPPER_CAMEL_CASE)
        .setPrettyPrinting()
        .setVersion(1.0)
        .create();
    ```
    
    NOTES:
    
    -  the order of invocation of configuration methods does not matter.
    -  The default serialization of Date and its subclasses in Gson does
     not contain time-zone information. So, if you are using date/time instances,
     use `GsonBuilder` and its `setDateFormat` methods.

    Author(s)
    - Jesse Wilson
    """

    def __init__(self):
        """
        Creates a GsonBuilder instance that can be used to build Gson with various configuration
        settings. GsonBuilder follows the builder pattern, and it is typically used by first
        invoking various configuration methods to set desired options, and finally calling
        .create().
        """
        ...


    def setVersion(self, version: float) -> "GsonBuilder":
        """
        Configures Gson to enable versioning support. Versioning support works based on the
        annotation types Since and Until. It allows including or excluding fields
        and classes based on the specified version. See the documentation of these annotation
        types for more information.
        
        By default versioning support is disabled and usage of `@Since` and `@Until`
        has no effect.

        Arguments
        - version: the version number to use.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Raises
        - IllegalArgumentException: if the version number is NaN or negative

        See
        - Until
        """
        ...


    def excludeFieldsWithModifiers(self, *modifiers: Tuple[int, ...]) -> "GsonBuilder":
        """
        Configures Gson to excludes all class fields that have the specified modifiers. By default,
        Gson will exclude all fields marked `transient` or `static`. This method will
        override that behavior.
        
        This is a convenience method which behaves as if an ExclusionStrategy which
        excludes these fields was .setExclusionStrategies(ExclusionStrategy...) registered with this builder.

        Arguments
        - modifiers: the field modifiers. You must use the modifiers specified in the
        java.lang.reflect.Modifier class. For example,
        java.lang.reflect.Modifier.TRANSIENT,
        java.lang.reflect.Modifier.STATIC.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def generateNonExecutableJson(self) -> "GsonBuilder":
        """
        Makes the output JSON non-executable in Javascript by prefixing the generated JSON with some
        special text. This prevents attacks from third-party sites through script sourcing. See
        <a href="http://code.google.com/p/google-gson/issues/detail?id=42">Gson Issue 42</a>
        for details.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def excludeFieldsWithoutExposeAnnotation(self) -> "GsonBuilder":
        """
        Configures Gson to exclude all fields from consideration for serialization and deserialization
        that do not have the com.google.gson.annotations.Expose annotation.
        
        This is a convenience method which behaves as if an ExclusionStrategy which excludes
        these fields was .setExclusionStrategies(ExclusionStrategy...) registered with this builder.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def serializeNulls(self) -> "GsonBuilder":
        """
        Configure Gson to serialize null fields. By default, Gson omits all fields that are null
        during serialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.2
        """
        ...


    def enableComplexMapKeySerialization(self) -> "GsonBuilder":
        """
        Enabling this feature will only change the serialized form if the map key is
        a complex type (i.e. non-primitive) in its <strong>serialized</strong> JSON
        form. The default implementation of map serialization uses `toString()`
        on the key; however, when this is called then one of the following cases
        apply:
        
        **Maps as JSON objects**
        
        For this case, assume that a type adapter is registered to serialize and
        deserialize some `Point` class, which contains an x and y coordinate,
        to/from the JSON Primitive string value `"(x,y)"`. The Java map would
        then be serialized as a JsonObject.
        
        Below is an example:
        ```  `Gson gson = new GsonBuilder()
              .register(Point.class, new MyPointTypeAdapter())
              .enableComplexMapKeySerialization()
              .create();
        
          Map<Point, String> original = new LinkedHashMap<>();
          original.put(new Point(5, 6), "a");
          original.put(new Point(8, 8), "b");
          System.out.println(gson.toJson(original, type));````
        The above code prints this JSON object:```  `{
            "(5,6)": "a",
            "(8,8)": "b"`
        }```
        
        **Maps as JSON arrays**
        
        For this case, assume that a type adapter was NOT registered for some
        `Point` class, but rather the default Gson serialization is applied.
        In this case, some `new Point(2,3)` would serialize as `{"x":2,"y":3`}.
        
        Given the assumption above, a `Map<Point, String>` will be
        serialize as an array of arrays (can be viewed as an entry set of pairs).
        
        Below is an example of serializing complex types as JSON arrays:
        ``` `Gson gson = new GsonBuilder()
              .enableComplexMapKeySerialization()
              .create();
        
          Map<Point, String> original = new LinkedHashMap<>();
          original.put(new Point(5, 6), "a");
          original.put(new Point(8, 8), "b");
          System.out.println(gson.toJson(original, type));`
        ```
        
        The JSON output would look as follows:
        ```   `[
            [
              {
                "x": 5,
                "y": 6`,
              "a"
            ],
            [
              {
                "x": 8,
                "y": 8
              },
              "b"
            ]
          ]
        }```

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.7
        """
        ...


    def disableInnerClassSerialization(self) -> "GsonBuilder":
        """
        Configures Gson to exclude inner classes (= non-`static` nested classes) during serialization
        and deserialization. This is a convenience method which behaves as if an ExclusionStrategy
        which excludes inner classes was .setExclusionStrategies(ExclusionStrategy...) registered with this builder.
        This means inner classes will be serialized as JSON `null`, and will be deserialized as
        Java `null` with their JSON data being ignored. And fields with an inner class as type will
        be ignored during serialization and deserialization.
        
        By default Gson serializes and deserializes inner classes, but ignores references to the
        enclosing instance. Deserialization might not be possible at all when .disableJdkUnsafe()
        is used (and no custom InstanceCreator is registered), or it can lead to unexpected
        `NullPointerException`s when the deserialized instance is used afterwards.
        
        In general using inner classes with Gson should be avoided; they should be converted to `static`
        nested classes if possible.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def setLongSerializationPolicy(self, serializationPolicy: "LongSerializationPolicy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific serialization policy for `Long` and `long`
        objects.

        Arguments
        - serializationPolicy: the particular policy to use for serializing longs.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def setFieldNamingPolicy(self, namingConvention: "FieldNamingPolicy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific naming policy to an object's fields during serialization
        and deserialization.
        
        This method just delegates to .setFieldNamingStrategy(FieldNamingStrategy).
        """
        ...


    def setFieldNamingStrategy(self, fieldNamingStrategy: "FieldNamingStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific naming strategy to an object's fields during
        serialization and deserialization.
        
        The created Gson instance might only use the field naming strategy once for a
        field and cache the result. It is not guaranteed that the strategy will be used
        again every time the value of a field is serialized or deserialized.

        Arguments
        - fieldNamingStrategy: the naming strategy to apply to the fields

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def setObjectToNumberStrategy(self, objectToNumberStrategy: "ToNumberStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific number strategy during deserialization of Object.

        Arguments
        - objectToNumberStrategy: the actual object-to-number strategy

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        See
        - ToNumberPolicy.DOUBLE The default object-to-number strategy

        Since
        - 2.8.9
        """
        ...


    def setNumberToNumberStrategy(self, numberToNumberStrategy: "ToNumberStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific number strategy during deserialization of Number.

        Arguments
        - numberToNumberStrategy: the actual number-to-number strategy

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        See
        - ToNumberPolicy.LAZILY_PARSED_NUMBER The default number-to-number strategy

        Since
        - 2.8.9
        """
        ...


    def setExclusionStrategies(self, *strategies: Tuple["ExclusionStrategy", ...]) -> "GsonBuilder":
        """
        Configures Gson to apply a set of exclusion strategies during both serialization and
        deserialization. Each of the `strategies` will be applied as a disjunction rule.
        This means that if one of the `strategies` suggests that a field (or class) should be
        skipped then that field (or object) is skipped during serialization/deserialization.
        The strategies are added to the existing strategies (if any); the existing strategies
        are not replaced.
        
        Fields are excluded for serialization and deserialization when
        ExclusionStrategy.shouldSkipField(FieldAttributes) shouldSkipField returns `True`,
        or when ExclusionStrategy.shouldSkipClass(Class) shouldSkipClass returns `True`
        for the field type. Gson behaves as if the field did not exist; its value is not serialized
        and on deserialization if a JSON member with this name exists it is skipped by default.
        When objects of an excluded type (as determined by
        ExclusionStrategy.shouldSkipClass(Class) shouldSkipClass) are serialized a
        JSON null is written to output, and when deserialized the JSON value is skipped and
        `null` is returned.
        
        The created Gson instance might only use an exclusion strategy once for a field or
        class and cache the result. It is not guaranteed that the strategy will be used again
        every time the value of a field or a class is serialized or deserialized.

        Arguments
        - strategies: the set of strategy object to apply during object (de)serialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.4
        """
        ...


    def addSerializationExclusionStrategy(self, strategy: "ExclusionStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply the passed in exclusion strategy during serialization.
        If this method is invoked numerous times with different exclusion strategy objects
        then the exclusion strategies that were added will be applied as a disjunction rule.
        This means that if one of the added exclusion strategies suggests that a field (or
        class) should be skipped then that field (or object) is skipped during its
        serialization.
        
        See the documentation of .setExclusionStrategies(ExclusionStrategy...)
        for a detailed description of the effect of exclusion strategies.

        Arguments
        - strategy: an exclusion strategy to apply during serialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.7
        """
        ...


    def addDeserializationExclusionStrategy(self, strategy: "ExclusionStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply the passed in exclusion strategy during deserialization.
        If this method is invoked numerous times with different exclusion strategy objects
        then the exclusion strategies that were added will be applied as a disjunction rule.
        This means that if one of the added exclusion strategies suggests that a field (or
        class) should be skipped then that field (or object) is skipped during its
        deserialization.
        
        See the documentation of .setExclusionStrategies(ExclusionStrategy...)
        for a detailed description of the effect of exclusion strategies.

        Arguments
        - strategy: an exclusion strategy to apply during deserialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.7
        """
        ...


    def setPrettyPrinting(self) -> "GsonBuilder":
        """
        Configures Gson to output Json that fits in a page for pretty printing. This option only
        affects Json serialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def setLenient(self) -> "GsonBuilder":
        """
        Configures Gson to allow JSON data which does not strictly comply with the JSON specification.
        
        Note: Due to legacy reasons most methods of Gson are always lenient, regardless of
        whether this builder method is used.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        See
        - JsonWriter.setLenient(boolean)
        """
        ...


    def disableHtmlEscaping(self) -> "GsonBuilder":
        """
        By default, Gson escapes HTML characters such as &lt; &gt; etc. Use this option to configure
        Gson to pass-through HTML characters as is.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def setDateFormat(self, pattern: str) -> "GsonBuilder":
        """
        Configures Gson to serialize `Date` objects according to the pattern provided. You can
        call this method or .setDateFormat(int) multiple times, but only the last invocation
        will be used to decide the serialization format.
        
        The date format will be used to serialize and deserialize java.util.Date and in case
        the `java.sql` module is present, also java.sql.Timestamp and java.sql.Date.
        
        Note that this pattern must abide by the convention provided by `SimpleDateFormat`
        class. See the documentation in java.text.SimpleDateFormat for more information on
        valid date and time patterns.

        Arguments
        - pattern: the pattern that dates will be serialized/deserialized to/from

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.2
        """
        ...


    def setDateFormat(self, style: int) -> "GsonBuilder":
        """
        Configures Gson to to serialize `Date` objects according to the style value provided.
        You can call this method or .setDateFormat(String) multiple times, but only the last
        invocation will be used to decide the serialization format.
        
        Note that this style value should be one of the predefined constants in the
        `DateFormat` class. See the documentation in java.text.DateFormat for more
        information on the valid style constants.

        Arguments
        - style: the predefined date style that date objects will be serialized/deserialized
        to/from

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.2
        """
        ...


    def setDateFormat(self, dateStyle: int, timeStyle: int) -> "GsonBuilder":
        """
        Configures Gson to to serialize `Date` objects according to the style value provided.
        You can call this method or .setDateFormat(String) multiple times, but only the last
        invocation will be used to decide the serialization format.
        
        Note that this style value should be one of the predefined constants in the
        `DateFormat` class. See the documentation in java.text.DateFormat for more
        information on the valid style constants.

        Arguments
        - dateStyle: the predefined date style that date objects will be serialized/deserialized
        to/from
        - timeStyle: the predefined style for the time portion of the date objects

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.2
        """
        ...


    def registerTypeAdapter(self, type: "Type", typeAdapter: "Object") -> "GsonBuilder":
        """
        Configures Gson for custom serialization or deserialization. This method combines the
        registration of an TypeAdapter, InstanceCreator, JsonSerializer, and a
        JsonDeserializer. It is best used when a single object `typeAdapter` implements
        all the required interfaces for custom serialization with Gson. If a type adapter was
        previously registered for the specified `type`, it is overwritten.
        
        This registers the type specified and no other types: you must manually register related
        types! For example, applications registering `boolean.class` should also register `Boolean.class`.
        
        JsonSerializer and JsonDeserializer are made "`null`-safe". This
        means when trying to serialize `null`, Gson will write a JSON `null` and the
        serializer is not called. Similarly when deserializing a JSON `null`, Gson will emit
        `null` without calling the deserializer. If it is desired to handle `null` values,
        a TypeAdapter should be used instead.

        Arguments
        - type: the type definition for the type adapter being registered
        - typeAdapter: This object must implement at least one of the TypeAdapter,
        InstanceCreator, JsonSerializer, and a JsonDeserializer interfaces.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def registerTypeAdapterFactory(self, factory: "TypeAdapterFactory") -> "GsonBuilder":
        """
        Register a factory for type adapters. Registering a factory is useful when the type
        adapter needs to be configured based on the type of the field being processed. Gson
        is designed to handle a large number of factories, so you should consider registering
        them to be at par with registering an individual type adapter.
        
        The created Gson instance might only use the factory once to create an adapter for
        a specific type and cache the result. It is not guaranteed that the factory will be used
        again every time the type is serialized or deserialized.

        Since
        - 2.1
        """
        ...


    def registerTypeHierarchyAdapter(self, baseType: type[Any], typeAdapter: "Object") -> "GsonBuilder":
        """
        Configures Gson for custom serialization or deserialization for an inheritance type hierarchy.
        This method combines the registration of a TypeAdapter, JsonSerializer and
        a JsonDeserializer. If a type adapter was previously registered for the specified
        type hierarchy, it is overridden. If a type adapter is registered for a specific type in
        the type hierarchy, it will be invoked instead of the one registered for the type hierarchy.

        Arguments
        - baseType: the class definition for the type adapter being registered for the base class
               or interface
        - typeAdapter: This object must implement at least one of TypeAdapter,
               JsonSerializer or JsonDeserializer interfaces.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.7
        """
        ...


    def serializeSpecialFloatingPointValues(self) -> "GsonBuilder":
        """
        Section 2.4 of <a href="http://www.ietf.org/rfc/rfc4627.txt">JSON specification</a> disallows
        special double values (NaN, Infinity, -Infinity). However,
        <a href="http://www.ecma-international.org/publications/files/ECMA-ST/Ecma-262.pdf">Javascript
        specification</a> (see section 4.3.20, 4.3.22, 4.3.23) allows these values as valid Javascript
        values. Moreover, most JavaScript engines will accept these special values in JSON without
        problem. So, at a practical level, it makes sense to accept these values as valid JSON even
        though JSON specification disallows them.
        
        Gson always accepts these special values during deserialization. However, it outputs
        strictly compliant JSON. Hence, if it encounters a float value Float.NaN,
        Float.POSITIVE_INFINITY, Float.NEGATIVE_INFINITY, or a double value
        Double.NaN, Double.POSITIVE_INFINITY, Double.NEGATIVE_INFINITY, it
        will throw an IllegalArgumentException. This method provides a way to override the
        default behavior when you know that the JSON receiver will be able to handle these special
        values.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def disableJdkUnsafe(self) -> "GsonBuilder":
        """
        Disables usage of JDK's `sun.misc.Unsafe`.
        
        By default Gson uses `Unsafe` to create instances of classes which don't have
        a no-args constructor. However, `Unsafe` might not be available for all Java
        runtimes. For example Android does not provide `Unsafe`, or only with limited
        functionality. Additionally `Unsafe` creates instances without executing any
        constructor or initializer block, or performing initialization of field values. This can
        lead to surprising and difficult to debug errors.
        Therefore, to get reliable behavior regardless of which runtime is used, and to detect
        classes which cannot be deserialized in an early stage of development, this method allows
        disabling usage of `Unsafe`.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 2.9.0
        """
        ...


    def addReflectionAccessFilter(self, filter: "ReflectionAccessFilter") -> "GsonBuilder":
        """
        Adds a reflection access filter. A reflection access filter prevents Gson from using
        reflection for the serialization and deserialization of certain classes. The logic in
        the filter specifies which classes those are.
        
        Filters will be invoked in reverse registration order, that is, the most recently
        added filter will be invoked first.
        
        By default Gson has no filters configured and will try to use reflection for
        all classes for which no TypeAdapter has been registered, and for which no
        built-in Gson `TypeAdapter` exists.
        
        The created Gson instance might only use an access filter once for a class or its
        members and cache the result. It is not guaranteed that the filter will be used again
        every time a class or its members are accessed during serialization or deserialization.

        Arguments
        - filter: filter to add

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 2.9.1
        """
        ...


    def create(self) -> "Gson":
        """
        Creates a Gson instance based on the current configuration. This method is free of
        side-effects to this `GsonBuilder` instance and hence can be called multiple times.

        Returns
        - an instance of Gson configured with the options currently set in this builder
        """
        ...
