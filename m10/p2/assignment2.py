'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def load_words():
   """
   Returns a list of valid words. Words are strings of lowercase letters.

   Depending on the size of the word list, this function may
   take a while to finish.
   """
   print("Loading word list from file...")
   in_file = open(WORDLIST_FILENAME, 'r')
   # line: string
   line = in_file.readline()
   # wordlist: list of strings
   wordlist = line.split()
   print("  ", len(wordlist), "words loaded.")
   return wordlist

def choose_word(wordlist):
   """
   wordlist (list): list of words (strings)

   Returns a word from wordlist at random
   """
   return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def isWordGuessed(secretWord, lettersGuessed):
   '''
   secretWord: string, the word the user is guessing
   lettersGuessed: list, what letters have been guessed so far
   returns: boolean, True if all the letters of secretWord are in lettersGuessed;
     False otherwise
   '''
   for char in secretWord:
       if char not in lettersGuessed:
           return False
   return True
def getGuessedWord(guessedWord, lettersGuessed):
   '''
   secretWord: string, the word the user is guessing
   lettersGuessed: list, what letters have been guessed so far
   returns: string, comprised of letters and underscores that represents
     what letters in secretWord have been guessed so far.
   '''
   # FILL IN YOUR CODE HERE...
   word_out = ''
   for char in secretWord:
       if char in lettersGuessed:
           word_out += char
       else:
           word_out += "_"
   return word_out



def getAvailableLetters(lettersGuessed):
   '''
   lettersGuessed: list, what letters have been guessed so far
   returns: string, comprised of letters that represents what letters have not
     yet been guessed.
   '''
   # FILL IN YOUR CODE HERE...
   import string
   alphabets = string.ascii_lowercase
   for char in lettersGuessed:
       if char in lettersGuessed:
           alphabets = alphabets.replace(char, "")
   return alphabets


def hangman(secretWord):
   '''
   secretWord: string, the secret word to guess.

   Starts up an interactive game of Hangman.

   * At the start of the game, let the user know how many
     letters the secretWord contains.

   * Ask the user to supply one guess (i.e. letter) per round.

   * The user should receive feedback immediately after each guess
     about whether their guess appears in the computers word.

   * After each round, you should also display to the user the
     partially guessed word so far, as well as letters that the
     user has not yet guessed.

   Follows the other limitations detailed in the problem write-up.
   '''
   # FILL IN YOUR CODE HERE...
   print("Welcome to the game, Hangman!")
   print("I am thinking of a word that is ", len(secretWord), "letters long.")

   lettersGuessed = ''
   number_of_guesses = 8

   secretWord_list = list(secretWord)

   while number_of_guesses:

       print("You have ", number_of_guesses, "guesses left")

       print("Available letters: ", getAvailableLetters(lettersGuessed))

       print("Please guess a letter: ")
       guess = input()

       if guess in secretWord and guess not in lettersGuessed:
           lettersGuessed += guess
           print("Good guess: ", getGuessedWord(secretWord, lettersGuessed))
       elif guess in secretWord and guess in lettersGuessed:
           print("Oops! You've already guessed that letter:  ",
                 getGuessedWord(secretWord, lettersGuessed))
       elif guess not in secretWord:
           print("Oops! That letter is not in my word: ",
                 getGuessedWord(secretWord, lettersGuessed))
           number_of_guesses -= 1

       if lettersGuessed == secretWord:
           print("Congratulations, you won!")
           break
       print("Sorry, you ran out of guesses. The word was ", secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

global secretWord
secretWord = choose_word(wordlist).lower()
hangman(secretWord)
