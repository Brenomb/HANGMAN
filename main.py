#objetivos: Limpar o console, traduzir o jogo, tentar optimizar mais ainda
import random
import os
import gettext

lang_en = gettext.translation('game', localedir='locale', languages=['en'])
lang_pt = gettext.translation('game', localedir='locale', languages=['pt'])

lang = lang_en
lang.install()

clear = lambda: os.system('clear')

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
    guess = input("Guess a letter \n").upper()
    letters_guessed.append(guess)
    found = False

    for i, letter in enumerate(word):
        if letter == guess:
            blanks = blanks[:i] + letter + blanks[i + 1:]
            found = True
            clear()

    if not found:
        lives -= 1
        print(f"Incorrect guess! You have {lives} lives remaining.")
        clear()

    if "_" not in blanks:
        print(f"You guessed the word: {word}, Congratulations!")
        clear()
        break

    print(blanks)

if lives == 0:
    print(f"You ran out of lives! The word was: {word}")
