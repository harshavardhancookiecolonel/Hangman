import random

def Guess_the_word():
    attempts = 8
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    Guess_word = '-' * len(word)
    guessed_letters = []

    print('H A N G M A N # ' + str(attempts) + " attempts")
    print()

    while attempts > 0:
        print(Guess_word)
        letter = input("Input a letter: ")

        if len(letter) != 1:
            print("Please, input a single letter.")
            print()
        elif not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
        elif letter in guessed_letters:
            print("You've already guessed this letter.")
        else:
            guessed_letters.append(letter)
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        Guess_word = Guess_word[:i] + letter + Guess_word[i + 1:]
                        print()
                if Guess_word == word:
                    print(word)
                    print("You guessed the word " + Guess_word + "!")
                    print("You survived!")
                    break
            else:
                attempts -= 1
                print("That letter doesn't appear in the word. #" + str(attempts) + " attempts")
                print()

    if attempts == 0:
        print()
        print("You lost!")

Guess_the_word()
