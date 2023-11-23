#objetivos: Limpar o console, traduzir o jogo, tentar optimizar mais ainda
import random
import os
import gettext

os.environ['TERM'] = 'xterm'
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

translations = {
    'en': gettext.translation('game', localedir='locale', languages=['en']),
    'pt': gettext.translation('game', localedir='locale', languages=['pt'])
}

language = input("Please enter your preferred language (en/pt): ")

lang = translations.get(language, translations['en'])
lang.install()

lives = 6
word_list = [
    "PUMPKIN", "FRUIT", "SCHOOL", "APPLE", "BANANA", "GRAPE", "ORANGE", "STRAWBERRY", "RASPBERRY", "BLUEBERRY",
    "PYTHON", "JAVA", "JAVASCRIPT", "RUBY", "SWIFT", "KOTLIN", "GO", "RUST", "TYPESCRIPT", "CSHARP", "GITHUB",
    "LONDON", "PARIS", "BERLIN", "MADRID", "ROME", "DUBLIN", "LISBON", "VIENNA", "PRAGUE", "BUDAPEST",
    "ENGLAND", "FRANCE", "GERMANY", "SPAIN", "ITALY", "IRELAND", "PORTUGAL", "AUSTRIA", "SWITZERLAND", "HUNGARY",
    "ELEPHANT", "LION", "TIGER", "BEAR", "GIRAFFE", "ZEBRA", "KANGAROO", "PANDA", "KOALA", "MONKEY",
    "BASKETBALL", "FOOTBALL", "BASEBALL", "SOCCER", "TENNIS", "GOLF", "HOCKEY", "VOLLEYBALL", "RUGBY", "CRICKET",
    "PIANO", "GUITAR", "DRUMS", "VIOLIN", "FLUTE", "SAXOPHONE", "TRUMPET", "HARP", "CELLO", "UKULELE",
    "MATHEMATICS", "PHYSICS", "CHEMISTRY", "BIOLOGY", "ASTRONOMY", "GEOLOGY", "ECOLOGY", "ZOOLOGY", "BOTANY",
    "GENETICS",
    "DEMOCRACY", "MONARCHY", "REPUBLIC", "DICTATORSHIP", "FEDERATION", "CONFEDERATION", "EMPIRE", "KINGDOM",
    "PRINCIPALITY", "WEALTH", "DESTINY",
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN"
]

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

    if "_" not in blanks:
        print(f"You guessed the word: {word}, Congratulations!")
        break

    clear()
    print(blanks)

if lives == 0:
    print(f"You ran out of lives! The word was: {word}")
