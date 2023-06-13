# Tic-Tac-Toe AI
This is a Tic-Tac-Toe game implementation with an AI opponent using the minimax algorithm. The game is played on a 3x3 board, and the AI player uses the minimax algorithm to make optimal moves.

# Classes
## BTNode Class
Represents a node in a binary tree. Each node contains data, a reference to the right child node, and a reference to the left child node.

## BTree Class
Represents a binary tree. The tree is initialized with a root node and keeps track of its size. It provides a method to add items to the tree using recursion.

## Board Class
Generates the game board and manages the game logic. It keeps track of the game status, field positions, and the binary tree object. The class provides methods to make moves, check the status of the game, convert coordinates to numbers, and make the AI player's move using the minimax algorithm.

# Usage
Create an instance of the Board class.
Use the make_move method to make moves on the board by providing the position as a tuple (row, column) and the player's turn as a string 'x' or '0'.
The game status can be checked using the get_status method, which returns 'continue' if the game is ongoing, 'x' if player 'x' wins, '0' if player '0' wins, or 'draw' if the game ends in a draw.
The AI player can make its move using the make_computer_move method, which calculates the best move using the minimax algorithm and adds it to the binary tree.
The current state of the game board can be printed using the print function or by converting the Board object to a string using str(board_object).
# Example
```
def main():
    board = {'0': (0, 0), '1': (0, 1), '2': (0, 2),
             '3': (1, 0), '4': (1, 1), '5': (1, 2),
             '6': (2, 0), '7': (2, 1), '8': (2, 2)}
    tree_obj = Board()
    while tree_obj.get_status() == 'continue':
        print(tree_obj)
        enter_inp = input('Enter the coordinates{0-8}\n')
        tree_obj.make_move(board[enter_inp], 'x')
        tree_obj.make_computer_move()
    print(tree_obj.get_status())

main()

```
In the example, the game is played between a human player ('x') and the AI player ('0'). The player enters coordinates from 0 to 8 to make their move. The game continues until the status of the board is not 'continue'. Finally, the result of the game is printed.

Feel free to modify and enhance the code as per your requirements. Enjoy playing Tic-Tac-Toe against the AI opponent!
