"""Utilities for Electrostatic

Some useful utilities for the Electrostatic package.
"""
from pathlib import Path
from typing import Generic, Iterator, List, Sequence, Tuple, TypeVar


class Undefined:
    """A class to make it easier to distinguish between missing (undefined) and None values"""

    pass


class Node:
    """Node class"""

    __slots__ = ("value", "children")

    def __init__(self, value=Undefined):
        self.value = value
        self.children = dict()

    def __len__(self):
        """Return the number of keys in the subtree rooted at this node."""
        return int(self.value is not Undefined) + sum(map(len, self.children.values()))

    def __repr__(self):
        return "(%s, {%s})" % (
            self.value is Undefined and "NULL" or repr(self.value),
            ", ".join("%r: %r" % t for t in self.children.items()),
        )

    def __getstate__(self):
        return self.value, self.children

    def __setstate__(self, state):
        self.value, self.children = state


T = TypeVar("T")


class PrefixMatcher(Generic[T]):
    """Prefix Matcher
    This is loosely based on PyTrie (https://github.com/gsakkis/pytrie/), but we've
    departed from the mapping-style API quite radically.

    It is intended to be immutable, and purpose-built to match prefixes to URLs and
    return an ordered list of matches, longest match first.
    """

    def __set_item(self, key: str, value: T) -> None:
        node = self._root
        for part in key:
            next_node = node.children.get(part)
            if next_node is None:
                node = node.children.setdefault(part, Node())
            else:
                node = next_node
        node.value = value

    def __init__(self, items: Sequence[Tuple[str, T]]):
        self._root = Node()

        for k, v in items:
            self.__set_item(k, v)

    def prefix_matches(self, key: str) -> Iterator[Tuple[str, T]]:
        """Return an iterator over the items (``(key,value)`` tuples) of this
        trie that are associated with keys that are prefixes of ``key``, longest
        match first.
        """
        # Iterates over each character of the string, looking for matches
        prefix_chars: List[str] = []
        prefix_append = prefix_chars.append
        node = self._root
        if node.value is not Undefined:
            yield "".join(prefix_chars), node.value

        for part in key:
            node = node.children.get(part)
            if node is None:
                break
            prefix_append(part)
            if node.value is not Undefined:
                yield "".join(prefix_chars), node.value

    def prefixes(self) -> Iterator[str]:
        """Return a list of the prefixes in this matcher"""

        return (key for key, value in self.items())

    def items(self) -> Iterator[Tuple[str, T]]:
        parts: List[str] = []
        parts_append = parts.append

        def generator(node: Node) -> Iterator[Tuple[str, T]]:
            nonlocal parts, parts_append

            if node.value is not Undefined:
                yield "".join(parts), node.value
            for part, child in node.children.items():
                parts_append(part)
                for subresult in generator(child):
                    yield subresult
                del parts[-1]

        return generator(self._root)

    def values(self) -> Iterator[T]:
        """Return a list of the values in this matcher"""

        def generator(node: Node):
            if node.value is not Undefined:
                yield node.value
            for child in node.children.values():
                for subresult in generator(child):
                    yield subresult

        return generator(self._root)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(...)"


