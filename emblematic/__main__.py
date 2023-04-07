"""
Command-line interface for :mod:`emblematic`.

Implemented with :mod:`click`.
"""

import click
import bs4
import pathlib
import cairosvg

from .files import get_svgs
from .compose import compose_basic


@click.group()
def main():
    pass


@main.command("basic")
@click.option(
    "-b", "--background", "bg_file",
    type=click.File(mode="r"),
    required=True,
    help="SVG file to be used as background.",
)
@click.option(
    "-i", "--icon", "icon_paths",
    type=click.Path(exists=True),
    required=True,
    multiple=True,
    help="SVG files or directories of files to be used as foreground.",
)
@click.option(
    "-f", "--fill", "icon_fill",
    type=str,
    required=True,
    help="The color to fill icons with.",
)
@click.option(
    "-o", "--output-dir", "output_dir",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    required=True,
    help="The directory where output files should be placed in.",
)
@click.option(
    "-w", "--width", "width",
    type=int,
    default=2000,
    help="The width the output files should have.",
)
@click.option(
    "-h", "--height", "height",
    type=int,
    default=2000,
    help="The height the output files should have."
)
def basic(bg_file, icon_paths, icon_fill, output_dir, width, height):
    icon_paths = map(pathlib.Path, icon_paths)
    icon_paths = map(get_svgs, icon_paths)
    icon_paths = sum(icon_paths, start=[])

    output_dir = pathlib.Path(output_dir)

    bg_doc = bs4.BeautifulSoup(bg_file, features="lxml-xml")
    bg = bg_doc.svg

    for icon_path in icon_paths:
        icon_path: pathlib.Path
        output_path = output_dir.joinpath(f"{icon_path.stem}.png")

        with open(icon_path) as icon_file:
            click.echo(icon_path, nl=False)
            icon_doc = bs4.BeautifulSoup(icon_file, features="lxml-xml")
            icon = icon_doc.svg
            icon.path.attrs["fill"] = icon_fill
        
        click.echo(" → ", nl=False)
        svg_doc = compose_basic(background=bg, icon=icon, width=width, height=height)

        click.echo(" → ", nl=False)
        svg_bytes = bytes(svg_doc.prettify(), encoding="utf8")
        
        click.echo(" → ", nl=False)
        png_bytes = cairosvg.svg2png(bytestring=svg_bytes)

        with open(output_path, mode="wb") as output_file:
            click.echo(output_path, nl=False)
            output_file.write(png_bytes)

        click.echo()



if __name__ == "__main__":
    main()
