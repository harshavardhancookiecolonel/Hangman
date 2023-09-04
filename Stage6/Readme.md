DESCRIPTION:

So far, our game has been some kind of a draft; we still lack a way to handle the player's victory. The player has only eight attempts, and the number of remaining attempts decreases every turn, even if players guess them correctly.

In this stage, we will start reducing the attempts only after players make a mistake. They can be mistaken eight times: attempts are reduced if the suggested letter is not in the word or if it has already been suggested before (no matter whether it's been a correct one or not). If a player has guessed all the letters, they win. If a player has some attempts after guessing the word, discard them, notify the player, and terminate the game.

OBJECTIVES:

Players start the game with eight lives. In other words, they can make a mistake only eight times.

When players input a valid letter, uncover it in the word, and carry on.

Print That letter doesn't appear in the word. and reduce the number of attempts if the word doesn't contain the letter, even if this particular letter has already been suggested before.

Print No improvements. and reduce the attempt' counter when players input a letter that has been successfully uncovered before.

When players win, print the uncovered word, You guessed the word! , and the winning message. Each one should be on a new line.

EXAMPLE 1:

H A N G M A N  # 8 attempts

------

Input a letter: > t

--t---

Input a letter: > z

That letter doesn't appear in the word.  # 7 attempts

--t---

Input a letter: > t

No improvements.  # 6 attempts

--t---

Input a letter: > t

No improvements.  # 5 attempts

--t---

Input a letter: > y

-yt---

Input a letter: > x

That letter doesn't appear in the word.  # 4 attempts

-yt---

Input a letter: > y

No improvements.  # 3 attempts

-yt---

Input a letter: > p

pyt---

Input a letter: > p

No improvements.  # 2 attempts

pyt---

Input a letter: > q

That letter doesn't appear in the word.  # 1 attempt

pyt---

Input a letter: > p

No improvements.  # 0 attempts

You lost!


EXAMPLE 2:

H A N G M A N  # 8 attempts

----

Input a letter: > j

j---

Input a letter: > i

That letter doesn't appear in the word.  # 7 attempts

j---

Input a letter: > g

That letter doesn't appear in the word.  # 6 attempts

j---

Input a letter: > g

That letter doesn't appear in the word.  # 5 attempts

j---

Input a letter: > g

That letter doesn't appear in the word.  # 4 attempts

j---

Input a letter: > g

That letter doesn't appear in the word.  # 3 attempts

j---

Input a letter: > a

ja-a

Input a letter: > v

java

You guessed the word!

You survived!
