import click
from typing import Optional
from .file_handler import FileHandler


@click.command()
@click.argument("filename", required=False)
@click.option(
    "-c", "--collection", is_flag=True, help="Collective count of all words"
)
@click.option(
    "-r", "--recursive", is_flag=True, help="Recursively go through several files"
)
def wc(filename: Optional[str] = None, recursive: Optional[bool] = False, collection: Optional[bool] = False):
    """gets word count of a file"""
    if filename:
        f = FileHandler(filename=filename)
        f.print_count()
        if collection:
            f.print_collection()        
    click.echo(f"Youre opening file {filename}")
