"""
Python module generated from Java source file org.yaml.snakeyaml.DumperOptions

Java source file obtained from artifact snakeyaml version 1.33

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
    """
    Configuration for serialisation
    """

    def isAllowUnicode(self) -> bool:
        """
        getter

        Returns
        - False when non-ASCII is escaped
        """
        ...


    def setAllowUnicode(self, allowUnicode: bool) -> None:
        """
        Specify whether to emit non-ASCII printable Unicode characters. The default value is True. When
        set to False then printable non-ASCII characters (Cyrillic, Chinese etc) will be not printed
        but escaped (to support ASCII terminals)

        Arguments
        - allowUnicode: if allowUnicode is False then all non-ASCII characters are escaped
        """
        ...


    def getDefaultScalarStyle(self) -> "ScalarStyle":
        """
        getter

        Returns
        - scalar style
        """
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
        """
        Define indentation. Must be within the limits (1-10)

        Arguments
        - indent: number of spaces to serve as indentation
        """
        ...


    def getIndent(self) -> int:
        """
        getter

        Returns
        - indent
        """
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
        """
        Of no use - it is better not to include YAML version as the directive

        Arguments
        - version: 1.0 or 1.1
        """
        ...


    def getVersion(self) -> "Version":
        """
        getter

        Returns
        - the expected version
        """
        ...


    def setCanonical(self, canonical: bool) -> None:
        """
        Force the emitter to produce a canonical YAML document.

        Arguments
        - canonical: True produce canonical YAML document
        """
        ...


    def isCanonical(self) -> bool:
        """
        getter

        Returns
        - True when well established format should be dumped
        """
        ...


    def setPrettyFlow(self, prettyFlow: bool) -> None:
        """
        Force the emitter to produce a pretty YAML document when using the flow style.

        Arguments
        - prettyFlow: True produce pretty flow YAML document
        """
        ...


    def isPrettyFlow(self) -> bool:
        """
        getter

        Returns
        - True for pretty style
        """
        ...


    def setWidth(self, bestWidth: int) -> None:
        """
        Specify the preferred width to emit scalars. When the scalar representation takes more then the
        preferred with the scalar will be split into a few lines. The default is 80.

        Arguments
        - bestWidth: the preferred width for scalars.
        """
        ...


    def getWidth(self) -> int:
        """
        getter

        Returns
        - the preferred width for scalars
        """
        ...


    def setSplitLines(self, splitLines: bool) -> None:
        """
        Specify whether to split lines exceeding preferred width for scalars. The default is True.

        Arguments
        - splitLines: whether to split lines exceeding preferred width for scalars.
        """
        ...


    def getSplitLines(self) -> bool:
        """
        getter

        Returns
        - True when to split lines exceeding preferred width for scalars
        """
        ...


    def getLineBreak(self) -> "LineBreak":
        """
        getter

        Returns
        - line break to separate lines
        """
        ...


    def setDefaultFlowStyle(self, defaultFlowStyle: "FlowStyle") -> None:
        """
        setter

        Arguments
        - defaultFlowStyle: - enum for the flow style
        """
        ...


    def getDefaultFlowStyle(self) -> "FlowStyle":
        """
        getter

        Returns
        - flow style for collections
        """
        ...


    def setLineBreak(self, lineBreak: "LineBreak") -> None:
        """
        Specify the line break to separate the lines. It is platform specific: Windows - "\r\n", old
        MacOS - "\r", Unix - "\n". The default value is the one for Unix.

        Arguments
        - lineBreak: to be used for the input
        """
        ...


    def isExplicitStart(self) -> bool:
        """
        getter

        Returns
        - True when '---' must be printed
        """
        ...


    def setExplicitStart(self, explicitStart: bool) -> None:
        """
        setter - require explicit '...'

        Arguments
        - explicitStart: - True to emit '---'
        """
        ...


    def isExplicitEnd(self) -> bool:
        """
        getter

        Returns
        - True when '...' must be printed
        """
        ...


    def setExplicitEnd(self, explicitEnd: bool) -> None:
        """
        setter - require explicit '...'

        Arguments
        - explicitEnd: - True to emit '...'
        """
        ...


    def getTags(self) -> dict[str, str]:
        """
        getter

        Returns
        - previously defined tag directives
        """
        ...


    def setTags(self, tags: dict[str, str]) -> None:
        """
        setter

        Arguments
        - tags: - tag directives for the YAML document
        """
        ...


    def isAllowReadOnlyProperties(self) -> bool:
        """
        Report whether read-only JavaBean properties (the ones without setters) should be included in
        the YAML document

        Returns
        - False when read-only JavaBean properties are not emitted
        """
        ...


    def setAllowReadOnlyProperties(self, allowReadOnlyProperties: bool) -> None:
        """
        Set to True to include read-only JavaBean properties (the ones without setters) in the YAML
        document. By default these properties are not included to be able to parse later the same
        JavaBean.

        Arguments
        - allowReadOnlyProperties: - True to dump read-only JavaBean properties
        """
        ...


    def getTimeZone(self) -> "TimeZone":
        """
        getter

        Returns
        - timezone to be used to emit Date
        """
        ...


    def setTimeZone(self, timeZone: "TimeZone") -> None:
        """
        Set the timezone to be used for Date. If set to `null` UTC is used.

        Arguments
        - timeZone: for created Dates or null to use UTC
        """
        ...


    def getAnchorGenerator(self) -> "AnchorGenerator":
        """
        getter

        Returns
        - generator to create anchor names
        """
        ...


    def setAnchorGenerator(self, anchorGenerator: "AnchorGenerator") -> None:
        """
        Provide a custom generator

        Arguments
        - anchorGenerator: - the way to create custom anchors
        """
        ...


    def getMaxSimpleKeyLength(self) -> int:
        ...


    def setMaxSimpleKeyLength(self, maxSimpleKeyLength: int) -> None:
        """
        Define max key length to use simple key (without '?') More info
        https://yaml.org/spec/1.1/#id934537

        Arguments
        - maxSimpleKeyLength: - the limit after which the key gets explicit key indicator '?'
        """
        ...


    def setProcessComments(self, processComments: bool) -> None:
        """
        Set the comment processing. By default, comments are ignored.

        Arguments
        - processComments: `True` to process; `False` to ignore
        """
        ...


    def isProcessComments(self) -> bool:
        """
        getter

        Returns
        - True when comments are not ignored and can be used after composing a Node
        """
        ...


    def getNonPrintableStyle(self) -> "NonPrintableStyle":
        ...


    def setNonPrintableStyle(self, style: "NonPrintableStyle") -> None:
        """
        When String contains non-printable characters SnakeYAML convert it to binary data with the
        !!binary tag. Set this to ESCAPE to keep the !!str tag and escape the non-printable chars with
        \\x or \\u

        Arguments
        - style: ESCAPE to force SnakeYAML to keep !!str tag for non-printable data
        """
        ...


    class ScalarStyle(Enum):
        """
        YAML provides a rich set of scalar styles. Block scalar styles include the literal style and
        the folded style; flow scalar styles include the plain style and two quoted styles, the
        single-quoted style and the double-quoted style. These styles offer a range of trade-offs
        between expressive power and readability.

        See
        - <a href="http://yaml.org/spec/1.1/.id858081">2.3. Scalars</a>
        """

        DOUBLE_QUOTED = ('"')
        """
        Double quoted scalar
        """
        SINGLE_QUOTED = ('\'')
        """
        Single quoted scalar
        """
        LITERAL = ('|')
        """
        Literal scalar
        """
        FOLDED = ('>')
        """
        Folded scalar
        """
        PLAIN = (None)
        """
        Plain scalar
        """


        def getChar(self) -> "Character":
            """
            getter

            Returns
            - the char behind the style
            """
            ...


        def toString(self) -> str:
            """
            getter

            Returns
            - for humans
            """
            ...


        @staticmethod
        def createStyle(style: "Character") -> "ScalarStyle":
            """
            Create

            Arguments
            - style: - source char

            Returns
            - parsed style
            """
            ...


    class FlowStyle(Enum):
        """
        Block styles use indentation to denote nesting and scope within the document. In contrast, flow
        styles rely on explicit indicators to denote nesting and scope.

        See
        - <a href="http://www.yaml.org/spec/current.html.id2509255">3.2.3.1. Node Styles
             (http://yaml.org/spec/1.1)</a>
        """

        FLOW = (True)
        """
        Flow style
        """
        BLOCK = (False)
        """
        Block style
        """
        AUTO = (None)
        """
        Auto (first block, than flow)
        """


        @staticmethod
        def fromBoolean(flowStyle: "Boolean") -> "FlowStyle":
            """
            Convenience for legacy constructors that took Boolean arguments since replaced by
            FlowStyle. Introduced in v1.22 but only to support that for backwards compatibility.

            Deprecated
            - Since restored in v1.22. Use the FlowStyle constants in your code
                        instead.
            """
            ...


        def getStyleBoolean(self) -> "Boolean":
            """
            getter

            Returns
            - bbolean value

            Deprecated
            - use enum instead
            """
            ...


        def toString(self) -> str:
            ...


    class LineBreak(Enum):
        """
        Platform dependent line break.
        """

        WIN = ("\r\n")
        """
        Windows
        """
        MAC = ("\r")
        """
        Old Mac (should not be used !)
        """
        UNIX = ("\n")
        """
        Linux and Mac
        """


        def getString(self) -> str:
            """
            getter

            Returns
            - the break
            """
            ...


        def toString(self) -> str:
            """
            for humans

            Returns
            - representation
            """
            ...


        @staticmethod
        def getPlatformLineBreak() -> "LineBreak":
            """
            Get the line break used by the current Operating System

            Returns
            - detected line break
            """
            ...


    class Version(Enum):
        """
        Specification version. Currently supported 1.0 and 1.1
        """

        V1_0 = (Integer[] { 1, 0 })
        """
        1.0
        """
        V1_1 = (Integer[] { 1, 1 })
        """
        1.1
        """


        def major(self) -> int:
            """
            getter

            Returns
            - major part (always 1)
            """
            ...


        def minor(self) -> int:
            """
            Minor part (0 or 1)

            Returns
            - 0 or 1
            """
            ...


        def getRepresentation(self) -> str:
            """
            getter

            Returns
            - representation for serialisation
            """
            ...


        def toString(self) -> str:
            """
            getter

            Returns
            - for humans
            """
            ...


    class NonPrintableStyle(Enum):
        """
        the way to serialize non-printable
        """

        BINARY = 0
        """
        Transform String to binary if it contains non-printable characters
        """
        ESCAPE = 1
        """
        Escape non-printable characters
        """
