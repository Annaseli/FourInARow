class Game:
    """This class represents the game "for in a row". It's in charge on
    the logic of the game and allows the players to make moves in the game"""

    ILLEGAL_MOVE_MSG = "Illegal move"
    ILLEGAL_LOC_MSG = "Illegal location"
    PLAYER_A_SYMBOL = "A"
    PLAYER_B_SYMBOL = "B"
    A_WIN = "AAAA"
    B_WIN = "BBBB"
    EMPTY_PLACE = "-"
    ROWS_NUM = 6
    COLS_NUM = 7

    def __init__(self):
        """The class' constructor, initialize the board, and the number of
        turns that were conducted by both of the players"""

        self.player_A_discs_num = 0  # Num of turns that was conducted by A
        self.player_B_discs_num = 0  # Num of turns that was conducted by B
        self.__last_disc_entered = []
        # The board
        self.__board = [[Game.EMPTY_PLACE for j in range(Game.COLS_NUM)]
                        for i in range(Game.ROWS_NUM)]

    def get_last_disc_entered(self):
        return self.__last_disc_entered

    def get_board(self):
        return self.__board

    def make_move(self, column):
        """This function gets a col number, and makes a move  - if the col
        num is legal (0-6 and there is a place in this col) - it will add a
        disc of the current player to this col.
        If the move is not legal - the function will raise an exception"""

        # Out of the range
        if column < 0 or column > Game.COLS_NUM - 1:
            raise Exception(Game.ILLEGAL_MOVE_MSG)
        # The col is full
        if self.__board[0][column] != Game.EMPTY_PLACE:
            raise Exception(Game.ILLEGAL_MOVE_MSG)

        # Get the first empty place in the col
        empty_r, empty_c = self.get_empty_place(column)
        # If this is player A's turn
        if self.get_current_player() == 1:
            self.__board[empty_r][empty_c] = Game.PLAYER_A_SYMBOL
            self.__last_disc_entered.clear()
            self.__last_disc_entered.extend([empty_r, empty_c, self.PLAYER_A_SYMBOL])
            self.player_A_discs_num += 1
        # If this is player B's turn
        else:
            self.__board[empty_r][empty_c] = Game.PLAYER_B_SYMBOL
            self.__last_disc_entered.clear()
            self.__last_disc_entered.extend([empty_r, empty_c, self.PLAYER_B_SYMBOL])
            self.player_B_discs_num += 1

    def get_empty_place(self, col):
        """This function gets a col num, and returns the first index (row,
        col) that is available (containing an empty place in the col).
        If there is no empty place, the function will return None [to both
        of the indexes (None, None)]"""

        # Check if there is an empty place
        for i in range(Game.ROWS_NUM - 1, -1, -1):
            if self.__board[i][col] == Game.EMPTY_PLACE:
                return i, col
        return None, None  # none otherwise

    def get_current_player(self):
        """This function returns 1 if the current turn is of player A,
        and 2 if the current tern is of player B"""

        if self.player_A_discs_num <= self.player_B_discs_num:
            return 1
        else:
            return 2

    def get_player_at(self, row, col):
        """This function gets indexes (row, col), and checks the data that
        in this place. If a disc of player A is in this place, the function
        will return 1. If a disc of player B is in this place - the function
        will 2. It the place is empty - the func will return None.
        In addition, if the indexes (row/col) is illegal, the function will
        raise an exception."""

        # The row index out of range
        if row < 0 or row > Game.ROWS_NUM - 1:
            raise Exception(Game.ILLEGAL_LOC_MSG)
        # The col index is out of range
        if col < 0 or col > Game.COLS_NUM - 1:
            raise Exception(Game.ILLEGAL_LOC_MSG)
        # A in this place
        if self.__board[row][col] == Game.PLAYER_A_SYMBOL:
            return 1
        # B in this place
        elif self.__board[row][col] == Game.PLAYER_B_SYMBOL:
            return 2
        # AN empty place
        else:
            return None

    def get_winner(self):
        """This function checks if there is a winner in the game (4 discs in
        a row/col/diagonal of the same player. If so - the function will
        return the winner player (A - 1, B - 2).
        It the game is over and there is not winners, the func will return
        0. If the game isn't over yet - it will return None"""

        all_directions_lst = list()
        # All the rows and col discs
        all_directions_lst.extend(self.check_rows_and_cols())
        # All the diagonal discs
        all_directions_lst.extend(self.check_diaganol())
        is_ended = True
        # Check if on of the combination is a winner
        for i in range(len(all_directions_lst)):
            if Game.A_WIN in all_directions_lst[i]:
                return 1
            if Game.B_WIN in all_directions_lst[i]:
                return 2
            # Check if there is an empty cell in the board
            if Game.EMPTY_PLACE in all_directions_lst[i]:
                is_ended = False
        # If there are no empty cells in the game and no winners
        if is_ended:
            return 0
        # If the game isn't over yet
        else:
            return None

    def check_rows_and_cols(self):
        """This function returns a list of all of the discs that in a row
        and in a col of the board"""

        col_str = ""
        row_str = ""
        vertical_and_hori_lst = list()

        # Checks all of the rows, and col 0-5
        for i in range(Game.ROWS_NUM):
            for j in range(Game.COLS_NUM):
                # Check that we are in the range
                if j < Game.ROWS_NUM:
                    col_str += self.__board[j][i]
                row_str += self.__board[i][j]
            # Adds the row&col discs
            vertical_and_hori_lst.append(col_str)
            vertical_and_hori_lst.append(row_str)
            col_str = ""
            row_str = ""

        # Check the last col
        for k in range(Game.ROWS_NUM):
            col_str += self.__board[k][Game.ROWS_NUM]
        vertical_and_hori_lst.append(col_str)

        return vertical_and_hori_lst

    def check_diaganol(self):
        """This function returns a list of all of the discs that in a
        diagonal direction in the board (upper from ltr and from rtl
        direction"""
        diagonal_list = list()
        up_str = ""

        # UP DIRECTION - LEFT TO RIGHT
        # Upper triangle

        less_row_n = 0
        while less_row_n < Game.ROWS_NUM:
            i = less_row_n
            j = 0
            while i >= 0:
                up_str += self.__board[i][j]
                i -= 1
                j += 1
            diagonal_list.append(up_str)
            up_str = ""
            less_row_n += 1
        # Lower triangle
        less_col_n = 1
        while less_col_n < Game.COLS_NUM:
            i = Game.ROWS_NUM - 1
            j = less_col_n
            while j < Game.COLS_NUM:
                up_str += self.__board[i][j]
                i -= 1
                j += 1
            diagonal_list.append(up_str)
            up_str = ""
            less_col_n += 1

        # UP DIRECTION - RIGHT TO LEFT
        # Upper triangle
        row_n = Game.ROWS_NUM
        while row_n > 0:
            i = Game.ROWS_NUM - row_n
            j = Game.ROWS_NUM
            while i >= 0:
                up_str += self.__board[i][j]
                i -= 1
                j -= 1
            diagonal_list.append(up_str)
            up_str = ""
            row_n -= 1
        # Lower triangle
        less_col = 1
        while less_col < Game.COLS_NUM:
            i = Game.ROWS_NUM - 1
            j = Game.ROWS_NUM - less_col
            while j >= 0:
                up_str += self.__board[i][j]
                i -= 1
                j -= 1
            diagonal_list.append(up_str)
            up_str = ""
            less_col += 1
        return diagonal_list  # return the list


if __name__ == '__main__':
    pass
