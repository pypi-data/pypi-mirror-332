"""
Python module generated from Java source file org.yaml.snakeyaml.DumperOptions

Java source file obtained from artifact snakeyaml version 1.27

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from enum import Enum
from java.util import TimeZone
from org.yaml.snakeyaml import *
from org.yaml.snakeyaml.emitter import Emitter
from org.yaml.snakeyaml.error import YAMLException
from org.yaml.snakeyaml.serializer import AnchorGenerator
from org.yaml.snakeyaml.serializer import NumberAnchorGenerator
from typing import Any, Callable, Iterable, Tuple


class DumperOptions:

    def isAllowUnicode(self) -> bool:
        ...


    def setAllowUnicode(self, allowUnicode: bool) -> None:
        """
        Specify whether to emit non-ASCII printable Unicode characters.
        The default value is True.
        When set to False then printable non-ASCII characters (Cyrillic, Chinese etc)
        will be not printed but escaped (to support ASCII terminals)

        Arguments
        - allowUnicode: if allowUnicode is False then all non-ASCII characters are
                   escaped
        """
        ...


    def getDefaultScalarStyle(self) -> "ScalarStyle":
        ...


    def setDefaultScalarStyle(self, defaultStyle: "ScalarStyle") -> None:
        """
        Set default style for scalars. See YAML 1.1 specification, 2.3 Scalars
        (http://yaml.org/spec/1.1/#id858081)

        Arguments
        - defaultStyle: set the style for all scalars
        """
        ...


    def setIndent(self, indent: int) -> None:
        ...


    def getIndent(self) -> int:
        ...


    def setIndicatorIndent(self, indicatorIndent: int) -> None:
        """
        Set number of white spaces to use for the sequence indicator '-'

        Arguments
        - indicatorIndent: value to be used as indent
        """
        ...


    def getIndicatorIndent(self) -> int:
        ...


    def getIndentWithIndicator(self) -> bool:
        ...


    def setIndentWithIndicator(self, indentWithIndicator: bool) -> None:
        """
        Set to True to add the indent for sequences to the general indent

        Arguments
        - indentWithIndicator: - True when indent for sequences is added to general
        """
        ...


    def setVersion(self, version: "Version") -> None:
        ...


    def getVersion(self) -> "Version":
        ...


    def setCanonical(self, canonical: bool) -> None:
        """
        Force the emitter to produce a canonical YAML document.

        Arguments
        - canonical: True produce canonical YAML document
        """
        ...


    def isCanonical(self) -> bool:
        ...


    def setPrettyFlow(self, prettyFlow: bool) -> None:
        """
        Force the emitter to produce a pretty YAML document when using the flow
        style.

        Arguments
        - prettyFlow: True produce pretty flow YAML document
        """
        ...


    def isPrettyFlow(self) -> bool:
        ...


    def setWidth(self, bestWidth: int) -> None:
        """
        Specify the preferred width to emit scalars. When the scalar
        representation takes more then the preferred with the scalar will be
        split into a few lines. The default is 80.

        Arguments
        - bestWidth: the preferred width for scalars.
        """
        ...


    def getWidth(self) -> int:
        ...


    def setSplitLines(self, splitLines: bool) -> None:
        """
        Specify whether to split lines exceeding preferred width for
        scalars. The default is True.

        Arguments
        - splitLines: whether to split lines exceeding preferred width for scalars.
        """
        ...


    def getSplitLines(self) -> bool:
        ...


    def getLineBreak(self) -> "LineBreak":
        ...


    def setDefaultFlowStyle(self, defaultFlowStyle: "FlowStyle") -> None:
        ...


    def getDefaultFlowStyle(self) -> "FlowStyle":
        ...


    def setLineBreak(self, lineBreak: "LineBreak") -> None:
        """
        Specify the line break to separate the lines. It is platform specific:
        Windows - "\r\n", old MacOS - "\r", Unix - "\n". The default value is the
        one for Unix.

        Arguments
        - lineBreak: to be used for the input
        """
        ...


    def isExplicitStart(self) -> bool:
        ...


    def setExplicitStart(self, explicitStart: bool) -> None:
        ...


    def isExplicitEnd(self) -> bool:
        ...


    def setExplicitEnd(self, explicitEnd: bool) -> None:
        ...


    def getTags(self) -> dict[str, str]:
        ...


    def setTags(self, tags: dict[str, str]) -> None:
        ...


    def isAllowReadOnlyProperties(self) -> bool:
        """
        Report whether read-only JavaBean properties (the ones without setters)
        should be included in the YAML document

        Returns
        - False when read-only JavaBean properties are not emitted
        """
        ...


    def setAllowReadOnlyProperties(self, allowReadOnlyProperties: bool) -> None:
        """
        Set to True to include read-only JavaBean properties (the ones without
        setters) in the YAML document. By default these properties are not
        included to be able to parse later the same JavaBean.

        Arguments
        - allowReadOnlyProperties: - True to dump read-only JavaBean properties
        """
        ...


    def getTimeZone(self) -> "TimeZone":
        ...


    def setTimeZone(self, timeZone: "TimeZone") -> None:
        """
        Set the timezone to be used for Date. If set to `null` UTC is
        used.

        Arguments
        - timeZone: for created Dates or null to use UTC
        """
        ...


    def getAnchorGenerator(self) -> "AnchorGenerator":
        ...


    def setAnchorGenerator(self, anchorGenerator: "AnchorGenerator") -> None:
        ...


    def getMaxSimpleKeyLength(self) -> int:
        ...


    def setMaxSimpleKeyLength(self, maxSimpleKeyLength: int) -> None:
        """
        Define max key length to use simple key (without '?')
        More info https://yaml.org/spec/1.1/#id934537

        Arguments
        - maxSimpleKeyLength: - the limit after which the key gets explicit key indicator '?'
        """
        ...


    def getNonPrintableStyle(self) -> "NonPrintableStyle":
        ...


    def setNonPrintableStyle(self, style: "NonPrintableStyle") -> None:
        """
        When String contains non-printable characters SnakeYAML convert it to binary data with the !!binary tag.
        Set this to ESCAPE to keep the !!str tag and escape the non-printable chars with \\x or \\u

        Arguments
        - style: ESCAPE to force SnakeYAML to keep !!str tag for non-printable data
        """
        ...


    class ScalarStyle(Enum):
        """
        YAML provides a rich set of scalar styles. Block scalar styles include
        the literal style and the folded style; flow scalar styles include the
        plain style and two quoted styles, the single-quoted style and the
        double-quoted style. These styles offer a range of trade-offs between
        expressive power and readability.

        See
        - <a href="http://yaml.org/spec/1.1/.id858081">2.3. Scalars</a>
        """

        DOUBLE_QUOTED = ('"')
        SINGLE_QUOTED = ('\'')
        LITERAL = ('|')
        FOLDED = ('>')
        PLAIN = (None)


        def getChar(self) -> "Character":
            ...


        def toString(self) -> str:
            ...


        @staticmethod
        def createStyle(style: "Character") -> "ScalarStyle":
            ...


    class FlowStyle(Enum):
        """
        Block styles use indentation to denote nesting and scope within the
        document. In contrast, flow styles rely on explicit indicators to denote
        nesting and scope.

        See
        - <a href="http://www.yaml.org/spec/current.html.id2509255">3.2.3.1.
             Node Styles (http://yaml.org/spec/1.1)</a>
        """

        FLOW = (True)
        BLOCK = (False)
        AUTO = (None)


        @staticmethod
        def fromBoolean(flowStyle: "Boolean") -> "FlowStyle":
            ...


        def getStyleBoolean(self) -> "Boolean":
            ...


        def toString(self) -> str:
            ...


    class LineBreak(Enum):
        """
        Platform dependent line break.
        """

        WIN = ("\r\n")
        MAC = ("\r")
        UNIX = ("\n")


        def getString(self) -> str:
            ...


        def toString(self) -> str:
            ...


        @staticmethod
        def getPlatformLineBreak() -> "LineBreak":
            ...


    class Version(Enum):
        """
        Specification version. Currently supported 1.0 and 1.1
        """

        V1_0 = (Integer[] { 1, 0 })
        V1_1 = (Integer[] { 1, 1 })


        def major(self) -> int:
            ...


        def minor(self) -> int:
            ...


        def getRepresentation(self) -> str:
            ...


        def toString(self) -> str:
            ...


    class NonPrintableStyle(Enum):

        BINARY = 0
        """
        Transform String to binary if it contains non-printable characters
        """
        ESCAPE = 1
        """
        Escape non-printable characters
        """
