'''
Author: Kevin Zhu
Wordle is owned by the NYT. This class aims to mimic its behavior for python users and is not the actual Wordle.
Please visit https://www.nytimes.com/games/wordle/index.html to play the actual game online.
'''

import random
import time

from collections import Counter
from importlib.resources import open_text

class Wordle:

    '''
    A class that provides a game like Wordle and allows for users to play in Python.

    The aim is to guess a 5-letter word within 6 attempts.

    When you guess the word, you will be given a color-coded result with the following key:

    - Green is the correct letter in the correct spot
    - Yellow is the correct letter but it is in a different spot
    - Gray/White means that the letter is not in the word
    '''

    '''
    Parameters
    ---------
    list custom_word_list, optional:
        a custom list of words to use that can be picked from

    list additional_guess_list, optional:
        a custom list of guesses to use that can be picked from, which must also include all words in custom_word_list

    Raises
    ------
        ValueError: if custom_word_list is [] and custom_guess_list is not []
        ValueError: not all words in custom_word_list are a part of custom_guess_list

    '''

    def __init__(self, custom_word_list = None, custom_guess_list = None):
        if custom_guess_list is not None and custom_word_list is not None:
            if custom_guess_list != [] and custom_word_list == []:
                raise ValueError('custom_word_list cannot be [] if custom_guess_list not also [].')

            elif (custom_guess_list is None and custom_word_list is not None) or (custom_guess_list != [] and not all(word in custom_guess_list for word in custom_word_list)):
                raise ValueError('If custom_word_list is provided, all valid words in custom_word_list must also be in custom_guess_list')

        self.word_list = []
        if custom_word_list is None:
            with open_text('mywordle.data', 'possible_words.txt') as file:
                text = file.read()
                self.word_list = text.splitlines()

        else:
            self.word_list = custom_word_list

        self.guess_list = []
        if custom_word_list is None:
            with open_text('mywordle.data', 'possible_guesses.txt') as file:
                text = file.read()
                self.guess_list = text.splitlines()

        if custom_guess_list is not None:
            self.guess_list += custom_guess_list

        self.word = ''

        # ANSI Colors
        self.GREEN = '\x1B[1m\033[32m'
        self.YELLOW = '\x1B[1m\033[33m'
        self.WHITE = '\x1B[1m\033[37m'
        self.GREY = '\x1B[1m\033[90m'
        self.RESET = '\x1B[0m\033[0m'

        self.keyboard = {}

    def play(self, custom_word = None, challenge_mode = False, word_length = 5, num_guesses = 6, allow_any_word = False):

        '''
        Plays the game Wordle, with the target either being a random word or custom_word!

        Parameters
        ----------
        string custom_word, optional unless if self.word_list = []:
            a word in the list of valid words to use as the target word if allow_any_word is False
            If allow_any_word is True, it must be a string without digits

        boolean challenge_mode, defaults to False:
            if True, players must follow all of the information they were given before--
            letters in green must be in the same place, yellow must appear, and grey must not appear.

        int word_length, defaults to 5:
            the length of the word to take from self.word_list

        int num_guesses, defaults to 6:
            the amount of guesses the player has to win

        boolean allow_any_word, defaults to False:
            allows any string of characters to be the custom_word, thus also allowing any string of characters to be the guess

        Returns
        -------
            A boolean of whether or not the player won

        Raises
        ------
            ValueError: if custom_word is not provided while self.word_list is empty
            ValueError: if the word is not valid or if it has digits
            ValueError: if the a custom word is not provided and the word list is empty
            ValueError: num_guesses or word_length are not positive
            ValueError: if the word_length is not found in self.word_list
        '''

        if not custom_word and self.word_list == []:
            raise ValueError('Since the word list is empty, please provide a custom word')

        if custom_word and not allow_any_word and not self.is_valid_guess(custom_word):
            raise ValueError('Invalid custom word')

        elif custom_word and any(char.isdigit() for char in custom_word):
            raise ValueError('Custom word has digits')

        if num_guesses <= 0:
            raise ValueError('num_guesses must be positive')

        if word_length <= 0:
            raise ValueError('word_length must be positive')

        if not custom_word:
            length_word_list = [word for word in self.word_list if len(word) == word_length]
            if length_word_list == []:
                raise ValueError('word_length is did not yield to any words')

        self.word = custom_word or length_word_list[random.randint(0, len(length_word_list) - 1)]
        self.word = self.word.upper()

        self.keyboard = [
            {'Q': self.WHITE, 'W': self.WHITE, 'E': self.WHITE, 'R': self.WHITE, 'T': self.WHITE, 'Y': self.WHITE, 'U': self.WHITE, 'I': self.WHITE, 'O': self.WHITE, 'P': self.WHITE},
                {'A': self.WHITE, 'S': self.WHITE, 'D': self.WHITE, 'F': self.WHITE, 'G': self.WHITE, 'H': self.WHITE, 'J': self.WHITE, 'K': self.WHITE, 'L': self.WHITE},
                    {'Z': self.WHITE, 'X': self.WHITE, 'C': self.WHITE, 'V': self.WHITE, 'B': self.WHITE, 'N': self.WHITE, 'M': self.WHITE}
        ]

        print(f'The word is ready! It is {len(self.word)} characters long.')
        guesses = []
        challenge_mode_info = []
        win = False

        for i in range(num_guesses):
            while True:
                print('-' * 25)
                self.print_keyboard()
                guess = input(f'Guess #{i + 1}: ').upper()

                if len(guess) != len(self.word):
                    print('Invalid length, please try again')

                elif any(not char.isalpha() for char in guess):
                    print('Only provide a-z. Symbols, numbers, or spaces are not allowed, please try again')

                elif not allow_any_word and not self.is_valid_guess(guess):
                    print('Invalid word, please try again')

                else:
                    if challenge_mode and not self.complete_challenge(guess, challenge_mode_info):
                        print('Because challenge_mode is on, which means your guesses must match the clues given in previous guesses')

                    else:
                        break

            result = self.guess_word(guess)

            full_guess = ''
            for char, color in zip(list(guess), list(result)):
                formatted_char = f'{color}{char}{self.RESET} '
                print(formatted_char, end = '', flush = True)
                full_guess += formatted_char
                time.sleep(0.4)
            print()
            guesses.append(full_guess)
            challenge_mode_info.append(zip(list(guess), list(result)))

            if ''.join(result) == self.GREEN * len(self.word):
                win = True
                break

        formatted_word = self.WHITE
        formatted_word += ' '.join(list(self.word))
        formatted_word += self.RESET

        if win:
            print(f'Congratulations! The word was {formatted_word}. You got it in {i + 1} guesses!')

        else:
            print(f'Sorry, you ran out of guesses! The word was {formatted_word}')

        print('Your guesses: ')
        print('\n'.join(guesses))

        return win

    def is_valid_word(self, word):

        '''
        Determines if this word is valid.

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return self.word_list == [] or word.lower() in self.word_list

    def is_valid_guess(self, word):
        '''
        Determines if this guess is valid.

        Parameters
        ----------
        string word:
            the word to check

        Returns
        -------
        boolean
            whether or not this word is valid
        '''

        return self.guess_list == [] or word.lower() in self.guess_list

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

        for i in range(len(word)):
            if guess_characters[i] == target_characters[i]:
                result.append(self.GREEN)
                self.update_keyboard(target_characters[i], self.GREEN)
                target_characters[i] = None

            else:
                result.append(None)

        for i in range(len(word)):
            if result[i] is None and guess_characters[i] in target_characters:
                result[i] = self.YELLOW
                self.update_keyboard(guess_characters[i], self.YELLOW)
                target_characters[target_characters.index(guess_characters[i])] = None

            elif result[i] is None:
                result[i] = self.GREY
                self.update_keyboard(guess_characters[i], self.GREY)

        return result

    def complete_challenge(self, guess, challenge_mode_info):

        '''
        Determines if this guesses matches challenge mode.

        Parameters
        ----------
            string guess:
                the guess to check
            list challenge_mode_info:
                all previous guesses with a list with a tuple of the letter and the color.

        Returns
        ------
            boolean of whether or not the challenge_mode conditions were met
        '''

        if challenge_mode_info == []:
            return True

        for previous_guess_info in challenge_mode_info:
            guess_letter_counts = Counter(guess)
            required_yellow_counts = Counter()

            # enforce green and count yellow
            for index, ((letter, color), guess_letter) in enumerate(zip(previous_guess_info, guess)):
                if color == self.GREEN:
                    if guess_letter != letter:
                        return False

                    guess_letter_counts[letter] -= 1

                elif color == self.YELLOW:
                    required_yellow_counts[letter] += 1

            # enforce yellow and grrey
            for letter in required_yellow_counts.keys():
                if letter not in guess_letter_counts.keys() or guess_letter_counts[letter] < required_yellow_counts[letter]:
                    return False

            for index, (letter, color) in enumerate(previous_guess_info):
                if color == self.YELLOW:
                    if letter == guess[index]:
                        return False

                    guess_letter_counts[letter] -= 1

                elif color == self.GREY:
                    if letter in guess_letter_counts.keys() and guess_letter_counts[letter] > 0:
                        return False # additional letters that have not been used and are grey may not be used

        return True

    def update_keyboard(self, key, color):

        '''
        Changes the keyboard to reflect the current game.

        Parameters
        ----------
        string key:
            the 1 letter key to update

        string color:
            the ANSI color to update the key with
        '''

        for row in self.keyboard:
            if key in row:
                if row[key] != self.GREEN and color == self.YELLOW:
                    row[key] = color
                    break

                if row[key] != self.GREEN and row[key] != self.YELLOW:
                    row[key] = color
                    break

    def print_keyboard(self):

        '''
        Prints the keyboard with the correct positioning and color coding.
        '''

        indent = ''
        for row in self.keyboard:
            print(indent, end = '')
            for key in row.keys():
                print(row[key] + key + self.RESET + ' ', end = '')
            print()
            indent += ' '