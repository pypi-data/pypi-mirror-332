# mywordle

mywordle is a library that is simply Wordle.

Millions of people enjoy Wordle every day from the NYT.
However, people cannot access it on Python and it is very difficult to customize.
This library brings this game to Python and lets them put their own twist to it.

- HomePage: https://github.com/kzhu2099/My-Wordle
- Issues: https://github.com/kzhu2099/My-Wordle/issues

Author: Kevin Zhu

## Features

- Allows users to play Wordle
- Allows for wordbank customization
- Allows for multiple lengths
- Allows for guess amount changing
- Has a helpful keyboard color-coder

## Installation

To install mywordle, use pip: ```pip install mywordle```.

However, many prefer to use a virtual environment.

macOS / Linux:

```sh
# make your desired directory
mkdir /path/to/your/directory
cd /path/to/your/directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mywordle
source .venv/bin/activate
pip install mywordle

deactivate # when you are completely done
```

Windows CMD:

```sh
# make your desired directory
mkdir C:path\to\your\directory
cd C:path\to\your\directory

# setup the .venv (or whatever you want to name it)
pip install virtualenv
python3 -m venv .venv

# install mywordle
.venv\Scripts\activate
pip install mywordle

deactivate # when you are completely done
```

## Information

Wordle is a game that is now owned by the NYT.
The aim is to guess a 5-letter word within 6 attempts.
When you guess the word, you will be given a color-coded result with the following key:

- Green is the correct letter in the correct spot
- Yellow is the correct letter but it is in a different spot
- Gray/White means that the letter is not in the word.

## Usage

This game aims to mimic Wordle with thousands of available words.
To use it is very simple! Simply run:

```python
from mywordle import Wordle

game = Wordle()

game.play()
```

Guesses/words are not case sensitive.

You may pass in a custom word to guess for but it must be 5 letters, just like guesses.

It also must be part of the ```guess_list```. This is a list of words that are valid guesses, while ```word_list``` is a list of words that are valid starting points.
Randomly generated words are from the latter, because they are more well known. However, if you want to use a custom target, it must be part of guess_list.

To check if a word falls into either, use ```is_valid_word``` or ```is_valid_guess```

This means that you can guess with ```xylyl``` but it won't ever appear unless if you use ```game.play('xylyl')```.

An intracacy to beware of is the color prioritization.
On the words, it will be easy to understand.
However, on the keyboard, if a letter has been green, it will be green, regardless if the letter is yellow elsewhere or at a different time.
The same applies to yellow, where a different grey will not change the color.
A white letter can change to any, a gray to yellow or green, and a yellow to green.

See examples for more information.

## Customization

Wordle has many variants, and this library's distinction is customization. You may change the amount of guesses or change the word length.

You may alter ```num_guesses``` to be a different amount, like 7.
You may set ```restrict_word = False```.
This setting removes restrictions on word length or its appearance in the ```word_list```, allowing any alphabetical string as a guess.

If you want to have the word ```magazine```, guessed, you may do the following:

```python
game.play('magazine', num_guesses = 7, restrict_word = False)
```

Another option is to input your own ```custom_word_list``` and/or ```custom_guess_list```.
This is sometimes preferable because it allows for a random word to be chosen while preventing a random string of characters from being the guess.

If you provide a ```custom_word_list```, words will be randomly chosen from it, and they can have varying lengths.
To save you from a headache, if you pass ```[]``` for either, any word is allowed for a target word or a guess.

If you set guesses, words may not be empty.
If you set words without setting guesses, it will default to ```[]```.

For example, if you have a list of your own words that you want to use, you can have the following:

```python
game2 = Wordle(['magazine', 'apples', 'oranges'], []) # allows any guesses after picking from this list

game2.play()
```

One caveat of this is that the length of the word is given away.
Make sure that the player doesn't have access to the list or it is sufficiently large enough.

## Disclaimer

Wordle is owned by the NYT. This library provides a version of Wordle that mimics its behavior for personal and non-commercial use.

## License

The License is an MIT License found in the LICENSE file.