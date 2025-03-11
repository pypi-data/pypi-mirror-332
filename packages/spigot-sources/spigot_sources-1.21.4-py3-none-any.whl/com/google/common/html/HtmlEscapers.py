"""
Python module generated from Java source file com.google.common.html.HtmlEscapers

Java source file obtained from artifact guava version 33.3.1-jre

Because this Python module is automatically generated, it may contain errors
and/or code that cannot be parsed. Please report these issues at
https://github.com/magicmq/docs-translator/issues
"""
from com.google.common.annotations import GwtCompatible
from com.google.common.escape import Escaper
from com.google.common.escape import Escapers
from com.google.common.html import *
from typing import Any, Callable, Iterable, Tuple


class HtmlEscapers:
    """
    `Escaper` instances suitable for strings to be included in HTML attribute values and
    *most* elements' text contents. When possible, avoid manual escaping by using templating
    systems and high-level APIs that provide autoescaping.
    One Google-authored templating system available for external use is <a
    href="https://developers.google.com/closure/templates/">Closure Templates</a>.
    
    HTML escaping is particularly tricky: For example, <a
    href="https://www.w3.org/TR/html4/types.html#h-6.2">some elements' text contents must not be HTML
    escaped</a>. As a result, it is impossible to escape an HTML document correctly without
    domain-specific knowledge beyond what `HtmlEscapers` provides. We strongly encourage the
    use of HTML templating systems.

    Author(s)
    - David Beaumont

    Since
    - 15.0
    """

    @staticmethod
    def htmlEscaper() -> "Escaper":
        """
        Returns an Escaper instance that escapes HTML metacharacters as specified by <a
        href="http://www.w3.org/TR/html4/">HTML 4.01</a>. The resulting strings can be used both in
        attribute values and in *most* elements' text contents, provided that the HTML
        document's character encoding can encode any non-ASCII code points in the input (as UTF-8 and
        other Unicode encodings can).
        
        **Note:** This escaper only performs minimal escaping to make content structurally
        compatible with HTML. Specifically, it does not perform entity replacement (symbolic or
        numeric), so it does not replace non-ASCII code points with character references. This escaper
        escapes only the following five ASCII characters: `'"&<>`.
        """
        ...
