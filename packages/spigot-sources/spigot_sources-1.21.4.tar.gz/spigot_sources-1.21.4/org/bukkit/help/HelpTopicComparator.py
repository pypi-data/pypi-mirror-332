"""
Python module generated from Java source file org.bukkit.help.HelpTopicComparator

Java source file obtained from artifact spigot-api version 1.21.4-R0.1-20250303.102353-42

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from java.util import Comparator
from org.bukkit.help import *
from typing import Any, Callable, Iterable, Tuple


class HelpTopicComparator(Comparator):
    """
    Used to impose a custom total ordering on help topics.
    
    All topics are listed in alphabetic order, but topics that start with a
    slash come after topics that don't.
    """

    @staticmethod
    def topicNameComparatorInstance() -> "TopicNameComparator":
        ...


    @staticmethod
    def helpTopicComparatorInstance() -> "HelpTopicComparator":
        ...


    def compare(self, lhs: "HelpTopic", rhs: "HelpTopic") -> int:
        ...


    class TopicNameComparator(Comparator):

        def compare(self, lhs: str, rhs: str) -> int:
            ...
