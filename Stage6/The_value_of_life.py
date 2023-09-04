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
        letter = input("Input a letter: ")
        if letter in word:
            if letter in Guess_word:
                attempts -= 1
                print("No Improvements. # " + str(attempts) + " attempts")
            else:
                for i in range(len(word)):
                    if word[i] == letter:
                        Guess_word = Guess_word[:i] + letter + Guess_word[i + 1:]
                        print()
        else:
            attempts -= 1
            print("That letter doesn't appear in the word. #" + str(attempts) + " attempts")
            print()
        if Guess_word == word:
            print(word)
            print("You guessed the word!")
            print("You survived!")
            break

    if attempts == 0:
        print()
        print("You lost!")

Guess_the_word()
