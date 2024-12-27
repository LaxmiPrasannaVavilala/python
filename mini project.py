import random
import keyboard
class PuzzleGame:
    def __init__(self):
        self.grid_size = 4
        self.board = []
        self.blank_tile = None
        self.initialize_board()
    def initialize_board(self):
        """Initialize the puzzle board with numbers and one blank space."""
        numbers = list(range(1, self.grid_size**2)) + [0]
        random.shuffle(numbers)
        self.board = [numbers[i:i + self.grid_size] for i in range(0, len(numbers), self.grid_size)]
        self.blank_tile = self.find_blank_tile()
    def find_blank_tile(self):
        """Locate the position of the blank tile (0)."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.board[row][col] == 0:
                    return row, col
    def display_board(self):
        """Display the current state of the board."""
        print("\nCurrent Board:")
        for row in self.board:
            print(" ".join(f"{num:2}" if num != 0 else "  " for num in row))
    def move_tile(self, direction):
        """Move the blank tile in the specified direction."""
        row, col = self.blank_tile
        if direction == "up" and row > 0:
            self.swap_tiles(row, col, row - 1, col)
        elif direction == "down" and row < self.grid_size - 1:
            self.swap_tiles(row, col, row + 1, col)
        elif direction == "left" and col > 0:
            self.swap_tiles(row, col, row, col - 1)
        elif direction == "right" and col < self.grid_size - 1:
            self.swap_tiles(row, col, row, col + 1)
        else:
            print("Invalid move. Try a different direction.")
    def swap_tiles(self, row1, col1, row2, col2):
        """Swap two tiles on the board."""
        self.board[row1][col1], self.board[row2][col2] = self.board[row2][col2], self.board[row1][col1]
        self.blank_tile = (row2, col2)
    def is_solved(self):
        """Check if the puzzle is solved."""
        solved_numbers = list(range(1, self.grid_size**2)) + [0]
        flat_board = [num for row in self.board for num in row]
        return flat_board == solved_numbers
    def play(self):
        """Main game loop."""
        print("Welcome to the Number Puzzle Game!")
        print("Arrange the numbers in ascending order.")
        print("Use the arrow keys (↑, ↓, ←, →) to move the blank tile.")
        print("Press 'q' to quit the game.")
        self.display_board()
        while not self.is_solved():
            print("\nWaiting for your move...")
            while True:
                key = keyboard.read_event()
                if key.event_type == "down": 
                    if key.name == "up":
                        self.move_tile("up")
                        break
                    elif key.name == "down":
                        self.move_tile("down")
                        break
                    elif key.name == "left":
                        self.move_tile("left")
                        break
                    elif key.name == "right":
                        self.move_tile("right")
                        break
                    elif key.name == "q":
                        print("Thanks for playing!")
                        return
                    else:
                        continue           
            self.display_board()
        print("🎉 Congratulations! You solved the puzzle! 🎉")
        

class WordSearch:
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]
        self.words = []  
        self.placed_words = []
        self.found_words = []
    def add_words(self, word_list):
        """Add words to the word search and place them on the grid."""
        self.words = word_list
        for word in self.words:
            if self.place_word(word.upper()):
                continue
            else:
                print(f"Couldn't place the word: {word}")

    def place_word(self, word):
        """Attempt to place a word on the grid."""
        directions = ["horizontal", "vertical", "diagonal"]
        random.shuffle(directions)
        for direction in directions:
            if self.try_place_word(word, direction):
                return True
        return False

    def try_place_word(self, word, direction):
        """Try to place the word in a specific direction."""
        max_attempts = 100
        for _ in range(max_attempts):
            if direction == "horizontal":
                row = random.randint(0, self.grid_size - 1)
                col = random.randint(0, self.grid_size - len(word))
            elif direction == "vertical":
                row = random.randint(0, self.grid_size - len(word))
                col = random.randint(0, self.grid_size - 1)
            elif direction == "diagonal":
                row = random.randint(0, self.grid_size - len(word))
                col = random.randint(0, self.grid_size - len(word))
            else:
                return False

            if self.can_place_word(word, row, col, direction):
                self.fill_word(word, row, col, direction)
                return True
        return False

    def can_place_word(self, word, row, col, direction):
        """Check if a word can be placed at the given position."""
        for i in range(len(word)):
            if direction == "horizontal" and self.grid[row][col + i] not in (" ", word[i]):
                return False
            if direction == "vertical" and self.grid[row + i][col] not in (" ", word[i]):
                return False
            if direction == "diagonal" and self.grid[row + i][col + i] not in (" ", word[i]):
                return False
        return True

    def fill_word(self, word, row, col, direction):
        """Fill the word in the grid and save its position."""
        positions = []
        for i in range(len(word)):
            if direction == "horizontal":
                self.grid[row][col + i] = word[i]
                positions.append((row, col + i))
            elif direction == "vertical":
                self.grid[row + i][col] = word[i]
                positions.append((row + i, col))
            elif direction == "diagonal":
                self.grid[row + i][col + i] = word[i]
                positions.append((row + i, col + i))
        self.placed_words.append({"word": word, "positions": positions})

    def fill_empty_spaces(self):
        """Fill empty spaces in the grid with random letters."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                if self.grid[row][col] == " ":
                    self.grid[row][col] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def display_grid(self):
        """Display the word search grid with row and column numbers."""
        print("\nWord Search Grid:")
        print("    " + "".join(f"{col:2}" for col in range(self.grid_size)))  
        print("     " + " ".join("-" for _ in range(self.grid_size)))
        for row in range(self.grid_size):
            print(f"{row:2} | " + " ".join(self.grid[row]))
        print("\n")

    def display_words(self):
        """Display the list of words to find."""
        print("\nWords to Find:")
        for word_info in self.placed_words:
            word = word_info["word"]
            status = "✔ Found" if word in self.found_words else "❌ Not Found"
            print(f"{word} - {status}")
    def validate_word(self, row, col, word):
        """Check if the word starts at the given row and column."""
        word = word.upper()
        for word_info in self.placed_words:
            if word_info["word"] == word:
                positions = word_info["positions"]
                if (row, col) == positions[0]: 
                    if word not in self.found_words:
                        self.found_words.append(word)
                        print(f"✔ Correct! You found the word: {word.upper()}")
                        return
                    else:
                        print(f"You already found the word: {word.upper()}. Try another one.")
                        return
        print(f"❌ Incorrect! {word.upper()} is not starting at ({row}, {col}).")

    def play(self):
        """Start the interactive game."""
        self.fill_empty_spaces()
        print("Welcome to the Interactive Word Search Game!")
        print("Find the hidden words in the grid.")
        print("Enter the starting row, column (0-indexed), and the word.")
        while set(self.found_words) != set([info["word"] for info in self.placed_words]):
            self.display_grid()
            self.display_words()
            user_input = input("\nEnter 'row column word' (or type 'q' to quit): ").strip()
            if user_input.lower() == "q":
                print("Thank you for playing!")
                break
            try:
                row, col, word = user_input.split()
                row, col = int(row), int(col)
                if 0 <= row < self.grid_size and 0 <= col < self.grid_size:
                    self.validate_word(row, col, word)
                else:
                    print(f"Invalid coordinates! Row and column should be between 0 and {self.grid_size - 1}.")
            except ValueError:
                print("Invalid input. Please enter in the format 'row column word'.")
        else:
            print("\n🎉 Congratulations! You found all the words! 🎉")
       
if __name__ == "__main__":
    print("1.PuzzleGame")
    print("2.WordSearch")
    ip=input("Enter a number to choose game:")
    if ip=='0':
        print("Thank you for playing! Goodbye!")
    elif ip=='1':
        game = PuzzleGame()
        game.play()
    elif ip=='2':
        word_list = ["python", "class", "object", "module", "inheritance", "function", "method"]
        game = WordSearch(grid_size=12)
        game.add_words(word_list)
        game.play()
    else:
        print("You Entered a Invalid Number")
