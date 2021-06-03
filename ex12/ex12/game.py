PLAYER_ONE = 1
PLAYER_TWO = 2
ONE_DISC = 'B'
TWO_DISC = 'R'
ILLEGAL_MOVE = "Illegal move."
ILLEGAL_LOCATION = "Illegal location."
EMPTY = '_'
NUM_OF_DISC_WIN = 4
ROWS = 6
COLUMNS = 7
DRAW = 0
ONE_COLOR = "blue"
TWO_COLOR = "red"


class Game:

    def __init__(self):
        self.__board = [['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_'],
                        ['_', '_', '_', '_', '_', '_', '_']]
        self.__current_player = PLAYER_ONE
        self.__list_of_counters = [0, 0, 0, 0, 0, 0, 0]
        if self.__current_player == PLAYER_ONE:
            self.__color = ONE_COLOR
        else:
            self.__color = TWO_COLOR

    def get_list_of_counters(self):
        return self.__list_of_counters

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def make_move(self, column):
        """
        this method make the appropriate move that the player wants.
        :param column: the chosen column to put the disc in it.
        :return: returns None
        """
        flag = False
        row = 5
        if 0 <= column <= 6:
            while 0 <= row < len(self.__board):
                if self.__board[row][column] == EMPTY:
                    flag = True
                    break
                else:
                    row -= 1
            if flag:
                if self.get_current_player() == PLAYER_ONE:
                    self.__board[row][column] = ONE_DISC
                    self.__list_of_counters[column] += 1
                    self.set_current_player(PLAYER_TWO)
                    self.set_color(TWO_COLOR)
                else:
                    self.__board[row][column] = TWO_DISC
                    self.__list_of_counters[column] += 1
                    self.set_current_player(PLAYER_ONE)
                    self.set_color(ONE_COLOR)
                return
        raise Exception(ILLEGAL_MOVE)

    #############    Helpers    ##############

    def replace_matrix_columns_with_rows(self, matrix):
        """
        this function replace the columns of the matrix with its rows
        :param matrix: the matrix that we want to replace its columns
        :return: this function returns the new matrix
        """
        new_matrix = []  # empty matrix to add the new rows(lists) to it
        for row in range(len(matrix[0])):
            mtx = []
            for column in range(len(matrix)):
                mtx.append(matrix[column][row])
            new_matrix.append(list(mtx))
        return new_matrix

    def right_search(self, matrix):
        """
        this method searches for four discs in a row
        :param matrix: the chosen matrix to search in
        :return: returns if there is four in a row the number of the winning
        player if there is not it returns False.
        """
        for row in range(len(matrix)):
            # I know that I can replace range(...) with range(NUM_OF_DISC_WIN)
            for col in range(len(matrix[row]) - NUM_OF_DISC_WIN + 1):
                if matrix[row][col] != EMPTY:
                    disc = matrix[row][col]
                    flag = True
                else:
                    continue
                for i in range(1, NUM_OF_DISC_WIN):
                    if matrix[row][col + i] != disc:
                        flag = False
                if flag:
                    if disc == ONE_DISC:
                        return PLAYER_ONE
                    else:
                        return PLAYER_TWO
        return False

    def diagonal_search_helper(self, matrix):
        """
        this method takes all the diagonal rows and put them in list of lists.
        :return: returns list of lists
        """
        new_matrix = []
        for row in range(ROWS - NUM_OF_DISC_WIN + 1):
            for col in range(COLUMNS - NUM_OF_DISC_WIN + 1):
                single_list = []
                r = row
                c = col
                while 0 <= r <= ROWS - 1 and 0 <= c <= COLUMNS - 1:
                    single_list.append(matrix[r][c])
                    r += 1
                    c += 1
                new_matrix.append(single_list)
        return new_matrix

    def diagonal_search(self, matrix):
        return self.right_search(matrix)

    def blue_wins(self):
        """
        this method checks if player one has been won or not.
        :return: returns True if player one won and False if not.
        """
        down_search_matrix = self.replace_matrix_columns_with_rows(
            self.__board)
        right_diagonal_matrix = self.diagonal_search_helper(self.__board)
        left_diagonal_matrix = self.diagonal_search_helper(self.__board[::-1])
        right_search = self.right_search(self.__board) == PLAYER_ONE
        down_search = self.right_search(down_search_matrix) == PLAYER_ONE
        right_diagonal_search = self.diagonal_search(right_diagonal_matrix) \
                                == PLAYER_ONE
        left_diagonal_search = self.diagonal_search(left_diagonal_matrix) \
                               == PLAYER_ONE
        if right_search or down_search or right_diagonal_search or \
                left_diagonal_search:
            return True
        else:
            return False

    def red_wins(self):
        """
        this method checks if player two has been won or not.
        :return: returns True if player two won and False if not.
        """
        down_search_matrix = self.replace_matrix_columns_with_rows(
            self.__board)
        right_diagonal_matrix = self.diagonal_search_helper(self.__board)
        left_diagonal_matrix = self.diagonal_search_helper(self.__board[::-1])
        right_search = self.right_search(self.__board) == PLAYER_TWO
        down_search = self.right_search(down_search_matrix) == PLAYER_TWO
        right_diagonal_search = self.diagonal_search(right_diagonal_matrix) \
                                == PLAYER_TWO
        left_diagonal_search = self.diagonal_search(left_diagonal_matrix) \
                               == PLAYER_TWO
        if right_search or down_search or right_diagonal_search or \
                left_diagonal_search:
            return True
        else:
            return False

    def check_options(self):
        """
        this method checks if the game board has and empty coordinate or not.
        :return: returns True if there is empty coordinate or not.
        """
        for row in range(ROWS):
            if EMPTY in self.__board[row]:
                return False
        return True

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        # The game may assume this function returns a reasonable representation
        # of the board for printing, but may not assume details about it.
        text = ''
        for row in range(ROWS):
            t = ''
            for column in range(COLUMNS):
                t += self.__board[row][column] + " "
            text += (t + '\n')
        return text

    def empty_the_board(self):
        for row in range(ROWS):
            for column in range(COLUMNS):
                self.__board[row][column] = EMPTY
        self.__list_of_counters = [0] * COLUMNS

    ###############   Helpers   ##############

    def get_winner(self):
        """
        this method checks if there is a winner or is it draw or if the game
        didn't finish yet.
        :return: returns 1 if player one won or 2 if player two won or 0 if
        it is draw or None if the game didn't finish yet.
        """
        if self.blue_wins():
            return PLAYER_ONE
        elif self.red_wins():
            return PLAYER_TWO
        elif self.check_options():
            return DRAW
        else:
            return None

    def get_player_at(self, row, col):
        """
        this method takes the value of the coordinate and returns for who
        from the players it belongs or raises exception if the location is
        illegal.
        :param row: the chosen row coordinate.
        :param col: the chosen column coordinate
        :return: returns the number of the player that the disc belongs to
        or None if there is not any disc in these coordinates
        """
        if (0 <= row <= 5) or (0 <= col <= 6):
            if self.__board[row][col] == ONE_DISC:
                return PLAYER_ONE
            elif self.__board[row][col] == TWO_DISC:
                return PLAYER_TWO
            else:
                return None
        else:
            raise Exception(ILLEGAL_LOCATION)

    def get_current_player(self):
        return self.__current_player

    def set_current_player(self, player):
        self.__current_player = player
