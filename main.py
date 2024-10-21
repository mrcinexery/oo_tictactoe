"""
Module controls the flow of the game
"""
from player import Player
from game_board import GameBoard
from game import Game

if __name__ == "__main__":
    player1 = Player(player='Player1')
    player2 = Player(player='Player2')
    board = GameBoard([' ']*10)
    game = Game(player1, player2, board)

    board.print_rules()
    player1.input_name()
    player2.input_name()
    game.input_symbol()

    GAME_IS_RUNNING = True

    while True:

        game.whose_start()

        while GAME_IS_RUNNING:

            if player1.get_turn_flag():         # player1
                board.set_input_to_board(player1)
                board.print_board_game()

                if board.contain_cells_win(player1.get_symbol()):
                    print(f'{player1.get_name()} has won!')
                    player1.increment_score()
                    break

                if board.is_full():
                    break

                game.switch_turn_flags()

            else:
                # player2
                board.set_input_to_board(player2)
                board.print_board_game()
                if board.contain_cells_win(player2.get_symbol()):
                    print(f'{player2.get_name()} has won!')
                    player2.increment_score()
                    break

                if board.is_full():
                    break

                game.switch_turn_flags()

        if not game.new_game():
            break
