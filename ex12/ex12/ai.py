from random import *
from .game import *
# import time

NO_MOVES = "No possible AI moves."


class AI:

    def __init__(self, game, player):
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        row = randint(0, ROWS)
        column = randint(0, COLUMNS)
        if self.__game.get_winner() is None:
            while self.__game.get_player_at(row, column) is not None:
                row = randint(0, ROWS)
                column = randint(0, COLUMNS)
            return column
        else:
            raise Exception(NO_MOVES)

    def get_last_found_move(self):
        pass

    def get_player(self):
        return self.__player
