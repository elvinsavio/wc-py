import re
from collections import Counter
from .lib import print_table
from pathlib import Path
import os

class FileHandler:
    WORD_RE = re.compile(r"[A-Za-z]+")

    def __init__(self, filename: str):
        if not filename:
            raise ValueError("Filename is required")

        path = Path(filename)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filename}")

        self.filename = filename

        self.text = self.read_text(path)

        self.lines = self.text.splitlines()

        self._words = None
        self._word_count = None
        self._line_count = None
        self._counter = None

    def read_text(self, path):
        for enc in ("utf-8", "utf-16", "latin-1"):
            try:
                return path.read_text(encoding=enc)
            except UnicodeDecodeError:
                continue
        raise ValueError("Unsupported text encoding")


    def _extract_words(self):
        return self.WORD_RE.findall(self.text)

    @property
    def words(self):
        if self._words is None:
            self._words = self._extract_words()
        return self._words

    @property
    def word_count(self):
        if self._word_count is None:
            self._word_count = len(self.words)
        return self._word_count

    @property
    def line_count(self):
        if self._line_count is None:
            self._line_count = len(self.lines)
        return self._line_count

    @property
    def word_counter(self):
        if self._counter is None:
            normalized = (w.lower() for w in self.words)
            self._counter = Counter(normalized)
        return self._counter

    def print_collection(self):
        rows = [(word, count) for word, count in self.word_counter.most_common()]
        print_table(rows, headers=("Word", "Count"))

    def print_count(self, word_only: bool = True, line_only: bool = True):
        rows = (self.filename,)
        header = ("Filename",)
        if word_only:
            rows += (self.word_count,)
            header += ("Words",)
        if line_only:
            rows += (self.line_count,)
            header += ("Lines",)
        print_table([rows], headers=header)


class MultiFileHandler:
    def __init__(self, filenames: tuple[str]):
        self.files = [FileHandler(fn) for fn in filenames]

    def _combined_counter(self):
        total = Counter()
        for fh in self.files:
            total.update(fh.word_counter)
        return total

    def print_collection(self):
        counter = self._combined_counter()
        rows = [(word, count) for word, count in counter.most_common()]
        print_table(rows, headers=("Word", "Count"))

    def print_count(self, word_only: bool = True, line_only: bool = True):
        rows = [(fh.filename, fh.word_count, fh.line_count) for fh in self.files]
        print_table(rows, headers=("Filename", "Words", "Lines"))


class FolderHandler:
    def __init__(self, pathname: str): 
        self.pathname = pathname
        path = Path(pathname)

        if not path.exists():
            raise FileNotFoundError(f"Path not found: {pathname}")

        self._g_filename = []
        self.filenames = self.get_files(self.pathname)    
        del self._g_filename

            
    def get_files(self, pathname):
        for entry in os.listdir(pathname):
            full_path = os.path.join(pathname, entry)
            if os.path.isdir(full_path):
                self.get_files(full_path)
            else:
                self._g_filename += [FileHandler(full_path)]
        return self._g_filename
    
    def _combined_counter(self):
        total = Counter()
        for fh in self.filenames:
            total.update(fh.word_counter)
        return total

    def print_collection(self):
        counter = self._combined_counter()
        rows = [(word, count) for word, count in counter.most_common()]
        print_table(rows, headers=("Word", "Count"))

    def print_count(self, word_only: bool = True, line_only: bool = True):
        rows = [(fh.filename, fh.word_count, fh.line_count) for fh in self.filenames]
        print_table(rows, headers=("Filename", "Words", "Lines"))
