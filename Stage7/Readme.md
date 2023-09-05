DESCRIPTION:

The skeleton of the game is ready; let's put some more gameplay meat on it.

In the previous stage, if players entered the same letter twice or more, the program reduced the number of remaining attempts regardless of whether this was a correct letter or not. This doesn’t seem fair, right? Players gain nothing, and the number of attempts gets smaller. Let's fix it!

OBJECTIVES:

To complete this stage, follow the suggested order of the required checks:

Check whether players enter exactly one letter. If not, print Please, input a single letter.. Remember that when players input nothing or non-letter characters, it shouldn't count as a correct input either.

Make sure that the player entered a lowercase English letter. If not, the program should print Please, enter a lowercase letter from the English alphabet.;
If users enter the same letter twice (doesn't matter whether it appears in the word or not), then the program should output You've already guessed this letter.. Do not decrease the number of attempts in this case.

None of the three errors described above should reduce the number of remaining attempts!

When players win, print You guessed the word <word>!, where <word> should be substituted with the uncovered word, and the winning message. Each one should be on a new line.

EXAMPLE 1:

H A N G M A N  # 8 attempts

----------

Input a letter: > a

-a-a------

Input a letter: > i

-a-a---i--

Input a letter: > o

That letter doesn't appear in the word.  # 7 attempts

-a-a---i--

Input a letter: > o

You've already guessed this letter.

-a-a---i--

Input a letter: > p

-a-a---ip-

Input a letter: > p

You've already guessed this letter.

-a-a---ip-

Input a letter: > h

That letter doesn't appear in the word.  # 6 attempts

-a-a---ip-

Input a letter: > k

That letter doesn't appear in the word.  # 5 attempts

-a-a---ip-

Input a letter: > a

You've already guessed this letter.

-a-a---ip-

Input a letter: > z

That letter doesn't appear in the word.  # 4 attempts

-a-a---ip-

Input a letter: > t

-a-a---ipt

Input a letter: > x

That letter doesn't appear in the word.  # 3 attempts

-a-a---ipt

Input a letter: > b

That letter doesn't appear in the word.  # 2 attempts

-a-a---ipt

Input a letter: > d

That letter doesn't appear in the word.  # 1 attempt

-a-a---ipt

Input a letter: > w

That letter doesn't appear in the word.  # 0 attempts

You lost!

EXAMPLE 2:

H A N G M A N  # 8 attempts

----

Input a letter: > j

j---

Input a letter: > i

That letter doesn't appear in the word.  # 7 attempts

j---

Input a letter: > +

Please, enter a lowercase letter from the English alphabet.

j---

Input a letter: > A

Please, enter a lowercase letter from the English alphabet.

j---

Input a letter: > ii

Please, input a single letter.

j---

Input a letter: > ++

Please, input a single letter.

j---

Input a letter: >

Please, input a single letter.

j---

Input a letter: > g

That letter doesn't appear in the word.  # 6 attempts

j---

Input a letter: > a

ja-a

Input a letter: > v

You guessed the word java!

You survived!
