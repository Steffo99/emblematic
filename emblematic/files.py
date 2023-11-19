"""
Module containing functions to operate on files or directories.
"""

import pathlib


def get_svgs(path: pathlib.Path):
    """
    Find all SVGs in the given path.
    """
    if not path.exists():
        raise ValueError("Given path does not exist.")
    if not path.is_dir():
        return [path]

    return list(path.glob("**/*.svg"))


__all__ = (
    "get_svgs",
)
