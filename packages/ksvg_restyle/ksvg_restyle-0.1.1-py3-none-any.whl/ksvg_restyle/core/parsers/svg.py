# -*- coding: utf-8 -*-
import gzip
from pathlib import Path

from lxml import etree

from ksvg_restyle.core.wrappers import SvgImage


def parse_svg(path: Path, xml_parser: etree.XMLParser) -> SvgImage:
    if path.suffix in [".svgz", ".svg.gz"]:
        f = gzip.open(path, "rb")
    else:
        f = open(path, "rb")
    xml = f.read()
    f.close()

    return SvgImage(path, etree.fromstring(xml, xml_parser))


def create_copy(
    svg: etree.Element, xml_parser: etree.XMLParser
) -> etree.Element:
    """
    Creates a copy of the original SVG XML representation to manipulate on
    """
    copy = etree.tostring(svg)
    return etree.fromstring(copy, parser=xml_parser)


def transform_svg(
    svg: etree.ElementTree, template: str, xml_parser: etree.XMLParser
) -> etree.ElementTree:
    """
    Applies the XSLT transform to the SVG image
    """
    xslt = etree.XML(template, parser=xml_parser)
    transform = etree.XSLT(xslt)
    return transform(svg)


def save_svg(compressed: bool, path: Path, content: bytes) -> str:
    if compressed:
        path = f"{path}.svgz"
        file = gzip.open(path, "wb")
    else:
        path = f"{path}.svg"
        file = open(path, "wb")
    file.write(content)
    file.close()

    return path
