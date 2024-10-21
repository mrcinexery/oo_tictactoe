"""
Module represents the player class and contains all function
which are related to that.
"""

import re


class Player:
    """
    Represents a player in the Tic-Tac-Toe game. This class contains attributes
    and methods related to managing the player's details, such as name, symbol,
    score, and turn status.

    Attributes:
        player (str): Identifier for the player (e.g., 'Player1' or 'Player2').
        name (str): The name of the player.
        symbol (str): The player's symbol, either 'X' or 'O'.
        score (int): The player's current score.
        turn_flag (bool): Indicates if it's currently this player's turn.

    Methods:
        get_player(): Returns the player identifier.
        get_name(): Returns the player's name.
        get_symbol(): Returns the player's symbol.
        get_score(): Returns the player's current score.
        get_turn_flag(): Returns the player's turn flag status.
        print_stats(): Prints the player's current statistics.
        set_name(name): Sets the player's name.
        set_symbol(symbol): Sets the player's symbol.
        set_turn_flag(turn_flag): Sets the player's turn flag status.
        increment_score(): Increments the player's score by one.
        input_coordinates(): Prompts the player for valid board coordinates.
        input_name(): Prompts the player to input their name.
    """

    def __init__(self, player='', name='', symbol='', score=0, turn_flag=False):
        self.player = player
        self.name = name
        self.symbol = symbol
        self.score = score
        self.turn_flag = turn_flag

    def get_player(self):
        """
        Function to return player attr of a player.
        :return: Player attr of the player
        """
        return self.player

    def get_name(self):
        """
        Function to return name of a player.
        :return: Name of the player
        """
        return self.name

    def get_symbol(self):
        """
        Function to return symbol of a player.
        :return: Symbol of the player
        """
        return self.symbol

    def get_score(self):
        """
        Function to return score of a player.
        :return: Score of the player
        """
        return self.score

    def get_turn_flag(self):
        """
        Function to return turn flag of a player.
        :return: Turn flag of the player
        """
        return self.turn_flag

    def print_stats(self):
        """
        Function to print stats of a player.
        """
        print(f'Player:: {self.player}, Name: {self.name},'
              f'Symbol: {self.symbol}, Score: {self.score}')

    def set_name(self, name):
        """
        Function to set the name of a player
        :param name: Name of the player
        """
        self.name = name

    def set_symbol(self, symbol):
        """
        Function to set the symbol of a player.
        :param symbol: Symbol of the player
        """
        self.symbol = symbol

    def set_turn_flag(self, turn_flag):
        """
        Function to set the turn_flag of a player.
        :param turn_flag: Turn flag of the player
        """
        self.turn_flag = turn_flag

    def increment_score(self):
        """
        Function to increment the score of the player.
        """
        self.score += 1

    @staticmethod
    def input_coordinates():
        """
        Get input of user - check whether input are valid coordinates.
        :return: tuple of coordinates
        """
        while True:
            coordinate_input = (
                input('Please enter coordinates for placing your symbol: '
                      '\n (You can choose between 1,1 and 3,3) '))

            is_coordinate_valid = (
                re.fullmatch("[1-3],[1-3]", coordinate_input))

            if is_coordinate_valid:
                lst = coordinate_input.split(',')
                return int(lst[0]), int(lst[1])

    def input_name(self):
        """
        Function to input name of player.
        """
        self.set_name(input(f'What is your name {self.get_player()}? '))
