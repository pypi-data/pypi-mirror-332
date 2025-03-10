"""
Python module generated from Java source file org.yaml.snakeyaml.LoaderOptions

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from org.yaml.snakeyaml import *
from typing import Any, Callable, Iterable, Tuple


class LoaderOptions:

    def isAllowDuplicateKeys(self) -> bool:
        ...


    def setAllowDuplicateKeys(self, allowDuplicateKeys: bool) -> None:
        """
        Allow/Reject duplicate map keys in the YAML file.
        
        Default is to allow.
        
        YAML 1.1 is slightly vague around duplicate entries in the YAML file. The
        best reference is <a href="http://www.yaml.org/spec/1.1/#id862121">
        3.2.1.3. Nodes Comparison</a> where it hints that a duplicate map key is
        an error.
        
        For future reference, YAML spec 1.2 is clear. The keys MUST be unique.
        <a href="http://www.yaml.org/spec/1.2/spec.html#id2759572">1.3. Relation
        to JSON</a>

        Arguments
        - allowDuplicateKeys: False to reject duplicate mapping keys
        """
        ...


    def isWrappedToRootException(self) -> bool:
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
        ...


    def setMaxAliasesForCollections(self, maxAliasesForCollections: int) -> None:
        """
        Restrict the amount of aliases for collections (sequences and mappings) to avoid https://en.wikipedia.org/wiki/Billion_laughs_attack

        Arguments
        - maxAliasesForCollections: set max allowed value (50 by default)
        """
        ...


    def setAllowRecursiveKeys(self, allowRecursiveKeys: bool) -> None:
        """
        Allow recursive keys for mappings. By default it is not allowed.
        This setting only prevents the case when the key is the value. If the key is only a part of the value
        (the value is a sequence or a mapping) then this case is not recognized and always allowed.

        Arguments
        - allowRecursiveKeys: - False to disable recursive keys
        """
        ...


    def getAllowRecursiveKeys(self) -> bool:
        ...
