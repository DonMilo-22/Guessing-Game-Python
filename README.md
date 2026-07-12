# Guessing Game (Spanish Version)

A simple console based number‑guessing game written in Python. The computer picks a random integer between 1 and 100, and the player has five attempts to guess it. After each guess the program tells you whether the secret number is higher (`+`) or lower (`-`) and displays a random, humorous Spanish hint.

## Features
- Randomized secret number each round.
- Five attempts with a clear attempt counter.
- Playful Spanish hints for "too high" and "too low".
- Optional "doble o nada" (double‑or‑nothing) continuation after a win.
- Replay option after a loss.

## Prerequisites
- Python 3.6 or newer (the script uses only the standard library).

## Installation
1. Clone the repository or copy the `Game v1.0.py` file.
2. Ensure you have Python installed. You can check with:
   ```bash
   python3 --version
   ```
3. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

## Running the Game
Execute the script from the terminal:
```bash
python3 "Game v1.0.py"
```
Follow the on‑screen prompts (in Spanish) to guess the number.

## License
This project is released under the MIT License – see the `LICENSE` file for details.