# mime types, based on whitenoise media_types.py
FALLBACK_MIME_TYPE = "application/octet-stream"
# Mime types determined by full base filename
MIME_TYPE_NAMES = {
    "apple-app-site-association": "application/pkc7-mime",
    # Adobe Products - see:
    # https://www.adobe.com/devnet-docs/acrobatetk/tools/AppSec/xdomain.html#policy-file-host-basics
    "crossdomain.xml": "text/x-cross-domain-policy",
}
# Mime types determined by file extension
MIME_TYPE_EXTENSIONS = {
    ".3gp": "video/3gpp",
    ".3gpp": "video/3gpp",
    ".7z": "application/x-7z-compressed",
    ".ai": "application/postscript",
    ".asf": "video/x-ms-asf",
    ".asx": "video/x-ms-asf",
    ".atom": "application/atom+xml",
    ".avi": "video/x-msvideo",
    ".bmp": "image/x-ms-bmp",
    ".cco": "application/x-cocoa",
    ".crt": "application/x-x509-ca-cert",
    ".css": "text/css",
    ".der": "application/x-x509-ca-cert",
    ".doc": "application/msword",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".ear": "application/java-archive",
    ".eot": "application/vnd.ms-fontobject",
    ".eps": "application/postscript",
    ".flv": "video/x-flv",
    ".gif": "image/gif",
    ".hqx": "application/mac-binhex40",
    ".htc": "text/x-component",
    ".htm": "text/html",
    ".html": "text/html",
    ".ico": "image/x-icon",
    ".jad": "text/vnd.sun.j2me.app-descriptor",
    ".jar": "application/java-archive",
    ".jardiff": "application/x-java-archive-diff",
    ".jng": "image/x-jng",
    ".jnlp": "application/x-java-jnlp-file",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "text/javascript",
    ".json": "application/json",
    ".kar": "audio/midi",
    ".kml": "application/vnd.google-earth.kml+xml",
    ".kmz": "application/vnd.google-earth.kmz",
    ".m3u8": "application/vnd.apple.mpegurl",
    ".m4a": "audio/x-m4a",
    ".m4v": "video/x-m4v",
    ".md": "text/markdown",
    ".mid": "audio/midi",
    ".midi": "audio/midi",
    ".mjs": "text/javascript",
    ".mml": "text/mathml",
    ".mng": "video/x-mng",
    ".mov": "video/quicktime",
    ".mp3": "audio/mpeg",
    ".mp4": "video/mp4",
    ".mpeg": "video/mpeg",
    ".mpg": "video/mpeg",
    ".ogg": "audio/ogg",
    ".pdb": "application/x-pilot",
    ".pdf": "application/pdf",
    ".pem": "application/x-x509-ca-cert",
    ".pl": "application/x-perl",
    ".pm": "application/x-perl",
    ".png": "image/png",
    ".ppt": "application/vnd.ms-powerpoint",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ".prc": "application/x-pilot",
    ".ps": "application/postscript",
    ".ra": "audio/x-realaudio",
    ".rar": "application/x-rar-compressed",
    ".rpm": "application/x-redhat-package-manager",
    ".rss": "application/rss+xml",
    ".rtf": "application/rtf",
    ".run": "application/x-makeself",
    ".sea": "application/x-sea",
    ".shtml": "text/html",
    ".sit": "application/x-stuffit",
    ".svg": "image/svg+xml",
    ".svgz": "image/svg+xml",
    ".swf": "application/x-shockwave-flash",
    ".tcl": "application/x-tcl",
    ".tif": "image/tiff",
    ".tiff": "image/tiff",
    ".tk": "application/x-tcl",
    ".ts": "video/mp2t",
    ".txt": "text/plain",
    ".wasm": "application/wasm",
    ".war": "application/java-archive",
    ".wbmp": "image/vnd.wap.wbmp",
    ".webm": "video/webm",
    ".webp": "image/webp",
    ".wml": "text/vnd.wap.wml",
    ".wmlc": "application/vnd.wap.wmlc",
    ".wmv": "video/x-ms-wmv",
    ".woff": "application/font-woff",
    ".woff2": "font/woff2",
    ".xhtml": "application/xhtml+xml",
    ".xls": "application/vnd.ms-excel",
    ".xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ".xml": "text/xml",
    ".xpi": "application/x-xpinstall",
    ".xspf": "application/xspf+xml",
    ".zip": "application/zip",
}


def get_mime_type(path: Path) -> str:
    """Get MIME type information for a file, based on file extension"""

    mime_type = MIME_TYPE_NAMES.get(path.name.lower(), None)
    if mime_type is None:
        mime_type = MIME_TYPE_EXTENSIONS.get(path.suffix.lower(), None)

    if mime_type is None:
        mime_type = FALLBACK_MIME_TYPE

    return mime_type
