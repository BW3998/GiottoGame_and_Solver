from words import wordlist
import random
from maingamefunctions import valid
from maingamefunctions import match

def giotto():
    tries = 1
    attempt=input("\nWelcome to giotto! You have fifteen guesses to guess an English word with five different letters, what will you first guess be?\n")
    answer = wordlist[random.randrange(0, len(wordlist))]
    while valid(attempt) == False:
        attempt=input()
    while attempt != answer and tries <=13:
        print("You got {} letter(s) right.\n".format(match(answer,attempt)), "\nTry Again!")
        attempt = input()
        tries += 1
        while valid(attempt) == False:
            attempt=input()
    if attempt == answer:
        print("You got it! Great job!")
    else:
        if tries == 15:
            print("You got {} letter(s) right.\n".format(match(answer,attempt)))
            print("\nYou have no tries left! Better luck next time!")
            print("\nThe word was: {}".format(answer))

giotto()