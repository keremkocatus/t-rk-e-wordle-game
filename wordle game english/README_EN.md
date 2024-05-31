# English Wordle Game

This project is an English version of the Wordle-like word guessing game. The player tries to guess the secret word of a given length. Correct letters in the correct position are shown in green, correct letters in the wrong position are shown in yellow, and incorrect letters are shown in gray.

## Features

- Option to play with 5-letter, 6-letter, and 7-letter words
- Correct handling of lower case characters
- Play the game via the terminal

## Requirements

This project requires Python 3 to be installed.

## Installation

1. Clone or download this project.
    ```bash
    git clone https://github.com/your-username/english-wordle.git
    cd english-wordle
    ```

2. Create the necessary word files and place them in the same directory:
    - `words_5.txt`
    - `words_6.txt`
    - `words_7.txt`

   Each of these files should contain the relevant words, one per line.

## Usage

Run the following command in the terminal or command prompt to start the game:
```bash
python game.py
