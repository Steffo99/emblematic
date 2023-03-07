import click
import bs4


@click.command()
@click.option(
    "-o", "--output-file", "output_file",
    help="File to output the icon to.", 
    required=True,
    type=click.File(mode="w"),
)
@click.option(
    "-b", "--background-file", "background_file",
    help="File to use as the background of the icon.",
    required=True,
    type=click.File(mode="r"),
)
@click.option(
    "-f", "--foreground-file", "foreground_file",
    help="File to use as the foreground of the icon.",
    required=True,
    type=click.File(mode="r"),
)
def main(output_file, background_file, foreground_file):
    background_soup = bs4.BeautifulSoup(background_file, "lxml-xml")
    foreground_soup = bs4.BeautifulSoup(foreground_file, "lxml-xml")

    foreground_tag = foreground_soup.path
    foreground_scaled_tag = bs4.BeautifulSoup("""<g id="icon" transform="matrix(2,0,0,2,-4.3209502e-5,512)"></g>""", "lxml-xml")
    foreground_scaled_tag.g.append(foreground_tag)

    background_soup.svg.append(foreground_scaled_tag)

    output_file.write(background_soup.prettify())


if __name__ == "__main__":
    main()
