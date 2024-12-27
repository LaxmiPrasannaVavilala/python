# Interactive Games: PuzzleGame and WordSearch

Welcome to the **Interactive Games** repository! This project contains two exciting Python-based games:

1. **PuzzleGame**: A sliding number puzzle game.
2. **WordSearch**: An interactive word search game.

---

## Features

### PuzzleGame
- A classic sliding puzzle game with a 4x4 grid.
- Rearrange the numbers in ascending order to solve the puzzle.
- Use arrow keys (`↑`, `↓`, `←`, `→`) for smooth gameplay.
- Intuitive interface with real-time updates.
- Displays congratulatory messages upon solving the puzzle.

### WordSearch
- A word search game with a customizable grid size.
- Automatically generates grids and places words horizontally, vertically, or diagonally.
- Words are hidden among random letters, challenging your search skills.
- Provides interactive feedback on word validation.
- Keeps track of found and unfound words.

---

## Prerequisites

- Python 3.6 or higher
- Required packages: `keyboard` (install via `pip install keyboard`)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/interactive-games.git
   cd interactive-games
   ```

2. Install the required package:
   ```bash
   pip install keyboard
   ```

---

## How to Play

1. Run the main script:
   ```bash
   python main.py
   ```

2. Choose the game to play:
   - Enter `1` to play **PuzzleGame**.
   - Enter `2` to play **WordSearch**.

3. Follow the on-screen instructions for the selected game.

### Controls

#### PuzzleGame:
- Use the following arrow keys to move the blank tile:
  - `↑` for up
  - `↓` for down
  - `←` for left
  - `→` for right
- Press `q` to quit the game.

#### WordSearch:
- Enter the starting position (`row` and `column`) and the word you found (e.g., `0 1 python`).
- Press `q` to quit the game.

---

## Example Output

### PuzzleGame
```
Welcome to the Number Puzzle Game!
Arrange the numbers in ascending order.
Use the arrow keys (↑, ↓, ←, →) to move the blank tile.
Press 'q' to quit the game.

Current Board:
 1  2  3  4
 5  6  7  8
 9 10 11   
13 14 15 12

Waiting for your move...
```

### WordSearch
```
Welcome to the Interactive Word Search Game!
Find the hidden words in the grid.
Enter the starting row, column (0-indexed), and the word.

Word Search Grid:
    0  1  2  3  4  5  6  7  8  9 10 11
     -  -  -  -  -  -  -  -  -  -  -  -
 0 | P Y T H O N    M O D U L E
 1 | ...

Words to Find:
PYTHON - ❌ Not Found
MODULE - ❌ Not Found
...

Enter 'row column word' (or type 'q' to quit):
```

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests for improvements.

### To Do:
- Add more features to the games (e.g., difficulty levels).
- Improve grid visualization for WordSearch.
- Add multiplayer options.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

Thank you for exploring this project! Have fun playing and feel free to share feedback!

