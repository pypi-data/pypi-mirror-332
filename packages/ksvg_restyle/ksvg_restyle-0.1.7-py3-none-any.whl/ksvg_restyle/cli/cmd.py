# -*- coding: utf-8 -*-
import click

from ksvg_restyle.cli import handlers
from ksvg_restyle.cli.env import pass_env
from ksvg_restyle.core import builder, parsers


@click.command()
@click.argument(
    "svg", type=click.Path(exists=True), callback=handlers.load_svg_image
)
@click.option(
    "-c",
    "--color-scheme",
    required=True,
    type=click.Path(exists=True),
    callback=handlers.load_color_theme,
    help="Path to the Plasma Color Theme file",
)
@click.option(
    "-o",
    "--output",
    type=click.Path(exists=False),
    help="Output destination path (recolored SVG image)",
)
@click.option(
    "-r",
    "--replace",
    is_flag=True,
    default=False,
    help="Replace existing SVG. Effective only when no output path provided.",
)
@pass_env
def run(env, svg, color_scheme, output, replace) -> None:
    css = env.render_template("stylesheet.jinja2", colors=color_scheme.data)
    xslt = env.render_template("transform.xsl")

    styled, old_colors = builder.find_or_add_style(
        nsmap=svg.xmlns, svg=svg.data, template=css, xml_parser=env.xml_parser
    )
    changed = builder.apply_stylesheet(
        color_scheme=color_scheme,
        nsmap=svg.xmlns,
        old_colors=old_colors,
        svg=styled,
        template=xslt,
        xml_parser=env.xml_parser,
    )
    if not output:
        if replace:
            output = svg.location / svg.filename
        else:
            output = svg.location / f"{svg.filename}_copy"

    result = parsers.svg.save_svg(svg.compressed, output, changed)
    click.echo(f"The restyled SVG has been written to {result}.")
