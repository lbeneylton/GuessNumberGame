# Guessing Number Game 

A simple CLI (Command Line Interface) game where the player must guess a randomly generated number between **1 and 100**.

---

## How the Game Works

- The game randomly selects a number between **1 and 100**.
- The player tries to guess the number.
- After each attempt, the game gives feedback indicating whether the guess is too high or too low.
- The game ends when the player guesses the correct number or loses the round.

---

## Features

- Play multiple rounds in a single session
- Tracks:
  - Number of attempts
  - Time taken to win or lose a round
- Personal record system based on:
  - Fastest completion time
  - Fewest attempts

---

## Project Structure

- `main.py` Main game file

---

## How to Run

1. Make sure you have **Python 3** installed.
2. Clone this repository:

```bash
git clone https://github.com/lbeneylton/GuessNumberGame
cd GuessNumberGame
```

3. Run the game using the command:

```bash
python main.py
```

or, if necessary:

```bash
python3 main.py
```
---
## Notes

This project is intended for learning and practicing Python basics.

The game runs entirely in the terminal.

Have fun and good luck guessing the number! 😄

---

## Next Steps

 - Implement a JSON file to save game records (time, attempts, and personal bests)
 - Improve CLI interface with colors and formatting with colorama

