from words import validwords

alphabet = "abcdefghijklmnopqrstuvwxyz"

def valid(word):
    global validwords
    global alphabet
    word = word.lower()
    wordlist = [*word]
    for i in range(0,26):
        while alphabet[i] in wordlist:
            wordlist.remove(alphabet[i])
    if len(wordlist) > 0:
        print("That is not a word.")
        return False
    else:
        if len(word) != 5:
            print("The word length is not five.")
            return False
        else:
            if word not in validwords:
                print("This is not a valid word.")
                return False
            else:
                return True

def match(ans, guess):
    letters = []
    guess = guess.lower()
    for i in range(0,5):
        if guess[i] in ans and guess[i] not in letters:
            letters.append(guess[i])
    return len(letters)
          