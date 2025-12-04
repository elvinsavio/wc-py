import re
from collections import Counter
from .lib import print_table

class FileHandler:
    def __init__(self, filename: str) -> None:
        if not filename:
            raise ValueError("Error: Filename is required")

        self.filename = filename
        self.file = open(filename, "r")
        self.word_count = self.__get_word_count()
        self.line_count = self.__get_line_count()
        self.word_counter = self.__get_word_counter()

    def __get_word_counter(self) -> Counter:
        self.file.seek(0)
        words = []
        for line in self.file:
            words.extend(re.findall(r"[A-Za-z]+", line))
        return Counter(words)
    
    def __get_word_count(self) -> int:
        self.file.seek(0)                
        count = 0
        for line in self.file:
            count += len(re.findall(r"[A-Za-z]+", line))
        self.file.seek(0)                 
        return count
    
    def __get_line_count(self) -> int:
        self.file.seek(0)
        return len(self.file.readlines())

    def print_collection(self) -> None: 
        counts = self.word_counter
        rows = [(word, count) for word, count in counts.most_common()]
        print_table(rows, headers=("Word", "Count"))



    def print_count(self) -> None:
        rows = [(self.filename, self.word_count, self.line_count)]
        print_table(rows, headers=("Filename", "Words", "Lines"))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.file.close()


class MultiFileHandler:
    def __init__(self, filenames: tuple[str]) -> None:
        self.filenames = filenames
        self.files = [FileHandler(filename) for filename in self.filenames]
    
    def _combined_counter(self) -> Counter:
        total = Counter()
        for fh in self.files:
            total += fh.word_counter
        return total

    def print_collection(self) -> None:
        counts = self._combined_counter()
        rows = [(word, count) for word, count in counts.most_common()]
        print_table(rows, headers=("Word", "Count"))
        
    def print_count(self) -> None:
        rows = [(fh.filename, fh.word_count, fh.line_count) for fh in self.files]
        print_table(rows, headers=("Filename", "Words", "Lines"))
