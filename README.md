# GiottoGame_and_Solver
## The Game
Giotto (also called Jotto) is played with two or more people where one person chooses a word for others to guess. The word must be in the English dictionary, can not be a proper noun, and must have five different letters. The other players attempts to guess five letter words, and the amount of correct letters is revealed (i.e. the amount of common letters).

For example, the secret word might be RAISE and someone might guess WATCH, the player with the secret word will then announce 1 because there is only one letter in WATCH that is also in RAISE.

A detailed explanation of the game can be found [Here](https://en.wikipedia.org/wiki/Jotto)

In the program titled "giotto.py", the bot will take the role of the player with the secret word and it will be your job to guess the word that the bot picks and you will have 15 tries. (Note: This game is still under development so you might encounter many different bugs.)

## The Solver
Within this game, there is another file titled "solver.py", simply enter the amount of letters that it got right and it will calculate what is the next best option to enter!
