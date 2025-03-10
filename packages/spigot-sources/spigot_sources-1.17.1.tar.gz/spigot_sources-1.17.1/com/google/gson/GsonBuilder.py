"""
Python module generated from Java source file com.google.gson.GsonBuilder

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from com.google.gson.internal import $Gson$Preconditions
from com.google.gson.internal import Excluder
from com.google.gson.internal.bind import TreeTypeAdapter
from com.google.gson.internal.bind import TypeAdapters
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from java.lang.reflect import Type
from java.text import DateFormat
from java.util import Collections
from java.util import Date
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


    def setVersion(self, ignoreVersionsAfter: float) -> "GsonBuilder":
        """
        Configures Gson to enable versioning support.

        Arguments
        - ignoreVersionsAfter: any field or type marked with a version higher than this value
        are ignored during serialization or deserialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def excludeFieldsWithModifiers(self, *modifiers: Tuple[int, ...]) -> "GsonBuilder":
        """
        Configures Gson to excludes all class fields that have the specified modifiers. By default,
        Gson will exclude all fields marked transient or static. This method will override that
        behavior.

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
        Configures Gson to exclude all fields from consideration for serialization or deserialization
        that do not have the com.google.gson.annotations.Expose annotation.

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
        
        <h3>Maps as JSON objects</h3>
        For this case, assume that a type adapter is registered to serialize and
        deserialize some `Point` class, which contains an x and y coordinate,
        to/from the JSON Primitive string value `"(x,y)"`. The Java map would
        then be serialized as a JsonObject.
        
        Below is an example:
        ```  `Gson gson = new GsonBuilder()
              .register(Point.class, new MyPointTypeAdapter())
              .enableComplexMapKeySerialization()
              .create();
        
          Map<Point, String> original = new LinkedHashMap<Point, String>();
          original.put(new Point(5, 6), "a");
          original.put(new Point(8, 8), "b");
          System.out.println(gson.toJson(original, type));````
        The above code prints this JSON object:```  `{
            "(5,6)": "a",
            "(8,8)": "b"`
        }```
        
        <h3>Maps as JSON arrays</h3>
        For this case, assume that a type adapter was NOT registered for some
        `Point` class, but rather the default Gson serialization is applied.
        In this case, some `new Point(2,3)` would serialize as `{"x":2,"y":5`}.
        
        Given the assumption above, a `Map<Point, String>` will be
        serialize as an array of arrays (can be viewed as an entry set of pairs).
        
        Below is an example of serializing complex types as JSON arrays:
        ``` `Gson gson = new GsonBuilder()
              .enableComplexMapKeySerialization()
              .create();
        
          Map<Point, String> original = new LinkedHashMap<Point, String>();
          original.put(new Point(5, 6), "a");
          original.put(new Point(8, 8), "b");
          System.out.println(gson.toJson(original, type));`
        
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
        Configures Gson to exclude inner classes during serialization.

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
        Configures Gson to apply a specific naming policy to an object's field during serialization
        and deserialization.

        Arguments
        - namingConvention: the JSON field naming convention to use for serialization and
        deserialization.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern
        """
        ...


    def setFieldNamingStrategy(self, fieldNamingStrategy: "FieldNamingStrategy") -> "GsonBuilder":
        """
        Configures Gson to apply a specific naming policy strategy to an object's field during
        serialization and deserialization.

        Arguments
        - fieldNamingStrategy: the actual naming strategy to apply to the fields

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        Since
        - 1.3
        """
        ...


    def setExclusionStrategies(self, *strategies: Tuple["ExclusionStrategy", ...]) -> "GsonBuilder":
        """
        Configures Gson to apply a set of exclusion strategies during both serialization and
        deserialization. Each of the `strategies` will be applied as a disjunction rule.
        This means that if one of the `strategies` suggests that a field (or class) should be
        skipped then that field (or object) is skipped during serialization/deserialization.

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
        By default, Gson is strict and only accepts JSON as specified by
        <a href="http://www.ietf.org/rfc/rfc4627.txt">RFC 4627</a>. This option makes the parser
        liberal in what it accepts.

        Returns
        - a reference to this `GsonBuilder` object to fulfill the "Builder" pattern

        See
        - JsonReader.setLenient(boolean)
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
        
        The date format will be used to serialize and deserialize java.util.Date, java.sql.Timestamp and java.sql.Date.
        
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


    def create(self) -> "Gson":
        """
        Creates a Gson instance based on the current configuration. This method is free of
        side-effects to this `GsonBuilder` instance and hence can be called multiple times.

        Returns
        - an instance of Gson configured with the options currently set in this builder
        """
        ...
