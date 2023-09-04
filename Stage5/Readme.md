DESCRIPTION:

Let's make the game iterative. In this stage, we'll adjust our game to resemble the classic version of Hangman. Players should now guess the letters in a word instead of inputting an entire word. If an attempt is successful, uncover the letter. We also need to add the lose condition — players have eight attempts to guess all letters that appear in the word. When players run out of attempts, the game ends.

Don't forget to get rid of the hints: replace all the letters in a word with hyphens at the beginning. Players input one lowercase letter at a time, so there is no need to worry about that.

Later on, we will also determine the win conditions, but in this stage, let's just see how well our player guesses the word on each attempt.


OBJECTIVES:

Your game should work as follows:

Players have exactly eight attempts to guess the word by entering letters one by one. Asking for a letter, print: Input a letter:. If a player uncovered all the letters, but some attempts are still left, the program must continue to ask for input until all the tries are exhausted.

If the letter doesn't appear in the word, the computer takes one try away – even if a user has already suggested this letter – and prints That letter doesn't appear in the word.

If the letter does appear in the word but a user has already suggested this letter and it's open, no need to print any messages.

If all attempts are exhausted, the game ends; the program shows a final message (Thanks for playing!). Otherwise, players can continue to input letters.

We continue to stick with the word list from the previous stage: python, java, swift, javascript. It ensures that your program is tested reliably. Don't worry about javascript. Yes, it's longer than 8 characters, but we'll keep it in the list for consistency since we're not done with developing the game yet and for now there is no win or lose.

EXAMPLES:

H A N G M A N  # 8 attempts

----------

Input a letter: > a  # 7 attempts

-a-a------

Input a letter: > i  # 6 attempts

-a-a---i--

Input a letter: > o

That letter doesn't appear in the word.  # 5 attempts

-a-a---i--
Input a letter: > z

That letter doesn't appear in the word.  # 4 attempts

-a-a---i--

Input a letter: > l

That letter doesn't appear in the word.  # 3 attempts

-a-a---i--

Input a letter: > p  # 2 attempts

-a-a---ip-

Input a letter: > h

That letter doesn't appear in the word.  # 1 attempt

-a-a---ip-

Input a letter: > k

That letter doesn't appear in the word.  # 0 attempts

Thanks for playing!
