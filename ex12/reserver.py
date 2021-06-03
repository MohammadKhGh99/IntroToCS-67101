#game_ex12#

# for row in range(len(matrix)):
#     for
# for row in range(ROWS - NUM_OF_DISC_WIN + 1):
#     for col in range(COLUMNS - NUM_OF_DISC_WIN + 1):
#         if self.__board[row][col] != EMPTY:
#             disc = self.__board[row][col]
#             flag = True
#             curr = row
#             curr += 1
#         else:
#             continue
#         while 1 <= curr <= row +
#             for i in range(1, NUM_OF_DISC_WIN):
#                 if self.__board[row][col + i] != disc:
#                     flag = False
#         if flag:
#             if disc == ONE_DISC:
#                 return PLAYER_ONE
#             else:
#                 return PLAYER_TWO
# return False

# def search(self):
#     down_search_matrix = self.replace_matrix_columns_with_rows(
#         self.__board)
#     right_diagonal_matrix = self.diagonal_search_helper()
#     left_diagonal_matrix = right_diagonal_matrix[::-1]
#     right_search = self.right_search(self.__board)
#     down_search = self.right_search(down_search_matrix)
#     right_diagonal_search = self.diagonal_search(right_diagonal_matrix)
#     left_diagonal_search = self.diagonal_search(left_diagonal_matrix)
#     if right_search==PLAYER_ONE or down_search==PLAYER_ONE or \
#     right_diagonal_search==PLAYER_ONE or
# left_diagonal_search==PLAYER_ONE:
#         return PLAYER_ONE

