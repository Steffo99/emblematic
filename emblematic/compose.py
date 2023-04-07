"""
Module containing the functions used to generate ``<svg>`` icons from other ``<svg>`` :class:`bs4.Tag`.
"""

import bs4


def compose_basic(background: bs4.Tag, icon: bs4.Tag, width: int, height: int) -> bs4.Tag:
    """
    Create a new and nice ``<svg>`` icon from the given background ``<svg>`` and the given foreground ``<svg>``.
    """

    if background.name != "svg":
        raise ValueError("bg is not a <svg> tag.")
    if icon.name != "svg":
        raise ValueError("fg is not a <svg> tag.")
        
    background = background.__copy__()
    background.attrs["id"] = "emblematic-background"
    background.attrs["width"] = "100%"
    background.attrs["height"] = "100%"
    
    icon = icon.__copy__()
    icon.attrs["id"] = "emblematic-icon"
    icon.attrs["width"] = "63%"
    icon.attrs["height"] = "63%"
    icon.attrs["preserveAspectRatio"] = "xMidYMid meet"
    icon.attrs["transform"] = f"translate({width * 0.37 / 2}, {height * 0.37 / 2})"    
    
    doc = bs4.BeautifulSoup(f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">
    </svg>
    """, features="lxml-xml")
    container: bs4.Tag = doc.svg
    container.append(background)
    container.append(icon)

    return doc
    

__all__ = (
    "compose_basic",
)
