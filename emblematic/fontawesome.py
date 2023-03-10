"""
Module containing function to process `Font Awesome <https://fontawesome.com/>`_ SVG icons.
"""

import typing as t
import bs4
import pathlib


def get_icons(path: pathlib.Path):
    if not path.exists():
        raise ValueError("Given path does not exist.")
    if not path.is_dir():
        raise ValueError("Given path is not a directory.")
    
    svgs = path.joinpath("svgs")
    return svgs.glob("**/*.svg")


__all__ = (
    "get_icons",
)
