# Words, Words, Words

Words, Words, Words is a simple Python word guessing game designed to help users improve their vocabulary and word recognition skills. The game selects a random word from a predefined list, and the player has a limited number of turns to guess it correctly.

## Features

- Random word selection from a word bank
- Feedback on guessed letters, including correct letters and misplaced letters
- 5 turns to guess the word correctly
- Encourages letter and word recognition

## How to Play

1. The game will randomly select a word from the word bank (words.txt).
2. You will be informed of the number of letters in the word.
3. Enter your guess, which must have the same number of letters as the secret word.
4. After each guess, you will receive feedback:
   - Correct letters in the right position will be displayed.
   - Misplaced letters (correct letters in the wrong position) will be tracked,
   - Incorrect letters will also be noted.
5. You have 5 turns to guess the word correctly.

## Example

```zsh
Welcome to Words, Words, Words

There are 5 letters in the word

You have 5 turns remaining

Enter your guess: apple
a _ _ _ _

Misplaced letters: ['p']
Incorrect letters: ['l', 'e']

You have 4 turns remaining
Enter your guess: plane
p l _ _ _
```

## How to Run

1. Make sure you have Python installed on your machine.
2. Clone this repository or download the script.
3. Place your word list in a file named words.txt in the same directory as the script.
4. Run the script using the following command:

```bash
python app.py
```

## License

This project is open source and free to use.

This README should give users an understanding of how to play and run the game!
