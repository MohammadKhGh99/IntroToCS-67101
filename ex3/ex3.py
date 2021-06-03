def input_list():
    """
    This function asks the user to enter a string and finishes the entering
    when the user enter a blank string ""
    :this function returns a list with all the entered strings:
    """
    lst = []
    string_from_user = input()
    while (string_from_user != ""):
        lst.append(string_from_user)
        string_from_user = input()
    return lst


def concat_list(str_list):
    """
    This function adds all the strings in the list to each other with space
    between them
    :param str_list this parameter contains number of strings:
    :return this function returns the addition between all strings in list:
    """
    s = ""
    if str_list == []:
        return s
    else:
        for i in range(len(str_list)):
            s += (str_list[i] + " ")
        str_list=str_list[:len(str_list)-1]#deleting the last space
        return s

print(concat_list(['H']))
def maximum(num_list):
    """
    this function gives us the maximum number in it
    :param num_list= this parameter contains numbers:
    :return this function returns the maximum number in the list:
    """
    if num_list == []:
        return None
    else:
        m = num_list[0]
        for i in range(1, len(num_list)):
            if num_list[i] > m:
                m = num_list[i]
    return m


def cyclic(lst1,lst2):
    """
    this function checks if the second list is cyclic for the first one
    :param lst1 this is the checker list:
    :param lst2 this is the list that we want to check:
    :return this function returns True if the second list is cyclic for the
    first one:
    """
    if len(lst1)!=len(lst2):
        return False
    elif lst1==[] and lst2==[]:
        return True
    else:
        for i in range (len(lst1)):
            if lst1[i:]+lst1[:i]==lst2:
                return True
        return False


def seven_boom(n):
    """
    this function append the numbers like string from 1 to n and if the
    number divides on 7 or contains 7 it will change it to boom
    :param n this parameter determines which category of numbers the
    function will add to the list:
    :return the function returns a list with strings:
    """
    lst = []
    for i in range(1, n + 1):
        s = str(i)
        if s.find("7") != -1 or i % 7 == 0:
            lst.append("boom")
        else:
            lst.append(s)
    return lst


def histogram(n, num_list):
    """
    this function check how much all the numbers from 0 to n-1, how much they
    appear in the list
    :param n the range of the numbers that the function will check:
    :param num_list the list that we will check:
    :return the function returns a list with how much the numbers appears in
    num_list:
    """
    lst = []
    for i in range(n):
        count = 0
        for j in num_list:
            if i == j:
                count += 1
        lst.append(count)
    return lst


def prime_factors(n):
    """
    this function checks the prime factors of the n
    :param n this parameter that we will check his prime factors:
    :return this function returns the prime factors of the n:
    """
    lst = []
    for i in range(2, n + 1):
        while n % i == 0:
            lst.append(i)
            n = n / i
    return lst


def cartesian(lst1, lst2):
    """
    this function works as cartesian multiplecation
    :param lst1:
    :param lst2:
    :return the function returns the cartesian multiplecation by list:
    """
    c_lst = []
    if lst1 != [] and lst2 != []:
        for i in lst1:
            for j in lst2:
                c_lst.append([i, j])

        return c_lst
    else:
        return c_lst


def pairs(num_list,n):
    pairs_lst=[]
    for i in range(len(num_list)):
        Copy_List=num_list[i+1:]
        for j in Copy_List:
            if num_list[i]+j==n:
                pairs_lst.append([num_list[i],j])
    return pairs_lst
