#objetivos: traduzir o jogo
import random
import os
import gettext
from words import word_list
from art import stages

os.environ['TERM'] = 'xterm'
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

translations = {
    'en': gettext.translation('game', localedir='locale', languages=['en']),
    'pt': gettext.translation('game', localedir='locale', languages=['pt'])
}

language = input("Please enter your preferred language (en/pt): ")

lang = translations.get(language, translations['pt'])
lang.install()

lives = 6

word = random.choice(word_list)
blanks = "_" * len(word)
letters_guessed = []

while lives > 0:
    print(f"letters guessed: {letters_guessed}")
    print(f"You have {lives} lives remaining.")
    guess = input("Guess a letter \n").upper()
    letters_guessed.append(guess)
    found = False

    for i, letter in enumerate(word):
        if letter == guess:
            blanks = blanks[:i] + letter + blanks[i + 1:]
            found = True

    if not found:
        lives -= 1
        print(stages[lives])

    if "_" not in blanks:
        print(f"You guessed the word: {word}, Congratulations!")
        break

    clear()
    print(blanks)

if lives == 0:
    print(f"You ran out of lives! The word was: {word}")
