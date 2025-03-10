"""
Python module generated from Java source file org.yaml.snakeyaml.nodes.Node

Java source file obtained from artifact snakeyaml version 1.33

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml.comments import CommentLine
from org.yaml.snakeyaml.error import Mark
from org.yaml.snakeyaml.nodes import *
from typing import Any, Callable, Iterable, Tuple


class Node:
    """
    Base class for all nodes.
    
    The nodes form the node-graph described in the <a href="http://yaml.org/spec/1.1/">YAML
    Specification</a>.
    
    
    While loading, the node graph is usually created by the
    org.yaml.snakeyaml.composer.Composer, and later transformed into application specific
    Java classes by the classes from the org.yaml.snakeyaml.constructor package.
    """

    def __init__(self, tag: "Tag", startMark: "Mark", endMark: "Mark"):
        ...


    def getTag(self) -> "Tag":
        """
        Tag of this node.
        
        Every node has a tag assigned. The tag is either local or global.

        Returns
        - Tag of this node.
        """
        ...


    def getEndMark(self) -> "Mark":
        ...


    def getNodeId(self) -> "NodeId":
        """
        For error reporting.

        Returns
        - scalar, sequence, mapping

        See
        - "class variable 'id' in PyYAML"
        """
        ...


    def getStartMark(self) -> "Mark":
        ...


    def setTag(self, tag: "Tag") -> None:
        ...


    def equals(self, obj: "Object") -> bool:
        """
        Node is only equal to itself
        """
        ...


    def getType(self) -> type["Object"]:
        ...


    def setType(self, type: type["Object"]) -> None:
        ...


    def setTwoStepsConstruction(self, twoStepsConstruction: bool) -> None:
        ...


    def isTwoStepsConstruction(self) -> bool:
        """
        Indicates if this node must be constructed in two steps.
        
        Two-step construction is required whenever a node is a child (direct or indirect) of it self.
        That is, if a recursive structure is build using anchors and aliases.
        
        
        Set by org.yaml.snakeyaml.composer.Composer, used during the construction process.
        
        
        Only relevant during loading.

        Returns
        - `True` if the node is self referenced.
        """
        ...


    def hashCode(self) -> int:
        ...


    def useClassConstructor(self) -> bool:
        ...


    def setUseClassConstructor(self, useClassConstructor: "Boolean") -> None:
        ...


    def isResolved(self) -> bool:
        """
        Indicates if the tag was added by org.yaml.snakeyaml.resolver.Resolver.

        Returns
        - True if the tag of this node was resolved

        Deprecated
        - Since v1.22. Absent in immediately prior versions, but present previously. Restored
                    deprecated for backwards compatibility.
        """
        ...


    def getAnchor(self) -> str:
        ...


    def setAnchor(self, anchor: str) -> None:
        ...


    def getInLineComments(self) -> list["CommentLine"]:
        """
        The ordered list of in-line comments. The first of which appears at the end of the line
        respresent by this node. The rest are in the following lines, indented per the Spec to indicate
        they are continuation of the inline comment.

        Returns
        - the comment line list.
        """
        ...


    def setInLineComments(self, inLineComments: list["CommentLine"]) -> None:
        ...


    def getBlockComments(self) -> list["CommentLine"]:
        """
        The ordered list of blank lines and block comments (full line) that appear before this node.

        Returns
        - the comment line list.
        """
        ...


    def setBlockComments(self, blockComments: list["CommentLine"]) -> None:
        ...


    def getEndComments(self) -> list["CommentLine"]:
        """
        The ordered list of blank lines and block comments (full line) that appear AFTER this node.
        
        NOTE: these comment should occur only in the last node in a document, when walking the node
        tree "in order"

        Returns
        - the comment line list.
        """
        ...


    def setEndComments(self, endComments: list["CommentLine"]) -> None:
        ...
