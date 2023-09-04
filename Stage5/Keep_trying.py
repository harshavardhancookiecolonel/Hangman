import random

def Guess_the_word():
    attempts = 8
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    Guess_word = '-' * len(word)

    print('H A N G M A N # ' + str(attempts) + " attempts")
    print()

    while attempts > 0:
        print(Guess_word)
        attempts -= 1
        letter = input("Input a letter: #" + str(attempts) + " attempts")
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    Guess_word = Guess_word[:i] + letter + Guess_word[i + 1:]
        else:
            print("That letter doesn't appear in the word. #" + str(attempts) + " attempts")
    print(Guess_word)
    print()
    print("Thanks for playing!")

Guess_the_word()
