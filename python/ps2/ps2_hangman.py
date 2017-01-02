# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

# your code begins here!

def updateAvailalbeLetters(available_letters,guess):
    new_available_letters = available_letters.replace(guess,"")
    return new_available_letters

def trial(word,template,guess):
    if guess in word:
        new_template = ""
        for i in range(len(word)):
            if template[i] == "_":
                if guess == word[i]:
                    new_template += guess
                else:
                    new_template += "_"
            else:
                new_template += template[i]
        template = new_template
        print "Good guess: " + template
    else:
        print "Oops! That letter is not in my word: " + template
        global life
        life -= 1
    return template


wordlist = load_words()
word = choose_word(wordlist)
template = "_"* len(word)
available_letters = "abcdefghijklmnopqrstuvwxyz"
global life
life = 8
print "Welcome to the game, Hangman!"
print "I am thinking of a word that is " + str(len(word)) + " letters long."
while template != word:
    if life > 0:
        print "You have " + str(life) + " guess left."
        print template
        print "Available letters: " + available_letters
        guess = raw_input("Please guess a letter: ")
        while guess not in available_letters:
            print "Available letters: " + available_letters
            guess = raw_input("That letter was already tried before! Guess another letter: ")
        template = trial(word,template,guess)
        available_letters=updateAvailalbeLetters(available_letters,guess)
    else:
        break

if life==0:
    print "You lost! The answer was: " +word
if template == word:
    print "Congratulations, you won!"
