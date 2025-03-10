"""
Python module generated from Java source file com.google.gson.internal.ConstructorConstructor

Java source file obtained from artifact gson version 2.10

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import InstanceCreator
from com.google.gson import JsonIOException
from com.google.gson import ReflectionAccessFilter
from com.google.gson.ReflectionAccessFilter import FilterResult
from com.google.gson.internal import *
from com.google.gson.internal.reflect import ReflectionHelper
from com.google.gson.reflect import TypeToken
from java.lang.reflect import Constructor
from java.lang.reflect import InvocationTargetException
from java.lang.reflect import Modifier
from java.lang.reflect import ParameterizedType
from java.lang.reflect import Type
from java.util import ArrayDeque
from java.util import EnumMap
from java.util import EnumSet
from java.util import LinkedHashSet
from java.util import Queue
from java.util import SortedMap
from java.util import SortedSet
from java.util.concurrent import ConcurrentHashMap
from java.util.concurrent import ConcurrentMap
from java.util.concurrent import ConcurrentNavigableMap
from java.util.concurrent import ConcurrentSkipListMap
from typing import Any, Callable, Iterable, Tuple


class ConstructorConstructor:
    """
    Returns a function that can construct an instance of a requested type.
    """

    def __init__(self, instanceCreators: dict["Type", "InstanceCreator"[Any]], useJdkUnsafe: bool, reflectionFilters: list["ReflectionAccessFilter"]):
        ...


    def get(self, typeToken: "TypeToken"["T"]) -> "ObjectConstructor"["T"]:
        ...


    def toString(self) -> str:
        ...
