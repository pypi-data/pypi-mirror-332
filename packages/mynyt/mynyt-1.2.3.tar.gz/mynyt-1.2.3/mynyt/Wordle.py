'''
Author: Kevin Zhu
Wordle is owned by the NYT. This class aims to mimic its behavior for python users and is not the actual Wordle.
Please visit https://www.nytimes.com/games/wordle/index.html to play the actual game online.
'''

import random
import time

from importlib.resources import open_text

class Wordle:

    '''
    A class that provides a game like Wordle and allows for users to play in Python.

    The aim is to guess a 5-letter word within 6 attempts.
    When you guess the word, you will be given a color-coded result with the following key:

    - Green is the correct letter in the correct spot
    - Yellow is the correct letter but it is in a different spot
    - Gray/White means that the letter is not in the word.

    '''

    def __init__(self):
        self.word_list = []
        with open_text('mynyt.data', 'possible_words.txt') as file:
            text = file.read()
            self.word_list = text.split('\n')

        self.guess_list = []
        with open_text('mynyt.data', 'possible_guesses.txt') as file:
            text = file.read()
            self.guess_list = text.split('\n')

        self.word = ''

        self.GREEN = '\033[32m'
        self.YELLOW = '\033[33m'
        self.WHITE = '\033[37m'
        self.RESET = '\033[0m'

    def play(self, custom_word = None):

        '''
        Plays the game Wordle, with the target either being a random word or custom_word!

        Parameters
        ----------
        string custom_word, optional:
            a 5-letter word in the list of vaid words to use as the target word. If it is not valid, defaults to a random word.

        Returns
        -------
            A boolean of whether or not the player won.
        '''

        if custom_word and not self.is_valid_guess(custom_word):
            print('Invalid custom word, using a default one instead.')
            custom_word = None

        self.word = custom_word or self.word_list[random.randint(0, len(self.word_list))]
        self.word = self.word.upper()

        print('The word is ready!')

        for i in range(6):
            while True:
                guess = input(f'Guess #{i + 1}: ').upper()

                if self.is_valid_guess(guess):
                    print('Invalid word, please try again.')

                else:
                    break

            result = self.guess_word(guess)

            for char, color in zip(list(guess), list(result)):
                print(f'{color}{char}{self.RESET} ', end = '', flush = True)
                time.sleep(0.3)
            print()

            if ''.join(result) == self.GREEN * 5:
                print(f'Congratulations! The word was {self.word}. You got it in {i + 1} guess', end = '')
                if i + 1 > 1:
                    print('es', end = '')
                print('!')

                return True

        print(f'Sorry, you ran out of guesses! The word was {self.word}.')
        return False

    def is_valid_word(self, word):

        '''
        Determines if this word is valid (if it has 5 letters and is inside the WORD list).

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return len(word) != 5 or word.lower() not in self.word_list

    def is_valid_guess(self, word):
        '''
        Determines if this guess is valid (if it has 5 letters and is inside the GUESS list).

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return len(word) != 5 or word.lower() not in self.guess_list

    def guess_word(self, guess, target_word = None):

        '''
        Determines whether how close the guess is to the target word.

        Parameters
        ----------
        string guess:
            a valid 5 letter word
        string target_word, optional:
            an optional word to use for the target (defaults to self.word)

        Returns
        -------
        list
            a list of colors depending on each character's value
        '''

        word = target_word or self.word
        result = []
        target_characters = list(word)
        guess_characters = list(guess)

        for i in range(5):
            if guess_characters[i] == target_characters[i]:
                result.append(self.GREEN)
                target_characters[i] = None

            else:
                result.append(None)

        for i in range(5):
            if result[i] is None and guess_characters[i] in target_characters:
                result[i] = self.YELLOW
                target_characters[target_characters.index(guess_characters[i])] = None

            elif result[i] is None:
                result[i] = self.WHITE

        return result