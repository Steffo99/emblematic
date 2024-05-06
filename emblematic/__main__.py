"""
Command-line interface for :mod:`emblematic`.

Implemented with :mod:`click`.
"""

import pathlib
import subprocess

import bs4
import click

from .compose import compose_basic
from .files import get_svgs


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
@click.option(
    "--icon-shadow-fill", "icon_shadow_fill",
    type=str,
    default=None,
    help="The color that the drop shadow added to the icon should have."
)
@click.option(
    "--icon-shadow-x", "icon_shadow_x",
    type=str,
    default=None,
    help="The horizontal offset that the drop shadow will have relative to the icon."
)
@click.option(
    "--icon-shadow-y", "icon_shadow_y",
    type=str,
    default=None,
    help="The vertical offset that the drop shadow will have relative to the icon."
)
@click.option(
    "--icon-shadow-blur", "icon_shadow_blur",
    type=str,
    default=None,
    help="The radius of the blur applied to the shadow."
)
def basic(bg_file, icon_paths, icon_fill, output_dir, width, height, icon_shadow_fill, icon_shadow_x, icon_shadow_y, icon_shadow_blur):
    if 0 < sum(map(bool, [icon_shadow_fill, icon_shadow_x, icon_shadow_y, icon_shadow_blur])) < 4:
        raise click.ClickException("--icon-shadow-* options cannot be partially set.")

    icon_paths = map(pathlib.Path, icon_paths)
    icon_paths = map(get_svgs, icon_paths)
    icon_paths = sum(icon_paths, start=[])

    output_dir = pathlib.Path(output_dir)

    bg_doc = bs4.BeautifulSoup(bg_file, features="lxml-xml")
    bg = bg_doc.svg

    for icon_path in icon_paths:
        icon_path: pathlib.Path
        output_svg_path = output_dir.joinpath(f"{icon_path.stem}.svg")
        output_png_path = output_dir.joinpath(f"{icon_path.stem}.png")

        with open(icon_path) as icon_file:
            click.echo(icon_path, nl=False)
            icon_doc = bs4.BeautifulSoup(icon_file, features="lxml-xml")
            icon = icon_doc.svg
            icon.path.attrs["fill"] = icon_fill

        if icon_shadow_fill:
            icon.path.attrs["filter"] = "url(#emblematic-filter)"
            defs_doc = bs4.BeautifulSoup(f"""
                <defs>
                    <filter id="emblematic-filter" color-interpolation-filters="sRGB">
                        <feFlood flood-color="{icon_shadow_fill}" in="SourceGraphic" result="flood"/>
                        <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="{icon_shadow_blur}"/>
                        <feOffset dx="{icon_shadow_x}" dy="{icon_shadow_y}" in="blur" result="offset"/>
                        <feComposite in="flood" in2="offset" operator="in" result="comp1"/>
                        <feComposite in="SourceGraphic" in2="comp1" result="comp2"/>
                    </filter>
                </defs>
            """, features="lxml-xml")
            icon.insert(0, defs_doc)

        click.echo(" → ", nl=False)
        svg_doc = compose_basic(background=bg, icon=icon, width=width, height=height).prettify()

        with open(output_svg_path, mode="w") as output_file:
            click.echo(output_svg_path, nl=False)
            output_file.write(svg_doc)

        click.echo(" → ", nl=False)

        subprocess.run([
            "inkscape",
            output_svg_path,
            "--export-type=png",
            f"--export-filename={output_png_path}",
            f"--export-width={width}",
            f"--export-height={height}",
        ])

        click.echo(output_png_path, nl=False)


if __name__ == "__main__":
    main()
