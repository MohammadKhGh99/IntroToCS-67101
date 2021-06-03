################################################################
#                       Tester for ex7                         #
################################################################
# Move to the same folder with ex7 then run through the pytest #
# Nadav Har-Tuv                                                #
# nadav.har-tuv1@mail.huji.ac.il                               #
################################################################

import ex7
import math


def nCr(n, r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))


def test_print_to_n():
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_to_n(5)
    assert [1, 2, 3, 4, 5] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_to_n(0)
    assert [] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_to_n(1)
    assert [1] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_to_n(-7)
    assert [] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_to_n(10)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == output


def test_print_reversed():
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_reversed(5)
    assert [5, 4, 3, 2, 1] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_reversed(0)
    assert [] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_reversed(1)
    assert [1] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_reversed(-7)
    assert [] == output

    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_reversed(10)
    assert [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] == output


def test_is_prime():
    assert ex7.is_prime(0) is False
    assert ex7.is_prime(1) is False
    assert ex7.is_prime(2) is True
    assert ex7.is_prime(3) is True
    assert ex7.is_prime(4) is False
    assert ex7.is_prime(5) is True
    assert ex7.is_prime(6) is False
    assert ex7.is_prime(7) is True
    assert ex7.is_prime(8) is False
    assert ex7.is_prime(17) is True
    assert ex7.is_prime(25) is False
    assert ex7.is_prime(19) is True
    assert ex7.is_prime(100) is False
    assert ex7.is_prime(-5) is False
    assert ex7.is_prime(47) is True
    assert ex7.is_prime(-100) is False
    try:
        assert ex7.is_prime(1973) is True
    except RecursionError:
        print("**********************************")
        print("The code works! but is ineffective")
        print("**********************************")
        assert ex7.is_prime(1973) is True


def test_exp_n_x():
    nums = [1, 1.4, 2.2, 3, 5, 19, 3.2, -3.7, -2, 0]
    for x in nums:
        sum = 0
        for i in range(0, 30):
            sum += (x**i) / math.factorial(i)
            assert sum == ex7.exp_n_x(i, x)


def test_play_hanoi_1():
    src = ['A', 'B', 'C', 'D', 'E']
    dest = []
    temp = []
    print(type(hanoi))
    game = hanoi()
    ex7.play_hanoi(game, 5, src, dest, temp)
    assert src == []
    assert temp == []
    assert dest == ['A', 'B', 'C', 'D', 'E']


def test_play_hanoi_2():
    src = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    dest = []
    temp = []
    game = hanoi()
    ex7.play_hanoi(game, 4, src, dest, temp)
    assert src == ['A', 'B', 'C']
    assert temp == []
    assert dest == ['D', 'E', 'F', 'G']


def test_play_hanoi_3():
    src = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    dest = []
    temp = []
    game = hanoi()
    ex7.play_hanoi(game, 0, src, dest, temp)
    assert src == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert temp == []
    assert dest == []


def test_play_hanoi_4():
    src = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    dest = []
    temp = []
    game = hanoi()
    ex7.play_hanoi(game, -4, src, dest, temp)
    assert src == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert temp == []
    assert dest == []


def test_print_sequences():
    char_list = ['a', 'c', 'd', 't', 'G', '7']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_sequences(char_list, 6)
    assert len(output) == len(char_list) ** 6
    assert 'adcGt7' in output
    assert '7GGGdc' in output
    assert 'cccccc' in output
    assert 'tatata' in output
    assert '77777d' in output
    assert 'a7cdcc' in output
    for stri in output:
        assert len(stri) == 6
        for char in stri:
            assert char in char_list
    assert len(set(output)) == len(output)

    char_list = ['R']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_sequences(char_list, 6)
    assert len(output) == len(char_list) ** 6
    assert ['RRRRRR'] == output

    char_list = ['1', '2', 'F', 'D']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_sequences(char_list, 0)
    assert [] == output


