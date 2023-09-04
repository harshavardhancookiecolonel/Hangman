import random

def Guess_the_word(word):
    print("H A N G M A N")
    words = ('python', 'java', 'swift', 'javascript')
    word = str(input("Guess the word: "))
    if word == random.choice(words):
        print("You survived!")
    else:
        print("You lost!")

Guess_the_word("python")
