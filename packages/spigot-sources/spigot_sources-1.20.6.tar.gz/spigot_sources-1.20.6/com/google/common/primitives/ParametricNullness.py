"""
Python module generated from Java source file com.google.common.primitives.ParametricNullness

Java source file obtained from artifact guava version 32.1.2-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.primitives import *
from typing import Any, Callable, Iterable, Tuple


class ParametricNullness:
    """
    Annotates a "top-level" type-variable usage that takes its nullness from the type argument
    supplied by the user of the class. For example, `Multiset.Entry.getElement()` returns
    `@ParametricNullness E`, which means:
    
    
      - `getElement` on a `Multiset.Entry<@NonNull String>` returns `@NonNull
          String`.
      - `getElement` on a `Multiset.Entry<@Nullable String>` returns `@Nullable
          String`.
    
    
    This is the same behavior as type-variable usages have to Kotlin and to the Checker Framework.
    Contrast the method above to:
    
    
      - methods whose return type is a type variable but which can never return `null`,
          typically because the type forbids nullable type arguments: For example, `ImmutableList.get` returns `E`, but that value is never `null`. (Accordingly,
          `ImmutableList` is declared to forbid `ImmutableList<@Nullable String>`.)
      - methods whose return type is a type variable but which can return `null` regardless
          of the type argument supplied by the user of the class: For example, `ImmutableMap.get` returns `@Nullable E` because the method can return `null`
          even on an `ImmutableMap<K, @NonNull String>`.
    
    
    Consumers of this annotation include:
    
    
      - Kotlin, for which it makes the type-variable usage (a) a Kotlin platform type when the type
          argument is non-nullable and (b) nullable when the type argument is nullable. We use this
          to "undo" ElementTypesAreNonnullByDefault. It is the best we can do for Kotlin
          under our current constraints.
      - NullAway, which will <a
          href="https://github.com/google/guava/issues/6126#issuecomment-1204399671">treat it
          identically to `Nullable` as of version 0.9.9</a>. To treat it that way before then,
          you can set `-XepOpt:NullAway:CustomNullableAnnotations=com.google.common.base.ParametricNullness,...,com.google.common.util.concurrent.ParametricNullness`,
          where the `...` contains the names of all the other `ParametricNullness`
          annotations in Guava. Or you might prefer to omit Guava from your `AnnotatedPackages`
          list.
      - <a href="https://developers.google.com/j2objc">J2ObjC</a>
      - `NullPointerTester`, at least in the Android backport (where the type-use annotations
          `NullPointerTester` would need are not available) and in case of <a
          href="https://bugs.openjdk.java.net/browse/JDK-8202469">JDK-8202469</a>
    
    
    This annotation is a temporary hack. We will remove it after we're able to adopt the <a
    href="https://jspecify.dev/">JSpecify</a> nullness annotations and <a
    href="https://github.com/google/guava/issues/6126#issuecomment-1203145963">tools no longer need
    it</a>.
    """


