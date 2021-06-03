def find_pos_of_zero(board):
    """
    This function checks if there is a zero in the sudoku board or not.
    :param board: the sudoku board.
    :return: returns the position of the zero in the sudoku board, else it
    returns (-1,-1).
    """
    length = len(board)
    for row in range(length):
        for column in range(length):
            if board[row][column] == 0:
                return row, column
    return -1, -1


def valid_option(board, num, position):
    """
    This function checks if we can replace the zero with the choosen number
    or not.
    :param board: the sudoku board.
    :param num: the choosen number.
    :param position: the position of the zero.
    :return: returns True if we can, and False if we cannot.
    """
    row, column = position
    length = len(board)
    if num in board[row]:
        return False
    for index in range(length):
        if board[index][column] == num:
            return False
    r = row
    x = int(length ** 0.5)
    for s in range(x):
        if r % x == 0:
            break
        else:
            r -= 1
    c = column
    for sq in range(x):
        if c % x == 0:
            break
        else:
            c -= 1
    for ro in range(r, r + x):
        for col in range(c, c + x):
            if board[ro][col] == num:
                return False

    return True


def sudoku_helper(board):
    """
    This function returns True if the sudoku board have a solution or not.
    :param board: the sudoku board.
    :return: returns True if there is a solution and False if there is not.
    """
    length = len(board)
    row, column = find_pos_of_zero(board)
    if row == -1:
        return True
    for number in range(1, length + 1):
        validity = valid_option(board, number, (row, column))
        if validity:
            board[row][column] = number
            if not sudoku_helper(board):
                board[row][column] = 0
    print("Sudoku: ")
    for i in range(len(board)):
        print(board[i])
    if find_pos_of_zero(board)[0] == -1:
        return True
    else:
        return False


def solve_sudoku(board):
    """
    This function returns True if the sudoku board have a solution or not.
    :param board: the sudoku board.
    :return: returns True if there is a solution and False if there is not.
    """
    return sudoku_helper(board)


print(solve_sudoku([
        [9, 0, 5, 0, 0, 0, 0, 0, 8],
        [4, 0, 0, 5, 7, 0, 1, 0, 6],
        [0, 2, 7, 6, 0, 0, 0, 4, 0],
        [0, 9, 6, 0, 0, 3, 5, 1, 2],
        [7, 0, 4, 0, 1, 0, 3, 0, 0],
        [2, 1, 0, 9, 8, 0, 0, 0, 4],
        [0, 8, 1, 0, 0, 4, 0, 9, 0],
        [3, 0, 0, 8, 0, 0, 0, 5, 1],
        [0, 0, 2, 0, 0, 7, 0, 6, 0]
    ]))


def print_k_helper(n, k, lst):
    """
    This function prints all the subsets, as list, as long as k,
    and in range of {0,...,n-1}.
    :param n: the range of the numbers.
    :param k: the length of the subsets.
    :param lst: empty list to add the legal subsets.
    :return: the function returns None.
    """
    if n == 0 or k == 0:
        print(lst)
    else:
        for num in range(n):
            if lst != [] and num > lst[-1]:
                lst.append(num)
                print_k_helper(n, k - 1, lst)
                lst.pop()
            elif lst == []:
                lst.append(num)
                print_k_helper(n, k - 1, lst)
                lst.pop()


def print_k_subsets(n, k):
    """
    This function prints all the subsets, as list, as long as k,
    and in range of {0,...,n-1}.
    :param n: the range of the numbers.
    :param k: the length of the subsets.
    :return: the function returns None.
    """
    print_k_helper(n, k, [])
# for i in range(33):
#     print_k_subsets(32,i)

def return_list(cur_set):
    """
    this function make list from cur_set.
    :param cur_set:
    :return: this function returns a list.
    """
    lst = []
    for (idx, in_cur_set) in enumerate(cur_set):
        if in_cur_set:
            lst.append(idx)
    return lst


def k_subset_helper(cur_set, k, index, picked, list_of_lists):
    # Base: we picked out k items.
    if k == picked:
        # print_set(cur_set)
        list_of_lists.append(return_list(cur_set))
        return
    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return
    # Runs on all sets that include this index.
    cur_set[index] = True
    k_subset_helper(cur_set, k, index + 1, picked + 1, list_of_lists)
    # Runs on all sets that do not include index.
    cur_set[index] = False
    k_subset_helper(cur_set, k, index + 1, picked, list_of_lists)
    return list_of_lists


def fill_k_subsets(n, k, lst):
    """
    This function fill a list with all the subsets, as list, as long as k,
    and in range of {0,...,n-1}, but returns anything.
    :param n: the range of the numbers.
    :param k: the length of the legal subsets.
    :param lst: empty list to add legal subsets.
    :return: the function returns None.
    """
    if k <= n:
        k_subset_helper(lst, k, 0, 0, [])


def all_lists_no_arg_helper(n, k, picked):
    """
    this function make a list of the legal lists of legal subsets.
    :param n: the range of the numbers.
    :param k: the length of the legal subsets.
    :param picked:
    :return: the function returns list of lists.
    """
    if k == picked:
        return [[]]

    res = []
    for i in range(n):
        lists_with_i = all_lists_no_arg_helper(n, k, picked + 1)
        for lst in lists_with_i:
            if lst == []:
                lst.append(i)
            else:
                if i > lst[-1]:
                    lst.append(i)
        res += lists_with_i
    return res


def return_k_subsets(n, k):
    """
    this function make a list of the legal lists of legal subsets.
    :param n: the range of the numbers.
    :param k: the length of the legal subsets.
    :return: the function returns list of lists.
    """
    lst = all_lists_no_arg_helper(n, k, 0)
    result = []
    for index in range(len(lst)):
        if len(lst[index]) == k:
            result.append(lst[index])
    return sorted(result)
