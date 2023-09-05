import random

def Guess_the_word():
    attempts = 8
    words = ['python', 'java', 'swift', 'javascript']
    word = random.choice(words)
    Guess_word = '-' * len(word)
    guessed_letters = []

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
                    return True
            else:
                attempts -= 1
                print("That letter doesn't appear in the word. #" + str(attempts) + " attempts")
                print()

    if attempts == 0:
        print()
        print("You lost!")
        return False

def main():
    games_won = 0
    games_lost = 0

    while True:
        print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        choice = input().lower()

        if choice == "play":
            if Guess_the_word():
                games_won += 1
            else:
                games_lost += 1
        elif choice == "results":
            print(f"You won: {games_won} times")
            print(f"You lost: {games_lost} times")
        elif choice == "exit":
            break
        else:
            print("Invalid input. Please enter 'play', 'results', or 'exit'.")

if __name__ == "__main__":
    main()
