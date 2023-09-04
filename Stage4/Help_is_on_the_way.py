import random

def Guess_the_word():
    print("H A N G M A N")
    words = ('python', 'java', 'swift', 'javascript')
    word = random.choice(words)
    modified_word = word[:3] + '-' * (len(word) - 3)

    print(f"Guess the word {modified_word}: ")
    guess = str(input())

    if guess.lower() == word:
        print("You survived!")
    else:
        print("You lost!")

Guess_the_word()

