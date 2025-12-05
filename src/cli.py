import click
from .file_handler import FileHandler, MultiFileHandler
import os
import warnings


def _is_dir(filenames: tuple[str]):
    for filename in filenames:
        if os.path.isdir(filename):
            return True
    return False


def wc_files(
    filenames: tuple[str],
    len_files: int,
    collection: bool,
    word_only: bool,
    line_only: bool,
):
    if len_files == 1:
        handler = FileHandler(filename=filenames[0])
    else:
        handler = MultiFileHandler(filenames=filenames)

    if collection:
        handler.print_collection()
        warnings.warn("Cannot use -w or -l with -c")
    else:
        handler.print_count(word_only=word_only, line_only=line_only)


@click.command()
@click.argument("filenames", nargs=-1)
@click.option("-c", "--collection", is_flag=True, help="Collective count of all words")
@click.option("-w", "--word", is_flag=True, help="Word count only")
@click.option("-l", "--line", is_flag=True, help="Line count only")
def wc(
    filenames: tuple[str],
    collection: bool = False,
    word: bool = True,
    line: bool = True,
):
    """gets word count of a file"""
    len_files = len(filenames)

    if not filenames:
        raise ValueError("Error: No files provided.")

    is_dir = _is_dir(filenames=filenames)

    if len_files > 1 and is_dir:
        raise ValueError(
            f"Error: Only 1 directory can be scanned at a time \nExpected 1 got {len_files}."
        )
    
    # show both incase no option -w or -l
    if not word and not line:
        word = line = True

    if not is_dir:
        wc_files(
            filenames=filenames,
            len_files=len_files,
            collection=collection,
            word_only=word,
            line_only=line,
        )
