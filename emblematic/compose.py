import bs4


def compose_basic(bg: bs4.Tag, fg: bs4.Tag) -> bs4.Tag:
    """
    Create a nice icon from the given background ``<svg>`` and the given foreground ``<svg>``.
    """

    if bg.name != "svg":
        raise ValueError("bg is not a <svg> tag.")
    if fg.name != "svg":
        raise ValueError("fg is not a <svg> tag.")
        
    bg = bg.__copy__()
    bg.attrs["id"] = "emblematic-bg"
    bg.attrs["width"] = "100%"
    bg.attrs["height"] = "100%"
    
    fg = fg.__copy__()
    fg.attrs["id"] = "emblematic-fg"
    fg.attrs["width"] = "63%"
    fg.attrs["height"] = "63%"
    fg.attrs["preserveAspectRation"] = "xMidYMid meet"
    fg.attrs["transform"] = "translate(185, 185)"    
    
    doc = bs4.BeautifulSoup("""
    <?xml version="1.0" encoding="UTF-8"?>
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">
    </svg>
    """)
    container: bs4.Tag = doc.svg
    container.append(bg)
    container.append(fg)

    return doc
    
