from collections import Counter

class FileHandler:
    def __init__(self, filename: str) -> None:
        if not filename:
            raise ValueError("Error: Filename is required")

        self.filename = filename
        self.file = open(filename, "r")
        self.word_count = self.get_word_count()

    def get_word_count(self):
        self.file.seek(0)                
        count = 0
        for line in self.file:
            count += len(line.split())
        self.file.seek(0)                 
        return count

    def print_collection(self) -> None:
        self.file.seek(0)
        words = []
        for line in self.file:
            words.extend(line.split())
        print(Counter(words))


    def print_count(self) -> None:
        print(f'Filename: {self.filename}\t\t: {self.word_count}')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.file.close()