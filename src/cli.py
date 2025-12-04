import click
from typing import Optional
from .file_handler import FileHandler, MultiFileHandler


@click.command()
@click.argument("filenames", nargs=-1)
@click.option(
    "-c", "--collection", is_flag=True, help="Collective count of all words"
)
@click.option(
    "-r", "--recursive", is_flag=True, help="Recursively go through several files"
)
def wc(filenames: tuple[str], recursive: Optional[bool] = False, collection: Optional[bool] = False):
    """gets word count of a file"""

    if not filenames:
            click.echo("No files provided.")
            return

    if len(filenames) == 1:
        f = FileHandler(filename=filenames[0])
        f.print_count()
        if collection:
            f.print_collection()

    else:
         f = MultiFileHandler(filenames=filenames)
         f.print_count()
         if collection:
              f.print_collection()