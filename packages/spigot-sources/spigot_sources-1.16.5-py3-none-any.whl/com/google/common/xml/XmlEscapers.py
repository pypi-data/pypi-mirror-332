"""
Python module generated from Java source file com.google.common.xml.XmlEscapers

Java source file obtained from artifact guava version 21.0

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import Beta
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import Escaper
from com.google.common.escape import Escapers
from com.google.common.xml import *
from typing import Any, Callable, Iterable, Tuple


class XmlEscapers:
    """
    `Escaper` instances suitable for strings to be included in XML attribute values and
    elements' text contents. When possible, avoid manual escaping by using templating systems and
    high-level APIs that provide autoescaping. For example, consider
    <a href="http://www.xom.nu/">XOM</a> or <a href="http://www.jdom.org/">JDOM</a>.
    
    **Note:** Currently the escapers provided by this class do not escape any characters
    outside the ASCII character range. Unlike HTML escaping the XML escapers will not escape
    non-ASCII characters to their numeric entity replacements. These XML escapers provide the minimal
    level of escaping to ensure that the output can be safely included in a Unicode XML document.
    
    
    For details on the behavior of the escapers in this class, see sections
    <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#charsets">2.2</a> and
    <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#syntax">2.4</a> of the XML specification.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    @staticmethod
    def xmlContentEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes special characters in a string so it can
        safely be included in an XML document as element content. See section
        <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#syntax">2.4</a> of the XML specification.
        
        **Note:** Double and single quotes are not escaped, so it is **not safe** to use this
        escaper to escape attribute values. Use .xmlContentEscaper if the output can appear in
        element content or .xmlAttributeEscaper in attribute values.
        
        This escaper substitutes `0xFFFD` for non-whitespace control characters and the
        character values `0xFFFE` and `0xFFFF` which are not permitted in XML. For more
        detail see section <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#charsets">2.2</a> of
        the XML specification.
        
        This escaper does not escape non-ASCII characters to their numeric character references
        (NCR). Any non-ASCII characters appearing in the input will be preserved in the output.
        Specifically "\r" (carriage return) is preserved in the output, which may result in it being
        silently converted to "\n" when the XML is parsed.
        
        This escaper does not treat surrogate pairs specially and does not perform Unicode
        validation on its input.
        """
        ...


    @staticmethod
    def xmlAttributeEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes special characters in a string so it can
        safely be included in XML document as an attribute value. See section
        <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#AVNormalize">3.3.3</a> of the XML
        specification.
        
        This escaper substitutes `0xFFFD` for non-whitespace control characters and the
        character values `0xFFFE` and `0xFFFF` which are not permitted in XML. For more
        detail see section <a href="http://www.w3.org/TR/2008/REC-xml-20081126/#charsets">2.2</a> of
        the XML specification.
        
        This escaper does not escape non-ASCII characters to their numeric character references
        (NCR). However, horizontal tab `'\t'`, line feed `'\n'` and carriage return
        `'\r'` are escaped to a corresponding NCR `"&.x9;"`, `"&.xA;"`, and
        `"&.xD;"` respectively. Any other non-ASCII characters appearing in the input will be
        preserved in the output.
        
        This escaper does not treat surrogate pairs specially and does not perform Unicode
        validation on its input.
        """
        ...
