"""
Python module generated from Java source file org.yaml.snakeyaml.TypeDescription

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Collections
from java.util import LinkedHashSet
from org.yaml.snakeyaml import *
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.internal import Logger
from org.yaml.snakeyaml.introspector import BeanAccess
from org.yaml.snakeyaml.introspector import Property
from org.yaml.snakeyaml.introspector import PropertySubstitute
from org.yaml.snakeyaml.introspector import PropertyUtils
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from typing import Any, Callable, Iterable, Tuple


class TypeDescription:
    """
    Provides additional runtime information necessary to create a custom Java instance.
    
    In general this class is thread-safe and can be used as a singleton, the only exception being the
    PropertyUtils field. A singleton PropertyUtils should be constructed and shared between all YAML
    Constructors used if a singleton TypeDescription is used, since Constructor sets its
    propertyUtils to the TypeDescription that is passed to it, hence you may end up in a situation
    when propertyUtils in TypeDescription is from different Constructor.
    """

    def __init__(self, clazz: type["Object"], tag: "Tag"):
        ...


    def __init__(self, clazz: type["Object"], tag: "Tag", impl: type[Any]):
        ...


    def __init__(self, clazz: type["Object"], tag: str):
        ...


    def __init__(self, clazz: type["Object"]):
        ...


    def __init__(self, clazz: type["Object"], impl: type[Any]):
        ...


    def getTag(self) -> "Tag":
        """
        Get tag which shall be used to load or dump the type (class).

        Returns
        - tag to be used. It may be a tag for Language-Independent Types
                (http://www.yaml.org/type/)
        """
        ...


    def getType(self) -> type["Object"]:
        """
        Get represented type (class)

        Returns
        - type (class) to be described.
        """
        ...


    def putListPropertyType(self, property: str, type: type["Object"]) -> None:
        """
        Specify that the property is a type-safe `List`.

        Arguments
        - property: name of the JavaBean property
        - type: class of List values
        """
        ...


    def putMapPropertyType(self, property: str, key: type["Object"], value: type["Object"]) -> None:
        """
        Specify that the property is a type-safe `Map`.

        Arguments
        - property: property name of this JavaBean
        - key: class of keys in Map
        - value: class of values in Map
        """
        ...


    def addPropertyParameters(self, pName: str, *classes: Tuple[type[Any], ...]) -> None:
        """
        Adds new substitute for property `pName` parameterized by `classes` to
        this `TypeDescription`. If `pName` has been added before - updates
        parameters with `classes`.

        Arguments
        - pName: - parameter name
        - classes: - parameterized by
        """
        ...


    def toString(self) -> str:
        ...


    def getProperty(self, name: str) -> "Property":
        ...


    def substituteProperty(self, pName: str, pType: type[Any], getter: str, setter: str, *argParams: Tuple[type[Any], ...]) -> None:
        """
        Adds property substitute for `pName`

        Arguments
        - pName: property name
        - pType: property type
        - getter: method name for getter
        - setter: method name for setter
        - argParams: actual types for parameterized type (List&lt;?&gt;, Map&lt;?&gt;)
        """
        ...


    def substituteProperty(self, substitute: "PropertySubstitute") -> None:
        ...


    def setPropertyUtils(self, propertyUtils: "PropertyUtils") -> None:
        ...


    def setIncludes(self, *propNames: Tuple[str, ...]) -> None:
        ...


    def setExcludes(self, *propNames: Tuple[str, ...]) -> None:
        ...


    def getProperties(self) -> set["Property"]:
        ...


    def setupPropertyType(self, key: str, valueNode: "Node") -> bool:
        ...


    def setProperty(self, targetBean: "Object", propertyName: str, value: "Object") -> bool:
        ...


    def newInstance(self, node: "Node") -> "Object":
        """
        This method should be overridden for TypeDescription implementations that are supposed to
        implement instantiation logic that is different from default one as implemented in YAML
        constructors. Note that even if you override this method, default filling of fields with
        variables from parsed YAML will still occur later.

        Arguments
        - node: - node to construct the instance from

        Returns
        - new instance
        """
        ...


    def newInstance(self, propertyName: str, node: "Node") -> "Object":
        ...


    def finalizeConstruction(self, obj: "Object") -> "Object":
        """
        Is invoked after entity is filled with values from deserialized YAML

        Arguments
        - obj: - deserialized entity

        Returns
        - postprocessed deserialized entity
        """
        ...
