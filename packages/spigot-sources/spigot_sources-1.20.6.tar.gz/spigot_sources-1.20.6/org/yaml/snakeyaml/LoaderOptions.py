"""
Python module generated from Java source file org.yaml.snakeyaml.LoaderOptions

Java source file obtained from artifact snakeyaml version 2.2

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import *
from org.yaml.snakeyaml.inspector import TagInspector
from org.yaml.snakeyaml.inspector import UnTrustedTagInspector
from typing import Any, Callable, Iterable, Tuple


class LoaderOptions:
    """
    Configuration for loading
    """

    def isAllowDuplicateKeys(self) -> bool:
        """
        getter

        Returns
        - True when duplicate keys in mapping allowed (the latter overrides the former)
        """
        ...


    def setAllowDuplicateKeys(self, allowDuplicateKeys: bool) -> None:
        """
        Allow/Reject duplicate map keys in the YAML file.
        
        Default is to allow.
        
        YAML 1.1 is slightly vague around duplicate entries in the YAML file. The best reference is
        <a href="http://www.yaml.org/spec/1.1/#id862121"> 3.2.1.3. Nodes Comparison</a> where it hints
        that a duplicate map key is an error.
        
        For future reference, YAML spec 1.2 is clear. The keys MUST be unique.
        <a href="http://www.yaml.org/spec/1.2/spec.html#id2759572">1.3. Relation to JSON</a>

        Arguments
        - allowDuplicateKeys: False to reject duplicate mapping keys
        """
        ...


    def isWrappedToRootException(self) -> bool:
        """
        getter

        Returns
        - True when wrapped
        """
        ...


    def setWrappedToRootException(self, wrappedToRootException: bool) -> None:
        """
        Wrap runtime exception to YAMLException during parsing or leave them as they are
        
        Default is to leave original exceptions

        Arguments
        - wrappedToRootException: - True to convert runtime exception to YAMLException
        """
        ...


    def getMaxAliasesForCollections(self) -> int:
        """
        getter

        Returns
        - show the limit
        """
        ...


    def setMaxAliasesForCollections(self, maxAliasesForCollections: int) -> None:
        """
        Restrict the amount of aliases for collections (sequences and mappings) to avoid
        https://en.wikipedia.org/wiki/Billion_laughs_attack

        Arguments
        - maxAliasesForCollections: set max allowed value (50 by default)
        """
        ...


    def getAllowRecursiveKeys(self) -> bool:
        """
        getter

        Returns
        - when recursive keys are allowed (the document should be trusted)
        """
        ...


    def setAllowRecursiveKeys(self, allowRecursiveKeys: bool) -> None:
        """
        Allow recursive keys for mappings. By default, it is not allowed. This setting only prevents
        the case when the key is the value. If the key is only a part of the value (the value is a
        sequence or a mapping) then this case is not recognized and always allowed.

        Arguments
        - allowRecursiveKeys: - False to disable recursive keys
        """
        ...


    def isProcessComments(self) -> bool:
        """
        getter

        Returns
        - comments are kept in Node
        """
        ...


    def setProcessComments(self, processComments: bool) -> "LoaderOptions":
        """
        Set the comment processing. By default, comments are ignored.

        Arguments
        - processComments: `True` to process; `False` to ignore

        Returns
        - applied options
        """
        ...


    def isEnumCaseSensitive(self) -> bool:
        """
        getter

        Returns
        - True when parsing enum case-sensitive
        """
        ...


    def setEnumCaseSensitive(self, enumCaseSensitive: bool) -> None:
        """
        Disables or enables case sensitivity during construct enum constant from string value Default
        is False.

        Arguments
        - enumCaseSensitive: - True to set enum case-sensitive, False the reverse
        """
        ...


    def getNestingDepthLimit(self) -> int:
        """
        getter

        Returns
        - the limit
        """
        ...


    def setNestingDepthLimit(self, nestingDepthLimit: int) -> None:
        """
        Set max depth of nested collections. When the limit is exceeded an exception is thrown.
        Aliases/Anchors are not counted. This is to prevent a DoS attack

        Arguments
        - nestingDepthLimit: - depth to be accepted (50 by default)
        """
        ...


    def getCodePointLimit(self) -> int:
        """
        getter

        Returns
        - max code points in the input document
        """
        ...


    def setCodePointLimit(self, codePointLimit: int) -> None:
        """
        The max amount of code points for every input YAML document in the stream. Please be aware that
        byte limit depends on the encoding.

        Arguments
        - codePointLimit: - the max allowed size of a single YAML document in a stream
        """
        ...


    def getTagInspector(self) -> "TagInspector":
        ...


    def setTagInspector(self, tagInspector: "TagInspector") -> None:
        ...
