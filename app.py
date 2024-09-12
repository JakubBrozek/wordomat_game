import random
import customtkinter

HARD_STARTING_LETTER = 'y'
class GUI:
    def __init__(self):
        app = customtkinter.CTk()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        app.title("Wordomat")
        app.geometry("800x500")

        self.entry = customtkinter.CTkEntry(app, placeholder_text="Answer", width=500, height=25, corner_radius=5)
        self.entry.grid(row=0, column=0, padx=20, pady=20)

        send_button = customtkinter.CTkButton(app, text="Accept", command=player_move_send(self))
        send_button.grid(row=10, column=0, padx=20, pady=20)

        app.grid_columnconfigure(0, weight=1)
        app.mainloop()

    def gui_get_entry(self):
        return self.entry.get()

class Dictionary:
    def __init__(self):
        with open('dictionary.txt', 'r', encoding='utf-8') as words:
            self.dictionary = words.read().splitlines()
    def get_dictionary(self):
        if not self.dictionary:
            print("Lista słów jest pusta ")
            return
        return self.dictionary
    def get_alphabet(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alphabet = alphabet

        return alphabet

def player_move_send(gui):
    print(gui.gui_get_entry())

def enemy_move(words, letter):
    while True:
        word = random.choice(words)
        if word.startswith(letter) and not word.endswith(HARD_STARTING_LETTER):
            return word

def get_user_word(words, letter):
    while True:
        user_word = input("Podaj słowo zaczynające się na '" + letter + "': ").lower()
        if user_word.startswith(letter):
            if user_word in words:
                return user_word
            print("To słowo nie znajduje się w moim słowniku, wymyśl coś innego: ")
        else:
            print("Proszę podać słowo zaczynające się na '" + letter + "': ")

def main():
    dictionary = Dictionary()
    word_list = dictionary.get_dictionary()
    current_letter = random.choice(dictionary.get_alphabet())
    gui = GUI()
    while True:
        enemy_word = enemy_move(word_list, current_letter)
        print("Słowo przeciwnika:" ,enemy_word)
        current_letter = enemy_word[-1]
        word_list.remove(enemy_word)

        user_word = get_user_word(word_list, current_letter)
        current_letter = user_word[-1]
        word_list.remove(user_word)

        print("Ostatnie słowo:", user_word)

main()