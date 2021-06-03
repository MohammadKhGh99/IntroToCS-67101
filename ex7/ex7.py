def print_to_n(n):
    """
    this function prints the numbers from 1 to n recursive.
    :param n: the chosen number.
    :return: this number returns None
    """
    if n >= 1:
        print_to_n(n - 1)
        print(n)


def print_reversed(n):
    """
    this function prints the number from n to 1 recursive.
    :param n: the chosen number
    :return: this function returns None
    """
    if n >= 1:
        print(n)
        print_reversed(n - 1)


def has_divisor_smaller_than(n, i):
    """
    this function checks if the number n divides on one of the numbers
    smaller than i.
    :param n: the chosen number.
    :param i: the chosen number to check below it.
    :return: this function returns True if there is number that n divides on
    it and False if not.
    """
    i = int(i)
    if i == 1:
        return True
    elif n % i == 0:
        return False
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """
    this function checks if the chosen number is prime or not.
    :param n: the chosen number.
    :return: this number returns True if it is prime and False if it is not.
    """
    if n <= 1:
        return False
    else:
        return has_divisor_smaller_than(n, int(n ** 0.5))


def factorial(n):
    """
    this function calculates the factorial of the chosen number,
    the multiplication of the numbers from n to 1.
    :param n: the chosen number.
    :return: this function returns the factorial of the number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def exp_n_x(n, x):
    """
    this function calculates the exponential sum from 0 to n.
    :param n: the chosen number.
    :param x: the exponential of e.
    :return: this function returns the exponential sum.
    """
    if n == 0:
        return 1
    else:
        return (x ** n) / factorial(n) + exp_n_x(n - 1, x)


def play_hanoi(hanoi, n, src, dest, temp):
    """
    this function plays the hanoi game.
    :param hanoi: object composed, that he is the graphic game in which the
    change is made.
    :param n: the number of discs.
    :param src: the source column.
    :param dest: the destination column.
    :param temp: the helping column.
    :return: this function returns if the number of the discs is less than 1
    zero, and if not returns None.
    """
    if n < 1:
        return 0
    elif n == 1:
        hanoi.move(src, dest)
    else:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)




def string_from_list(char_list, n, stri):
    """
    this function prints texts with n length from the char list.
    :param char_list: the chosen char list.
    :param n: the chosen number.
    :param stri: the current situation of the stri.
    :return: the function returns None.
    """
    if n < 1:
        print(stri)
    else:
        for i in range(len(char_list)):
            stri += char_list[i]
            string_from_list(char_list, n - 1, stri)
            # stri = stri[:-1]  # deleting the last char in stri

# print(string_from_list(["a","b","c"],2,""))


def print_sequences(char_list, n):
    """
    this function prints texts with n length from the char list, by calling
    the helping function string_from_list.
    :param char_list: the chosen char list.
    :param n: the chosen number.
    :return: the function returns None.
    """
    if n < 1:
        return
    else:
        return string_from_list(char_list, n, '')


def without_char_repeat(char_list, n, stri):
    """
    this function prints texts with n length from the char list, without
    repetition for each char in the stri.
    :param char_list: the chosen char list.
    :param n: the chosen number.
    :param stri: the current situation of the stri.
    :return: the function returns None.
    """
    if n < 1:
        print(stri)
    else:
        for i in range(len(char_list)):
            if char_list[i] not in stri:
                stri += char_list[i]
                without_char_repeat(char_list, n - 1, stri)
                stri = stri[:-1]


def print_no_repetition_sequences(char_list, n):
    """
    this function prints texts with n length from the char list, without
    repetition for each char in the stri, by calling the helping function
    without_char_repeat.
    :param char_list: the chosen char list.
    :param n: the chosen number.
    :return: the function returns None.
    """
    if n < 1:
        return
    else:
        return without_char_repeat(char_list, n, '')


def parenthesis_helper(n, k, stri, str_list):
    """
    this function prints strings contains '(' and ')', but the number of '('
    must be bigger than or equals the number of ')'.
    :param n: the number of '('.
    :param k: the number of ')'.
    :param stri: the current situation of the stri.
    :return: the function returns None.
    """
    if n == 0 and k == 0:
        if stri[-1] == '(' or stri[0] == ')':
            pass
        else:
            str_list.append(stri)
    else:
        if n > 0:
            stri += '('
            parenthesis_helper(n - 1, k, stri, str_list)
            stri = stri[:-1]
        if k > 0 and stri.count('(') > stri.count(')'):
            stri += ')'
            parenthesis_helper(n, k - 1, stri, str_list)
    return str_list



def parentheses(n):
    """
    this function prints strings contains '(' and ')', but the number of '('
    must be bigger than or equals the number of ')'.
    :param n: the number of the pairs of '(' and ')'.
    :return: the function returns None.
    """
    if n < 1:
        return
    else:
        return parenthesis_helper(n, n, '', [])
print(parentheses(4))


def right_up(n, k, stri):
    """
    this function prints texts contains 'u' and 'r' by the number k and n
    respectively.
    :param n: the number of 'r' in the stri.
    :param k: the number of 'u' in the stri.
    :param stri: the current situation of the stri.
    :return: the function returns None.
    """
    if n == 0 and k == 0:
        print(stri)
    if n > 0:
        stri += 'r'
        right_up(n - 1, k, stri)
        stri = stri[:-1]
    if k > 0:
        stri += 'u'
        right_up(n, k - 1, stri)


def up_and_right(n, k):
    """
    this function prints texts contains 'u' and 'r' by the number k and n
    respectively.
    :param n: the number of 'r' in the stri.
    :param k: the number of 'u' in the stri.
    :return: the function returns None.
    """
    if n <= 0:
        print(k * 'u')
    elif k <= 0:
        print(n * 'r')
    else:
        return right_up(n, k, '')


def flood_fill(image, start):
    """
    this function convert the '.' to '*' in the start place and around it in
    the matrix.
    :param image: the chosen matrix (list of lists).
    :param start: the beginning place to start converting.
    :return: this function returns None.
    """
    x, y = start[0], start[1]
    image[x][y] = '*'
    if image[x][y + 1] == '.':
        flood_fill(image, (x, y + 1))
    if image[x][y - 1] == '.':
        flood_fill(image, (x, y - 1))
    if image[x + 1][y] == '.':
        flood_fill(image, (x + 1, y))
    if image[x - 1][y] == '.':
        flood_fill(image, (x - 1, y))
