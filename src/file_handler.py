import re
from collections import Counter


class FileHandler:
    def __init__(self, filename: str) -> None:
        if not filename:
            raise ValueError("Error: Filename is required")

        self.filename = filename
        self.file = open(filename, "r")
        self.word_count = self.__get_word_count()
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

    def print_collection(self) -> None:
        counts = self.word_counter

        max_key_len = max(len(w) for w in counts)

        print(f'{"WORD".ljust(max_key_len)} | COUNT')
        print('-' * (max_key_len + 8))

        for key, value in counts.most_common():
            print(f'{key.ljust(max_key_len)} | {value}')


    def print_count(self) -> None:
        print(f'Filename: {self.filename}\t\t: {self.word_count}')

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

        if not counts:
            print("No words found.")
            return

        max_key_len = max(len(word) for word in counts)
        header = f"{'WORD'.ljust(max_key_len)} | COUNT"
        print(header)
        print("-" * len(header))

        for word, cnt in counts.most_common():
            print(f"{word.ljust(max_key_len)} | {cnt}")

    def print_count(self) -> None:
        for filename in self.files:
            print(f"{'Filename: ' + filename.filename:<40} : {filename.word_count}")
