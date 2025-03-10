"""
Python module generated from Java source file org.yaml.snakeyaml.Yaml

Java source file obtained from artifact snakeyaml version 1.28

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.io import IOException
from java.io import InputStream
from java.io import Reader
from java.io import StringReader
from java.io import StringWriter
from java.io import Writer
from java.util import Iterator
from java.util import NoSuchElementException
from java.util.regex import Pattern
from org.yaml.snakeyaml import *
from org.yaml.snakeyaml.DumperOptions import FlowStyle
from org.yaml.snakeyaml.composer import Composer
from org.yaml.snakeyaml.constructor import BaseConstructor
from org.yaml.snakeyaml.constructor import Constructor
from org.yaml.snakeyaml.emitter import Emitable
from org.yaml.snakeyaml.emitter import Emitter
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.events import Event
from org.yaml.snakeyaml.introspector import BeanAccess
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.parser import Parser
from org.yaml.snakeyaml.parser import ParserImpl
from org.yaml.snakeyaml.reader import StreamReader
from org.yaml.snakeyaml.reader import UnicodeReader
from org.yaml.snakeyaml.representer import Representer
from org.yaml.snakeyaml.resolver import Resolver
from org.yaml.snakeyaml.serializer import Serializer
from typing import Any, Callable, Iterable, Tuple


class Yaml:
    """
    Public YAML interface. This class is not thread-safe. Which means that all the methods of the same
    instance can be called only by one thread.
    It is better to create an instance for every YAML stream.
    """

    def __init__(self):
        """
        Create Yaml instance.
        """
        ...


    def __init__(self, dumperOptions: "DumperOptions"):
        """
        Create Yaml instance.

        Arguments
        - dumperOptions: DumperOptions to configure outgoing objects
        """
        ...


    def __init__(self, loadingConfig: "LoaderOptions"):
        """
        Create Yaml instance.

        Arguments
        - loadingConfig: LoadingConfig to control load behavior
        """
        ...


    def __init__(self, representer: "Representer"):
        """
        Create Yaml instance.

        Arguments
        - representer: Representer to emit outgoing objects
        """
        ...


    def __init__(self, constructor: "BaseConstructor"):
        """
        Create Yaml instance.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        """
        ...


    def __init__(self, constructor: "BaseConstructor", representer: "Representer"):
        """
        Create Yaml instance.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        - representer: Representer to emit outgoing objects
        """
        ...


    def __init__(self, representer: "Representer", dumperOptions: "DumperOptions"):
        """
        Create Yaml instance. It is safe to create a few instances and use them
        in different Threads.

        Arguments
        - representer: Representer to emit outgoing objects
        - dumperOptions: DumperOptions to configure outgoing objects
        """
        ...


    def __init__(self, constructor: "BaseConstructor", representer: "Representer", dumperOptions: "DumperOptions"):
        """
        Create Yaml instance. It is safe to create a few instances and use them
        in different Threads.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        - representer: Representer to emit outgoing objects
        - dumperOptions: DumperOptions to configure outgoing objects
        """
        ...


    def __init__(self, constructor: "BaseConstructor", representer: "Representer", dumperOptions: "DumperOptions", loadingConfig: "LoaderOptions"):
        """
        Create Yaml instance. It is safe to create a few instances and use them
        in different Threads.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        - representer: Representer to emit outgoing objects
        - dumperOptions: DumperOptions to configure outgoing objects
        - loadingConfig: LoadingConfig to control load behavior
        """
        ...


    def __init__(self, constructor: "BaseConstructor", representer: "Representer", dumperOptions: "DumperOptions", resolver: "Resolver"):
        """
        Create Yaml instance. It is safe to create a few instances and use them
        in different Threads.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        - representer: Representer to emit outgoing objects
        - dumperOptions: DumperOptions to configure outgoing objects
        - resolver: Resolver to detect implicit type
        """
        ...


    def __init__(self, constructor: "BaseConstructor", representer: "Representer", dumperOptions: "DumperOptions", loadingConfig: "LoaderOptions", resolver: "Resolver"):
        """
        Create Yaml instance. It is safe to create a few instances and use them
        in different Threads.

        Arguments
        - constructor: BaseConstructor to construct incoming documents
        - representer: Representer to emit outgoing objects
        - dumperOptions: DumperOptions to configure outgoing objects
        - loadingConfig: LoadingConfig to control load behavior
        - resolver: Resolver to detect implicit type
        """
        ...


    def dump(self, data: "Object") -> str:
        """
        Serialize a Java object into a YAML String.

        Arguments
        - data: Java object to be Serialized to YAML

        Returns
        - YAML String
        """
        ...


    def represent(self, data: "Object") -> "Node":
        """
        Produce the corresponding representation tree for a given Object.

        Arguments
        - data: instance to build the representation tree for

        Returns
        - representation tree

        See
        - <a href="http://yaml.org/spec/1.1/.id859333">Figure 3.1. Processing
        Overview</a>
        """
        ...


    def dumpAll(self, data: Iterator["Object"]) -> str:
        """
        Serialize a sequence of Java objects into a YAML String.

        Arguments
        - data: Iterator with Objects

        Returns
        - YAML String with all the objects in proper sequence
        """
        ...


    def dump(self, data: "Object", output: "Writer") -> None:
        """
        Serialize a Java object into a YAML stream.

        Arguments
        - data: Java object to be serialized to YAML
        - output: stream to write to
        """
        ...


    def dumpAll(self, data: Iterator["Object"], output: "Writer") -> None:
        """
        Serialize a sequence of Java objects into a YAML stream.

        Arguments
        - data: Iterator with Objects
        - output: stream to write to
        """
        ...


    def dumpAs(self, data: "Object", rootTag: "Tag", flowStyle: "FlowStyle") -> str:
        """
        
        Serialize a Java object into a YAML string. Override the default root tag
        with `rootTag`.
        
        
        
        This method is similar to `Yaml.dump(data)` except that the
        root tag for the whole document is replaced with the given tag. This has
        two main uses.
        
        
        
        First, if the root tag is replaced with a standard YAML tag, such as
        `Tag.MAP`, then the object will be dumped as a map. The root
        tag will appear as `!!map`, or blank (implicit !!map).
        
        
        
        Second, if the root tag is replaced by a different custom tag, then the
        document appears to be a different type when loaded. For example, if an
        instance of MyClass is dumped with the tag !!YourClass, then it will be
        handled as an instance of YourClass when loaded.

        Arguments
        - data: Java object to be serialized to YAML
        - rootTag: the tag for the whole YAML document. The tag should be Tag.MAP
                         for a JavaBean to make the tag disappear (to use implicit tag
                         !!map). If `null` is provided then the standard tag
                         with the full class name is used.
        - flowStyle: flow style for the whole document. See Chapter 10. Collection
                         Styles http://yaml.org/spec/1.1/#id930798. If
                         `null` is provided then the flow style from
                         DumperOptions is used.

        Returns
        - YAML String
        """
        ...


    def dumpAsMap(self, data: "Object") -> str:
        """
        
        Serialize a Java object into a YAML string. Override the default root tag
        with `Tag.MAP`.
        
        
        This method is similar to `Yaml.dump(data)` except that the
        root tag for the whole document is replaced with `Tag.MAP` tag
        (implicit !!map).
        
        
        Block Mapping is used as the collection style. See 10.2.2. Block Mappings
        (http://yaml.org/spec/1.1/#id934537)

        Arguments
        - data: Java object to be serialized to YAML

        Returns
        - YAML String
        """
        ...


    def serialize(self, node: "Node", output: "Writer") -> None:
        """
        Serialize (dump) a YAML node into a YAML stream.

        Arguments
        - node: YAML node to be serialized to YAML
        - output: stream to write to
        """
        ...


    def serialize(self, data: "Node") -> list["Event"]:
        """
        Serialize the representation tree into Events.

        Arguments
        - data: representation tree

        Returns
        - Event list

        See
        - <a href="http://yaml.org/spec/1.1/.id859333">Processing Overview</a>
        """
        ...


    def load(self, yaml: str) -> "T":
        """
        Parse the only YAML document in a String and produce the corresponding
        Java object. (Because the encoding in known BOM is not respected.)
        
        Type `<T>`: the class of the instance to be created

        Arguments
        - yaml: YAML data to load from (BOM must not be present)

        Returns
        - parsed object
        """
        ...


    def load(self, io: "InputStream") -> "T":
        """
        Parse the only YAML document in a stream and produce the corresponding
        Java object.
        
        Type `<T>`: the class of the instance to be created

        Arguments
        - io: data to load from (BOM is respected to detect encoding and removed from the data)

        Returns
        - parsed object
        """
        ...


    def load(self, io: "Reader") -> "T":
        """
        Parse the only YAML document in a stream and produce the corresponding
        Java object.
        
        Type `<T>`: the class of the instance to be created

        Arguments
        - io: data to load from (BOM must not be present)

        Returns
        - parsed object
        """
        ...


    def loadAs(self, io: "Reader", type: type["T"]) -> "T":
        """
        Parse the only YAML document in a stream and produce the corresponding
        Java object.
        
        Type `<T>`: Class is defined by the second argument

        Arguments
        - io: data to load from (BOM must not be present)
        - type: Class of the object to be created

        Returns
        - parsed object
        """
        ...


    def loadAs(self, yaml: str, type: type["T"]) -> "T":
        """
        Parse the only YAML document in a String and produce the corresponding
        Java object. (Because the encoding in known BOM is not respected.)
        
        Type `<T>`: Class is defined by the second argument

        Arguments
        - yaml: YAML data to load from (BOM must not be present)
        - type: Class of the object to be created

        Returns
        - parsed object
        """
        ...


    def loadAs(self, input: "InputStream", type: type["T"]) -> "T":
        """
        Parse the only YAML document in a stream and produce the corresponding
        Java object.
        
        Type `<T>`: Class is defined by the second argument

        Arguments
        - input: data to load from (BOM is respected to detect encoding and removed from the data)
        - type: Class of the object to be created

        Returns
        - parsed object
        """
        ...


    def loadAll(self, yaml: "Reader") -> Iterable["Object"]:
        """
        Parse all YAML documents in the Reader and produce corresponding Java
        objects. The documents are parsed only when the iterator is invoked.

        Arguments
        - yaml: YAML data to load from (BOM must not be present)

        Returns
        - an Iterable over the parsed Java objects in this String in proper
        sequence
        """
        ...


    def loadAll(self, yaml: str) -> Iterable["Object"]:
        """
        Parse all YAML documents in a String and produce corresponding Java
        objects. (Because the encoding in known BOM is not respected.) The
        documents are parsed only when the iterator is invoked.

        Arguments
        - yaml: YAML data to load from (BOM must not be present)

        Returns
        - an Iterable over the parsed Java objects in this String in proper
        sequence
        """
        ...


    def loadAll(self, yaml: "InputStream") -> Iterable["Object"]:
        """
        Parse all YAML documents in a stream and produce corresponding Java
        objects. The documents are parsed only when the iterator is invoked.

        Arguments
        - yaml: YAML data to load from (BOM is respected to detect encoding and removed from the data)

        Returns
        - an Iterable over the parsed Java objects in this stream in proper
        sequence
        """
        ...


    def compose(self, yaml: "Reader") -> "Node":
        """
        Parse the first YAML document in a stream and produce the corresponding
        representation tree. (This is the opposite of the represent() method)

        Arguments
        - yaml: YAML document

        Returns
        - parsed root Node for the specified YAML document

        See
        - <a href="http://yaml.org/spec/1.1/.id859333">Figure 3.1. Processing
        Overview</a>
        """
        ...


    def composeAll(self, yaml: "Reader") -> Iterable["Node"]:
        """
        Parse all YAML documents in a stream and produce corresponding
        representation trees.

        Arguments
        - yaml: stream of YAML documents

        Returns
        - parsed root Nodes for all the specified YAML documents

        See
        - <a href="http://yaml.org/spec/1.1/.id859333">Processing Overview</a>
        """
        ...


    def addImplicitResolver(self, tag: "Tag", regexp: "Pattern", first: str) -> None:
        """
        Add an implicit scalar detector. If an implicit scalar value matches the
        given regexp, the corresponding tag is assigned to the scalar.

        Arguments
        - tag: tag to assign to the node
        - regexp: regular expression to match against
        - first: a sequence of possible initial characters or null (which means
                      any).
        """
        ...


    def toString(self) -> str:
        ...


    def getName(self) -> str:
        """
        Get a meaningful name. It simplifies debugging in a multi-threaded
        environment. If nothing is set explicitly the address of the instance is
        returned.

        Returns
        - human readable name
        """
        ...


    def setName(self, name: str) -> None:
        """
        Set a meaningful name to be shown in toString()

        Arguments
        - name: human readable name
        """
        ...


    def parse(self, yaml: "Reader") -> Iterable["Event"]:
        """
        Parse a YAML stream and produce parsing events.

        Arguments
        - yaml: YAML document(s)

        Returns
        - parsed events

        See
        - <a href="http://yaml.org/spec/1.1/.id859333">Processing Overview</a>
        """
        ...


    def setBeanAccess(self, beanAccess: "BeanAccess") -> None:
        ...


    def addTypeDescription(self, td: "TypeDescription") -> None:
        ...
