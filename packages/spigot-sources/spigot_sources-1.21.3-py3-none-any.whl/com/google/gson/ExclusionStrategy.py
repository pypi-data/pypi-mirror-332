"""
Python module generated from Java source file com.google.gson.ExclusionStrategy

Java source file obtained from artifact gson version 2.10.1

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import *
from typing import Any, Callable, Iterable, Tuple


class ExclusionStrategy:
    """
    A strategy (or policy) definition that is used to decide whether or not a field or
    class should be serialized or deserialized as part of the JSON output/input.
    
    The following are a few examples that shows how you can use this exclusion mechanism.
    
    <strong>Exclude fields and objects based on a particular class type:</strong>
    <pre class="code">
    private static class SpecificClassExclusionStrategy implements ExclusionStrategy {
      private final Class&lt;?&gt; excludedThisClass;
    
      public SpecificClassExclusionStrategy(Class&lt;?&gt; excludedThisClass) {
        this.excludedThisClass = excludedThisClass;
      }
    
      public boolean shouldSkipClass(Class&lt;?&gt; clazz) {
        return excludedThisClass.equals(clazz);
      }
    
      public boolean shouldSkipField(FieldAttributes f) {
        return excludedThisClass.equals(f.getDeclaredClass());
      }
    }
    ```
    
    <strong>Excludes fields and objects based on a particular annotation:</strong>
    <pre class="code">
    public &#64;interface FooAnnotation {
      // some implementation here
    }
    
    // Excludes any field (or class) that is tagged with an "&#64;FooAnnotation"
    private static class FooAnnotationExclusionStrategy implements ExclusionStrategy {
      public boolean shouldSkipClass(Class&lt;?&gt; clazz) {
        return clazz.getAnnotation(FooAnnotation.class) != null;
      }
    
      public boolean shouldSkipField(FieldAttributes f) {
        return f.getAnnotation(FooAnnotation.class) != null;
      }
    }
    ```
    
    Now if you want to configure `Gson` to use a user defined exclusion strategy, then
    the `GsonBuilder` is required. The following is an example of how you can use the
    `GsonBuilder` to configure Gson to use one of the above samples:
    <pre class="code">
    ExclusionStrategy excludeStrings = new UserDefinedExclusionStrategy(String.class);
    Gson gson = new GsonBuilder()
        .setExclusionStrategies(excludeStrings)
        .create();
    ```
    
    For certain model classes, you may only want to serialize a field, but exclude it for
    deserialization. To do that, you can write an `ExclusionStrategy` as per normal;
    however, you would register it with the
    GsonBuilder.addDeserializationExclusionStrategy(ExclusionStrategy) method.
    For example:
    <pre class="code">
    ExclusionStrategy excludeStrings = new UserDefinedExclusionStrategy(String.class);
    Gson gson = new GsonBuilder()
        .addDeserializationExclusionStrategy(excludeStrings)
        .create();
    ```

    Author(s)
    - Joel Leitch

    See
    - GsonBuilder.addSerializationExclusionStrategy(ExclusionStrategy)

    Since
    - 1.4
    """

    def shouldSkipField(self, f: "FieldAttributes") -> bool:
        """
        Arguments
        - f: the field object that is under test

        Returns
        - True if the field should be ignored; otherwise False
        """
        ...


    def shouldSkipClass(self, clazz: type[Any]) -> bool:
        """
        Arguments
        - clazz: the class object that is under test

        Returns
        - True if the class should be ignored; otherwise False
        """
        ...
