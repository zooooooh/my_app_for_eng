import os
import random

class Data:
    def __init__(self, filename="dictionary.txt"):
        self.filename = filename
        self.dictionary = self.load_dictionary()

    def load_dictionary(self):
        dictionary = {}
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    word, translation = line.strip().split(":")
                    dictionary[word] = translation
        return dictionary

    def add_word(self, word, translation):
        if word not in self.dictionary:
            self.dictionary[word] = translation
            self.save_dictionary()
        else:
            return False  # Возвращаем False, если слово уже существует

    def get_translation(self, word):
        return self.dictionary.get(word)

    def save_dictionary(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            for word, translation in self.dictionary.items():
                file.write(f"{word}:{translation}\n")

    def get_random_words(self, num_words):
        return random.sample(list(self.dictionary.keys()), num_words)
