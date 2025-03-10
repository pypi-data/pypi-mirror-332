# -*- coding: utf-8 -*-
from collections import UserDict
from pathlib import Path
from typing import Any

from lxml.etree import Element


class SvgImage:
    """
    SvgImage class. - A wrapper around a svg image.

    Attributes:
        __path: Full Path to the svg image.
        filename: Name of the original file.
        location: Path to the parent directory of the original file.
        data: lxml.etree.Element representation of the svg image.
    """

    __path: Path

    def __init__(self, path: Path, xml: Element):
        self.__path = path
        self.filename = path.stem
        self.location = path.parent
        self.data = xml

    @property
    def compressed(self) -> bool:
        """
        Whether the svg image is gzip-compressed or not.
        """
        return self.__path.suffix in [".svgz", ".svg.gz"]

    @property
    def xmlns(self) -> dict[str, Any]:
        """
        Holds the XML namespaces definitions from the SVG.
        Copies the nsmap attribute and replaces None with an underscore key

        Used to mitigate missing namespace errors when using .find() or .xpath()
        """
        # Copy the dictionary to ensure not changing nsmap on the original
        nsmap = dict(self.data.nsmap)
        # Drop a default field that gets stored by the None key in the dict
        default = nsmap.pop(None)
        return {"_": default, **nsmap}


class ColorScheme(UserDict):
    """
    ColorScheme class. - A wrapper around the parsed KDE Plasma Color Theme.

    Attributes:
        data: a Python dictionary representation of the color scheme.
    """

    def __init__(self, colors: dict[str, Any]):
        super().__init__()
        self.data = {
            "Text": colors["Window"]["ForegroundNormal"],
            "Background": colors["Window"]["BackgroundNormal"],
            "Highlight": colors["Window"]["DecorationFocus"],
            "ViewText": colors["View"]["ForegroundNormal"],
            "ViewBackground": colors["View"]["BackgroundNormal"],
            "ViewHover": colors["View"]["DecorationHover"],
            "ViewFocus": colors["View"]["DecorationFocus"],
            "ButtonText": colors["Button"]["ForegroundNormal"],
            "ButtonBackground": colors["Button"]["BackgroundNormal"],
            "ButtonHover": colors["Button"]["DecorationHover"],
            "ButtonFocus": colors["Button"]["DecorationFocus"],
        }
