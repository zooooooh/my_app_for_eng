import random

class Logic:
    def __init__(self, data):
        self.data = data
        self.quiz_words = []

    def translate(self, word):
        return self.data.get_translation(word)

    def start_quiz(self, num_words):
        self.quiz_words = self.data.get_random_words(num_words)
        self.quiz_index = 0

    def check_answer(self, word, user_answer):
        return user_answer.lower() == self.data.get_translation(word).lower()

    def get_translation(self, word):
        return self.data.get_translation(word)
