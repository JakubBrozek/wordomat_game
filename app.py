import random

HARD_STARTING_LETTER = 'y'

class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as words:
            self.dictionary = words.read().splitlines()
    def get_dictionary(self):
        if not self.dictionary:
            print("Lista słów jest pusta ")
            return
        return self.dictionary

def enemy_move(words):
    while True:
        word = random.choice(words)
        if not word.endswith(HARD_STARTING_LETTER):
            return word

def get_user_word(letter):
    while True:
        user_word = input("Podaj słowo zaczynające się na '" + letter + "'")
        if user_word:
            return user_word

def main():
    dictionary = Dictionary()
    word_list = dictionary.get_dictionary()

main()