# -*- coding: utf-8 -*-
import re

from lxml import etree

from ksvg_restyle.core import parsers, wrappers

HEX_COLOR_PATTERN: str = r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})\b"


def get_old_colors(xml: str) -> list[str]:
    """Retrieves the original color palette from the file

    :param xml: XML string
    :return: A list of unique colors from the original SVG
    """
    seen = set()
    seen_add = seen.add
    # Get all HTML hexadecimal colors
    colors = re.findall(HEX_COLOR_PATTERN, xml)
    # Copy only the unique values from the color list while preserving order
    return [x for x in colors if not (x in seen or seen_add(x))]


def find_or_add_style(
    nsmap: dict[str, str],
    svg: etree.Element,
    template: str,
    xml_parser: etree.XMLParser,
) -> tuple[etree.Element, list[str]]:
    """Adds or changes value (if exists) of the <style> tag of the SVG image

    :param nsmap: XML namespace map
    :param svg: XML tree object
    :param template: CSS stylesheet
    :param xml_parser: Runtime XML parser instance

    :return: A tuple with a copy of the original tree with updated values
        and original color palette.
    """
    colors = get_old_colors(etree.tostring(svg).decode("utf-8"))
    temp = parsers.svg.create_copy(svg, xml_parser)
    defs = temp.find("svg:defs", nsmap)
    tags = temp.xpath(
        "//*/style[contains(@id, 'current-color-scheme')]", namespaces=nsmap
    )

    if not tags:
        style = etree.SubElement(
            _parent=defs,
            _tag="style",
            type="text/css",
            id="current-color-scheme",
        )
    else:
        style = tags[0]

    style.text = template.strip()
    return temp, colors


def update_attributes(
    attr: str, nsmap: dict[str, str], path: str, tree: etree.Element, val: str
) -> None:
    """Finds an attribute of a given tag and changes its value
    If the given attribute name is "style" -
    replace all occurrences of HTML hex colors with the value;
    Else just update value.

    :param attr: Attribute name
    :param nsmap: XML namespace map
    :param path: XPath to search for tags for the attribute update
    :param tree: XML tree object
    :param val: Value to replace with
    """
    tags = tree.xpath(path, namespaces=nsmap)
    if tags:
        for tag in tags:
            if attr == "style":
                prev = tag.attrib[attr]
                new = re.sub(HEX_COLOR_PATTERN, val, prev)
                tag.set(attr, new)
            else:
                tag.set(attr, val)


def apply_stylesheet(
    color_scheme: wrappers.ColorScheme,
    nsmap: dict[str, str],
    old_colors: list[str],
    svg: etree.Element,
    template: str,
    xml_parser: etree.XMLParser,
) -> etree.ElementTree:
    """Performs the final transformation on the SVG image

    First, applies the XSLT transformation on the tree
    Then, updates attributes to utilize the new color palette

    :param color_scheme: Plasma Color Theme representation
    :param nsmap: XML namespace map
    :param old_colors: Original color palette
    :param svg: XML tree object
    :param template: XSLT transformation template
    :param xml_parser: Runtime XML parser instance

    :return: A new XML representation copied
        from the original SVG image and transformed
    """
    temp = parsers.svg.create_copy(svg, xml_parser)
    tree = parsers.svg.transform_svg(temp, template, xml_parser)
    colors = list(old_colors)

    # Iterate over the original color palette
    for x in range(len(colors)):
        # Find an element that uses the color of the current iteration
        name = list(color_scheme.keys())[x]
        clr = colors[x]

        # Add a new CSS class from the stylesheet to any corresponding element
        update_attributes(
            attr="class",
            nsmap=nsmap,
            path=f"//*/*[contains(@style, '{clr}') and not(@class)]",
            tree=tree,
            val=f"ColorScheme-{name}",
        )
        # Update fills and stops - replace hardcoded colors with currentColor
        fills = f"//*/*[contains(@style, '{clr}') and not(local-name()='stop')]"
        update_attributes(
            attr="style",
            nsmap=nsmap,
            path=fills,
            tree=tree,
            val="currentColor",
        )
        update_attributes(
            attr="style",
            nsmap=nsmap,
            path=f"//*/*[contains(@style, '{clr}') and local-name()='stop']",
            tree=tree,
            val="currentColor",
        )

    return tree
