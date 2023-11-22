import random

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

word = word_list[random.randrange(0, len(word_list))]
blanks = "_" * len(word)

while lives > 0:
    guess = input("Guess a letter \n").upper()
    found = False

    for i, letter in enumerate(word):
        if letter == guess:
            blanks = blanks[:i] + letter + blanks[i + 1:]
            found = True

    if not found:
        lives -= 1
        print("Incorrect guess! You have", lives, "lives remaining.")

    if "_" not in blanks:
        print("You guessed the word:", word, "Congratulations!")
        break

    print(blanks)

if lives == 0:
    print("You ran out of lives! The word was:", word)

