import random


class AI:
    """This class is responsible for conducting moves by the computer in the
    game 'for in a row'"""

    NO_POS_MOVE_MSG = "No possible AI moves."
    ROWS_NUM = 6
    COLS_NUM = 7

    def __init__(self, game, player):
        """The class' constructor, Initialize the game and player object """
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """This function returns a legal move of the player, or raises an
        exception if there are no available moves (the board is full/there
        is a winner)"""

        if self.__game.get_winner() is not None:  # There is a winner (tie/Player A/Player B)
            raise Exception(AI.NO_POS_MOVE_MSG)
        lst_of_moves = list()
        # Checks all of the columns
        for i in range(AI.COLS_NUM):
            if self.__game.get_player_at(0, i) is None:  # There is no player in this place:
                lst_of_moves.append(i)
        # Return a random move
        return random.choice(lst_of_moves)

    def get_last_found_move(self):
        pass

