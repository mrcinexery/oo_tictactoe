"""
Module represents the game board class and all functions with it.
"""

class GameBoard:
    """
    The GameBoard class represents the 3x3 grid for Tic-Tac-Toe.

    It manages the state of the cells, checks for game conditions like a full board or a win,
    and provides methods to update and reset the board. It also includes functionality for
    printing the board and initializing the game rules.

    Attributes:
        cells (list): A list representing the 9 cells of the board.

    Methods:
        get_cell(cell_idx): Returns the value of a specific cell.
        set_cell(symbol, idx): Sets a player's symbol in the given cell.
        is_full(): Checks if all cells are filled (game draw).
        is_cell_engaged(idx): Checks if a specific cell is already occupied.
        contain_cells_win(symbol): Checks if the given symbol has won.
        transform_input(x_coordinate, y_coordinate): Transforms 2D coordinates into a 1D cell index.
        print_rules(): Prints the game rules.
        reset_board(): Resets the board for a new game.
        print_board_game(): Prints the current state of the game board.
        print_board_manual(): Prints the game board with instructions for coordinates.
        set_input_to_board(player): Updates the board with the player's input.
    """

    def __init__(self, cells):
        self.cells = cells

    def get_cell(self, cell_idx):
        """
        Function to return cell
        :param cell_idx: Index of cell
        :return: cell
        """
        return self.cells[cell_idx]


    def set_cell(self, symbol, idx):
        """
        Function to set content of a cell.
        :param symbol: Symbol of the player
        :param idx: Index of cell
        """
        self.cells[idx] = symbol


    def is_full(self):
        """
        Function to check if all cells are engaged.
        If so, a 'Draw' is going to be printed.
        :return: True, if all cells are engaged
        """
        for cell in self.cells:
            if cell not in ['X', 'O']:
                return False

        print('Game board is full!')
        print('It\'s a Draw!')
        return True


    def is_cell_engaged(self, idx):
        """
        Function to check whether a cell is engaged.
        :param idx: Cell index
        :return: True if cell is engaged
        """
        return self.cells[idx] in ['X', 'O']


    def contain_cells_win(self, symbol):
        """
        Function to check whether a player has won.
        :param symbol: Symbol of the player
        :return: True if victory, False if not
        """
        return ((self.cells[1] == symbol and self.cells[2] == symbol and
            self.cells[3] == symbol) or
            (self.cells[4] == symbol and self.cells[5] == symbol and
             self.cells[6] == symbol) or
            (self.cells[7] == symbol and self.cells[8] == symbol and
             self.cells[9] == symbol) or
            (self.cells[1] == symbol and self.cells[4] == symbol and
             self.cells[7] == symbol) or
            (self.cells[2] == symbol and self.cells[5] == symbol and
             self.cells[8] == symbol) or
            (self.cells[3] == symbol and self.cells[6] == symbol and
             self.cells[9] == symbol) or
            (self.cells[1] == symbol and self.cells[5] == symbol and
             self.cells[9] == symbol) or
            (self.cells[3] == symbol and self.cells[5] == symbol and
             self.cells[7] == symbol))


    @staticmethod
    def transform_input(x_coordinate, y_coordinate):
        """
        Static function to transform coordinates to cell_idx
        :param x_coordinate: X-coordinate
        :param y_coordinate: Y-coordinate
        :return: Cell Idx
        """
        dictionary = {(1, 1) : 1, (2, 1) : 2, (3, 1) : 3, (1, 2) : 4,
                       (2, 2) : 5, (3, 2) : 6, (1, 3) : 7, (2, 3) : 8,
                       (3, 3) : 9}

        return dictionary[x_coordinate,y_coordinate]

    def print_rules(self):
        """
        Function to initialise the rules of the game.
        """
        print('###### Welcome to the Tic-Tac-Toe Game! ######')
        print(
            '###### Two players take turns placing their symbols, "X" or "O", on'
            ' a 3x3 grid. ######')
        print(
            '###### The goal is to be the first to align three symbols in a row.'
            '######')
        print('###### This can be done vertically, horizontally, or diagonally.'
              '######')
        print(
            '###### If all spaces are filled and no one has three in a row, the'
            ' game ends in a draw. ######')
        print('')
        self.print_board_manual()
        print('')
        print(
            'Let\'s start by choosing the names and symbols of the players...')


    def reset_board(self):
        """
        Function to reset the board
        """
        for idx in range(len(self.cells)):
            self.cells[idx] = ' '


    def print_board_game(self):
        """
        Function to print the game board
        """
        print(f'\t\t{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')
        print('\t\t--+---+--')
        print(f'\t\t{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print('\t\t--+---+--')
        print(f'\t\t{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')


    def print_board_manual(self):
        """
        Function to print the manual of the game board
        """
        print('\ty')
        print('\t^')
        print(f'3\t|\t{self.cells[7]} | {self.cells[8]} | {self.cells[9]}')
        print('\t|\t--+---+--')
        print(f'2\t|\t{self.cells[4]} | {self.cells[5]} | {self.cells[6]}')
        print('\t|\t--+---+--')
        print(f'1\t|\t{self.cells[1]} | {self.cells[2]} | {self.cells[3]}')
        print('\t----------------> x')
        print('\t\t1\t2\t3')

    def set_input_to_board(self, player):
        """
        Function to set user input to board
        :param player: Player
        """
        while True:
            coordinates = player.input_coordinates()
            cell_idx = self.transform_input(coordinates[0], coordinates[1])

            if not self.is_cell_engaged(cell_idx):
                self.cells[cell_idx] = player.get_symbol()
                break

            print(f'Cell is already engaged with symbol'
                  f'{self.get_cell(cell_idx)}.'
                  f' Please enter new coordinates')
