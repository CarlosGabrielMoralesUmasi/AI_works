class BTNode:
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = None
        self.left = None

class BTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, item):
        """Adds item to the tree."""

        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left is None:
                    node.left = BTNode(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BTNode(item)
            else:
                recurse(node.right)

        if self.isEmpty():
            self.root = BTNode(item)
        else:
            recurse(self.root)
        self.size += 1

    def isEmpty(self):
        """
        Returns bool if the tree is empty
        """
        return self.size == 0

class Board:
    """
    Generates the game board
    """
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.x_val = None
        self.y_val = None
        self.coord = None
        self.turn = None
        self.tree = BTree()

    def get_status(self):
        """
        Returns the status of game
        """
        for row in range(3):
            if self.field[row][0] == self.field[row][1] == self.field[row][2] and\
                    self.field[row][0] != ' ':
                return self.field[row][0]
        for col in range(3):
            if self.field[0][col] == self.field[1][col] == self.field[2][col] and\
                    self.field[0][col] != ' ':
                return self.field[0][row]
        """
        Checking the diagonal
        """
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != ' ':
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != ' ':
            return self.field[0][2]
        for element in range(3):
            if self.field[element].count(' ') > 1:
                return 'continue'
        else:
            return 'draw'

    def get_number(self, coord):
        """
        Converts the coordinates to the number for a binary tree
        """
        if coord[0] == 0:
            coef = coord[0] + coord[1]
        elif coord[0] == 1:
            coef = coord[0] + coord[1] + 2
        else:
            coef = coord[0] + coord[1] + 4
        return int(coef)

    def is_position_taken(self, coord):
        """
        Returns bool if the position is taken
        """
        return self.field[coord] != ' '

    def make_move(self, position, turn):
        """
        Makes a move
        :param position: tuple
        :param turn: str
        :return: None
        """
        x_val = position[0]
        y_val = position[1]
        if x_val > 2 and y_val > 2 or self.field[x_val][y_val] != ' ':
            raise IndexError
        self.coord = position
        self.field[x_val][y_val] = turn
        self.turn = turn
        self.tree.add(self.get_number(self.coord))

    def make_computer_move(self):
        """
        Generates a move
        """
        best_score = -5
        best_move = 0
        for row in range(3):
            for col in range(3):
                if self.field[row][col] == ' ':
                    self.field[row][col] = '0'
                    score = self.minimax(-5, False)
                    self.field[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        self.tree.add(self.get_number(best_move))
        self.make_move(best_move, '0')
        return

    def __str__(self):
        result = ''
        for row in range(3):
            if row != 2:
                result += str(self.field[row]) + '\n'
            else:
                result += str(self.field[row])
        return result

    def minimax(self, depth, is_maximizing):
        """
        Implementation of minimax algorithm
        """
        if self.get_status() == 'x':
            return -1
        elif self.get_status() == '0':
            return 1
        elif self.get_status() == 'draw':
            return 0
        if is_maximizing:
            best_score = -1
            for row in range(3):
                for col in range(3):
                    if self.field[row][col] == ' ':
                        self.field[row][col] = '0'
                        score = self.minimax(depth + 1, False)
                        self.field[row][col] = ' '
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 1
            for row in range(3):
                for col in range(3):
                    if self.field[row][col] == ' ':
                        self.field[row][col] = 'x'
                        score = self.minimax(depth + 1, True)
                        self.field[row][col] = ' '
                        if score < best_score:
                            best_score = score
            return best_score



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