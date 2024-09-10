import random

class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as words:
            self.dictionary = words.read().splitlines()
    def get_dictionary(self):
        if not self.dictionary:
            print("Lista słów jest pusta ")
            return
        return self.dictionary
