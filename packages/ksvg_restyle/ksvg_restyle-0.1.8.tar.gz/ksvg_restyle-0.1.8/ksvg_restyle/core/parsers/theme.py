# -*- coding: utf-8 -*-
import re
import tomllib
from typing import TextIO

from ksvg_restyle.core.wrappers import ColorScheme


def _clamp(value: int) -> int:
    """Ensures that the provided value is a valid integer
    In range between 0 and 255
    """
    return max(0, min(value, 255))


def _to_hex(rgb: str) -> str:
    """Transforms the provided rgb string to the HTML-valid hex color value"""
    red, green, blue = rgb.split(",")
    return "#{0:02x}{1:02x}{2:02x}".format(
        _clamp(int(red)),
        _clamp(int(green)),
        _clamp(int(blue)),
    )


def _str_literal(value: str) -> str:
    """Converts the provided value to a valid TOML string"""
    val = value.strip()
    # make sure boolean values are not stringified
    if val in ["true", "false"]:
        return f"{val}\n"

    return f'"{val}"\n'


def parse_color_theme(ct_file: TextIO) -> ColorScheme:
    """
    Read the KDE Plasma Color Theme stylesheet.

    Since its syntax is very close to TOML, patch content to make it valid TOML
    and then use tomllib to parse it and convert it to dict.
    :param ct_file: -- file contents (iostream)
    :return: a dict of colour theme styles
    """
    ct_str = ""
    re_header = r"^(\[\S+\])$"
    re_rgb = r"^\d+,\d+,\d+$"

    while line := ct_file.readline():
        if re.match(re_header, line):
            line = line.replace(":", ".")

        if "=" in line:
            k, v = line.split("=")
            val = v

            if re.match(re_rgb, v):
                val = _str_literal(_to_hex(v))

            if all(ch.isalpha() or ch.isspace() for ch in v):
                val = _str_literal(v)

            line = "=".join([k, val])
        ct_str += line

    try:
        theme_dict = tomllib.loads(ct_str)
    except tomllib.TOMLDecodeError as e:
        raise ValueError(str(e))
    else:
        color_theme = theme_dict.get("Colors")

        if not color_theme:
            raise ValueError("No color theme specification found")

        return ColorScheme(color_theme)
