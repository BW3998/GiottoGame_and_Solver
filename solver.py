from maingamefunctions import match
from random import choice
from words import wordlist

def solvervalid(input):
    numbers = "1234567890."
    inputlist = [*input]
    if input == "WIN":
        return True
    else:
        for i in range(0,11):
            while numbers[i] in inputlist:
                inputlist.remove(numbers[i])
        if len(inputlist) > 0:
            print("That is not a number.")
            return False
        else:
            if int(input) > 5 or int(input) < 0:
                print("That is not a valid number.")
                return False
            else:
                return True
    

def solver():
    global wordlist
    guess = choice(wordlist)
    tries = 1
    print("Having trouble in your giotto game? Use this solver to quickly find the best choice to enter and gurantee a win! If you want to stop the program, simply enter \"WIN\". To start, use word shown below and enter the number of right letters!")
    print("\n{}".format(guess))
    feedback = input()
    list = wordlist
    while solvervalid(feedback) == False:
        feedback = input()
    while feedback != "WIN" and tries <14:
        feedback = int(feedback)
        words = []
        if feedback == 5:
            list.remove(guess)
        for i in range(0, len(list)):
            if match(guess, list[i]) == feedback:
                words.append(list[i])
        guess = choice(words)
        print("\n{}".format(guess))
        feedback = input()
        while solvervalid(feedback) == False:
            feedback = input()
        list = words
        tries += 1
    if feedback == "WIN":
        print("\nHere is how many tries it took: {}.".format(tries))

solver()