def test_print_no_repetition_sequences():
    char_list = ['a', 'c', 'd', 't', 'G', '7', 'S']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_no_repetition_sequences(char_list, 6)
    assert len(output) == (nCr(len(char_list), 6)*math.factorial(6))
    assert 'adcGt7' in output
    assert 'tG7acd' in output
    assert 'tG7aSd' in output
    assert '7StaGd' in output
    for stri in output:
        assert len(stri) == 6
        for char in stri:
            assert char in char_list
    assert len(set(output)) == len(output)

    char_list = ['1', '2', 'F', 'D']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_no_repetition_sequences(char_list, 0)
    assert [] == output

    char_list = ['1', '2', 'F', 'D']
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.print_no_repetition_sequences(char_list, 2)
    assert len(output) == nCr(len(char_list), 2)*2
    assert '12' in output
    assert '1F' in output
    assert 'F1' in output
    assert 'DF' in output
    assert '2D' in output
    assert '1D' in output
    for stri in output:
        assert len(stri) == 2
        for char in stri:
            assert char in char_list
    assert len(set(output)) == len(output)


def test_parentheses():
    output = ex7.parentheses(6)
    assert len(output) == nCr(12, 6) // 7

    for stri in output:
        assert len(stri) == 12
        open = 0
        close = 0
        for char in stri:
            assert char == "(" or char == ")"
            if char == "(":
                open += 1
            else:
                close += 1
            assert open >= close

    assert len(set(output)) == len(output)

    output = ex7.parentheses(10)
    assert len(output) == nCr(20, 10) // 11

    for stri in output:
        assert len(stri) == 20
        for char in stri:
            assert char == "(" or char == ")"
            if char == "(":
                open += 1
            else:
                close += 1
            assert open >= close

    assert len(set(output)) == len(output)


def test_up_and_right():
    output = []
    ex7.print = lambda s: output.append(s)
    ex7.up_and_right(6,5)
    assert len(output) == nCr(6+5,6)

    for stri in output:
        assert len(stri) == 11

        up = 0
        down = 0
        for char in stri:
            assert char == "u" or char == "r"
            if char == "u":
                up += 1
            else:
                down += 1
            assert up <= 5 and down <= 6

    assert len(set(output)) == len(output)


    output = []
    ex7.print = lambda s: output.append(s)
    ex7.up_and_right(8,10)
    assert len(output) == nCr(18,8)

    for stri in output:
        assert len(stri) == 18

        up = 0
        down = 0
        for char in stri:
            assert char == "u" or char == "r"
            if char == "u":
                up += 1
            else:
                down += 1
            assert up <= 10 and down <= 8

    assert len(set(output)) == len(output)


def test_flood_fill_1():
    mat = [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]
    ex7.flood_fill(mat, (1, 4))
    assert mat == [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '*', '*'],
        ['*', '*', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]


def test_flood_fill_2():
    mat = [
        ['*', '*', '*', '*'],
        ['*', '.', '.', '*'],
        ['*', '.', '.', '*'],
        ['*', '.', '.', '*'],
        ['*', '*', '*', '*']
    ]

    ex7.flood_fill(mat, (1, 2))
    assert mat ==[
        ['*', '*', '*', '*'],
        ['*', '*', '*', '*'],
        ['*', '*', '*', '*'],
        ['*', '*', '*', '*'],
        ['*', '*', '*', '*']
    ]


def test_flood_fill_3():
    mat = [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]
    ex7.flood_fill(mat, (2, 2))
    assert mat == [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '.', '*'],
        ['*', '*', '*', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '.', '*'],
        ['*', '*', '*', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]


def test_flood_fill_4():
    mat = [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]

    ex7.flood_fill(mat, (5, 4))
    assert mat == [
        ['*', '*', '*', '*', '*', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '.', '.', '*', '.', '*'],
        ['*', '*', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '*', '*'],
        ['*', '.', '.', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*']
    ]


class hanoi:

    def __init__(self):
        pass

    def move(self, frm, to):
        assert len(frm) > 0
        moven = frm.pop(-1)
        to.append(moven)
        copy_to = to[:]
        copy_to.sort()
        assert to == copy_to


