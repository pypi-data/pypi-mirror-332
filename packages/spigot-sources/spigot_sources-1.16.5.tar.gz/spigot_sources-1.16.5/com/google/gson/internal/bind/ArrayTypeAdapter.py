"""
Python module generated from Java source file com.google.gson.internal.bind.ArrayTypeAdapter

Java source file obtained from artifact gson version 2.8.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.gson import Gson
from com.google.gson import TypeAdapter
from com.google.gson import TypeAdapterFactory
from com.google.gson.internal import $Gson$Types
from com.google.gson.internal.bind import *
from com.google.gson.reflect import TypeToken
from com.google.gson.stream import JsonReader
from com.google.gson.stream import JsonToken
from com.google.gson.stream import JsonWriter
from java.io import IOException
from java.lang.reflect import Array
from java.lang.reflect import GenericArrayType
from java.lang.reflect import Type
from typing import Any, Callable, Iterable, Tuple


class ArrayTypeAdapter(TypeAdapter):
    """
    Adapt an array of objects.
    """

    FACTORY = TypeAdapterFactory() {
    
        @SuppressWarnings({ "unchecked", "rawtypes" })
        @Override
        public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> typeToken) {
            Type type = typeToken.getType();
            if (!(type instanceof GenericArrayType || type instanceof Class && ((Class<?>) type).isArray())) {
                return null;
            }
            Type componentType = $Gson$Types.getArrayComponentType(type);
            TypeAdapter<?> componentTypeAdapter = gson.getAdapter(TypeToken.get(componentType));
            return ArrayTypeAdapter(gson, componentTypeAdapter, $Gson$Types.getRawType(componentType));
        }
    }


    def __init__(self, context: "Gson", componentTypeAdapter: "TypeAdapter"["E"], componentType: type["E"]):
        ...


    def read(self, in: "JsonReader") -> "Object":
        ...


    def write(self, out: "JsonWriter", array: "Object") -> None:
        ...
