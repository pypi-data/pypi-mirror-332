# -*- coding: utf-8 -*-
from pathlib import Path

from click import BadParameter

from ksvg_restyle.cli.env import pass_env
from ksvg_restyle.core import parsers, wrappers


@pass_env
def load_svg_image(env, _, param: str, value: str) -> wrappers.SvgImage:
    """Callback for click.option decorator
    Reads the provided SVG file

    :return: a wrapper class representing an SVG image
    """
    file_path = Path(value)
    if file_path.is_file():
        if file_path.suffix not in [".svg", ".svgz", ".svg.gz"]:
            raise BadParameter(f"{param}: {value} - Unsupported file type")

        return parsers.svg.parse_svg(file_path, env.xml_parser)
    else:
        raise BadParameter(f"{param}: {value} is not a file")


def load_color_theme(_, param: str, value: str) -> wrappers.ColorScheme:
    """Callback for click.option decorator
    Reads the color theme stylesheet, then converts it to dict.

    :return: A dictionary containing the color theme definition
        with valid HTML-encoded values (CSS-compatible)
    """
    file_path = Path(value)
    if file_path.is_file():
        with open(value, "r", encoding="UTF-8") as f:
            try:
                colors = parsers.theme.parse_color_theme(f)
            except ValueError as e:
                raise BadParameter(
                    message=f"{param}: Error reading color theme {value}:\n{e}"
                )
            else:
                return colors
    else:
        raise BadParameter(f"{param}: {value} is not a file")
