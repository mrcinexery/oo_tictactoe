"""
Module represents the game class and contains functions about the flow
"""
from random import randint


class Game:
    """
    The Game class manages the flow of the Tic-Tac-Toe game.

    It coordinates the players, handles the symbol selection,
    determines which player starts, switches turns between players,
    and manages the logic for starting a new game.

    Attributes:
        player1 (Player): The first player.
        player2 (Player): The second player.
        game_board (GameBoard): The game board used for tracking moves.

    Methods:
        input_symbol(): Assigns symbols (X or O) to players.
        whose_start(): Randomly selects which player starts the game.
        switch_turn_flags(): Switches the turn between players.
        new_game(): Prompts players to decide if they want to play another game.
    """

    def __init__(self, player1, player2, game_board):
        self.player1 = player1
        self.player2 = player2
        self.game_board = game_board

    def input_symbol(self):
        """
        Function to input the symbol of player1
        :return:
        """
        while self.player1.get_symbol() not in ['X', 'O']:
            self.player1.set_symbol(input('What is your symbol Player1?'
                                          '\n(You can choose '
                                          'between "X" and "O") '))

        if self.player1.get_symbol() == 'X':
            self.player2.set_symbol('O')
        else:
            self.player2.set_symbol('X')

    def whose_start(self):
        """
        Function to determine a random value between 0 and 1 to decide which
        player start the game.
        """
        number = randint(0, 1)
        if number == 1:
            self.player1.set_turn_flag(True)
            self.player2.set_turn_flag(False)
            print(f'##### {self.player1.get_name()} starts the game. #####')
        else:
            self.player1.set_turn_flag(False)
            self.player2.set_turn_flag(True)
            print(f'##### {self.player2.get_name()} starts the game. #####')

    def switch_turn_flags(self):
        """
        Function to switch the turn flag of the players in order to decide which
        player's turn
        """
        if self.player1.get_turn_flag():
            self.player1.set_turn_flag(False)
            self.player2.set_turn_flag(True)
            print(f"{self.player2.get_name()}\'s turn: ")
        else:
            self.player1.set_turn_flag(True)
            self.player2.set_turn_flag(False)
            print(f"{self.player1.get_name()}\'s turn: ")

    def new_game(self):
        """
        Function to decide if players want to play a new game
        :return: True if players want to play a new game, False if they want not
        play a new game.
        """
        answer = ''
        while answer not in ['y', 'n']:
            answer = input('Would you play another game? (y/n)')

        if answer == 'y':
            self.game_board.reset_board()
            self.player1.print_stats()
            self.player2.print_stats()
            return True
        return False
